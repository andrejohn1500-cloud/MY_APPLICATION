const functions = require("firebase-functions");
const admin = require("firebase-admin");
admin.initializeApp();

const db = admin.firestore();
const messaging = admin.messaging();

exports.onScoreSubmitted = functions.firestore
  .document("leaderboard/{docId}")
  .onWrite(async (change, context) => {
    const newData = change.after.exists ? change.after.data() : null;
    if (!newData) return null;

    const { name, score, total, category, level, rating, fcm_token } = newData;
    if (!category || !level) return null;

    // Find all scores in same category+level that are now lower than the new score
    const snapshot = await db.collection("leaderboard")
      .where("category", "==", category)
      .where("level", "==", level)
      .get();

    const displaced = [];
    snapshot.forEach(doc => {
      const d = doc.data();
      // Don't notify the scorer themselves
      if (d.name === name) return;
      // Only notify if their rating is now lower and they have a token
      if (d.rating < rating && d.fcm_token && d.fcm_token.length > 10) {
        displaced.push(d);
      }
    });

    const notifications = displaced.map(player => {
      const gap = score - (player.score || 0);
      const needed = gap > 0 ? `Score ${gap} more to reclaim your rank` : `Answer faster to reclaim #1`;

      return messaging.send({
        token: player.fcm_token,
        data: {
          title: "⚠️ You've been overtaken!",
          body: `${name} just scored ${score}/${total} in ${category} Lvl ${level}. ${needed}.`,
          category: category,
          their_score: `${score}/${total}`,
          your_score: `${player.score}/${player.total || 15}`,
          gap: String(gap),
          rival_name: name
        },
        android: {
          priority: "high",
          notification: {
            title: "⚠️ You've been overtaken!",
            body: `${name} scored ${score}/${total} in ${category}. ${needed}.`,
            channelId: "rivalry_channel"
          }
        }
      }).catch(err => {
        console.log("Failed to send to", player.name, err.message);
      });
    });

    await Promise.all(notifications);
    console.log(`Sent ${notifications.length} rivalry notifications for ${name} in ${category} Lvl ${level}`);
    return null;
  });

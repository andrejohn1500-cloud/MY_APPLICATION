package com.dresapps.dresquiz

import android.os.Bundle
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.firestore.FirebaseFirestore

class PlayerProfileActivity : AppCompatActivity() {

    private val db = FirebaseFirestore.getInstance()
    private val avatars = listOf("🐯","🦁","🐺","🦊","🐻","🦅","🐬","🦋","🐆","🦁","🐘","🦈")
    private val rankTiers = listOf(
        Triple(0,    "🌱 Rookie",           "#A8D8A8"),
        Triple(500,  "📚 Scholar",          "#A8D8EA"),
        Triple(1500, "🏆 Champion",         "#FFD700"),
        Triple(3000, "💎 Diamond",          "#B9F2FF"),
        Triple(5000, "👑 Master",           "#FF8C42"),
        Triple(8000, "🌴 Caribbean Legend", "#FF4500")
    )

    override fun onCreate(b: Bundle?) {
        super.onCreate(b)
        setContentView(R.layout.activity_player_profile)

        val name    = intent.getStringExtra("p_name") ?: "Player"
        val country = intent.getStringExtra("p_country") ?: ""
        val passedAvatar = intent.getStringExtra("p_avatar") ?: ""
        val avatarEmoji = if (passedAvatar.isNotEmpty()) passedAvatar
                          else avatars[Math.abs(name.hashCode()) % avatars.size]

        findViewById<TextView>(R.id.tvPAvatar).text   = avatarEmoji
        findViewById<TextView>(R.id.tvPName).text     = name
        findViewById<TextView>(R.id.tvPCountry).text  = if (country.isNotEmpty()) "🌍 $country" else "🌍"
        findViewById<View>(R.id.loadingBar).visibility = View.VISIBLE

        // Query Firebase leaderboard collection for this player (case-insensitive)
        db.collection("leaderboard")
            .get()
            .addOnSuccessListener { docs ->
                val scores = docs.filter {
                    (it.getString("name") ?: "").equals(name, ignoreCase = true)
                }
                runOnUiThread {
                    findViewById<View>(R.id.loadingBar).visibility = View.GONE
                    buildProfile(scores)
                }
            }
            .addOnFailureListener {
                runOnUiThread {
                    findViewById<View>(R.id.loadingBar).visibility = View.GONE
                    buildProfile(emptyList())
                }
            }

        findViewById<ImageButton>(R.id.btnPBack).setOnClickListener { finish() }
    }

    private fun buildProfile(scores: List<com.google.firebase.firestore.QueryDocumentSnapshot>) {
        val totalGames   = scores.size
        val bestScore    = scores.maxOfOrNull { it.getLong("score")?.toInt() ?: 0 } ?: 0
        val highestLevel = scores.maxOfOrNull { it.getLong("level")?.toInt() ?: 1 } ?: 1
        val cleanGames   = scores.count { (it.getLong("cheats")?.toInt() ?: 0) == 0 }
        val cleanRate    = if (totalGames > 0) (cleanGames * 100 / totalGames) else 0
        val bestCat      = scores.groupBy { it.getString("category") ?: "" }
                                 .maxByOrNull { it.value.size }?.key ?: "—"

        // Compute total rating from stored rating field, or fallback to pct
        var totalRating = 0
        for (s in scores) {
            val storedRating = s.getLong("rating")?.toInt() ?: 0
            if (storedRating > 0) {
                totalRating += storedRating
            } else {
                // fallback: estimate from score/total
                val score = s.getLong("score")?.toInt() ?: 0
                val total = s.getLong("total")?.toInt() ?: 15
                val level = s.getLong("level")?.toInt() ?: 1
                val cheats = s.getLong("cheats")?.toInt() ?: 0
                val pct = if (total > 0) (score * 100 / total) else 0
                val cleanBonus = if (cheats == 0) 15 else 0
                totalRating += pct + cleanBonus + (level * 5)
            }
        }

        val tier = rankTiers.lastOrNull { totalRating >= it.first } ?: rankTiers[0]
        val nextTier = rankTiers.getOrNull(rankTiers.indexOf(tier) + 1)

        findViewById<TextView>(R.id.tvPRating).text     = "⭐ Total Rating: $totalRating"
        findViewById<TextView>(R.id.tvPTier).text       = tier.second
        findViewById<TextView>(R.id.tvPGames).text      = totalGames.toString()
        findViewById<TextView>(R.id.tvPBestScore).text  = "$bestScore/15"
        findViewById<TextView>(R.id.tvPHighLevel).text  = "Lvl $highestLevel"
        findViewById<TextView>(R.id.tvPCleanRate).text  = "$cleanRate%"
        findViewById<TextView>(R.id.tvPBestCat).text    = bestCat
        findViewById<TextView>(R.id.tvPCleanStatus).text =
            if (cleanGames == totalGames && totalGames > 0) "✅ Clean Player"
            else "⚠️ Cheats: ${totalGames - cleanGames} game(s)"

        if (nextTier != null) {
            val ptsToNext = nextTier.first - tier.first
            val progress  = totalRating - tier.first
            val pct2      = (progress * 100 / ptsToNext).coerceIn(0, 100)
            findViewById<ProgressBar>(R.id.progressTier).progress = pct2
            findViewById<TextView>(R.id.tvPProgress).text =
                "$progress / $ptsToNext pts to ${nextTier.second}"
            findViewById<TextView>(R.id.tvPNextTier).text = nextTier.second
        } else {
            findViewById<TextView>(R.id.tvPProgress).text = "🌴 MAX RANK ACHIEVED!"
            findViewById<ProgressBar>(R.id.progressTier).progress = 100
        }
    }
}

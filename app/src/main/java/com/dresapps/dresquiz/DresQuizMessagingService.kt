package com.dresapps.dresquiz

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Build
import androidx.core.app.NotificationCompat
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

class DresQuizMessagingService : FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        super.onNewToken(token)
        applicationContext.getSharedPreferences("fcm_prefs", Context.MODE_PRIVATE)
            .edit().putString("fcm_token", token).apply()
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        super.onMessageReceived(remoteMessage)
        val data     = remoteMessage.data
        val title    = data["title"]       ?: "DREs Quiz"
        val body     = data["body"]        ?: ""
        val category = data["category"]    ?: ""
        val theirScore = data["their_score"] ?: ""
        val yourScore  = data["your_score"]  ?: ""
        val gap        = data["gap"]         ?: ""
        showRivalryNotification(title, body, category, theirScore, yourScore, gap)
    }

    private fun showRivalryNotification(
        title: String,
        body: String,
        category: String,
        theirScore: String,
        yourScore: String,
        gap: String
    ) {
        val ctx       = applicationContext
        val channelId = "rivalry_channel"
        val manager   = ctx.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                channelId,
                "Score Rivalry Alerts",
                NotificationManager.IMPORTANCE_HIGH
            ).apply {
                description = "Alerts when someone beats your score"
                enableVibration(true)
            }
            manager.createNotificationChannel(channel)
        }

        val intent = Intent(ctx, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
            putExtra("open_leaderboard", true)
            putExtra("rivalry_category", category)
            putExtra("their_score", theirScore)
            putExtra("your_score", yourScore)
            putExtra("gap", gap)
        }

        val pendingIntent = PendingIntent.getActivity(
            ctx, 0, intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )

        val notification = NotificationCompat.Builder(ctx, channelId)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentTitle(title)
            .setContentText(body)
            .setStyle(NotificationCompat.BigTextStyle().bigText(body))
            .setPriority(NotificationCompat.PRIORITY_HIGH)
            .setAutoCancel(true)
            .setContentIntent(pendingIntent)
            .setVibrate(longArrayOf(0, 500, 200, 500))
            .build()

        manager.notify(System.currentTimeMillis().toInt(), notification)
    }
}

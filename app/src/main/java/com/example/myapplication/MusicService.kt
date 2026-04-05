package com.example.myapplication

import android.app.Service
import android.content.Intent
import android.media.MediaPlayer
import android.os.IBinder

class MusicService : Service() {
    private var mediaPlayer: MediaPlayer? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        when (intent?.action) {
            "PAUSE" -> mediaPlayer?.pause()
            "RESUME" -> {
                if (mediaPlayer == null) {
                    mediaPlayer = MediaPlayer.create(this, R.raw.classical_bg)
                    mediaPlayer?.isLooping = true
                    mediaPlayer?.setVolume(0.35f, 0.35f)
                }
                mediaPlayer?.start()
            }
            else -> {
                if (mediaPlayer == null) {
                    mediaPlayer = MediaPlayer.create(this, R.raw.classical_bg)
                    mediaPlayer?.isLooping = true
                    mediaPlayer?.setVolume(0.35f, 0.35f)
                    mediaPlayer?.start()
                }
            }
        }
        return START_STICKY
    }

    override fun onDestroy() {
        mediaPlayer?.stop()
        mediaPlayer?.release()
        mediaPlayer = null
        super.onDestroy()
    }

    override fun onBind(intent: Intent?): IBinder? = null
}

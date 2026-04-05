package com.example.myapplication

import android.app.Service
import android.content.Intent
import android.media.MediaPlayer
import android.os.IBinder

class MusicService : Service() {
    companion object {
        var isPlaying = false
    }

    private var mediaPlayer: MediaPlayer? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val action = intent?.action
        if (action == "PAUSE") {
            mediaPlayer?.pause()
            isPlaying = false
        } else if (action == "RESUME" || action == null) {
            if (mediaPlayer == null) {
                try {
                    mediaPlayer = MediaPlayer.create(this, R.raw.classical_bg)
                    mediaPlayer?.isLooping = true
                    mediaPlayer?.setVolume(0.4f, 0.4f)
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
            if (mediaPlayer?.isPlaying == false) {
                mediaPlayer?.start()
                isPlaying = true
            }
        }
        return START_STICKY
    }

    override fun onDestroy() {
        mediaPlayer?.stop()
        mediaPlayer?.release()
        mediaPlayer = null
        isPlaying = false
        super.onDestroy()
    }

    override fun onBind(intent: Intent?): IBinder? = null
}

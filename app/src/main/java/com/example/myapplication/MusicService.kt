package com.example.myapplication

import android.app.Service
import android.content.Intent
import android.media.MediaPlayer
import android.os.IBinder

class MusicService : Service() {

    companion object {
        var isPlaying = false

        // ── MUSIC BANK ──────────────────────────────────────────────
        // Add new tracks here. Drop the .mp3 into res/raw/ and add a
        // Pair(R.raw.your_file, "Display Name") to this list.
        val TRACKS = listOf(
            Pair(R.raw.music_01, "Warm Memories"),
            Pair(R.raw.music_02, "Sweet Memories"),
            Pair(R.raw.music_03, "Sleepless City"),
            Pair(R.raw.music_04, "Rise"),
            Pair(R.raw.music_05, "Adrift Among Infinite Stars"),
            Pair(R.raw.music_06, "Coconut"),
            Pair(R.raw.music_07, "Sweet Sun"),
            Pair(R.raw.music_08, "Flying"),
            Pair(R.raw.music_09, "Calypso Cruise"),
            Pair(R.raw.music_10, "Coffee Cup Vibes"),
            Pair(R.raw.music_11, "Live Your Dream")
            // e.g. Pair(R.raw.hiphop_bg, "Hip Hop Beats"),
        )
        // ─────────────────────────────────────────────────────────────

        const val ACTION_PAUSE        = "PAUSE"
        const val ACTION_RESUME       = "RESUME"
        const val ACTION_CHANGE_TRACK = "CHANGE_TRACK"
        const val EXTRA_TRACK_INDEX   = "track_index"
    }

    private var mediaPlayer: MediaPlayer? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val action = intent?.action

        when (action) {
            ACTION_PAUSE -> {
                mediaPlayer?.pause()
                isPlaying = false
            }
            ACTION_CHANGE_TRACK -> {
                val index = intent.getIntExtra(EXTRA_TRACK_INDEX, 0)
                AppPreferences.setSelectedTrack(this, index)
                loadTrack(index)
                mediaPlayer?.start()
                isPlaying = true
            }
            else -> { // RESUME or null (first start)
                if (mediaPlayer == null) {
                    val trackIndex = AppPreferences.getSelectedTrack(this)
                    loadTrack(trackIndex)
                }
                if (mediaPlayer?.isPlaying == false) {
                    mediaPlayer?.start()
                    isPlaying = true
                }
            }
        }
        return START_STICKY
    }

    private fun loadTrack(index: Int) {
        val safeIndex = index.coerceIn(0, TRACKS.size - 1)
        val resId = TRACKS[safeIndex].first
        try {
            mediaPlayer?.stop()
            mediaPlayer?.release()
            mediaPlayer = MediaPlayer.create(this, resId)
            mediaPlayer?.isLooping = true
            mediaPlayer?.setVolume(0.4f, 0.4f)
        } catch (e: Exception) {
            e.printStackTrace()
        }
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

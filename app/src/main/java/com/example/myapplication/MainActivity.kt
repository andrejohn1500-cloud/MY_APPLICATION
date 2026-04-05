package com.example.myapplication

import android.content.Intent
import android.media.MediaPlayer
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private var bgMusic: MediaPlayer? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        startService(Intent(this, MusicService::class.java))

        binding.btnStart.setOnClickListener {
            startActivity(Intent(this, CategoryActivity::class.java))
        }
        binding.btnLeaderboard.setOnClickListener {
            startActivity(Intent(this, LeaderboardActivity::class.java))
        }
        binding.btnDonate.setOnClickListener {
            startActivity(Intent(this, DonationActivity::class.java))
        }
        binding.btnMyStory.setOnClickListener {
            startActivity(Intent(this, MyStoryActivity::class.java))
        }

        // Background music — add res/raw/bg_music.mp3 then uncomment:
        // bgMusic = MediaPlayer.create(this, R.raw.bg_music)
        // bgMusic?.isLooping = true
    }

    override fun onResume() {
        super.onResume()
        // bgMusic?.start()
    }

    override fun onPause() {
        super.onPause()
        bgMusic?.pause()
    }

    override fun onDestroy() {
        super.onDestroy()
        bgMusic?.release()
    }
}

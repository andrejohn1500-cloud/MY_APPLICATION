package com.dresapps.dresquiz

import android.content.Intent
import android.media.MediaPlayer
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.dresapps.dresquiz.databinding.ActivityMainBinding
import com.google.android.gms.ads.MobileAds

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private var bgMusic: MediaPlayer? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        MobileAds.initialize(this) {}
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Check Supabase for premium status on every launch
        val deviceId = SupabaseHelper.getDeviceId(this)
        SupabaseHelper.checkPremiumByDevice(deviceId) { isPremium ->
            if (isPremium) {
                AppPreferences.setPremium(this, true)
            }
        }
        startService(Intent(this, MusicService::class.java))

        // Vibrate helper
        val vib = getSystemService(android.content.Context.VIBRATOR_SERVICE) as android.os.Vibrator
        fun buzz() {
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                vib.vibrate(android.os.VibrationEffect.createOneShot(25, android.os.VibrationEffect.DEFAULT_AMPLITUDE))
            } else { vib.vibrate(25) }
        }

        listOf(binding.btnStart, binding.btnLeaderboard, binding.btnDonate, binding.btnMyStory, binding.btnSettings).forEach { btn ->
            btn.setOnTouchListener { v, event ->
                if (event.action == android.view.MotionEvent.ACTION_DOWN) { buzz(); v.performClick() }
                false
            }
        }

        // Set button backgrounds programmatically
        val goldColor = android.graphics.Color.parseColor("#FFD700")
        val navyAccent = android.graphics.Color.parseColor("#2A2F52")
        val darkText = android.graphics.Color.parseColor("#1A1D2E")

        val goldList   = android.content.res.ColorStateList.valueOf(goldColor)
        val navyList   = android.content.res.ColorStateList.valueOf(navyAccent)
        val darkList   = android.content.res.ColorStateList.valueOf(darkText)

        binding.btnStart.backgroundTintList = goldList
        binding.btnStart.setTextColor(darkText)

        listOf(binding.btnLeaderboard, binding.btnDonate, binding.btnMyStory).forEach { btn ->
            btn.backgroundTintList = navyList
            btn.setTextColor(goldColor)
        }

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
        binding.btnSettings.setOnClickListener {
            startActivity(Intent(this, SettingsActivity::class.java))
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

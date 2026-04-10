package com.example.myapplication

import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.widget.ImageButton
import android.widget.RadioButton
import android.widget.RadioGroup
import androidx.appcompat.app.AppCompatActivity
import androidx.cardview.widget.CardView
import com.google.android.material.switchmaterial.SwitchMaterial

class SettingsActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_settings)

        val switchMusic   = findViewById<SwitchMaterial>(R.id.switchMusic)
        val switchHaptics = findViewById<SwitchMaterial>(R.id.switchHaptics)
        val btnBack       = findViewById<ImageButton>(R.id.btnBack)
        val cardTrack     = findViewById<CardView>(R.id.cardTrackSelector)
        val radioGroup    = findViewById<RadioGroup>(R.id.radioGroupTracks)

        switchSound.isChecked   = AppPreferences.isSoundEnabled(this)
        switchMusic.isChecked   = AppPreferences.isMusicEnabled(this)
        switchHaptics.isChecked = AppPreferences.isHapticsEnabled(this)

        cardTrack.visibility = if (switchMusic.isChecked)
            android.view.View.VISIBLE else android.view.View.GONE

        val savedTrack = AppPreferences.getSelectedTrack(this)
        val goldColor  = Color.parseColor("#FFA500")
        val goldList   = android.content.res.ColorStateList.valueOf(goldColor)

        MusicService.TRACKS.forEachIndexed { index, (_, name) ->
            val rb = RadioButton(this).apply {
                id = index
                text = name
                setTextColor(Color.WHITE)
                textSize = 15f
                buttonTintList = goldList
                isChecked = (index == savedTrack)
            }
            radioGroup.addView(rb)
        }

        radioGroup.setOnCheckedChangeListener { _, checkedId ->
            AppPreferences.setSelectedTrack(this, checkedId)
            val i = Intent(this, MusicService::class.java)
            i.action = MusicService.ACTION_CHANGE_TRACK
            i.putExtra(MusicService.EXTRA_TRACK_INDEX, checkedId)
            startService(i)
        }

        switchMusic.setOnCheckedChangeListener { _, isChecked ->
            AppPreferences.setMusic(this, isChecked)
            cardTrack.visibility = if (isChecked)
                android.view.View.VISIBLE else android.view.View.GONE
            val i = Intent(this, MusicService::class.java)
            i.action = if (isChecked) MusicService.ACTION_RESUME else MusicService.ACTION_PAUSE
            startService(i)
        }


        switchHaptics.setOnCheckedChangeListener { _, isChecked ->
            AppPreferences.setHaptics(this, isChecked)
        }

        btnBack.setOnClickListener { finish() }
    }
}
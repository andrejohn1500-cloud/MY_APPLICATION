package com.example.myapplication

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.switchmaterial.SwitchMaterial
import android.widget.ImageButton

class SettingsActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_settings)

        val switchSound   = findViewById<SwitchMaterial>(R.id.switchSound)
        val switchMusic   = findViewById<SwitchMaterial>(R.id.switchMusic)
        val switchHaptics = findViewById<SwitchMaterial>(R.id.switchHaptics)
        val btnBack       = findViewById<ImageButton>(R.id.btnBack)

        // Load saved preferences
        switchSound.isChecked   = AppPreferences.isSoundEnabled(this)
        switchMusic.isChecked   = AppPreferences.isMusicEnabled(this)
        switchHaptics.isChecked = AppPreferences.isHapticsEnabled(this)

        // Save on toggle
        switchSound.setOnCheckedChangeListener { _, isChecked ->
            AppPreferences.setSound(this, isChecked)
        }

        switchMusic.setOnCheckedChangeListener { _, isChecked ->
            AppPreferences.setMusic(this, isChecked)
        }

        switchHaptics.setOnCheckedChangeListener { _, isChecked ->
            AppPreferences.setHaptics(this, isChecked)
        }

        btnBack.setOnClickListener { finish() }
    }
}

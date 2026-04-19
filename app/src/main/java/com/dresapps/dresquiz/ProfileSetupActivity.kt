package com.dresapps.dresquiz

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.dresapps.dresquiz.databinding.ActivityProfileSetupBinding

class ProfileSetupActivity : AppCompatActivity() {

    private lateinit var binding: ActivityProfileSetupBinding
    private var selectedCountry = ""
    private var selectedAvatar = "🎓"

    private val avatars = listOf(
        "🎓","🏆","🌴","🦁","⚡","🔥","💎","👑",
        "🎯","🚀","🌊","🦅","🏏","🎸","🧠","⭐"
    )

    private val countries = arrayOf(
        "🇦🇮 Anguilla","🇦🇬 Antigua & Barbuda","🇧🇧 Barbados","🇧🇿 Belize",
        "🇻🇬 British Virgin Islands","🇰🇾 Cayman Islands","🇩🇲 Dominica","🇬🇩 Grenada",
        "🇬🇾 Guyana","🇯🇲 Jamaica","🇲🇸 Montserrat","🇰🇳 St. Kitts & Nevis",
        "🇱🇨 St. Lucia","🇻🇨 St. Vincent & the Grenadines","🇹🇹 Trinidad & Tobago",
        "🇹🇨 Turks & Caicos Islands",
                "🇺🇸 United States",
                "🇨🇦 Canada",
                "🇬🇧 United Kingdom",
                "🇫🇷 France",
                "🇳🇱 Netherlands",
                "🇪🇸 Spain"
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityProfileSetupBinding.inflate(layoutInflater)
        setContentView(binding.root)

        buildAvatarPicker()

        binding.btnSelectCountry.setOnClickListener {
            android.app.AlertDialog.Builder(this)
                .setTitle("🌍 Select Your Country")
                .setItems(countries) { _, w ->
                    selectedCountry = countries[w]
                    binding.btnSelectCountry.text = selectedCountry
                    binding.btnSelectCountry.setTextColor(android.graphics.Color.WHITE)
                }
                .setNegativeButton("Cancel", null).show()
        }

        binding.btnStartPlaying.setOnClickListener {
            val name = binding.etProfileName.text.toString().trim()
            if (name.isEmpty()) {
                Toast.makeText(this, "Please enter your name", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            if (selectedCountry.isEmpty()) {
                Toast.makeText(this, "Please select your country", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            val prefs = getSharedPreferences("player_prefs", MODE_PRIVATE)
            prefs.edit()
                .putString("player_name", name)
                .putString("player_country", selectedCountry)
                .putString("player_avatar", selectedAvatar)
                .putBoolean("profile_set", true)
                .apply()
            startActivity(Intent(this, MainActivity::class.java))
            finish()
        }
    }

    private fun buildAvatarPicker() {
        avatars.forEach { emoji ->
            val btn = Button(this).apply {
                text = emoji
                textSize = 24f
                isAllCaps = false
                val size = resources.getDimensionPixelSize(android.R.dimen.app_icon_size)
                layoutParams = android.widget.LinearLayout.LayoutParams(size, size).apply {
                    setMargins(8, 0, 8, 0)
                }
                setBackgroundColor(if (emoji == selectedAvatar)
                    android.graphics.Color.parseColor("#FFA500")
                    else android.graphics.Color.parseColor("#1A1E3A"))
                setOnClickListener {
                    selectedAvatar = emoji
                    refreshAvatars()
                }
            }
            binding.layoutAvatars.addView(btn)
        }
    }

    private fun refreshAvatars() {
        for (i in 0 until binding.layoutAvatars.childCount) {
            val btn = binding.layoutAvatars.getChildAt(i) as Button
            btn.setBackgroundColor(if (btn.text == selectedAvatar)
                android.graphics.Color.parseColor("#FFA500")
                else android.graphics.Color.parseColor("#1A1E3A"))
        }
    }
}
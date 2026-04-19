package com.dresapps.dresquiz

import android.os.Bundle
import android.widget.ImageButton
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class PlayerProfileActivity : AppCompatActivity() {
    override fun onCreate(b: Bundle?) {
        super.onCreate(b)
        setContentView(R.layout.activity_player_profile)

        val name    = intent.getStringExtra("p_name") ?: "Player"
        val country = intent.getStringExtra("p_country") ?: "🌍"
        val rating  = intent.getIntExtra("p_rating", 0)
        val cheats  = intent.getIntExtra("p_cheats", 0)

        findViewById<TextView>(R.id.tvPName).text    = name
        findViewById<TextView>(R.id.tvPCountry).text = "🌍 $country"
        findViewById<TextView>(R.id.tvPRating).text  = "⭐ Rating: $rating"
        findViewById<TextView>(R.id.tvPClean).text   =
            if (cheats == 0) "✅ Clean Player" else "⚠️ Cheats Used: $cheats"
        findViewById<ImageButton>(R.id.btnPBack).setOnClickListener { finish() }
    }
}

package com.dresapps.dresquiz

import android.app.AlertDialog
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.dresapps.dresquiz.databinding.ActivityMyStoryBinding

class MyStoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMyStoryBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMyStoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val prefs   = getSharedPreferences("player_prefs", MODE_PRIVATE)
        val name    = prefs.getString("player_name", "Player") ?: "Player"
        val avatar  = prefs.getString("player_avatar", "🎓") ?: "🎓"
        val country = prefs.getString("player_country", "Unknown") ?: "Unknown"

        binding.tvProfileAvatar.text  = avatar
        binding.tvProfileName.text    = name
        binding.tvProfileCountry.text = country

        val totalRating = prefs.getInt("total_rating", 0)
        val totalGames  = prefs.getInt("total_games", 0)
        val highestLvl  = prefs.getInt("highest_level", 1)
        val cleanGames  = prefs.getInt("clean_games", 0)
        val cleanRate   = if (totalGames > 0) (cleanGames * 100 / totalGames) else 0
        val bestScore   = prefs.getInt("best_score", 0)
        val bestCat     = prefs.getString("best_category", "—") ?: "—"

        val rankName = when {
            totalRating < 500  -> "🌱 Rookie"
            totalRating < 1500 -> "📚 Scholar"
            totalRating < 3000 -> "🏆 Champion"
            totalRating < 5000 -> "⚡ Legend"
            else               -> "🌴 Caribbean Elite"
        }
        val nextRank = when {
            totalRating < 500  -> "Scholar"
            totalRating < 1500 -> "Champion"
            totalRating < 3000 -> "Legend"
            totalRating < 5000 -> "Caribbean Elite"
            else               -> "MAX"
        }
        val tierMin = when {
            totalRating < 500  -> 0
            totalRating < 1500 -> 500
            totalRating < 3000 -> 1500
            totalRating < 5000 -> 3000
            else               -> 5000
        }
        val tierMax = when {
            totalRating < 500  -> 500
            totalRating < 1500 -> 1500
            totalRating < 3000 -> 3000
            totalRating < 5000 -> 5000
            else               -> 5000
        }
        val nextPts = when {
            totalRating < 500  -> 500
            totalRating < 1500 -> 1500
            totalRating < 3000 -> 3000
            totalRating < 5000 -> 5000
            else               -> 5000
        }
        val progress = if (tierMax != tierMin)
            ((totalRating - tierMin) * 100 / (tierMax - tierMin)).coerceIn(0, 100)
        else 100

        binding.tvRankBadge.text        = rankName
        binding.tvTotalRating.text      = totalRating.toString()
        binding.tvTotalGames.text       = totalGames.toString()
        binding.tvHighestLevel.text     = "Lvl $highestLvl"
        binding.tvCleanRate.text        = "$cleanRate%"
        binding.tvBestScore.text        = "$bestScore/15"
        binding.tvBestCategory.text     = bestCat
        binding.tvCurrentRankLabel.text = rankName
        binding.tvNextRankLabel.text    = nextRank
        binding.progressRank.progress   = progress
        binding.tvGlobalRank.text       = ""
        binding.tvRankProgress.text     = if (totalRating < 5000)
            "$totalRating / $nextPts pts to $nextRank"
        else "MAX RANK ACHIEVED 🌴"

        binding.btnViewStory.setOnClickListener {
            AlertDialog.Builder(this)
                .setTitle("📖 My Story")
                .setMessage("My Story — Andre N. John\n\nI grew up in St. Vincent with no electricity, no running water, and no guarantees.\n\nOn June 14, 2025, I was seriously injured in the line of duty.\n\nWith no formal training in software development, I taught myself. I failed often. I kept going. DREs Quiz was built from that bed, question by question, screen by screen.\n\nPlay hard. Learn something. Carry it with you.\n\nYours Truly,\nAndre N. John\n\n\"Built in stillness. Released with purpose.\"")
                .setPositiveButton("Close", null)
                .show()
        }
        binding.btnBackStory.setOnClickListener { finish() }
    }
}
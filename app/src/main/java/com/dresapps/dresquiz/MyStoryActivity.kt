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
                .setMessage("A Message to You\n\nYou picked up this phone today.\n\nMaybe to pass time. Maybe someone sent you the link. Either way you are here now, and that matters.\n\nEvery Caribbean student who has ever felt like the system wasn't built for them this was made for you. Not to replace school. Just to give you an edge at the thing that can quietly change the direction of your life: your CXC exams.\n\nThe world is loud. Social media is louder. But somewhere in the middle of all that noise, your grades are still the one thing no one can take from you.\n\nYou don't have to be perfect. You just have to keep going.\n\nPlay this game like it matters. Because one day when you're holding your results slip you'll remember that you prepared. You'll remember that you showed up.\n\nThat's the version of you worth becoming.\n\nPlay hard. Study harder.\n\nAndré N. John")
                .setPositiveButton("Close", null)
                .show()
        }
        binding.btnBackStory.setOnClickListener { finish() }
    }
}
package com.dresapps.dresquiz

import android.os.Bundle
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class PlayerProfileActivity : AppCompatActivity() {

    private val avatars = listOf("🐯","🦁","🐺","🦊","🐻","🦅","🐬","🦋","🐆","🦁","🐘","🦈")
    private val rankTiers = listOf(
        Triple(0,    "🌱 Rookie",           "#A8D8A8"),
        Triple(500,  "📚 Scholar",          "#A8D8EA"),
        Triple(1500, "🏆 Champion",         "#FFD700"),
        Triple(3000, "💎 Diamond",          "#B9F2FF"),
        Triple(5000, "👑 Master",           "#FF8C42"),
        Triple(8000, "🌴 Caribbean Legend", "#FF4500")
    )

    override fun onCreate(b: Bundle?) {
        super.onCreate(b)
        setContentView(R.layout.activity_player_profile)

        val name    = intent.getStringExtra("p_name") ?: "Player"
        val country = intent.getStringExtra("p_country") ?: ""

        // Set name and avatar immediately
        val avatarIdx = Math.abs(name.hashCode()) % avatars.size
        findViewById<TextView>(R.id.tvPAvatar).text   = avatars[avatarIdx]
        findViewById<TextView>(R.id.tvPName).text     = name
        findViewById<TextView>(R.id.tvPCountry).text  = if (country.isNotEmpty()) "🌍 $country" else "🌍"
        findViewById<View>(R.id.loadingBar).visibility = View.VISIBLE

        SupabaseHelper.fetchPlayerScores(name) { scores ->
            runOnUiThread {
                findViewById<View>(R.id.loadingBar).visibility = View.GONE
                buildProfile(name, country, scores)
            }
        }

        findViewById<ImageButton>(R.id.btnPBack).setOnClickListener { finish() }
    }

    private fun buildProfile(name: String, country: String, scores: List<Map<String, Any>>) {
        val totalGames   = scores.size
        val bestScore    = scores.maxOfOrNull { (it["score"] as Int) } ?: 0
        val totalPts     = scores.size
        val highestLevel = scores.maxOfOrNull { (it["level"] as Int) } ?: 1
        val cleanGames   = scores.count { (it["cheats"] as Int) == 0 }
        val cleanRate    = if (totalGames > 0) (cleanGames * 100 / totalGames) else 0
        val bestCat      = scores.groupBy { it["category"] as String }
                                 .maxByOrNull { it.value.sumOf { s -> s["pct"] as Int } }?.key ?: "—"

        // Compute total rating using same formula as ResultActivity
        var totalRating = 0
        for (s in scores) {
            val pct       = s["pct"] as Int
            val cheats    = s["cheats"] as Int
            val level     = s["level"] as Int
            val timeTaken = s["time_taken"] as Int
            val speedBonus = maxOf(0, ((450 - timeTaken).toFloat() / 450 * 20).toInt())
            val cleanBonus = if (cheats == 0) 15 else 0
            val lvlBonus   = level * 5
            totalRating += pct + speedBonus + cleanBonus + lvlBonus
        }

        // Determine tier
        val tier = rankTiers.lastOrNull { totalRating >= it.first } ?: rankTiers[0]
        val nextTier = rankTiers.getOrNull(rankTiers.indexOf(tier) + 1)

        // Update UI
        findViewById<TextView>(R.id.tvPRating).text     = "⭐ Total Rating: $totalRating"
        findViewById<TextView>(R.id.tvPTier).text       = tier.second
        findViewById<TextView>(R.id.tvPGames).text      = totalGames.toString()
        findViewById<TextView>(R.id.tvPBestScore).text  = "$bestScore/15"
        findViewById<TextView>(R.id.tvPHighLevel).text  = "Lvl $highestLevel"
        findViewById<TextView>(R.id.tvPCleanRate).text  = "$cleanRate%"
        findViewById<TextView>(R.id.tvPBestCat).text    = bestCat
        findViewById<TextView>(R.id.tvPCleanStatus).text =
            if (cleanGames == totalGames && totalGames > 0) "✅ Clean Player" else "⚠️ Cheats: ${totalGames - cleanGames} game(s)"

        // Progress bar to next tier
        if (nextTier != null) {
            val ptsToNext = nextTier.first - tier.first
            val progress  = totalRating - tier.first
            val pct2      = (progress * 100 / ptsToNext).coerceIn(0, 100)
            findViewById<ProgressBar>(R.id.progressTier).progress = pct2
            findViewById<TextView>(R.id.tvPProgress).text =
                "$progress / $ptsToNext pts to ${nextTier.second}"
            findViewById<TextView>(R.id.tvPNextTier).text = nextTier.second
        } else {
            findViewById<TextView>(R.id.tvPProgress).text = "🌴 MAX RANK ACHIEVED!"
            findViewById<ProgressBar>(R.id.progressTier).progress = 100
        }
    }
}

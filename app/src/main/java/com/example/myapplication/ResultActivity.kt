package com.example.myapplication

import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityResultBinding
import com.google.firebase.firestore.FirebaseFirestore

class ResultActivity : AppCompatActivity() {

    private lateinit var binding: ActivityResultBinding
    private val db = FirebaseFirestore.getInstance()

    private val remarksHundred = listOf(
        "Perfect score! The curriculum bows to you.",
        "100 percent! Even I had to double-check the answers.",
        "Flawless. You did not need me at all today.",
        "A perfect ten. The class is silent with respect.",
        "Outstanding! Frame this result."
    )
    private val remarksHigh = listOf(
        "Almost perfect. The knowledge is clearly there.",
        "Strong performance. A little more focus next time.",
        "You are in the top tier. Keep pushing.",
        "Great work! One more push and it is perfect.",
        "The data backs you up on this one."
    )
    private val remarksMid = listOf(
        "Solid effort. The gaps are closeable.",
        "Good foundation. Build on it.",
        "My coffee was wrong too. Try again.",
        "You are getting there. Review and retry.",
        "Gravity gets it wrong sometimes too. Keep going."
    )
    private val remarksLow = listOf(
        "Back to the lab. We have work to do.",
        "Even Einstein failed exams. Rise up.",
        "The universe forgives you. Study does not.",
        "Plot twist nobody wanted. But recovery is possible.",
        "Science is still your friend. Trust the process."
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityResultBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val score    = intent.getIntExtra("score", 0)
        val total    = intent.getIntExtra("total", 17)
        val category = intent.getStringExtra("category") ?: ""
        val level    = intent.getIntExtra("level", 1)
        val pct      = if (total > 0) (score.toFloat() / total * 100).toInt() else 0

        binding.tvResultCategory.text = category
        binding.tvFinalScore.text = score.toString()
        binding.tvScoreLabel.text = " / $total"
        binding.tvPercent.text = "$pct%"
        binding.progressResult.progress = pct

        when {
            pct == 100 -> {
                binding.tvTrophy.text = "🏆"
                binding.tvGrade.text = "Outstanding!"
                binding.tvGrade.setTextColor(Color.parseColor("#4CAF50"))
            }
            pct >= 80 -> {
                binding.tvTrophy.text = "🥇"
                binding.tvGrade.text = "Great Work!"
                binding.tvGrade.setTextColor(Color.parseColor("#FFD700"))
            }
            pct >= 50 -> {
                binding.tvTrophy.text = "🥈"
                binding.tvGrade.text = "Good Effort!"
                binding.tvGrade.setTextColor(Color.parseColor("#FF9800"))
            }
            else -> {
                binding.tvTrophy.text = "📚"
                binding.tvGrade.text = "Keep Studying!"
                binding.tvGrade.setTextColor(Color.parseColor("#F44336"))
            }
        }

        val remark = when {
            pct == 100 -> remarksHundred.random()
            pct >= 80  -> remarksHigh.random()
            pct >= 50  -> remarksMid.random()
            else       -> remarksLow.random()
        }
        binding.tvTeacherRemark.text = remark

        if (pct >= 80) {
            binding.btnNextLevel.isEnabled = true
            binding.btnNextLevel.alpha = 1.0f
            binding.btnNextLevel.text = "🚀  NEXT LEVEL"
        } else {
            binding.btnNextLevel.isEnabled = false
            binding.btnNextLevel.alpha = 0.35f
            binding.btnNextLevel.text = "🔒  NEXT LEVEL  (80% required)"
        }

        binding.btnNextLevel.setOnClickListener {
            val nextIntent = Intent(this, QuizActivity::class.java)
            nextIntent.putExtra("category", category)
            nextIntent.putExtra("level", level + 1)
            startActivity(nextIntent)
            finish()
        }

        binding.btnSubmitScore.setOnClickListener {
            val name = binding.etPlayerName.text.toString().trim()
            if (name.isEmpty()) {
                Toast.makeText(this, "Please enter your name", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            submitScore(name, score, total, category)
        }

        binding.btnPlayAgain.setOnClickListener {
            startActivity(Intent(this, CategoryActivity::class.java))
            finish()
        }

        binding.btnShare.setOnClickListener {
            val shareText = "I scored $score/$total ($pct%) in $category on DREs Quiz! Can you beat me?"
            val intent = Intent(Intent.ACTION_SEND).apply {
                type = "text/plain"
                putExtra(Intent.EXTRA_TEXT, shareText)
            }
            startActivity(Intent.createChooser(intent, "Share your score"))
        }

        binding.btnHome.setOnClickListener {
            startActivity(Intent(this, MainActivity::class.java).apply {
                flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
            })
            finish()
        }
    }

    private fun submitScore(name: String, score: Int, total: Int, category: String) {
        db.collection("leaderboard")
            .whereEqualTo("name", name)
            .get()
            .addOnSuccessListener { docs ->
                val existing = docs.firstOrNull()
                val prevBest = existing?.getLong("score")?.toInt() ?: -1
                if (existing != null && prevBest >= score) {
                    Toast.makeText(this, "Your best score is already $prevBest/$total", Toast.LENGTH_SHORT).show()
                    binding.btnSubmitScore.isEnabled = false
                    binding.btnSubmitScore.alpha = 0.5f
                    return@addOnSuccessListener
                }
                val data = hashMapOf<String, Any>(
                    "name" to name,
                    "score" to score,
                    "total" to total,
                    "category" to category,
                    "timestamp" to System.currentTimeMillis()
                )
                if (existing != null) existing.reference.set(data)
                else db.collection("leaderboard").add(data)
                Toast.makeText(this, "New best score saved!", Toast.LENGTH_SHORT).show()
                binding.btnSubmitScore.isEnabled = false
                binding.btnSubmitScore.alpha = 0.5f
            }
            .addOnFailureListener {
                Toast.makeText(this, "Submission failed. Check connection.", Toast.LENGTH_SHORT).show()
            }
    }
}

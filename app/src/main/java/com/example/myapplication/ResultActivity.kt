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

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityResultBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val score    = intent.getIntExtra("score", 0)
        val total    = intent.getIntExtra("total", 17)
        val category = intent.getStringExtra("category") ?: ""
        val pct      = if (total > 0) (score.toFloat() / total * 100).toInt() else 0

        binding.tvFinalScore.text = score.toString()
        binding.tvScoreLabel.text = "out of $total"

        binding.tvGrade.apply {
            when {
                pct >= 90 -> { text = "🏆 Outstanding!";  setTextColor(Color.parseColor("#4CAF50")) }
                pct >= 70 -> { text = "⭐ Great Work!";   setTextColor(Color.parseColor("#FFD700")) }
                pct >= 50 -> { text = "👍 Good Effort!";  setTextColor(Color.parseColor("#FF9800")) }
                else       -> { text = "📚 Keep Studying!"; setTextColor(Color.parseColor("#F44336")) }
            }
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
                    "name" to name, "score" to score,
                    "total" to total, "category" to category,
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

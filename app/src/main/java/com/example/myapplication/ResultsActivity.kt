package com.example.myapplication

import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.view.View
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.button.MaterialButton
import com.google.firebase.firestore.FirebaseFirestore
import android.widget.EditText
import android.widget.Toast

class ResultsActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_results)

        val score    = intent.getIntExtra("score", 0)
        val total    = intent.getIntExtra("total", 1)
        val category = intent.getStringExtra("category") ?: "General"
        val cheats   = intent.getIntExtra("cheats", 0)

        val prefs        = getSharedPreferences("dres_prefs", MODE_PRIVATE)
        val levelKey     = "level_$category"
        val currentLevel = prefs.getInt(levelKey, 1)
        val pct          = if (total > 0) (score * 100 / total) else 0
        val passed       = pct >= 80

        val bestKey  = "best_$category"
        val prevBest = prefs.getInt(bestKey, 0)
        if (score > prevBest) prefs.edit().putInt(bestKey, score).apply()

        findViewById<TextView>(R.id.tvResultCategory).text = category.uppercase()
        findViewById<TextView>(R.id.tvScore).text          = "$score / $total"
        findViewById<TextView>(R.id.tvPercentage).text     = "$pct%"
        findViewById<TextView>(R.id.tvCheatsUsed).text     = if (cheats == 0) "None" else "$cheats"

        val tvLevel = findViewById<TextView>(R.id.tvLevel)
        val tvMsg   = findViewById<TextView>(R.id.tvLevelMessage)
        val btnNext = findViewById<MaterialButton>(R.id.btnNextLevel)

        if (passed) {
            val newLevel = currentLevel + 1
            prefs.edit().putInt(levelKey, newLevel).apply()
            tvLevel.text = "Lvl $newLevel"
            tvMsg.text = "Level $newLevel unlocked!"
            tvMsg.setTextColor(Color.parseColor("#1DB954"))
            btnNext.visibility = View.VISIBLE
            btnNext.setOnClickListener {
                startActivity(Intent(this, QuizActivity::class.java).apply {
                    putExtra("category", category)
                    putExtra("level", newLevel)
                })
                finish()
            }
        } else {
            tvLevel.text = "Lvl $currentLevel"
            tvMsg.text = "Score 80% or above to reach the next level"
            tvMsg.setTextColor(Color.parseColor("#E74C3C"))
            btnNext.visibility = View.GONE
        }

        val db = FirebaseFirestore.getInstance()
        val etName = findViewById<EditText>(R.id.etPlayerName)
        findViewById<MaterialButton>(R.id.btnSaveScore).setOnClickListener {
            val name = etName?.text?.toString()?.trim() ?: "Anonymous"
            if (name.isNotEmpty()) {
                db.collection("leaderboard").add(mapOf(
                    "name" to name, "score" to score,
                    "total" to total, "cheats" to cheats,
                    "category" to category
                )).addOnSuccessListener {
                }
            }
        }

        findViewById<MaterialButton>(R.id.btnPlayAgain).setOnClickListener {
            startActivity(Intent(this, QuizActivity::class.java).apply {
                putExtra("category", category)
            })
            finish()
        }

        findViewById<MaterialButton>(R.id.btnHome).setOnClickListener {
            startActivity(Intent(this, MainActivity::class.java))
            finishAffinity()
        }
    }
}
package com.example.myapplication

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.myapplication.databinding.ActivityLeaderboardBinding
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.Query

class LeaderboardActivity : AppCompatActivity() {

    private lateinit var binding: ActivityLeaderboardBinding
    private val db = FirebaseFirestore.getInstance()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLeaderboardBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.rvLeaderboard.layoutManager = LinearLayoutManager(this)
        binding.btnBack.setOnClickListener { finish() }
        loadLeaderboard()
    }

    private fun loadLeaderboard() {
        db.collection("leaderboard")
            .orderBy("score", Query.Direction.DESCENDING)
            .limit(20)
            .get()
            .addOnSuccessListener { docs ->
                val entries = docs.map { doc ->
                    LeaderEntry(
                        doc.getString("name") ?: "Anonymous",
                        doc.getLong("score")?.toInt() ?: 0,
                        doc.getLong("total")?.toInt() ?: 17
                    )
                }
                binding.rvLeaderboard.adapter = LeaderboardAdapter(entries)
            }
            .addOnFailureListener {
                Toast.makeText(this, "Could not load leaderboard.", Toast.LENGTH_SHORT).show()
            }
    }
}

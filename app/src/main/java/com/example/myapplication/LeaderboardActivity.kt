package com.example.myapplication

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.myapplication.databinding.ActivityLeaderboardBinding
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.Query
import java.text.SimpleDateFormat
import java.util.*

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
            .limit(100)
            .get()
            .addOnSuccessListener { docs ->
                val fmt = SimpleDateFormat("MMM d, yyyy", Locale.getDefault())
                val entries = docs.map { doc ->
                    val ts = doc.getTimestamp("date")
                    val dateStr = if (ts != null) fmt.format(ts.toDate()) else ""
                    LeaderEntry(
                        name     = doc.getString("name") ?: "Anonymous",
                        score    = doc.getLong("score")?.toInt() ?: 0,
                        total    = doc.getLong("total")?.toInt() ?: 0,
                        cheats   = doc.getLong("cheats")?.toInt() ?: 0,
                        category = doc.getString("category") ?: "",
                        date     = dateStr,
                        level    = doc.getLong("level")?.toInt() ?: 1
                    )
                }
                binding.rvLeaderboard.adapter = LeaderboardAdapter(entries)
            }
            .addOnFailureListener {
                Toast.makeText(this, "Could not load leaderboard.", Toast.LENGTH_SHORT).show()
            }
    }
}

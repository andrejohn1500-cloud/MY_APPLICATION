package com.example.myapplication

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.myapplication.databinding.ActivityLeaderboardBinding
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.ListenerRegistration
import com.google.firebase.firestore.Query
import java.text.SimpleDateFormat
import java.util.*

class LeaderboardActivity : AppCompatActivity() {

    private lateinit var binding: ActivityLeaderboardBinding
    private val db = FirebaseFirestore.getInstance()
    private var listener: ListenerRegistration? = null
    private var allEntries: List<LeaderEntry> = emptyList()
    private var selectedCategory = "All"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLeaderboardBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.rvLeaderboard.layoutManager = LinearLayoutManager(this)
        binding.btnBack.setOnClickListener { finish() }
        loadLeaderboard()
    }

    private fun loadLeaderboard() {
        listener = db.collection("leaderboard")
            .orderBy("score", Query.Direction.DESCENDING)
            .limit(100)
            .addSnapshotListener { docs, error ->
                if (error != null) {
                    Toast.makeText(this, "Could not load leaderboard.", Toast.LENGTH_SHORT).show()
                    return@addSnapshotListener
                }
                val fmt = SimpleDateFormat("MMM d, yyyy", Locale.getDefault())
                allEntries = docs?.map { doc ->
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
                } ?: emptyList()
                applyFilter()
            }
    }

    private fun applyFilter() {
        val filtered = if (selectedCategory == "All") allEntries
                       else allEntries.filter { it.category == selectedCategory }
        if (binding.rvLeaderboard.adapter == null) {
            binding.rvLeaderboard.adapter = LeaderboardAdapter(filtered)
        } else {
            (binding.rvLeaderboard.adapter as LeaderboardAdapter).updateEntries(filtered)
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        listener?.remove()
    }
}

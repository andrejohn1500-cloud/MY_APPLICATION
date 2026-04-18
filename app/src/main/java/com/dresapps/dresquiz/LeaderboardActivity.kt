package com.dresapps.dresquiz

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.dresapps.dresquiz.databinding.ActivityLeaderboardBinding
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.ListenerRegistration
import java.text.SimpleDateFormat
import java.util.*

class LeaderboardActivity : AppCompatActivity() {
    private lateinit var binding: ActivityLeaderboardBinding
    private val db = FirebaseFirestore.getInstance()
    private var listener: ListenerRegistration? = null
    private var allEntries: List<LeaderEntry> = emptyList()
    private var currentTab = "Global"
    private var myCountry = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLeaderboardBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.rvLeaderboard.layoutManager = LinearLayoutManager(this)
        binding.btnBack.setOnClickListener { finish() }
        binding.btnTabGlobal.setOnClickListener { switchTab("Global") }
        binding.btnTabCountry.setOnClickListener { switchTab("Country") }
        binding.btnTabCategory.setOnClickListener { switchTab("Category") }
        highlightTab("Global")
        loadLeaderboard()
    }

    private fun highlightTab(tab: String) {
        val gold = android.graphics.Color.parseColor("#FFA500")
        val dim = android.graphics.Color.parseColor("#2A2A4A")
        binding.btnTabGlobal.setBackgroundColor(if (tab == "Global") gold else dim)
        binding.btnTabCountry.setBackgroundColor(if (tab == "Country") gold else dim)
        binding.btnTabCategory.setBackgroundColor(if (tab == "Category") gold else dim)
    }

    private fun switchTab(tab: String) {
        currentTab = tab
        highlightTab(tab)
        if (tab == "Country" && myCountry.isEmpty()) showCountrySelector()
        else applyFilter()
    }

    private fun showCountrySelector() {
        val countries = arrayOf("Anguilla","Antigua & Barbuda","Barbados","Belize",
            "British Virgin Islands","Cayman Islands","Dominica","Grenada",
            "Guyana","Jamaica","Montserrat","St. Kitts & Nevis",
            "St. Lucia","St. Vincent & the Grenadines","Trinidad & Tobago",
            "Turks & Caicos Islands")
        android.app.AlertDialog.Builder(this)
            .setTitle("Select Your Country")
            .setItems(countries) { _, w ->
                myCountry = countries[w]
                binding.btnTabCountry.text = myCountry
                applyFilter()
            }
            .setNegativeButton("Cancel", null).show()
    }

    private fun loadLeaderboard() {
        listener = db.collection("leaderboard").limit(200)
            .addSnapshotListener { docs, error ->
                if (error != null) {
                    Toast.makeText(this, "Error: ${error.message}", Toast.LENGTH_LONG).show()
                    return@addSnapshotListener
                }
                val fmt = SimpleDateFormat("MMM d, yyyy", java.util.Locale.getDefault())
                allEntries = docs?.mapNotNull { doc ->
                    try {
                        val tsLong = doc.getLong("timestamp")
                        val ts = if (tsLong != null) com.google.firebase.Timestamp(tsLong / 1000, 0) else null
                        LeaderEntry(
                            name = doc.getString("name") ?: "Anonymous",
                            score = doc.getLong("score")?.toInt() ?: 0,
                            total = doc.getLong("total")?.toInt() ?: 0,
                            cheats = doc.getLong("cheats")?.toInt() ?: 0,
                            category = doc.getString("category") ?: "",
                            date = if (ts != null) fmt.format(java.util.Date(ts.seconds * 1000)) else "",
                            level = doc.getLong("level")?.toInt() ?: 1,
                            country = doc.getString("country") ?: "",
                            rating = doc.getLong("rating")?.toInt() ?: 0
                        )
                    } catch(e: Exception) { null }
                }?.sortedByDescending { it.rating } ?: emptyList()
                applyFilter()
            }
    }

    private fun applyFilter() {
        val filtered = if (currentTab == "Country")
            allEntries.filter { it.country.contains(myCountry, ignoreCase = true) || myCountry.contains(it.country, ignoreCase = true) }
        else allEntries
        if (binding.rvLeaderboard.adapter == null)
            binding.rvLeaderboard.adapter = LeaderboardAdapter(filtered)
        else
            (binding.rvLeaderboard.adapter as LeaderboardAdapter).updateEntries(filtered)
    }

    override fun onDestroy() { super.onDestroy(); listener?.remove() }
}
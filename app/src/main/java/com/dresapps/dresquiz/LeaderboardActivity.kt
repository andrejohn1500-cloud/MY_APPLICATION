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
    private var selectedCategory = "All"
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
        // Load saved country from profile
        val profilePrefs = getSharedPreferences("player_prefs", MODE_PRIVATE)
        val savedCountry = profilePrefs.getString("p_country", "") ?: ""
        if (savedCountry.isNotEmpty()) myCountry = savedCountry
        loadLeaderboard()
    }

    private fun highlightTab(tab: String) {
        val gold = android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#FFA500"))
        val dim  = android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#2A2A4A"))
        binding.btnTabGlobal.backgroundTintList    = if (tab == "Global")   gold else dim
        binding.btnTabCountry.backgroundTintList   = if (tab == "Country")  gold else dim
        binding.btnTabCategory.backgroundTintList  = if (tab == "Category") gold else dim
        binding.btnTabGlobal.setTextColor(if (tab == "Global") android.graphics.Color.BLACK else android.graphics.Color.WHITE)
        binding.btnTabCountry.setTextColor(if (tab == "Country") android.graphics.Color.BLACK else android.graphics.Color.WHITE)
        binding.btnTabCategory.setTextColor(if (tab == "Category") android.graphics.Color.BLACK else android.graphics.Color.WHITE)
    }

    private fun switchTab(tab: String) {
        currentTab = tab
        highlightTab(tab)
        when {
            tab == "Country" && myCountry.isEmpty() -> showCountrySelector()
            tab == "Category" -> showCategorySelector()
            else -> applyFilter()
        }
    }

    private fun showCountrySelector() {
        val countries = arrayOf("Anguilla","Antigua & Barbuda","Barbados","Belize",
                "British Virgin Islands","Canada","Cayman Islands","Dominica",
                "France","Grenada","Guyana","Jamaica","Montserrat",
                "Netherlands","St. Kitts & Nevis","St. Lucia",
                "St. Vincent and the Grenadines","Spain","Trinidad & Tobago",
                "Turks & Caicos Islands","UK","USA")
        android.app.AlertDialog.Builder(this)
            .setTitle("Select Your Country")
            .setItems(countries) { _, w ->
                myCountry = countries[w]
                binding.btnTabCountry.text = myCountry
                applyFilter()
            }
            .setNegativeButton("Cancel", null).show()
    }

    private fun showCategorySelector() {
        val cats = arrayOf("All","Caribbean History","Science & Tech","Sports","World Geography",
            "Arts & Culture","SVG & Vincy Life","CXC English A","CXC English B","CXC Maths",
            "CXC Integrated Science","CXC Social Studies","CXC Geography","CXC POB","CXC IT",
            "CXC Office Admin","CXC Physical Education")
        android.app.AlertDialog.Builder(this)
            .setTitle("Select Category")
            .setItems(cats) { _, w ->
                selectedCategory = cats[w]
                binding.btnTabCategory.text = if (selectedCategory == "All") "Category" else selectedCategory.take(10)
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
        var filtered = allEntries.sortedByDescending { it.rating }
        if (currentTab == "Country" && myCountry.isNotEmpty())
            filtered = filtered.filter {
                val c = it.country.trim()
                val m = myCountry.trim()
                c.contains(m, ignoreCase = true) || m.contains(c, ignoreCase = true) ||
                // Handle SVG name variants
                (m.contains("Vincent", ignoreCase = true) && c.contains("Vincent", ignoreCase = true))
            }
        if (currentTab == "Category" && selectedCategory != "All")
            filtered = filtered.filter { it.category.contains(selectedCategory, ignoreCase = true) }
        if (binding.rvLeaderboard.adapter == null)
            binding.rvLeaderboard.adapter = LeaderboardAdapter(filtered)
        else
            (binding.rvLeaderboard.adapter as LeaderboardAdapter).updateEntries(filtered)
    }

    override fun onResume() {
        super.onResume()
        val profilePrefs = getSharedPreferences("player_prefs", MODE_PRIVATE)
        val savedCountry = profilePrefs.getString("p_country", "") ?: ""
        val shortLabel2 = when (savedCountry) {
            "St. Vincent and the Grenadines" -> "St. Vincent"
            "Trinidad & Tobago" -> "T&T"
            "British Virgin Islands" -> "BVI"
            "Turks & Caicos Islands" -> "Turks & Caicos"
            "Antigua & Barbuda" -> "Antigua"
            else -> savedCountry
        }
        if (savedCountry.isNotEmpty()) {
            myCountry = savedCountry
            binding.btnTabCountry.text = shortLabel2
            highlightTab("Country")
            applyFilter()
        }
    }

    override fun onDestroy() { super.onDestroy(); listener?.remove() }
}
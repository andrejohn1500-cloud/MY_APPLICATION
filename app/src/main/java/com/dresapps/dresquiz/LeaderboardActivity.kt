package com.dresapps.dresquiz

import android.os.Bundle
import android.view.Gravity
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.dresapps.dresquiz.databinding.ActivityLeaderboardBinding
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
    private var currentTab = "Global"
    private var myCountry = ""

    // Tab button refs for highlight
    private lateinit var btnGlobal: Button
    private lateinit var btnCountry: Button
    private lateinit var btnCategory: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLeaderboardBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.rvLeaderboard.layoutManager = LinearLayoutManager(this)
        binding.btnBack.setOnClickListener { finish() }

        buildTabBar()
        loadLeaderboard()
    }

    private fun buildTabBar() {
        // Insert tab row programmatically above RecyclerView
        val parent = binding.rvLeaderboard.parent as android.view.ViewGroup
        val rvIndex = (0 until parent.childCount).first { parent.getChildAt(it) == binding.rvLeaderboard }

        val row = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity     = Gravity.CENTER
            setPadding(12, 16, 12, 8)
        }

        fun makeTab(label: String): Button = Button(this).apply {
            text      = label
            textSize  = 12f
            isAllCaps = false
            setTextColor(android.graphics.Color.WHITE)
            layoutParams = LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1f).apply {
                setMargins(6, 0, 6, 0)
            }
            background = android.graphics.drawable.GradientDrawable().apply {
                cornerRadius = 24f
                setColor(android.graphics.Color.parseColor("#555577"))
            }
        }

        btnGlobal   = makeTab("🌍 Global")
        btnCountry  = makeTab("🏳️ My Country")
        btnCategory = makeTab("📚 Category")

        btnGlobal.setOnClickListener   { switchTab("Global") }
        btnCountry.setOnClickListener  { switchTab("Country") }
        btnCategory.setOnClickListener { switchTab("Category") }

        row.addView(btnGlobal)
        row.addView(btnCountry)
        row.addView(btnCategory)
        parent.addView(row, rvIndex)

        highlightTab("Global")
    }

    private fun highlightTab(tab: String) {
        val gold = android.graphics.Color.parseColor("#FFA500")
        val dim  = android.graphics.Color.parseColor("#555577")
        listOf(btnGlobal to "Global", btnCountry to "Country", btnCategory to "Category").forEach { (btn, t) ->
            (btn.background as android.graphics.drawable.GradientDrawable).setColor(if (t == tab) gold else dim)
        }
    }

    private fun switchTab(tab: String) {
        currentTab = tab
        highlightTab(tab)
        if (tab == "Country" && myCountry.isEmpty()) showCountrySelector()
        else applyFilter()
    }

    private fun showCountrySelector() {
        val countries = arrayOf(
            "🇦🇮 Anguilla", "🇦🇬 Antigua & Barbuda", "🇧🇧 Barbados", "🇧🇿 Belize",
            "🇻🇬 British Virgin Islands", "🇰🇾 Cayman Islands", "🇩🇲 Dominica", "🇬🇩 Grenada",
            "🇬🇾 Guyana", "🇯🇲 Jamaica", "🇲🇸 Montserrat", "🇰🇳 St. Kitts & Nevis",
            "🇱🇨 St. Lucia", "🇻🇨 St. Vincent & the Grenadines", "🇹🇹 Trinidad & Tobago",
            "🇹🇨 Turks & Caicos Islands"
        )
        android.app.AlertDialog.Builder(this)
            .setTitle("🌍 Your Country")
            .setItems(countries) { _, which ->
                myCountry = countries[which]
                btnCountry.text = myCountry
                applyFilter()
            }
            .setNegativeButton("Cancel", null)
            .show()
    }

    private fun loadLeaderboard() {
        listener = db.collection("leaderboard")
            .orderBy("rating", Query.Direction.DESCENDING)
            .limit(200)
            .addSnapshotListener { docs, error ->
                if (error != null) {
                    Toast.makeText(this, "Could not load leaderboard.", Toast.LENGTH_SHORT).show()
                    return@addSnapshotListener
                }
                val fmt = SimpleDateFormat("MMM d, yyyy", Locale.getDefault())
                allEntries = docs?.map { doc ->
                    val ts      = doc.getTimestamp("timestamp")
                    val dateStr = if (ts != null) fmt.format(Date(ts.seconds * 1000)) else ""
                    LeaderEntry(
                        name     = doc.getString("name")            ?: "Anonymous",
                        score    = doc.getLong("score")?.toInt()    ?: 0,
                        total    = doc.getLong("total")?.toInt()    ?: 0,
                        cheats   = doc.getLong("cheats")?.toInt()   ?: 0,
                        category = doc.getString("category")        ?: "",
                        date     = dateStr,
                        level    = doc.getLong("level")?.toInt()    ?: 1,
                        country  = doc.getString("country")         ?: "",
                        rating   = doc.getLong("rating")?.toInt()   ?: 0
                    )
                } ?: emptyList()
                applyFilter()
            }
    }

    private fun applyFilter() {
        var filtered = if (selectedCategory == "All") allEntries
                       else allEntries.filter { it.category == selectedCategory }
        filtered = when (currentTab) {
            "Country"  -> filtered.filter { it.country == myCountry }
            else       -> filtered
        }
        if (binding.rvLeaderboard.adapter == null)
            binding.rvLeaderboard.adapter = LeaderboardAdapter(filtered)
        else
            (binding.rvLeaderboard.adapter as LeaderboardAdapter).updateEntries(filtered)
    }

    override fun onDestroy() {
        super.onDestroy()
        listener?.remove()
    }
}

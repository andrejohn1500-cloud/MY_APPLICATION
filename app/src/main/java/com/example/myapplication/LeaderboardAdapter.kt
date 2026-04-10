package com.example.myapplication

import android.graphics.Color
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

data class LeaderEntry(
    val name: String,
    val score: Int,
    val total: Int,
    val cheats: Int = 0,
    val category: String = "",
    val date: String = "",
    val level: Int = 1
)

class LeaderboardAdapter(private var entries: List<LeaderEntry>) :
    RecyclerView.Adapter<LeaderboardAdapter.VH>() {

    inner class VH(v: View) : RecyclerView.ViewHolder(v) {
        val tvRank:     TextView = v.findViewById(R.id.tvRank)
        val tvName:     TextView = v.findViewById(R.id.tvName)
        val tvScore:    TextView = v.findViewById(R.id.tvLeaderScore)
        val tvCategory: TextView = v.findViewById(R.id.tvLeaderCategory)
        val tvLevel:    TextView = v.findViewById(R.id.tvLeaderLevel)
        val tvCheats:   TextView = v.findViewById(R.id.tvLeaderCheats)
        val tvDate:     TextView = v.findViewById(R.id.tvLeaderDate)
        val cardRoot:   View     = v.findViewById(R.id.cardRoot)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) =
        VH(LayoutInflater.from(parent.context).inflate(R.layout.item_leaderboard, parent, false))

    override fun onBindViewHolder(holder: VH, position: Int) {
        val e = entries[position]

        // Rank badge + card accent
        when (position) {
            0 -> {
                holder.tvRank.text = "🥇"
                holder.cardRoot.setBackgroundColor(Color.parseColor("#2A1F00"))
            }
            1 -> {
                holder.tvRank.text = "🥈"
                holder.cardRoot.setBackgroundColor(Color.parseColor("#1A1F2A"))
            }
            2 -> {
                holder.tvRank.text = "🥉"
                holder.cardRoot.setBackgroundColor(Color.parseColor("#1F1510"))
            }
            else -> {
                holder.tvRank.text = "${position + 1}"
                holder.cardRoot.setBackgroundColor(Color.parseColor("#1A1E3A"))
            }
        }

        holder.tvName.text  = e.name
        holder.tvScore.text = "${e.score}/${e.total}"
        holder.tvCategory.text = e.category.ifBlank { "General" }
        holder.tvLevel.text = "Lvl ${e.level}"
        holder.tvDate.text  = e.date

        if (e.cheats > 0) {
            holder.tvCheats.text = "⚠️ ${e.cheats} cheat${if (e.cheats > 1) "s" else ""}"
            holder.tvCheats.visibility = View.VISIBLE
        } else {
            holder.tvCheats.text = "✅ Clean"
            holder.tvCheats.setTextColor(Color.parseColor("#1DB954"))
            holder.tvCheats.visibility = View.VISIBLE
        }
    }

    override fun getItemCount() = entries.size

    fun updateEntries(newEntries: List<LeaderEntry>) {
        entries = newEntries
        notifyDataSetChanged()
    }
}

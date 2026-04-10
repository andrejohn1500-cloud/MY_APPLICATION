package com.example.myapplication

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

data class LeaderEntry(val name: String, val score: Int, val total: Int, val cheats: Int = 0)

class LeaderboardAdapter(private val entries: List<LeaderEntry>) :
    RecyclerView.Adapter<LeaderboardAdapter.VH>() {

    inner class VH(v: View) : RecyclerView.ViewHolder(v) {
        val tvRank:  TextView = v.findViewById(R.id.tvRank)
        val tvName:  TextView = v.findViewById(R.id.tvName)
        val tvScore: TextView = v.findViewById(R.id.tvLeaderScore)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) =
        VH(LayoutInflater.from(parent.context).inflate(R.layout.item_leaderboard, parent, false))

    override fun onBindViewHolder(holder: VH, position: Int) {
        val e = entries[position]
        holder.tvRank.text  = when (position) { 0 -> "🥇"; 1 -> "🥈"; 2 -> "🥉"; else -> "${position + 1}." }
        holder.tvName.text  = e.name
        holder.tvScore.text = "${e.score}/${e.total}" + if (e.cheats > 0) "  🎯${e.cheats}" else ""
    }

    override fun getItemCount() = entries.size
}

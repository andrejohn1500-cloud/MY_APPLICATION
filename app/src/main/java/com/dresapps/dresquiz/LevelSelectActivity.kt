package com.dresapps.dresquiz
import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class LevelSelectActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val category = intent.getStringExtra("category") ?: return finish()
        val isPremium = AppPreferences.isPremium(this)
        val highest = AppPreferences.getHighestLevel(this, category)
        val scroll = ScrollView(this)
        val root = LinearLayout(this)
        root.orientation = LinearLayout.VERTICAL
        root.setBackgroundColor(Color.parseColor("#1A1D2E"))
        root.setPadding(32, 48, 32, 48)
        scroll.addView(root)

        val title = TextView(this)
        title.text = category
        title.textSize = 22f
        title.setTextColor(Color.parseColor("#FFA500"))
        title.gravity = android.view.Gravity.CENTER
        title.setPadding(0, 0, 0, 24)
        root.addView(title)

        if (!isPremium) {
            val banner = LinearLayout(this)
            banner.orientation = LinearLayout.VERTICAL
            banner.setBackgroundColor(Color.parseColor("#2A1A0E"))
            banner.setPadding(24, 24, 24, 24)
            val blp = LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT)
            blp.bottomMargin = 24
            banner.layoutParams = blp

            val t1 = TextView(this)
            t1.text = "Levels 3-20 Locked"
            t1.textSize = 16f
            t1.setTextColor(Color.WHITE)
            t1.gravity = android.view.Gravity.CENTER
            banner.addView(t1)

            val t2 = TextView(this)
            t2.text = "Unlock ALL levels forever for just USD2.99"
            t2.textSize = 13f
            t2.setTextColor(Color.parseColor("#FFA500"))
            t2.gravity = android.view.Gravity.CENTER
            t2.setPadding(0, 8, 0, 16)
            banner.addView(t2)

            val unlockBtn = Button(this)
            unlockBtn.text = "UNLOCK NOW - USD2.99"
            unlockBtn.textSize = 15f
            unlockBtn.setTextColor(Color.BLACK)
            unlockBtn.backgroundTintList = android.content.res.ColorStateList.valueOf(Color.parseColor("#FFA500"))
            unlockBtn.setOnClickListener {
                startActivity(Intent(Intent.ACTION_VIEW, android.net.Uri.parse("https://www.paypal.com/ncp/payment/Z48JTL598SJG8")))
            }
            banner.addView(unlockBtn)
            root.addView(banner)
        }

        val grid = GridLayout(this)
        grid.columnCount = 4
        grid.layoutParams = LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT)

        for (lvl in 1..20) {
            val unlocked = isPremium || lvl <= 2
            val beaten = lvl <= highest
            val isCurrent = lvl == highest + 1

            val btn = Button(this)
            btn.text = if (!unlocked) "[L$lvlFinal]" else if (beaten) "[V$lvlFinal]" else "$lvlFinal"
            btn.textSize = 12f

            val lp = GridLayout.LayoutParams()
            lp.width = 0
            lp.columnSpec = GridLayout.spec(GridLayout.UNDEFINED, 1f)
            lp.setMargins(8, 8, 8, 8)
            btn.layoutParams = lp

            val bgColor = if (!unlocked) "#2A2A3A" else if (beaten) "#1B3A1B" else if (isCurrent) "#3A2A00" else "#2A2F52"
            btn.backgroundTintList = android.content.res.ColorStateList.valueOf(Color.parseColor(bgColor))
            btn.setTextColor(if (unlocked) Color.WHITE else Color.parseColor("#555555"))
            btn.isEnabled = unlocked
            val lvlFinal = lvl
            btn.setOnClickListener {
                val i = Intent(this, QuizActivity::class.java)
                i.putExtra("category", category)
                i.putExtra("level", lvlFinal)
                startActivity(i)
            }
            grid.addView(btn)
        }
        root.addView(grid)
        setContentView(scroll)
    }
}

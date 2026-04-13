package com.dresapps.dresquiz
import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class LevelSelectActivity : AppCompatActivity() {
    private val PAYPAL_URL = "https://www.paypal.com/ncp/payment/Z48JTL598SJG8"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val category = intent.getStringExtra("category") ?: return finish()
        val isPremium = AppPreferences.isPremium(this)
        val highest = AppPreferences.getHighestLevel(this, category)

        val scroll = ScrollView(this)
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setBackgroundColor(Color.parseColor("#1A1D2E"))
            setPadding(32, 48, 32, 48)
        }
        scroll.addView(root)

        root.addView(TextView(this).apply {
            text = category
            textSize = 22f
            setTextColor(Color.parseColor("#FFA500"))
            gravity = android.view.Gravity.CENTER
            setPadding(0, 0, 0, 24)
        })

            val banner = LinearLayout(this).apply {
                orientation = LinearLayout.VERTICAL
                setBackgroundColor(Color.parseColor("#2A1A0E"))
                setPadding(24, 24, 24, 24)
                layoutParams = LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT).also { it.bottomMargin = 24 }
            }
            banner.addView(TextView(this).apply {
                text = "🔒 Levels 3-20 Locked"
                textSize = 16f; setTextColor(Color.WHITE)
                gravity = android.view.Gravity.CENTER
            })
            banner.addView(TextView(this).apply {
                text = "Unlock ALL levels forever for just $2.99"
                textSize = 13f; setTextColor(Color.parseColor("#FFA500"))
                gravity = android.view.Gravity.CENTER
                setPadding(0, 8, 0, 16)
            })
            banner.addView(Button(this).apply {
                text = "UNLOCK NOW — $2.99"
                textSize = 15f; setTextColor(Color.BLACK)
                backgroundTintList = android.content.res.ColorStateList.valueOf(Color.parseColor("#FFA500"))
                setOnClickListener { openPayPal() }
            })
            root.addView(banner)
        }

        val grid = GridLayout(this).apply {
            columnCount = 4
            layoutParams = LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT)
        }

        for (lvl in 1..20) {
            val unlocked = isPremium || lvl <= 2
            val beaten = lvl < highest || (lvl == highest)
            val isCurrent = lvl == highest + 1
            val btn = Button(this).apply {
                textSize = 12f
                layoutParams = GridLayout.LayoutParams().apply {
                    width = 0; columnSpec = GridLayout.spec(GridLayout.UNDEFINED, 1f)
                    setMargins(8, 8, 8, 8)
                }
                backgroundTintList = android.content.res.ColorStateList.valueOf(Color.parseColor(
                ))
                setTextColor(if (unlocked) Color.WHITE else Color.parseColor("#555555"))
                isEnabled = unlocked
                setOnClickListener {
                    startActivity(Intent(this@LevelSelectActivity, QuizActivity::class.java).also {
                        it.putExtra("category", category); it.putExtra("level", lvl)
                    })
                }
            }
            grid.addView(btn)
        }
        root.addView(grid)
        setContentView(scroll)
    }

    private fun openPayPal() {
        startActivity(Intent(Intent.ACTION_VIEW, android.net.Uri.parse(PAYPAL_URL)))
    }
}

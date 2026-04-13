package com.dresapps.dresquiz

import android.content.Intent
import android.content.res.ColorStateList
import android.os.Bundle
import android.view.Gravity
import android.widget.LinearLayout
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.dresapps.dresquiz.databinding.ActivityCategoryBinding

class CategoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCategoryBinding

    // ============================================================
    // ADD NEW CATEGORIES HERE — buttons generate automatically
    // ============================================================
    private val categories = listOf(
        "🌍  Caribbean History",
        "🔬  Science & Tech",
        "⚽  Sports",
        "🗺️  World Geography",
        "🎭  Arts & Culture",
        "🇻🇨 SVG & Vincy Life",
        // Add new categories below this
        "CXC English A",
        "CXC English B",
        "CXC Maths",
        "CXC Integrated Science",
        "CXC Social Studies",
        "CXC Geography",
        "CXC POB",
        "CXC IT",
        "CXC Office Admin",
        "CXC Physical Education",
        // "🍽️  Food & Cuisine",
        // "🎵  Music & Dance"
    )

    // Soft amber — matches Main Menu text color
    private val TEXT_COLOR   = "#FFC107"
    private val BUTTON_COLOR = "#2A2F52"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCategoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val vib = getSystemService(android.content.Context.VIBRATOR_SERVICE) as android.os.Vibrator
        fun buzz() {
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                vib.vibrate(android.os.VibrationEffect.createOneShot(25, android.os.VibrationEffect.DEFAULT_AMPLITUDE))
            } else {
                vib.vibrate(25)
            }
        }

        val container = binding.categoryContainer
        val density   = resources.displayMetrics.density

        fun dp(value: Int) = (value * density).toInt()

        // Add top spacing to separate from SELECT CATEGORY heading
        val topSpacer = android.view.View(this)
        topSpacer.layoutParams = LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, dp(16)
        )
        container.addView(topSpacer)

        categories.forEach { category ->
            val btn = Button(this)
            btn.text              = category
            btn.textSize          = 15f
            btn.letterSpacing     = 0.08f
            btn.isAllCaps         = true
            btn.gravity           = Gravity.CENTER
            btn.setTextColor(android.graphics.Color.parseColor(TEXT_COLOR))
            btn.backgroundTintList = ColorStateList.valueOf(
                android.graphics.Color.parseColor(BUTTON_COLOR)
            )
            btn.stateListAnimator = null

            // Auto-equal spacing: each button gets same weight
            val params = LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                dp(64),
                1f  // weight — all buttons share space equally
            )
            params.bottomMargin = dp(14)
            btn.layoutParams = params

            btn.setOnClickListener {
                buzz()
                val intent = Intent(this@CategoryActivity, LevelSelectActivity::class.java)
                intent.putExtra("category", category)
                startActivity(intent)
            }
            container.addView(btn)
        }
    }
}

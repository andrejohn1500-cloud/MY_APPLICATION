kt = '''package com.example.myapplication

import android.content.Intent
import android.os.Bundle
import android.view.Gravity
import android.widget.LinearLayout
import android.widget.Button
import android.content.res.ColorStateList
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityCategoryBinding

class CategoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCategoryBinding

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
        val dpToPx = { dp: Int -> (dp * resources.displayMetrics.density).toInt() }

        QuestionBank.categories.forEach { category ->
            val btn = android.widget.Button(this).apply {
                text                = category
                textSize            = 15f
                letterSpacing       = 0.08f
                isAllCaps           = true
                gravity             = Gravity.CENTER
                setTextColor(android.graphics.Color.parseColor("#FFD700"))
                backgroundTintList  = ColorStateList.valueOf(android.graphics.Color.parseColor("#2A2F52"))
                stateListAnimator   = null
                val params = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    dpToPx(68)
                ).apply { bottomMargin = dpToPx(14) }
                layoutParams = params
                setOnClickListener {
                    buzz()
                    val intent = Intent(this@CategoryActivity, QuizActivity::class.java)
                    intent.putExtra("category", category)
                    startActivity(intent)
                }
            }
            container.addView(btn)
        }
    }
}
'''

open("./app/src/main/java/com/example/myapplication/CategoryActivity.kt", "w").write(kt)
print("Done")

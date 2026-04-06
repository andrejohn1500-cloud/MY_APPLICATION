package com.example.myapplication

import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.view.Gravity
import android.widget.Button
import android.widget.GridLayout
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityCategoryBinding

class CategoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCategoryBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val vib = getSystemService(android.content.Context.VIBRATOR_SERVICE) as android.os.Vibrator
        fun buzz() {
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                vib.vibrate(android.os.VibrationEffect.createOneShot(25, android.os.VibrationEffect.DEFAULT_AMPLITUDE))
            } else { vib.vibrate(25) }
        }

        binding = ActivityCategoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val grid = binding.gridCategories

        QuestionBank.categories.forEachIndexed { index, category ->
            val btn = Button(this).apply {
                text = category
                textSize = 14f
                setTextColor(Color.WHITE)
                gravity = Gravity.CENTER
                setBackgroundResource(R.drawable.bg_category)
                setPadding(16, 28, 16, 28)
                val params = GridLayout.LayoutParams().apply {
                    width  = 0
                    height = GridLayout.LayoutParams.WRAP_CONTENT
                    columnSpec = GridLayout.spec(index % 2, 1, 1f)
                    rowSpec    = GridLayout.spec(index / 2, 1, 1f)
                    setMargins(12, 12, 12, 12)
                }
                layoutParams = params
                setOnClickListener {
                    val intent = Intent(this@CategoryActivity, QuizActivity::class.java)
                    intent.putExtra("category", category)
                    startActivity(intent)
                }
            }
            grid.addView(btn)
        }
    }
}

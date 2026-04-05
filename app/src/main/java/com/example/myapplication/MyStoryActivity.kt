package com.example.myapplication

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityMyStoryBinding

class MyStoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMyStoryBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMyStoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.tvStory.text = """My Story — Andre N. John

On June 14, 2025, my life changed in a single moment.

I was on duty as a Police Constable with the Special Service Unit of the Royal St. Vincent and the Grenadines Police Force — serving my country with pride and purpose — when I was seriously injured in the line of duty.

What followed was nearly a year at home. A year of stillness, reflection, and at times, real uncertainty about what the future held. But through it all, one truth anchored me — God is faithful. Every morning I opened my eyes was a reminder that my life had been spared for a reason, and that reason was worth fighting for.

In that season of recovery, I made a decision. If I could not be out in the world, I would create something for it.

With no formal training in app development, I taught myself — through failure, persistence, and faith. DREs Quizz was born in that recovery room, built question by question, screen by screen, by a man determined to turn a difficult chapter into something meaningful.

This app is my testimony. It is proof that resilience is not the absence of struggle — it is what you build in the middle of it.

If this game has brought you joy, I give God the glory. And if you feel moved to support the journey behind it, a small donation through PayPal would mean the world to me.

Thank you for playing. Thank you for reading. And above all — thank God for life.

— Andre N. John
Police Constable #738 | Special Service Unit
Royal St. Vincent and the Grenadines Police Force

"Built in stillness. Released with purpose."
        """.trimIndent()

        binding.btnBackStory.setOnClickListener { finish() }
    }
}

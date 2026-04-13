package com.dresapps.dresquiz

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.dresapps.dresquiz.databinding.ActivityMyStoryBinding

class MyStoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMyStoryBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMyStoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.tvStory.text = """
My Story — Andre N. John

I grew up in St. Vincent with no electricity, no running water, and no guarantees. We washed clothes at the river on weekends. We cooked by lantern light. We borrowed water from neighbours so we wouldn't seem too dependent. We made do quietly, without complaint. That was the simple life.

I was a quiet child. Raised in the Seventh-day Adventist Church, academically just above average, full of imagination. At five years old I flew to New York for the first time. At eight, I went again. I walked through the Bronx Zoo, stared up at the Statue of Liberty, and ran races on the block for small prizes I was both delighted and grateful to win. I came home to St. Vincent and told myself I wanted to be a pilot.

Dreams evolve. Life redirects.

I eventually found purpose in service and was assigned to the Special Service Unit of the Royal St. Vincent and the Grenadines Police Force.

On June 14, 2025, I was seriously injured in the line of duty.

What followed was months at home. Still. Grounded. Uncertain about what came next. But lying on my bed in recovery, the same kind of stillness I once knew as a boy waiting for the lantern to be lit, something took shape. A vision. Clear and steady.

I would build something.

With no formal training in software development, I taught myself. I failed often. I kept going. DREs Quiz was built from that bed, question by question, screen by screen.

It began with one simple intention: to help my son, a Form 5 student at St. Martin's Secondary School, prepare for his CXC examinations. What started as a father's instinct to support his child grew into something I never anticipated.

It became an app tailored for every Caribbean student who deserves better tools to learn.

I give God the glory for one reason above all. I am still here!

I did not get here alone. To my family and friends who carried this season with me financially, mentally, and spiritually, I see every one of you.

This journey has had a real toll on the John's family, and not a single sacrifice made on my behalf has gone unnoticed.

Whether you gave, prayed, called, sat with me, or drove me to and from the hospital time and time again without complaint, you are woven into every part of this.

This app is for the student who thinks they are not smart enough. It is for the young Vincentian who has never seen their culture reflected in what they study. It is for anyone who needs proof that your beginning does not determine your ceiling.

Play hard. Learn something. Carry it with you.

Yours Truly,
Andre N. John

"Built in stillness. Released with purpose."
        """.trimIndent()

        binding.btnBackStory.setOnClickListener { finish() }
    }
}

content = open("./app/src/main/java/com/example/myapplication/MainActivity.kt").read()

old = "        binding.btnStart.setOnClickListener {"

new = """        // Set button backgrounds programmatically
        val goldColor = android.graphics.Color.parseColor("#FFD700")
        val navyAccent = android.graphics.Color.parseColor("#2A2F52")
        val darkText = android.graphics.Color.parseColor("#1A1D2E")

        binding.btnStart.setBackgroundColor(goldColor)
        binding.btnStart.setTextColor(darkText)
        binding.btnStart.stateListAnimator = null

        listOf(binding.btnLeaderboard, binding.btnDonate, binding.btnMyStory).forEach { btn ->
            btn.setBackgroundColor(navyAccent)
            btn.setTextColor(goldColor)
            btn.stateListAnimator = null
        }

        binding.btnStart.setOnClickListener {"""

content = content.replace(old, new)
open("./app/src/main/java/com/example/myapplication/MainActivity.kt", "w").write(content)
print("Done")

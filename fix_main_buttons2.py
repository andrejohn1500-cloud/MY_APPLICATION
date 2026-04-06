content = open("./app/src/main/java/com/example/myapplication/MainActivity.kt").read()

old = "        // Set button backgrounds programmatically"

new = """        // Set button backgrounds programmatically
        import android.content.res.ColorStateList"""

# Just patch the color setting approach
old2 = """        binding.btnStart.setBackgroundColor(goldColor)
        binding.btnStart.setTextColor(darkText)
        binding.btnStart.stateListAnimator = null

        listOf(binding.btnLeaderboard, binding.btnDonate, binding.btnMyStory).forEach { btn ->
            btn.setBackgroundColor(navyAccent)
            btn.setTextColor(goldColor)
            btn.stateListAnimator = null
        }"""

new2 = """        val goldList   = android.content.res.ColorStateList.valueOf(goldColor)
        val navyList   = android.content.res.ColorStateList.valueOf(navyAccent)
        val darkList   = android.content.res.ColorStateList.valueOf(darkText)

        binding.btnStart.backgroundTintList = goldList
        binding.btnStart.setTextColor(darkText)

        listOf(binding.btnLeaderboard, binding.btnDonate, binding.btnMyStory).forEach { btn ->
            btn.backgroundTintList = navyList
            btn.setTextColor(goldColor)
        }"""

content = content.replace(old2, new2)
open("./app/src/main/java/com/example/myapplication/MainActivity.kt", "w").write(content)
print("Done")

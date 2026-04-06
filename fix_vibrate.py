content = open("./app/src/main/java/com/example/myapplication/MainActivity.kt").read()

old = "        // Set button backgrounds programmatically"

new = """        // Vibrate helper
        val vib = getSystemService(android.content.Context.VIBRATOR_SERVICE) as android.os.Vibrator
        fun buzz() {
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                vib.vibrate(android.os.VibrationEffect.createOneShot(25, android.os.VibrationEffect.DEFAULT_AMPLITUDE))
            } else { vib.vibrate(25) }
        }

        listOf(binding.btnStart, binding.btnLeaderboard, binding.btnDonate, binding.btnMyStory).forEach { btn ->
            btn.setOnTouchListener { v, event ->
                if (event.action == android.view.MotionEvent.ACTION_DOWN) { buzz(); v.performClick() }
                false
            }
        }

        // Set button backgrounds programmatically"""

content = content.replace(old, new)
open("./app/src/main/java/com/example/myapplication/MainActivity.kt", "w").write(content)
print("Done")

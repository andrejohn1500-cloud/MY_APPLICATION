import os

buzz_helper = """
        val vib = getSystemService(android.content.Context.VIBRATOR_SERVICE) as android.os.Vibrator
        fun buzz() {
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                vib.vibrate(android.os.VibrationEffect.createOneShot(25, android.os.VibrationEffect.DEFAULT_AMPLITUDE))
            } else { vib.vibrate(25) }
        }
"""

# ── CategoryActivity ──────────────────────────────────────────────────────────
cat_path = "./app/src/main/java/com/example/myapplication/CategoryActivity.kt"
cat = open(cat_path).read()
if 'fun buzz()' not in cat:
    cat = cat.replace("super.onCreate(savedInstanceState)",
                      "super.onCreate(savedInstanceState)" + buzz_helper)
    # Add buzz to every button click
    cat = cat.replace(".setOnClickListener {", ".setOnClickListener { buzz();")
    open(cat_path, "w").write(cat)
    print("✅ CategoryActivity patched")
else:
    print("CategoryActivity already has buzz")

# ── QuizActivity ──────────────────────────────────────────────────────────────
quiz_path = "./app/src/main/java/com/example/myapplication/QuizActivity.kt"
quiz = open(quiz_path).read()
if 'fun buzz()' not in quiz:
    quiz = quiz.replace("super.onCreate(savedInstanceState)",
                        "super.onCreate(savedInstanceState)" + buzz_helper)
    quiz = quiz.replace(".setOnClickListener {", ".setOnClickListener { buzz();")
    open(quiz_path, "w").write(quiz)
    print("✅ QuizActivity patched")
else:
    print("QuizActivity already has buzz")

print("\nDone.")

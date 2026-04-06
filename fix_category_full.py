import re, os

# ── CONFIG — change these values easily in future ────────────────────────────
GOLD           = "#FFD700"
NAVY_ACCENT    = "#2A2F52"
HEADING_SIZE   = "28sp"
BTN_TEXT_SIZE  = "15sp"
BTN_HEIGHT_DP  = "68dp"
BTN_MARGIN_DP  = "14dp"
LETTER_SPACING = "0.08"
HEADING_TEXT   = "SELECT CATEGORY"

# ── XML — ScrollView + LinearLayout so buttons stack cleanly ─────────────────
xml = f'''<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/bg_main_gradient"
    android:fillViewport="true">

    <LinearLayout
        android:id="@+id/categoryContainer"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:gravity="center_horizontal"
        android:paddingStart="24dp"
        android:paddingEnd="24dp"
        android:paddingTop="48dp"
        android:paddingBottom="32dp">

        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="{HEADING_TEXT}"
            android:textColor="@color/gold"
            android:textSize="{HEADING_SIZE}"
            android:textStyle="bold"
            android:letterSpacing="{LETTER_SPACING}"
            android:gravity="center"
            android:layout_marginBottom="32dp"/>

    </LinearLayout>
</ScrollView>'''

# ── KOTLIN — clean builder function, easy to extend ──────────────────────────
kt_path  = "./app/src/main/java/com/example/myapplication/CategoryActivity.kt"
xml_path = "./app/src/main/res/layout/activity_category.xml"

kt = open(kt_path).read()

# Replace GridLayout import with LinearLayout
kt = kt.replace(
    "import android.widget.GridLayout",
    "import android.widget.LinearLayout"
)

# Build the new button-creation block
new_code = '''        val container = binding.categoryContainer
        val dpToPx = { dp: Int -> (dp * resources.displayMetrics.density).toInt() }

        // ── Category button builder — add new categories in QuestionBank only ──
        QuestionBank.categories.forEach { category ->
            val btn = android.widget.Button(this).apply {
                text          = category
                textSize      = 15f
                letterSpacing = 0.08f
                isAllCaps     = true
                gravity       = android.view.Gravity.CENTER
                setTextColor(android.graphics.Color.parseColor("#FFD700"))
                backgroundTintList = android.content.res.ColorStateList.valueOf(
                    android.graphics.Color.parseColor("#2A2F52"))
                stateListAnimator = null

                val params = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    dpToPx(68)
                ).apply {
                    bottomMargin = dpToPx(14)
                }
                layoutParams = params

                setOnClickListener {
                    buzz()
                    val intent = android.content.Intent(
                        this@CategoryActivity, QuizActivity::class.java)
                    intent.putExtra("category", category)
                    startActivity(intent)
                }
            }
            container.addView(btn)
        }'''

# ── Replace the old grid block (flexible regex handles minor whitespace diffs)
old_pattern = re.compile(
    r'val grid = binding\.gridCategories.*?grid\.addView\(btn\)\s*\}\s*\}',
    re.DOTALL
)

if old_pattern.search(kt):
    kt = old_pattern.sub(new_code, kt)
    print("✅ Kotlin grid block replaced")
else:
    print("⚠️  Pattern not found — check CategoryActivity.kt manually")

# ── Write files ───────────────────────────────────────────────────────────────
with open(xml_path, "w") as f:
    f.write(xml)
print("✅ activity_category.xml written")

with open(kt_path, "w") as f:
    f.write(kt)
print("✅ CategoryActivity.kt written")
print("\nAll done — commit and push.")

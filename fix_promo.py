file_path = "app/src/main/java/com/dresapps/dresquiz/LevelSelectActivity.kt"

with open(file_path, "r") as f:
    lines = f.readlines()

promo = '''
            val promoLink = TextView(this)
            promoLink.text = "Have a promo code?"
            promoLink.textSize = 12f
            promoLink.setTextColor(Color.parseColor("#FFA500"))
            promoLink.gravity = android.view.Gravity.CENTER
            promoLink.setPadding(0, 8, 0, 8)
            promoLink.setOnClickListener {
                val promoInput = android.widget.EditText(this)
                promoInput.hint = "Enter promo code"
                android.app.AlertDialog.Builder(this)
                    .setTitle("Promo Code")
                    .setView(promoInput)
                    .setPositiveButton("Redeem") { _, _ ->
                        val code = promoInput.text.toString().trim()
                        if (code == "NICK&NYLA2026") {
                            AppPreferences.setPremium(this, true)
                            android.widget.Toast.makeText(this, "Premium unlocked!", android.widget.Toast.LENGTH_SHORT).show()
                            recreate()
                        } else {
                            android.widget.Toast.makeText(this, "Invalid promo code.", android.widget.Toast.LENGTH_SHORT).show()
                        }
                    }
                    .setNegativeButton("Cancel", null)
                    .show()
            }
            banner.addView(promoLink)
'''

lines.insert(85, promo)

with open(file_path, "w") as f:
    f.writelines(lines)

print("Done!")

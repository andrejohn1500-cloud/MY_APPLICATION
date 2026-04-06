import re

path = "./app/src/main/java/com/example/myapplication/QuizActivity.kt"
with open(path, "r") as f:
    content = f.read()

# Fix correct answer stroke
content = content.replace(
    'options[selected].setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#1DB954")))',
    '(options[selected] as? com.google.android.material.button.MaterialButton)?.setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#1DB954")))'
)

# Fix wrong answer stroke  
content = content.replace(
    'options[selected].setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#E74C3C")))',
    '(options[selected] as? com.google.android.material.button.MaterialButton)?.setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#E74C3C")))'
)

# Fix showCorrect stroke
content = content.replace(
    '.setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#1DB954")))',
    '.let { (it as? com.google.android.material.button.MaterialButton)?.setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#1DB954"))) }'
)

with open(path, "w") as f:
    f.write(content)
print("✅ setStrokeColor calls fixed with MaterialButton cast")

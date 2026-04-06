import re

path = "./app/src/main/java/com/example/myapplication/QuizActivity.kt"
with open(path, "r") as f:
    content = f.read()

# Remove ALL setBackgroundResource calls on buttons
content = re.sub(r'btn\.setBackgroundResource\(R\.drawable\.bg_option_default\)', 
                 '/* stroke preserved */', content)
content = re.sub(r'options\[selected\]\.setBackgroundResource\(R\.drawable\.bg_option_correct\)',
                 'options[selected].setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#1DB954")))', content)
content = re.sub(r'\.setBackgroundResource\(R\.drawable\.bg_option_correct\)',
                 '.setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#1DB954")))', content)
content = re.sub(r'options\[selected\]\.setBackgroundResource\(R\.drawable\.bg_option_wrong\)',
                 'options[selected].setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#E74C3C")))', content)
content = re.sub(r'\.setBackgroundResource\(R\.drawable\.bg_option_wrong\)',
                 '.setStrokeColor(android.content.res.ColorStateList.valueOf(android.graphics.Color.parseColor("#E74C3C")))', content)

# Remove any remaining setBackgroundResource on buttons
content = re.sub(r'(btn\w*|options\[\w+\])\.setBackgroundResource\([^)]*\)', 
                 '/* backgroundResource removed */', content)

with open(path, "w") as f:
    f.write(content)
print("✅ setBackgroundResource removed — gold strokes will now survive at runtime")

# Verify
remaining = [l.strip() for l in content.split('\n') if 'setBackgroundResource' in l]
if remaining:
    print(f"⚠️  Still remaining: {remaining}")
else:
    print("✅ Zero setBackgroundResource calls remain")

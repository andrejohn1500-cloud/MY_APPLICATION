import re

# ── FILE 1: activity_quiz.xml ──
path = "./app/src/main/res/layout/activity_quiz.xml"
with open(path, "r") as f:
    content = f.read()

# Replace each btnOption with premium styled version
for i in range(4):
    pattern = rf'(<com\.google\.android\.material\.button\.MaterialButton\s[^>]*android:id="@\+id/btnOption{i}"[^/]*/?>)'
    replacement = f'''<com.google.android.material.button.MaterialButton
        android:id="@+id/btnOption{i}"
        android:layout_width="match_parent"
        android:layout_height="64dp"
        android:layout_marginStart="8dp"
        android:layout_marginEnd="8dp"
        android:layout_marginBottom="12dp"
        android:textColor="@color/white"
        android:textSize="15sp"
        android:textStyle="bold"
        android:gravity="center"
        android:paddingStart="20dp"
        android:paddingEnd="20dp"
        app:strokeColor="#FFD700"
        app:strokeWidth="2dp"
        app:cornerRadius="16dp"
        app:backgroundTint="@android:color/transparent" />'''
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        print(f"✅ btnOption{i} replaced")
    else:
        print(f"⚠️  btnOption{i} NOT matched — trying fallback")
        # Fallback: find by id only and patch attributes
        content = re.sub(
            rf'(android:id="@\+id/btnOption{i}")',
            f'android:id="@+id/btnOption{i}"\n        app:strokeColor="#FFD700"\n        app:strokeWidth="2dp"',
            content
        )
        print(f"✅ btnOption{i} patched via fallback")

# Remove any backgroundTint that isn't transparent
content = re.sub(r'app:backgroundTint="(?!@android:color/transparent)[^"]*"', 
                 'app:backgroundTint="@android:color/transparent"', content)

with open(path, "w") as f:
    f.write(content)
print("✅ activity_quiz.xml saved")

# ── FILE 2: colors.xml — add premium glow colors ──
colors_path = "./app/src/main/res/values/colors.xml"
with open(colors_path, "r") as f:
    colors = f.read()

additions = """
    <color name="gold_stroke">#FFD700</color>
    <color name="answer_correct">#1DB954</color>
    <color name="answer_wrong">#E74C3C</color>
    <color name="card_bg">#1A1E3A</color>
"""

if "gold_stroke" not in colors:
    colors = colors.replace("</resources>", additions + "</resources>")
    with open(colors_path, "w") as f:
        f.write(colors)
    print("✅ colors.xml updated with premium palette")
else:
    print("✅ colors.xml already has premium colors")

print("\n🎉 Premium UI patch complete!")

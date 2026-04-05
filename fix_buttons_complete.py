import re

path = "./app/src/main/res/layout/activity_quiz.xml"

with open(path, "r") as f:
    content = f.read()

# Strip backgroundTint and AppCompat style overrides
content = re.sub(r'\s*android:backgroundTint="[^"]*"', '', content)
content = re.sub(r'\s*style="@style/Widget\.AppCompat\.Button[^"]*"', '', content)

# Replace all 4 answer buttons by ID pattern
for i in range(1, 5):
    pattern = rf'(<(?:com\.google\.android\.material\.button\.)?MaterialButton[^>]*android:id="@\+id/btnAnswer{i}"[^/]*/?>)'
    replacement = f'''<com.google.android.material.button.MaterialButton
        android:id="@+id/btnAnswer{i}"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginStart="16dp"
        android:layout_marginEnd="16dp"
        android:layout_marginBottom="8dp"
        android:textColor="?attr/colorOnPrimary"
        android:textSize="15sp"
        android:paddingTop="12dp"
        android:paddingBottom="12dp"
        app:strokeColor="?attr/colorOnPrimary"
        app:strokeWidth="2dp"
        app:cornerRadius="8dp"
        android:text="Answer {i}" />'''
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    print(f"✅ btnAnswer{i} replaced")

with open(path, "w") as f:
    f.write(content)

print("✅ All 4 answer buttons fully patched. No manual editing needed.")

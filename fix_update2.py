import os, re

# ── PATCH 1: Replace answer buttons in activity_quiz.xml ──
layout_path = "./app/src/main/res/layout/activity_quiz.xml"

with open(layout_path, "r") as f:
    content = f.read()

new_buttons = '''
    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnAnswer1"
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
        android:text="Answer 1" />

    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnAnswer2"
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
        android:text="Answer 2" />

    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnAnswer3"
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
        android:text="Answer 3" />

    <com.google.android.material.button.MaterialButton
        android:id="@+id/btnAnswer4"
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
        android:text="Answer 4" />'''

# Remove any backgroundTint on answer buttons
content = re.sub(r'\s*android:backgroundTint="[^"]*"', '', content)
# Remove any style= overrides on MaterialButtons
content = re.sub(r'\s*style="@style/Widget\.AppCompat\.Button[^"]*"', '', content)

with open(layout_path, "w") as f:
    f.write(content)

print("✅ activity_quiz.xml patched — backgroundTint and style overrides removed")
print("⚠️  Now manually paste the 4 button blocks above into activity_quiz.xml via the editor tab")
print("Done.")

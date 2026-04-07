path = "./app/src/main/res/layout/activity_quiz.xml"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix 1: Remove weight from question text - use wrap_content + margin instead
content = content.replace(
    'android:id="@+id/tvQuestion"\n        android:layout_width="match_parent"\n        android:layout_height="0dp"\n        android:layout_weight="1"',
    'android:id="@+id/tvQuestion"\n        android:layout_width="match_parent"\n        android:layout_height="wrap_content"\n        android:layout_marginBottom="24dp"'
)

# Fix 2: Add top margin to first button so it doesn't crowd question
content = content.replace(
    'android:id="@+id/btnOption0"',
    'android:id="@+id/btnOption0"\n        android:layout_marginTop="8dp"'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done! Verifying tvQuestion block:")
import re
match = re.search(r'id="@\+id/tvQuestion"[^<]*', content)
if match:
    print(match.group())

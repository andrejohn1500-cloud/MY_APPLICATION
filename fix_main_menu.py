import os

# ── 1. Gradient background drawable ──────────────────────────────────────────
gradient_xml = '''<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient
        android:type="linear"
        android:angle="180"
        android:startColor="#1A1D2E"
        android:centerColor="#1E2240"
        android:endColor="#141626"/>
</shape>'''

# ── 2. Button background: accent fill + ripple press effect ───────────────────
btn_accent_xml = '''<?xml version="1.0" encoding="utf-8"?>
<ripple xmlns:android="http://schemas.android.com/apk/res/android"
    android:color="#66FFD700">
    <item>
        <shape>
            <solid android:color="#2A2F52"/>
            <corners android:radius="12dp"/>
            <stroke android:width="1.5dp" android:color="#66FFD700"/>
        </shape>
    </item>
</ripple>'''

# ── 3. PLAY button: gold fill + ripple ────────────────────────────────────────
btn_play_xml = '''<?xml version="1.0" encoding="utf-8"?>
<ripple xmlns:android="http://schemas.android.com/apk/res/android"
    android:color="#FFFFA000">
    <item>
        <shape>
            <solid android:color="#FFD700"/>
            <corners android:radius="12dp"/>
        </shape>
    </item>
</ripple>'''

# ── 4. Main menu layout ───────────────────────────────────────────────────────
main_xml = '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/bg_main_gradient"
    android:gravity="center"
    android:orientation="vertical"
    android:padding="32dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="DREs"
        android:textColor="@color/gold"
        android:textSize="82sp"
        android:textStyle="bold"
        android:letterSpacing="0.08"
        android:shadowColor="#99FFD700"
        android:shadowDx="0"
        android:shadowDy="0"
        android:shadowRadius="18"/>

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="QUIZ"
        android:textColor="@color/white"
        android:textSize="36sp"
        android:letterSpacing="0.5"
        android:textStyle="bold"/>

    <View
        android:layout_width="100dp"
        android:layout_height="3dp"
        android:layout_marginTop="14dp"
        android:layout_marginBottom="52dp"
        android:background="@color/gold"/>

    <Button
        android:id="@+id/btnStart"
        android:layout_width="260dp"
        android:layout_height="60dp"
        android:layout_marginBottom="16dp"
        android:background="@drawable/bg_button_play"
        android:text="▶  PLAY"
        android:textColor="#1A1D2E"
        android:textSize="18sp"
        android:textStyle="bold"
        android:letterSpacing="0.1"/>

    <Button
        android:id="@+id/btnLeaderboard"
        android:layout_width="260dp"
        android:layout_height="60dp"
        android:layout_marginBottom="16dp"
        android:background="@drawable/bg_button_accent"
        android:text="🏆  LEADERBOARD"
        android:textColor="@color/gold"
        android:textSize="16sp"
        android:textStyle="bold"
        android:letterSpacing="0.06"/>

    <Button
        android:id="@+id/btnDonate"
        android:layout_width="260dp"
        android:layout_height="60dp"
        android:layout_marginBottom="16dp"
        android:background="@drawable/bg_button_accent"
        android:text="💛  SUPPORT US"
        android:textColor="@color/gold"
        android:textSize="16sp"
        android:textStyle="bold"
        android:letterSpacing="0.06"/>

    <Button
        android:id="@+id/btnMyStory"
        android:layout_width="260dp"
        android:layout_height="60dp"
        android:background="@drawable/bg_button_accent"
        android:text="📖  MY STORY"
        android:textColor="@color/gold"
        android:textSize="16sp"
        android:textStyle="bold"
        android:letterSpacing="0.06"/>

</LinearLayout>'''

# ── Write files ───────────────────────────────────────────────────────────────
drawable_path = "./app/src/main/res/drawable"
layout_path   = "./app/src/main/res/layout"

os.makedirs(drawable_path, exist_ok=True)
os.makedirs(layout_path,   exist_ok=True)

with open(f"{drawable_path}/bg_main_gradient.xml",  "w") as f: f.write(gradient_xml)
with open(f"{drawable_path}/bg_button_accent.xml",  "w") as f: f.write(btn_accent_xml)
with open(f"{drawable_path}/bg_button_play.xml",    "w") as f: f.write(btn_play_xml)
with open(f"{layout_path}/activity_main.xml",       "w") as f: f.write(main_xml)

print("✅ bg_main_gradient.xml created")
print("✅ bg_button_accent.xml created")
print("✅ bg_button_play.xml created")
print("✅ activity_main.xml overwritten")
print("\nAll done — commit and push.")

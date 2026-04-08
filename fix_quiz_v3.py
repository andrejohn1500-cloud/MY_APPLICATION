import shutil, re

# --- XML ---
xml_path = "./app/src/main/res/layout/activity_quiz.xml"
shutil.copy(xml_path, "./activity_quiz_backup3.xml")

xml = '''<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#1A1D2E">

    <!-- MAIN CONTENT -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:paddingStart="16dp"
        android:paddingEnd="16dp"
        android:paddingTop="16dp"
        android:paddingBottom="12dp">

        <!-- CATEGORY: top, large, centered -->
        <TextView
            android:id="@+id/tvCategory"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textColor="#FFA500"
            android:textSize="26sp"
            android:textStyle="bold"
            android:textAllCaps="true"
            android:letterSpacing="0.10"
            android:gravity="center"
            android:layout_marginBottom="0dp"/>

        <!-- SPACER: pushes bottom section down -->
        <Space
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1"/>

        <!-- QUESTION COUNTER + CLOCK ROW -->
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:gravity="center_vertical"
            android:layout_marginBottom="4dp">
            <TextView
                android:id="@+id/tvProgress"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:textColor="@color/white"
                android:textSize="15sp"
                android:textStyle="bold"/>
            <TextView
                android:id="@+id/tvTimer"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textColor="#FFA500"
                android:textSize="20sp"
                android:textStyle="bold"/>
        </LinearLayout>

        <!-- PROGRESS BAR: underlines the counter row, full width, thick -->
        <ProgressBar
            android:id="@+id/progressTimer"
            style="?android:attr/progressBarStyleHorizontal"
            android:layout_width="match_parent"
            android:layout_height="10dp"
            android:layout_marginBottom="14dp"
            android:progressBackgroundTint="#2A2D4E"
            android:progressTint="#FFA500"
            android:max="30"/>

        <!-- QUESTION TEXT -->
        <TextView
            android:id="@+id/tvQuestion"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="20dp"
            android:textColor="@color/white"
            android:textSize="20sp"
            android:textStyle="bold"
            android:lineSpacingMultiplier="1.3"/>

        <!-- ANSWER BUTTONS -->
        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnOption0"
            app:strokeColor="#FFA500"
            app:strokeWidth="2dp"
            app:cornerRadius="14dp"
            android:layout_width="match_parent"
            android:layout_height="54dp"
            android:layout_marginBottom="10dp"
            android:textColor="@color/white"
            android:textSize="15sp"
            android:gravity="start|center_vertical"
            android:paddingStart="16dp"/>

        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnOption1"
            app:strokeColor="#FFA500"
            app:strokeWidth="2dp"
            app:cornerRadius="14dp"
            android:layout_width="match_parent"
            android:layout_height="54dp"
            android:layout_marginBottom="10dp"
            android:textColor="@color/white"
            android:textSize="15sp"
            android:gravity="start|center_vertical"
            android:paddingStart="16dp"/>

        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnOption2"
            app:strokeColor="#FFA500"
            app:strokeWidth="2dp"
            app:cornerRadius="14dp"
            android:layout_width="match_parent"
            android:layout_height="54dp"
            android:layout_marginBottom="10dp"
            android:textColor="@color/white"
            android:textSize="15sp"
            android:gravity="start|center_vertical"
            android:paddingStart="16dp"/>

        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnOption3"
            app:strokeColor="#FFA500"
            app:strokeWidth="2dp"
            app:cornerRadius="14dp"
            android:layout_width="match_parent"
            android:layout_height="54dp"
            android:layout_marginBottom="10dp"
            android:textColor="@color/white"
            android:textSize="15sp"
            android:gravity="start|center_vertical"
            android:paddingStart="16dp"/>

        <!-- SCORE -->
        <TextView
            android:id="@+id/tvScore"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textColor="@color/white_alpha"
            android:textSize="13sp"
            android:gravity="center"/>

    </LinearLayout>

    <!-- TEACHER CARD: floats below category, slides in from right -->
    <androidx.cardview.widget.CardView
        android:id="@+id/scientistCard"
        android:layout_width="280dp"
        android:layout_height="wrap_content"
        android:layout_gravity="top|end"
        android:layout_marginTop="110dp"
        android:layout_marginEnd="16dp"
        android:translationX="700dp"
        app:cardCornerRadius="12dp"
        app:cardBackgroundColor="#1E2340"
        app:cardElevation="10dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:gravity="center_vertical"
            android:padding="10dp">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="&#129489;&#127997;&#8205;&#127979;"
                android:textSize="36sp"
                android:layout_marginEnd="10dp"/>

            <TextView
                android:id="@+id/tvScientistRemark"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:textColor="#FFA500"
                android:textSize="13sp"
                android:textStyle="italic"
                android:lineSpacingMultiplier="1.3"/>

        </LinearLayout>
    </androidx.cardview.widget.CardView>

</FrameLayout>'''

with open(xml_path, "w") as f:
    f.write(xml)
print("XML written.")

# --- KOTLIN: update timer icon ---
kt_path = "./app/src/main/java/com/example/myapplication/QuizActivity.kt"
with open(kt_path, "r") as f:
    kt = f.read()

kt = kt.replace('binding.tvTimer.text = "\\u29210 $secs"', 'binding.tvTimer.text = "\\uD83D\\uDD50 $secs"')
kt = kt.replace('binding.tvTimer.text = "⊙ $secs"', 'binding.tvTimer.text = "🕐 $secs"')
kt = kt.replace('binding.tvTimer.text = "\\u2299 $secs"', 'binding.tvTimer.text = "🕐 $secs"')

with open(kt_path, "w") as f:
    f.write(kt)
print("Kotlin timer icon updated.")
print("Done. Backup: activity_quiz_backup3.xml")

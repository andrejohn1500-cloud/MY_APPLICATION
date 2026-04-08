import shutil

path = "./app/src/main/res/layout/activity_quiz.xml"
shutil.copy(path, "./activity_quiz_backup2.xml")

xml = '''<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#1A1D2E">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:paddingStart="16dp"
        android:paddingEnd="16dp"
        android:paddingTop="16dp"
        android:paddingBottom="12dp">

        <!-- TOP ROW: Question counter + Timer -->
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:layout_marginBottom="10dp">
            <TextView
                android:id="@+id/tvProgress"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:textColor="@color/white"
                android:textSize="14sp"
                android:textStyle="bold"/>
            <TextView
                android:id="@+id/tvTimer"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:textColor="@color/gold"
                android:textSize="18sp"
                android:textStyle="bold"/>
        </LinearLayout>

        <!-- CATEGORY: orange line position, centered, bold, 30% bigger -->
        <TextView
            android:id="@+id/tvCategory"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textColor="#FFA500"
            android:textSize="22sp"
            android:textStyle="bold"
            android:textAllCaps="true"
            android:letterSpacing="0.12"
            android:gravity="center"
            android:layout_marginBottom="8dp"/>

        <!-- SPACER pushes bar + question down -->
        <Space
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1"/>

        <!-- PROGRESS BAR: yellow line position, 70% width, thick, centered -->
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:gravity="center"
            android:layout_marginBottom="24dp">
            <Space android:layout_width="0dp" android:layout_height="0dp" android:layout_weight="0.15"/>
            <ProgressBar
                android:id="@+id/progressTimer"
                style="?android:attr/progressBarStyleHorizontal"
                android:layout_width="0dp"
                android:layout_height="10dp"
                android:layout_weight="0.7"
                android:progressBackgroundTint="#2A2D4E"
                android:progressTint="#FFA500"
                android:max="30"/>
            <Space android:layout_width="0dp" android:layout_height="0dp" android:layout_weight="0.15"/>
        </LinearLayout>

        <!-- QUESTION: green line position, just above buttons -->
        <TextView
            android:id="@+id/tvQuestion"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="16dp"
            android:textColor="@color/white"
            android:textSize="20sp"
            android:textStyle="bold"
            android:lineSpacingMultiplier="1.3"/>

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

        <TextView
            android:id="@+id/tvScore"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textColor="@color/white_alpha"
            android:textSize="13sp"
            android:gravity="center"/>

    </LinearLayout>

    <!-- SCIENTIST CARD: purple line position, floats middle-right -->
    <androidx.cardview.widget.CardView
        android:id="@+id/scientistCard"
        android:layout_width="250dp"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom|end"
        android:layout_marginEnd="16dp"
        android:layout_marginBottom="420dp"
        android:translationX="700dp"
        app:cardCornerRadius="12dp"
        app:cardBackgroundColor="#1A1E3A"
        app:cardElevation="8dp">
        <TextView
            android:id="@+id/tvScientistRemark"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textColor="@color/white"
            android:textSize="13sp"
            android:padding="12dp"
            android:lineSpacingMultiplier="1.3"/>
    </androidx.cardview.widget.CardView>

</FrameLayout>'''

with open(path, "w") as f:
    f.write(xml)

print("Done. Backup saved as activity_quiz_backup2.xml")

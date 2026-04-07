xml = '''<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#1A1D2E"
    android:fillViewport="true">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:gravity="center_horizontal"
        android:paddingTop="48dp"
        android:paddingBottom="32dp"
        android:paddingLeft="24dp"
        android:paddingRight="24dp">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="QUIZ COMPLETE!"
            android:textSize="28sp"
            android:textStyle="bold"
            android:letterSpacing="0.08"
            android:textColor="#FFC107"
            android:layout_marginBottom="24dp"/>

        <androidx.cardview.widget.CardView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="28dp"
            app:cardBackgroundColor="#2A2F52"
            app:cardCornerRadius="16dp"
            app:cardElevation="6dp">

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical"
                android:gravity="center_horizontal"
                android:padding="28dp">

                <TextView
                    android:id="@+id/tvFinalScore"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="0"
                    android:textSize="72sp"
                    android:textStyle="bold"
                    android:textColor="#FFFFFF"/>

                <TextView
                    android:id="@+id/tvScoreLabel"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="out of 17"
                    android:textSize="16sp"
                    android:textColor="#9099B7"
                    android:layout_marginBottom="12dp"/>

                <TextView
                    android:id="@+id/tvGrade"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text=""
                    android:textSize="18sp"
                    android:textStyle="bold"
                    android:layout_marginBottom="24dp"/>

                <View
                    android:layout_width="match_parent"
                    android:layout_height="1dp"
                    android:background="#3D4470"
                    android:layout_marginBottom="24dp"/>

                <EditText
                    android:id="@+id/etPlayerName"
                    android:layout_width="220dp"
                    android:layout_height="wrap_content"
                    android:hint="Enter your name"
                    android:hintTextColor="#9099B7"
                    android:textColor="#FFFFFF"
                    android:textSize="15sp"
                    android:gravity="center"
                    android:inputType="textPersonName"
                    android:maxLines="1"
                    android:background="@null"
                    android:layout_marginBottom="4dp"/>

                <View
                    android:layout_width="220dp"
                    android:layout_height="2dp"
                    android:background="#FFC107"
                    android:layout_marginBottom="20dp"/>

                <com.google.android.material.button.MaterialButton
                    android:id="@+id/btnSubmitScore"
                    android:layout_width="220dp"
                    android:layout_height="52dp"
                    android:text="SAVE TO LEADERBOARD"
                    android:textSize="12sp"
                    android:textStyle="bold"
                    android:letterSpacing="0.04"
                    android:textColor="#1A1D2E"
                    app:backgroundTint="#FFC107"
                    app:cornerRadius="26dp"
                    android:stateListAnimator="@null"/>

            </LinearLayout>
        </androidx.cardview.widget.CardView>

        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnPlayAgain"
            android:layout_width="match_parent"
            android:layout_height="56dp"
            android:text="PLAY AGAIN"
            android:textSize="15sp"
            android:textStyle="bold"
            android:letterSpacing="0.06"
            android:textColor="#FFC107"
            app:backgroundTint="#2A2F52"
            app:cornerRadius="28dp"
            android:stateListAnimator="@null"
            android:layout_marginBottom="14dp"/>

        <com.google.android.material.button.MaterialButton
            android:id="@+id/btnHome"
            android:layout_width="match_parent"
            android:layout_height="56dp"
            android:text="HOME"
            android:textSize="15sp"
            android:textStyle="bold"
            android:letterSpacing="0.06"
            android:textColor="#FFC107"
            app:backgroundTint="#2A2F52"
            app:cornerRadius="28dp"
            android:stateListAnimator="@null"/>

    </LinearLayout>
</ScrollView>'''

open("./app/src/main/res/layout/activity_result.xml", "w").write(xml)
print("Done")

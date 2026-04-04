#!/usr/bin/env python3
"""
DREs Quiz — Complete Android File Generator
Run: python3 generate_app.py
Writes every source file, layout, resource, and Gradle config needed.
"""

import os

BASE = "/workspaces/MY_APPLICATION"

def w(rel_path, content):
    path = os.path.join(BASE, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ {rel_path}")

P = "app/src/main/java/com/example/myapplication"
R = "app/src/main/res"

print("🚀 DREs Quiz — Generating all files...")
print("=" * 55)
print()
print("  ⚠️  Preserving root Gradle files (they already work)")
print("  ✍️  Writing app/ source files and resources only")
print()

# NOTE: root build.gradle.kts, settings.gradle.kts, gradle.properties
# are intentionally NOT overwritten — the existing project builds fine.
# We only need to update app/build.gradle.kts for new dependencies.

# ── app/build.gradle.kts ──────────────────────────────────────
# Replaces the default Compose build config with a Views-based one.
# Adds Firebase, RecyclerView, Material, and signing config.
w("app/build.gradle.kts", """plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("com.google.gms.google-services")
}

android {
    namespace = "com.example.myapplication"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.myapplication"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    signingConfigs {
        create("release") {
            storeFile = file("../release.keystore")
            storePassword = "Andre2025"
            keyAlias = "mykey"
            keyPassword = "Andre2025"
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            signingConfig = signingConfigs.getByName("release")
        }
        debug {
            signingConfig = signingConfigs.getByName("release")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    kotlinOptions {
        jvmTarget = "1.8"
    }
    buildFeatures {
        viewBinding = true
        // Compose disabled — this app uses traditional XML Views
        compose = false
    }
}

dependencies {
    // Core
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("com.google.android.material:material:1.11.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
    implementation("androidx.recyclerview:recyclerview:1.3.2")
    // Firebase
    implementation(platform("com.google.firebase:firebase-bom:32.7.0"))
    implementation("com.google.firebase:firebase-firestore-ktx")
    implementation("com.google.firebase:firebase-auth-ktx")
    // Test
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.1.5")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
}
""")

# ── AndroidManifest.xml ───────────────────────────────────────
w("app/src/main/AndroidManifest.xml", """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.DresQuiz">

        <activity android:name=".MainActivity" android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <activity android:name=".CategoryActivity"   android:exported="false"/>
        <activity android:name=".QuizActivity"       android:exported="false"/>
        <activity android:name=".ResultActivity"     android:exported="false"/>
        <activity android:name=".LeaderboardActivity" android:exported="false"/>
        <activity android:name=".DonationActivity"   android:exported="false"/>
        <activity android:name=".MyStoryActivity"    android:exported="false"/>
    </application>
</manifest>
""")

# ── RESOURCES ─────────────────────────────────────────────────

w(f"{R}/values/colors.xml", """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="navy_dark">#1A1A2E</color>
    <color name="navy_mid">#16213E</color>
    <color name="navy_light">#0F3460</color>
    <color name="gold">#FFD700</color>
    <color name="gold_dark">#FFA500</color>
    <color name="white">#FFFFFF</color>
    <color name="white_alpha">#CCFFFFFF</color>
    <color name="correct">#4CAF50</color>
    <color name="wrong">#F44336</color>
    <color name="timer_warning">#FF9800</color>
    <color name="text_secondary">#B0B0B0</color>
</resources>
""")

w(f"{R}/values/strings.xml", """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">DREs Quiz</string>
</resources>
""")

w(f"{R}/values/themes.xml", """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.DresQuiz" parent="Theme.MaterialComponents.DayNight.NoActionBar">
        <item name="colorPrimary">@color/navy_dark</item>
        <item name="colorPrimaryVariant">@color/navy_mid</item>
        <item name="colorOnPrimary">@color/gold</item>
        <item name="colorSecondary">@color/gold</item>
        <item name="colorOnSecondary">@color/navy_dark</item>
        <item name="android:windowBackground">@color/navy_dark</item>
        <item name="android:statusBarColor">@color/navy_dark</item>
    </style>
</resources>
""")

# ── DRAWABLES ─────────────────────────────────────────────────

w(f"{R}/drawable/bg_button_gold.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#FFD700"/>
    <corners android:radius="12dp"/>
</shape>
""")

w(f"{R}/drawable/bg_option_default.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#0F3460"/>
    <corners android:radius="10dp"/>
    <stroke android:width="1dp" android:color="#FFD700"/>
</shape>
""")

w(f"{R}/drawable/bg_option_correct.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#4CAF50"/>
    <corners android:radius="10dp"/>
</shape>
""")

w(f"{R}/drawable/bg_option_wrong.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#F44336"/>
    <corners android:radius="10dp"/>
</shape>
""")

w(f"{R}/drawable/bg_category.xml", """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#0F3460"/>
    <corners android:radius="16dp"/>
    <stroke android:width="2dp" android:color="#FFD700"/>
</shape>
""")

# ── LAYOUTS ───────────────────────────────────────────────────

w(f"{R}/layout/activity_main.xml", """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/navy_dark"
    android:gravity="center"
    android:orientation="vertical"
    android:padding="32dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="DREs"
        android:textColor="@color/gold"
        android:textSize="72sp"
        android:textStyle="bold"/>

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="QUIZ"
        android:textColor="@color/white"
        android:textSize="30sp"
        android:letterSpacing="0.4"/>

    <View
        android:layout_width="80dp"
        android:layout_height="3dp"
        android:layout_marginTop="12dp"
        android:layout_marginBottom="52dp"
        android:background="@color/gold"/>

    <Button
        android:id="@+id/btnStart"
        android:layout_width="240dp"
        android:layout_height="56dp"
        android:layout_marginBottom="14dp"
        android:background="@drawable/bg_button_gold"
        android:text="🎯  START QUIZ"
        android:textColor="@color/navy_dark"
        android:textSize="16sp"
        android:textStyle="bold"/>

    <Button
        android:id="@+id/btnLeaderboard"
        android:layout_width="240dp"
        android:layout_height="56dp"
        android:layout_marginBottom="14dp"
        android:background="@drawable/bg_option_default"
        android:text="🏆  LEADERBOARD"
        android:textColor="@color/gold"
        android:textSize="16sp"
        android:textStyle="bold"/>

    <Button
        android:id="@+id/btnDonate"
        android:layout_width="240dp"
        android:layout_height="56dp"
        android:layout_marginBottom="14dp"
        android:background="@drawable/bg_option_default"
        android:text="💛  SUPPORT US"
        android:textColor="@color/gold"
        android:textSize="16sp"
        android:textStyle="bold"/>

    <Button
        android:id="@+id/btnMyStory"
        android:layout_width="240dp"
        android:layout_height="56dp"
        android:background="@drawable/bg_option_default"
        android:text="📖  MY STORY"
        android:textColor="@color/gold"
        android:textSize="16sp"
        android:textStyle="bold"/>
</LinearLayout>
""")

w(f"{R}/layout/activity_category.xml", """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/navy_dark"
    android:orientation="vertical"
    android:padding="20dp">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="28dp"
        android:layout_marginBottom="28dp"
        android:text="SELECT CATEGORY"
        android:textColor="@color/gold"
        android:textSize="22sp"
        android:textStyle="bold"
        android:gravity="center"/>

    <GridLayout
        android:id="@+id/gridCategories"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:columnCount="2"
        android:rowCount="3"
        android:useDefaultMargins="true"/>
</LinearLayout>
""")

w(f"{R}/layout/activity_quiz.xml", """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/navy_dark"
    android:orientation="vertical"
    android:padding="20dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:layout_marginTop="20dp"
        android:layout_marginBottom="6dp">
        <TextView
            android:id="@+id/tvProgress"
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:textColor="@color/white_alpha"
            android:textSize="14sp"/>
        <TextView
            android:id="@+id/tvTimer"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textColor="@color/gold"
            android:textSize="20sp"
            android:textStyle="bold"/>
    </LinearLayout>

    <ProgressBar
        android:id="@+id/progressTimer"
        style="?android:attr/progressBarStyleHorizontal"
        android:layout_width="match_parent"
        android:layout_height="8dp"
        android:layout_marginBottom="20dp"
        android:progressTint="@color/gold"
        android:progressBackgroundTint="@color/navy_light"
        android:max="30"/>

    <TextView
        android:id="@+id/tvCategory"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:textColor="@color/gold"
        android:textSize="12sp"
        android:textAllCaps="true"
        android:letterSpacing="0.15"
        android:layout_marginBottom="10dp"/>

    <TextView
        android:id="@+id/tvQuestion"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:textColor="@color/white"
        android:textSize="20sp"
        android:textStyle="bold"
        android:lineSpacingMultiplier="1.3"/>

    <Button
        android:id="@+id/btnOption0"
        android:layout_width="match_parent"
        android:layout_height="54dp"
        android:layout_marginBottom="10dp"
        android:background="@drawable/bg_option_default"
        android:textColor="@color/white"
        android:textSize="15sp"
        android:gravity="start|center_vertical"
        android:paddingStart="16dp"/>

    <Button
        android:id="@+id/btnOption1"
        android:layout_width="match_parent"
        android:layout_height="54dp"
        android:layout_marginBottom="10dp"
        android:background="@drawable/bg_option_default"
        android:textColor="@color/white"
        android:textSize="15sp"
        android:gravity="start|center_vertical"
        android:paddingStart="16dp"/>

    <Button
        android:id="@+id/btnOption2"
        android:layout_width="match_parent"
        android:layout_height="54dp"
        android:layout_marginBottom="10dp"
        android:background="@drawable/bg_option_default"
        android:textColor="@color/white"
        android:textSize="15sp"
        android:gravity="start|center_vertical"
        android:paddingStart="16dp"/>

    <Button
        android:id="@+id/btnOption3"
        android:layout_width="match_parent"
        android:layout_height="54dp"
        android:layout_marginBottom="20dp"
        android:background="@drawable/bg_option_default"
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
""")

w(f"{R}/layout/activity_result.xml", """<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/navy_dark">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center"
        android:orientation="vertical"
        android:padding="32dp">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="QUIZ COMPLETE!"
            android:textColor="@color/gold"
            android:textSize="26sp"
            android:textStyle="bold"
            android:layout_marginTop="24dp"
            android:layout_marginBottom="16dp"/>

        <TextView
            android:id="@+id/tvFinalScore"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textColor="@color/white"
            android:textSize="80sp"
            android:textStyle="bold"/>

        <TextView
            android:id="@+id/tvScoreLabel"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textColor="@color/text_secondary"
            android:textSize="18sp"
            android:layout_marginBottom="8dp"/>

        <TextView
            android:id="@+id/tvGrade"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textSize="22sp"
            android:textStyle="bold"
            android:layout_marginBottom="32dp"/>

        <EditText
            android:id="@+id/etPlayerName"
            android:layout_width="260dp"
            android:layout_height="wrap_content"
            android:hint="Enter your name"
            android:textColor="@color/white"
            android:textColorHint="@color/text_secondary"
            android:backgroundTint="@color/gold"
            android:inputType="textPersonName"
            android:layout_marginBottom="14dp"/>

        <Button
            android:id="@+id/btnSubmitScore"
            android:layout_width="240dp"
            android:layout_height="52dp"
            android:layout_marginBottom="12dp"
            android:background="@drawable/bg_button_gold"
            android:text="🏆 SUBMIT SCORE"
            android:textColor="@color/navy_dark"
            android:textStyle="bold"/>

        <Button
            android:id="@+id/btnPlayAgain"
            android:layout_width="240dp"
            android:layout_height="52dp"
            android:layout_marginBottom="12dp"
            android:background="@drawable/bg_option_default"
            android:text="🔄 PLAY AGAIN"
            android:textColor="@color/gold"
            android:textStyle="bold"/>

        <Button
            android:id="@+id/btnHome"
            android:layout_width="240dp"
            android:layout_height="52dp"
            android:background="@drawable/bg_option_default"
            android:text="🏠 HOME"
            android:textColor="@color/gold"
            android:textStyle="bold"/>
    </LinearLayout>
</ScrollView>
""")

w(f"{R}/layout/activity_leaderboard.xml", """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/navy_dark"
    android:orientation="vertical"
    android:padding="20dp">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="🏆 LEADERBOARD"
        android:textColor="@color/gold"
        android:textSize="24sp"
        android:textStyle="bold"
        android:gravity="center"
        android:layout_marginTop="24dp"
        android:layout_marginBottom="24dp"/>

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/rvLeaderboard"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"/>

    <Button
        android:id="@+id/btnBack"
        android:layout_width="match_parent"
        android:layout_height="52dp"
        android:layout_marginTop="16dp"
        android:background="@drawable/bg_option_default"
        android:text="← BACK"
        android:textColor="@color/gold"
        android:textStyle="bold"/>
</LinearLayout>
""")

w(f"{R}/layout/item_leaderboard.xml", """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal"
    android:padding="16dp"
    android:layout_marginBottom="8dp"
    android:background="@drawable/bg_category">

    <TextView
        android:id="@+id/tvRank"
        android:layout_width="44dp"
        android:layout_height="wrap_content"
        android:textColor="@color/gold"
        android:textSize="18sp"
        android:textStyle="bold"/>

    <TextView
        android:id="@+id/tvName"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:textColor="@color/white"
        android:textSize="16sp"/>

    <TextView
        android:id="@+id/tvLeaderScore"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textColor="@color/gold"
        android:textSize="16sp"
        android:textStyle="bold"/>
</LinearLayout>
""")

w(f"{R}/layout/activity_donation.xml", """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/navy_dark"
    android:gravity="center"
    android:orientation="vertical"
    android:padding="32dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="💛"
        android:textSize="64sp"
        android:layout_marginBottom="16dp"/>

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="SUPPORT US"
        android:textColor="@color/gold"
        android:textSize="28sp"
        android:textStyle="bold"
        android:layout_marginBottom="16dp"/>

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Your support keeps DREs Quiz free and growing. Every contribution makes a real difference!"
        android:textColor="@color/white_alpha"
        android:textSize="16sp"
        android:gravity="center"
        android:lineSpacingMultiplier="1.4"
        android:layout_marginBottom="40dp"/>

    <Button
        android:id="@+id/btnPayPal"
        android:layout_width="260dp"
        android:layout_height="56dp"
        android:background="@drawable/bg_button_gold"
        android:text="💳  DONATE VIA PAYPAL"
        android:textColor="@color/navy_dark"
        android:textStyle="bold"
        android:layout_marginBottom="16dp"/>

    <Button
        android:id="@+id/btnBackDonate"
        android:layout_width="260dp"
        android:layout_height="52dp"
        android:background="@drawable/bg_option_default"
        android:text="← BACK"
        android:textColor="@color/gold"
        android:textStyle="bold"/>
</LinearLayout>
""")

w(f"{R}/layout/activity_my_story.xml", """<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/navy_dark">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:padding="24dp">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="📖 MY STORY"
            android:textColor="@color/gold"
            android:textSize="26sp"
            android:textStyle="bold"
            android:layout_marginTop="28dp"
            android:layout_marginBottom="24dp"/>

        <TextView
            android:id="@+id/tvStory"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:textColor="@color/white_alpha"
            android:textSize="16sp"
            android:lineSpacingMultiplier="1.6"/>

        <Button
            android:id="@+id/btnBackStory"
            android:layout_width="match_parent"
            android:layout_height="52dp"
            android:layout_marginTop="32dp"
            android:layout_marginBottom="16dp"
            android:background="@drawable/bg_option_default"
            android:text="← BACK"
            android:textColor="@color/gold"
            android:textStyle="bold"/>
    </LinearLayout>
</ScrollView>
""")

# ── QuestionBank.kt ───────────────────────────────────────────
# NOTE: Options use "|" as delimiter to avoid comma conflicts in numbers.

w(f"{P}/QuestionBank.kt", """package com.example.myapplication

data class Question(
    val text: String,
    val options: List<String>,
    val correctIndex: Int,
    val category: String
)

object QuestionBank {

    val categories = listOf(
        "🌍 Caribbean History",
        "🧪 Science & Tech",
        "⚽ Sports",
        "🗺️ World Geography",
        "🎭 Arts & Culture",
        "🇻🇨 SVG & Vincy Life"
    )

    private fun q(text: String, opts: String, correct: Int, cat: String) =
        Question(text, opts.split("|"), correct, cat)

    // ── 1. CARIBBEAN HISTORY (17 questions) ──────────────────

    private val caribbeanHistory = listOf(
        q("Which country was the FIRST Caribbean nation to gain independence?",
            "Haiti|Cuba|Jamaica|Trinidad and Tobago", 0, "🌍 Caribbean History"),
        q("In what year did Haiti declare independence from France?",
            "1791|1804|1838|1962", 1, "🌍 Caribbean History"),
        q("Which Caribbean island was the first to be colonized by the British?",
            "Barbados|Jamaica|St. Kitts|Antigua", 2, "🌍 Caribbean History"),
        q("The 1831 Baptist War slave rebellion took place in which island?",
            "Barbados|Jamaica|Trinidad|St. Vincent", 1, "🌍 Caribbean History"),
        q("Which European power first colonized Trinidad?",
            "Britain|France|Spain|Netherlands", 2, "🌍 Caribbean History"),
        q("In what year did slavery officially end in the British Caribbean?",
            "1834|1838|1807|1865", 1, "🌍 Caribbean History"),
        q("CARICOM was formally established in which year?",
            "1958|1973|1965|1981", 1, "🌍 Caribbean History"),
        q("The West Indies Federation was dissolved in which year?",
            "1958|1962|1965|1970", 1, "🌍 Caribbean History"),
        q("Which country hosts the CARICOM Secretariat?",
            "Barbados|Trinidad|Guyana|Jamaica", 2, "🌍 Caribbean History"),
        q("The Caribbean Community was established by which treaty?",
            "Treaty of Chaguaramas|Treaty of Kingston|Treaty of Bridgetown|Treaty of Basseterre",
            0, "🌍 Caribbean History"),
        q("Marcus Garvey, the Pan-African leader, was born in which country?",
            "Trinidad|Barbados|Jamaica|Haiti", 2, "🌍 Caribbean History"),
        q("The 1970 Black Power Revolution occurred in which Caribbean nation?",
            "Jamaica|Trinidad and Tobago|Barbados|Guyana", 1, "🌍 Caribbean History"),
        q("Which Caribbean island is known as 'The Land of Wood and Water'?",
            "Barbados|Jamaica|Dominica|St. Lucia", 1, "🌍 Caribbean History"),
        q("The Morant Bay Rebellion of 1865 took place in which country?",
            "Barbados|Jamaica|Trinidad|Guyana", 1, "🌍 Caribbean History"),
        q("Toussaint Louverture led the revolution in which country?",
            "Cuba|Haiti|Dominican Republic|Martinique", 1, "🌍 Caribbean History"),
        q("Which Caribbean nation was the last to gain independence from Britain (1983)?",
            "St. Kitts and Nevis|Belize|St. Vincent|Antigua", 0, "🌍 Caribbean History"),
        q("The Grenada Revolution of 1979 was led by which political movement?",
            "GULP|New Jewel Movement|NDC|GNP", 1, "🌍 Caribbean History")
    )

    // ── 2. SCIENCE & TECH (17 questions) ─────────────────────

    private val scienceTech = listOf(
        q("What does DNA stand for?",
            "Deoxyribonucleic Acid|Dinitrogen Acid|Dynamic Nuclear Array|Dense Nucleic Arrangement",
            0, "🧪 Science & Tech"),
        q("Which planet is known as the Red Planet?",
            "Venus|Jupiter|Mars|Saturn", 2, "🧪 Science & Tech"),
        q("What is the chemical symbol for gold?",
            "Go|Gd|Au|Ag", 2, "🧪 Science & Tech"),
        q("How many bones are in the adult human body?",
            "196|206|216|226", 1, "🧪 Science & Tech"),
        q("What is known as the powerhouse of the cell?",
            "Nucleus|Ribosome|Mitochondria|Chloroplast", 2, "🧪 Science & Tech"),
        q("The speed of light is approximately how many km per second?",
            "150,000|300,000|450,000|600,000", 1, "🧪 Science & Tech"),
        q("What is the most abundant gas in Earth's atmosphere?",
            "Oxygen|Carbon Dioxide|Hydrogen|Nitrogen", 3, "🧪 Science & Tech"),
        q("Which scientist formulated the theory of general relativity?",
            "Newton|Bohr|Einstein|Hawking", 2, "🧪 Science & Tech"),
        q("What does HTTP stand for?",
            "HyperText Transfer Protocol|High Tech Transfer Process|HyperText Transmission Path|Host Transfer Protocol",
            0, "🧪 Science & Tech"),
        q("The unit of electrical resistance is called what?",
            "Volt|Ampere|Ohm|Watt", 2, "🧪 Science & Tech"),
        q("What is the hardest natural substance on Earth?",
            "Gold|Diamond|Platinum|Quartz", 1, "🧪 Science & Tech"),
        q("Which planet has the most moons in our solar system?",
            "Jupiter|Saturn|Uranus|Neptune", 1, "🧪 Science & Tech"),
        q("What does AI stand for in technology?",
            "Automated Interface|Artificial Intelligence|Advanced Integration|Analytic Index",
            1, "🧪 Science & Tech"),
        q("The study of earthquakes is called what?",
            "Meteorology|Seismology|Volcanology|Geology", 1, "🧪 Science & Tech"),
        q("How many chromosomes does a typical human cell have?",
            "23|36|46|48", 2, "🧪 Science & Tech"),
        q("What is the boiling point of water in Celsius?",
            "90|95|100|105", 2, "🧪 Science & Tech"),
        q("Which organ produces insulin in the human body?",
            "Liver|Kidney|Stomach|Pancreas", 3, "🧪 Science & Tech")
    )

    // ── 3. SPORTS (17 questions) ──────────────────────────────

    private val sports = listOf(
        q("Which country won the FIFA World Cup in 2022?",
            "France|Brazil|Argentina|Germany", 2, "⚽ Sports"),
        q("How many players from each team are on the court in basketball?",
            "4|5|6|7", 1, "⚽ Sports"),
        q("Usain Bolt, the world's fastest man, is from which Caribbean country?",
            "Trinidad|Barbados|Jamaica|Bahamas", 2, "⚽ Sports"),
        q("Which country has won the most Cricket World Cups?",
            "Australia|West Indies|India|England", 0, "⚽ Sports"),
        q("In tennis, what is the term for a score of 40-40?",
            "Tie|Deuce|Set Point|Match Point", 1, "⚽ Sports"),
        q("The Summer Olympic Games are held every how many years?",
            "2|3|4|5", 2, "⚽ Sports"),
        q("Chris Gayle is associated with which Caribbean cricket team?",
            "Trinidad|Barbados|Jamaica|Guyana", 2, "⚽ Sports"),
        q("Which sport uses a shuttlecock?",
            "Squash|Badminton|Volleyball|Polo", 1, "⚽ Sports"),
        q("How many holes are played in a standard round of golf?",
            "9|12|18|21", 2, "⚽ Sports"),
        q("The Shot Put is a discipline in which sport?",
            "Swimming|Athletics|Gymnastics|Weightlifting", 1, "⚽ Sports"),
        q("Serena Williams is celebrated for which sport?",
            "Golf|Tennis|Basketball|Volleyball", 1, "⚽ Sports"),
        q("Which Caribbean nation is famous for its Winter Olympics bobsled team?",
            "Trinidad|Jamaica|Barbados|Cuba", 1, "⚽ Sports"),
        q("In which country was the sport of cricket invented?",
            "Australia|West Indies|England|India", 2, "⚽ Sports"),
        q("What colour jersey does the leader wear in the Tour de France?",
            "Red|Green|Yellow|Blue", 2, "⚽ Sports"),
        q("How many individual events make up a Decathlon?",
            "8|10|12|15", 1, "⚽ Sports"),
        q("The FIFA World Cup is held every how many years?",
            "2|3|4|6", 2, "⚽ Sports"),
        q("Which Caribbean nation won gold in the men's 4x100m relay at the 2008 Beijing Olympics?",
            "Trinidad|Jamaica|Bahamas|Cuba", 1, "⚽ Sports")
    )

    // ── 4. WORLD GEOGRAPHY (16 questions) ─────────────────────

    private val worldGeo = listOf(
        q("What is the largest continent by land area?",
            "Africa|Antarctica|Asia|South America", 2, "🗺️ World Geography"),
        q("Which river is the longest in the world?",
            "Amazon|Congo|Mississippi|Nile", 3, "🗺️ World Geography"),
        q("What is the capital city of Australia?",
            "Sydney|Melbourne|Canberra|Brisbane", 2, "🗺️ World Geography"),
        q("Which country currently has the largest population in the world?",
            "India|China|USA|Indonesia", 0, "🗺️ World Geography"),
        q("Mount Everest is located in which mountain range?",
            "Andes|Alps|Rockies|Himalayas", 3, "🗺️ World Geography"),
        q("What is the smallest country in the world by area?",
            "Monaco|San Marino|Vatican City|Liechtenstein", 2, "🗺️ World Geography"),
        q("Which is the largest ocean on Earth?",
            "Atlantic|Indian|Pacific|Arctic", 2, "🗺️ World Geography"),
        q("The Amazon rainforest is primarily located in which country?",
            "Colombia|Peru|Venezuela|Brazil", 3, "🗺️ World Geography"),
        q("What is the capital city of Japan?",
            "Osaka|Kyoto|Tokyo|Hiroshima", 2, "🗺️ World Geography"),
        q("The Sahara Desert spans across which continent?",
            "Asia|South America|Australia|Africa", 3, "🗺️ World Geography"),
        q("Which country has the most freshwater lakes in the world?",
            "Russia|USA|Brazil|Canada", 3, "🗺️ World Geography"),
        q("The Panama Canal connects which two major oceans?",
            "Indian and Pacific|Atlantic and Pacific|Atlantic and Indian|Pacific and Arctic",
            1, "🗺️ World Geography"),
        q("What is the capital city of Brazil?",
            "Rio de Janeiro|Sao Paulo|Brasilia|Salvador", 2, "🗺️ World Geography"),
        q("Which country is home to the Great Barrier Reef?",
            "New Zealand|Philippines|Australia|Indonesia", 2, "🗺️ World Geography"),
        q("How many member states does the African Union have?",
            "45|54|63|72", 1, "🗺️ World Geography"),
        q("The Strait of Hormuz connects the Persian Gulf to which body of water?",
            "Red Sea|Gulf of Oman|Arabian Sea|Bay of Bengal", 1, "🗺️ World Geography")
    )

    // ── 5. ARTS & CULTURE (16 questions) ──────────────────────

    private val artsCulture = listOf(
        q("Who painted the world-famous Mona Lisa?",
            "Michelangelo|Raphael|Leonardo da Vinci|Caravaggio", 2, "🎭 Arts & Culture"),
        q("Which music genre was pioneered in Trinidad and Tobago?",
            "Reggae|Calypso|Soca|Zouk", 1, "🎭 Arts & Culture"),
        q("The legendary Bob Marley was from which country?",
            "Trinidad|Barbados|Jamaica|Cuba", 2, "🎭 Arts & Culture"),
        q("Who wrote the dystopian novel '1984'?",
            "Aldous Huxley|George Orwell|Ernest Hemingway|Franz Kafka", 1, "🎭 Arts & Culture"),
        q("Which Caribbean writer won the Nobel Prize in Literature in 1992?",
            "C.L.R. James|V.S. Naipaul|Derek Walcott|George Lamming", 2, "🎭 Arts & Culture"),
        q("Reggae music originated and rose to prominence in which decade?",
            "1950s|1960s|1970s|1980s", 1, "🎭 Arts & Culture"),
        q("Which Shakespeare play features 'To be or not to be, that is the question'?",
            "Macbeth|Romeo and Juliet|King Lear|Hamlet", 3, "🎭 Arts & Culture"),
        q("The famous Louvre Museum is located in which city?",
            "Rome|Madrid|Paris|London", 2, "🎭 Arts & Culture"),
        q("Soca music is most closely associated with which Caribbean country?",
            "Jamaica|Barbados|Trinidad and Tobago|St. Lucia", 2, "🎭 Arts & Culture"),
        q("Which Caribbean author wrote the classic novel 'A House for Mr Biswas'?",
            "Derek Walcott|Samuel Selvon|V.S. Naipaul|George Lamming", 2, "🎭 Arts & Culture"),
        q("What instrument is the heart of Caribbean Steelpan music?",
            "Drums|Steel drum pan|Guitar|Saxophone", 1, "🎭 Arts & Culture"),
        q("The Booker Prize is the world's most prestigious award for what?",
            "Film|Music|Literature|Architecture", 2, "🎭 Arts & Culture"),
        q("Who directed the groundbreaking film 'Black Panther'?",
            "Jordan Peele|Ryan Coogler|Spike Lee|Ava DuVernay", 1, "🎭 Arts & Culture"),
        q("Crop Over is a major cultural festival celebrated in which Caribbean island?",
            "Trinidad|Jamaica|Barbados|Grenada", 2, "🎭 Arts & Culture"),
        q("Which famous artist is known for cutting off part of his own ear?",
            "Claude Monet|Pablo Picasso|Vincent van Gogh|Salvador Dali", 2, "🎭 Arts & Culture"),
        q("The Notting Hill Carnival in London primarily celebrates which cultures?",
            "Asian|Caribbean|African|Latin American", 1, "🎭 Arts & Culture")
    )

    // ── 6. SVG & VINCY LIFE (17 questions) ───────────────────

    private val svgVincy = listOf(
        q("What is the capital city of St. Vincent and the Grenadines?",
            "Georgetown|Layou|Kingstown|Calliaqua", 2, "🇻🇨 SVG & Vincy Life"),
        q("La Soufrière in SVG is a what?",
            "Mountain range|Active volcano|National park|Earthquake fault", 1, "🇻🇨 SVG & Vincy Life"),
        q("St. Vincent and the Grenadines gained independence from Britain in which year?",
            "1969|1974|1979|1983", 2, "🇻🇨 SVG & Vincy Life"),
        q("What is the national bird of St. Vincent?",
            "St. Vincent Amazon parrot|Frigate Bird|Hummingbird|Pelican", 0, "🇻🇨 SVG & Vincy Life"),
        q("Which island is the largest of the Grenadine islands?",
            "Bequia|Union Island|Mustique|Canouan", 0, "🇻🇨 SVG & Vincy Life"),
        q("SVG is a member of which major Caribbean regional organisation?",
            "NAFTA|MERCOSUR|CARICOM|ASEAN", 2, "🇻🇨 SVG & Vincy Life"),
        q("Which staple food features prominently in SVG's national dish, Roasted Breadfruit and Jackfish?",
            "Breadfruit|Ackee|Plantain|Cassava", 0, "🇻🇨 SVG & Vincy Life"),
        q("Hurricane Beryl caused major damage to SVG in which year?",
            "2022|2023|2024|2025", 2, "🇻🇨 SVG & Vincy Life"),
        q("What has historically been the main agricultural export of SVG?",
            "Sugar|Bananas|Cocoa|Coffee", 1, "🇻🇨 SVG & Vincy Life"),
        q("The RSS Regional Security System headquarters is in which country?",
            "Trinidad|Barbados|SVG|Jamaica", 1, "🇻🇨 SVG & Vincy Life"),
        q("Vincy Mas is SVG's version of which annual cultural celebration?",
            "Christmas|Carnival|Easter|Independence Day", 1, "🇻🇨 SVG & Vincy Life"),
        q("Which political party won SVG's November 2025 general election ending 25 years of ULP rule?",
            "ULP|NDP|SVG Labour|PDP", 1, "🇻🇨 SVG & Vincy Life"),
        q("The Argyle International Airport in SVG opened in which year?",
            "2015|2016|2017|2018", 2, "🇻🇨 SVG & Vincy Life"),
        q("What is the official name of SVG's national police force?",
            "RSVGPF|SVGPF|CSVGP|VPF", 0, "🇻🇨 SVG & Vincy Life"),
        q("The Black Caribs (Garifuna people) were exiled from SVG to Central America in which year?",
            "1783|1797|1814|1838", 1, "🇻🇨 SVG & Vincy Life"),
        q("Mustique island in the Grenadines is world-renowned for attracting which visitors?",
            "Fishermen|Royalty and celebrities|Marine scientists|Backpackers", 1, "🇻🇨 SVG & Vincy Life"),
        q("What is the name of the volcanic eruption in SVG that caused mass evacuations in 2021?",
            "Hurricane Elsa|La Soufrière eruption|Mount Bequia blast|Kingstown earthquake",
            1, "🇻🇨 SVG & Vincy Life")
    )

    fun getQuestions(category: String): List<Question> = when (category) {
        "🌍 Caribbean History" -> caribbeanHistory
        "🧪 Science & Tech"   -> scienceTech
        "⚽ Sports"            -> sports
        "🗺️ World Geography"  -> worldGeo
        "🎭 Arts & Culture"   -> artsCulture
        "🇻🇨 SVG & Vincy Life" -> svgVincy
        else -> caribbeanHistory
    }

    fun getAllQuestions(): List<Question> =
        caribbeanHistory + scienceTech + sports + worldGeo + artsCulture + svgVincy
}
""")

# ── MainActivity.kt ───────────────────────────────────────────
w(f"{P}/MainActivity.kt", """package com.example.myapplication

import android.content.Intent
import android.media.MediaPlayer
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private var bgMusic: MediaPlayer? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnStart.setOnClickListener {
            startActivity(Intent(this, CategoryActivity::class.java))
        }
        binding.btnLeaderboard.setOnClickListener {
            startActivity(Intent(this, LeaderboardActivity::class.java))
        }
        binding.btnDonate.setOnClickListener {
            startActivity(Intent(this, DonationActivity::class.java))
        }
        binding.btnMyStory.setOnClickListener {
            startActivity(Intent(this, MyStoryActivity::class.java))
        }

        // Background music — add res/raw/bg_music.mp3 then uncomment:
        // bgMusic = MediaPlayer.create(this, R.raw.bg_music)
        // bgMusic?.isLooping = true
    }

    override fun onResume() {
        super.onResume()
        // bgMusic?.start()
    }

    override fun onPause() {
        super.onPause()
        bgMusic?.pause()
    }

    override fun onDestroy() {
        super.onDestroy()
        bgMusic?.release()
    }
}
""")

# ── CategoryActivity.kt ───────────────────────────────────────
w(f"{P}/CategoryActivity.kt", """package com.example.myapplication

import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.view.Gravity
import android.widget.Button
import android.widget.GridLayout
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityCategoryBinding

class CategoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCategoryBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCategoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val grid = binding.gridCategories

        QuestionBank.categories.forEachIndexed { index, category ->
            val btn = Button(this).apply {
                text = category
                textSize = 14f
                setTextColor(Color.WHITE)
                gravity = Gravity.CENTER
                setBackgroundResource(R.drawable.bg_category)
                setPadding(16, 28, 16, 28)
                val params = GridLayout.LayoutParams().apply {
                    width  = 0
                    height = GridLayout.LayoutParams.WRAP_CONTENT
                    columnSpec = GridLayout.spec(index % 2, 1, 1f)
                    rowSpec    = GridLayout.spec(index / 2, 1, 1f)
                    setMargins(12, 12, 12, 12)
                }
                layoutParams = params
                setOnClickListener {
                    val intent = Intent(this@CategoryActivity, QuizActivity::class.java)
                    intent.putExtra("category", category)
                    startActivity(intent)
                }
            }
            grid.addView(btn)
        }
    }
}
""")

# ── QuizActivity.kt ───────────────────────────────────────────
w(f"{P}/QuizActivity.kt", """package com.example.myapplication

import android.content.Intent
import android.media.AudioAttributes
import android.media.SoundPool
import android.os.Bundle
import android.os.CountDownTimer
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityQuizBinding

class QuizActivity : AppCompatActivity() {

    private lateinit var binding: ActivityQuizBinding
    private lateinit var questions: List<Question>
    private var currentIndex = 0
    private var score = 0
    private var answered = false
    private var timer: CountDownTimer? = null
    private lateinit var soundPool: SoundPool
    private var sndCorrect = 0
    private var sndWrong   = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityQuizBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val category = intent.getStringExtra("category") ?: QuestionBank.categories[0]
        questions = QuestionBank.getQuestions(category).shuffled()
        binding.tvCategory.text = category

        val attrs = AudioAttributes.Builder()
            .setUsage(AudioAttributes.USAGE_GAME)
            .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
            .build()
        soundPool = SoundPool.Builder().setMaxStreams(2).setAudioAttributes(attrs).build()
        // Add res/raw/correct.mp3 and res/raw/wrong.mp3 then uncomment:
        // sndCorrect = soundPool.load(this, R.raw.correct, 1)
        // sndWrong   = soundPool.load(this, R.raw.wrong,   1)

        val options = listOf(binding.btnOption0, binding.btnOption1,
                             binding.btnOption2, binding.btnOption3)
        options.forEachIndexed { i, btn -> btn.setOnClickListener { handleAnswer(i, options) } }
        loadQuestion(options)
    }

    private fun loadQuestion(options: List<Button>) {
        if (currentIndex >= questions.size) { goToResult(); return }
        answered = false
        val q = questions[currentIndex]
        binding.tvProgress.text = "Question \${currentIndex + 1} of \${questions.size}"
        binding.tvQuestion.text  = q.text
        binding.tvScore.text     = "Score: $score"
        options.forEachIndexed { i, btn ->
            btn.text = q.options[i]
            btn.setBackgroundResource(R.drawable.bg_option_default)
            btn.setTextColor(getColor(R.color.white))
            btn.isEnabled = true
        }
        startTimer(options)
    }

    private fun startTimer(options: List<Button>) {
        timer?.cancel()
        binding.progressTimer.max = 30
        timer = object : CountDownTimer(30_000L, 1_000L) {
            override fun onTick(ms: Long) {
                val secs = (ms / 1000).toInt()
                binding.tvTimer.text = "⏱ $secs"
                binding.progressTimer.progress = secs
                binding.tvTimer.setTextColor(
                    if (secs <= 5) getColor(R.color.wrong) else getColor(R.color.gold)
                )
            }
            override fun onFinish() {
                if (!answered) {
                    binding.tvTimer.text = "⏱ 0"
                    showCorrect(options)
                    disableAll(options)
                    nextDelayed(options)
                }
            }
        }.start()
    }

    private fun handleAnswer(selected: Int, options: List<Button>) {
        if (answered) return
        answered = true
        timer?.cancel()
        val q = questions[currentIndex]
        if (selected == q.correctIndex) {
            score++
            options[selected].setBackgroundResource(R.drawable.bg_option_correct)
            soundPool.play(sndCorrect, 1f, 1f, 0, 0, 1f)
        } else {
            options[selected].setBackgroundResource(R.drawable.bg_option_wrong)
            soundPool.play(sndWrong, 1f, 1f, 0, 0, 1f)
            showCorrect(options)
        }
        disableAll(options)
        nextDelayed(options)
    }

    private fun showCorrect(options: List<Button>) {
        options[questions[currentIndex].correctIndex]
            .setBackgroundResource(R.drawable.bg_option_correct)
    }

    private fun disableAll(options: List<Button>) = options.forEach { it.isEnabled = false }

    private fun nextDelayed(options: List<Button>) {
        binding.root.postDelayed({
            currentIndex++
            loadQuestion(options)
        }, 1300)
    }

    private fun goToResult() {
        startActivity(
            Intent(this, ResultActivity::class.java).apply {
                putExtra("score",    score)
                putExtra("total",    questions.size)
                putExtra("category", binding.tvCategory.text.toString())
            }
        )
        finish()
    }

    override fun onDestroy() {
        super.onDestroy()
        timer?.cancel()
        soundPool.release()
    }
}
""")

# ── ResultActivity.kt ─────────────────────────────────────────
w(f"{P}/ResultActivity.kt", """package com.example.myapplication

import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityResultBinding
import com.google.firebase.firestore.FirebaseFirestore

class ResultActivity : AppCompatActivity() {

    private lateinit var binding: ActivityResultBinding
    private val db = FirebaseFirestore.getInstance()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityResultBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val score    = intent.getIntExtra("score", 0)
        val total    = intent.getIntExtra("total", 17)
        val category = intent.getStringExtra("category") ?: ""
        val pct      = if (total > 0) (score.toFloat() / total * 100).toInt() else 0

        binding.tvFinalScore.text = score.toString()
        binding.tvScoreLabel.text = "out of $total"

        binding.tvGrade.apply {
            when {
                pct >= 90 -> { text = "🏆 Outstanding!";  setTextColor(Color.parseColor("#4CAF50")) }
                pct >= 70 -> { text = "⭐ Great Work!";   setTextColor(Color.parseColor("#FFD700")) }
                pct >= 50 -> { text = "👍 Good Effort!";  setTextColor(Color.parseColor("#FF9800")) }
                else       -> { text = "📚 Keep Studying!"; setTextColor(Color.parseColor("#F44336")) }
            }
        }

        binding.btnSubmitScore.setOnClickListener {
            val name = binding.etPlayerName.text.toString().trim()
            if (name.isEmpty()) {
                Toast.makeText(this, "Please enter your name", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            submitScore(name, score, total, category)
        }

        binding.btnPlayAgain.setOnClickListener {
            startActivity(Intent(this, CategoryActivity::class.java))
            finish()
        }
        binding.btnHome.setOnClickListener {
            startActivity(Intent(this, MainActivity::class.java).apply {
                flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
            })
            finish()
        }
    }

    private fun submitScore(name: String, score: Int, total: Int, category: String) {
        db.collection("leaderboard").add(
            hashMapOf(
                "name"      to name,
                "score"     to score,
                "total"     to total,
                "category"  to category,
                "timestamp" to System.currentTimeMillis()
            )
        ).addOnSuccessListener {
            Toast.makeText(this, "Score submitted! 🏆", Toast.LENGTH_SHORT).show()
            binding.btnSubmitScore.isEnabled = false
            binding.btnSubmitScore.alpha = 0.5f
        }.addOnFailureListener {
            Toast.makeText(this, "Submission failed. Check connection.", Toast.LENGTH_SHORT).show()
        }
    }
}
""")

# ── LeaderboardActivity.kt ────────────────────────────────────
w(f"{P}/LeaderboardAdapter.kt", """package com.example.myapplication

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

data class LeaderEntry(val name: String, val score: Int, val total: Int)

class LeaderboardAdapter(private val entries: List<LeaderEntry>) :
    RecyclerView.Adapter<LeaderboardAdapter.VH>() {

    inner class VH(v: View) : RecyclerView.ViewHolder(v) {
        val tvRank:  TextView = v.findViewById(R.id.tvRank)
        val tvName:  TextView = v.findViewById(R.id.tvName)
        val tvScore: TextView = v.findViewById(R.id.tvLeaderScore)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) =
        VH(LayoutInflater.from(parent.context).inflate(R.layout.item_leaderboard, parent, false))

    override fun onBindViewHolder(holder: VH, position: Int) {
        val e = entries[position]
        holder.tvRank.text  = when (position) { 0 -> "🥇"; 1 -> "🥈"; 2 -> "🥉"; else -> "${position + 1}." }
        holder.tvName.text  = e.name
        holder.tvScore.text = "${e.score}/${e.total}"
    }

    override fun getItemCount() = entries.size
}
""")

w(f"{P}/LeaderboardActivity.kt", """package com.example.myapplication

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.myapplication.databinding.ActivityLeaderboardBinding
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.Query

class LeaderboardActivity : AppCompatActivity() {

    private lateinit var binding: ActivityLeaderboardBinding
    private val db = FirebaseFirestore.getInstance()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLeaderboardBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.rvLeaderboard.layoutManager = LinearLayoutManager(this)
        binding.btnBack.setOnClickListener { finish() }
        loadLeaderboard()
    }

    private fun loadLeaderboard() {
        db.collection("leaderboard")
            .orderBy("score", Query.Direction.DESCENDING)
            .limit(20)
            .get()
            .addOnSuccessListener { docs ->
                val entries = docs.map { doc ->
                    LeaderEntry(
                        doc.getString("name") ?: "Anonymous",
                        doc.getLong("score")?.toInt() ?: 0,
                        doc.getLong("total")?.toInt() ?: 17
                    )
                }
                binding.rvLeaderboard.adapter = LeaderboardAdapter(entries)
            }
            .addOnFailureListener {
                Toast.makeText(this, "Could not load leaderboard.", Toast.LENGTH_SHORT).show()
            }
    }
}
""")

# ── DonationActivity.kt ───────────────────────────────────────
w(f"{P}/DonationActivity.kt", """package com.example.myapplication

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityDonationBinding

class DonationActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDonationBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDonationBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnPayPal.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW,
                Uri.parse("https://www.paypal.com/paypalme/andrejohn1500"))
            startActivity(intent)
        }
        binding.btnBackDonate.setOnClickListener { finish() }
    }
}
""")

# ── MyStoryActivity.kt ────────────────────────────────────────
w(f"{P}/MyStoryActivity.kt", """package com.example.myapplication

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityMyStoryBinding

class MyStoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMyStoryBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMyStoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.tvStory.text = \"\"\"My Story — Andre N. John

On June 14, 2025, my life changed in a single moment.

I was on duty as a Police Constable with the Special Service Unit of the Royal St. Vincent and the Grenadines Police Force — serving my country with pride and purpose — when I was seriously injured in the line of duty.

What followed was nearly a year at home. A year of stillness, reflection, and at times, real uncertainty about what the future held. But through it all, one truth anchored me — God is faithful. Every morning I opened my eyes was a reminder that my life had been spared for a reason, and that reason was worth fighting for.

In that season of recovery, I made a decision. If I could not be out in the world, I would create something for it.

With no formal training in app development, I taught myself — through failure, persistence, and faith. DREs Quizz was born in that recovery room, built question by question, screen by screen, by a man determined to turn a difficult chapter into something meaningful.

This app is my testimony. It is proof that resilience is not the absence of struggle — it is what you build in the middle of it.

If this game has brought you joy, I give God the glory. And if you feel moved to support the journey behind it, a small donation through PayPal would mean the world to me.

Thank you for playing. Thank you for reading. And above all — thank God for life.

— Andre N. John
Police Constable #738 | Special Service Unit
Royal St. Vincent and the Grenadines Police Force

"Built in stillness. Released with purpose."
        \"\"\".trimIndent()

        binding.btnBackStory.setOnClickListener { finish() }
    }
}
""")

# gradle.properties intentionally preserved — not overwritten

# ── DONE ──────────────────────────────────────────────────────

print()
print("=" * 55)
print("✅  ALL FILES GENERATED SUCCESSFULLY!")
print("=" * 55)
print()
print("📋  NEXT STEPS — do these in order:\n")
print("  1️⃣   Firebase setup (REQUIRED for leaderboard):")
print("       → console.firebase.google.com")
print("       → Create project > Add Android app")
print("       → Package name: com.example.myapplication")
print("       → Download google-services.json")
print("       → Place it at: app/google-services.json\n")
print("  2️⃣   Build the release APK:")
print("       cd /workspaces/MY_APPLICATION")
print("       ./gradlew assembleRelease\n")
print("  3️⃣   APK will be at:")
print("       app/build/outputs/apk/release/app-release.apk\n")
print("  4️⃣   Optional — add sound files to res/raw/:")
print("       correct.mp3   (correct answer sound)")
print("       wrong.mp3     (wrong answer sound)")
print("       bg_music.mp3  (background music)")
print("       Then uncomment the sound lines in QuizActivity.kt & MainActivity.kt\n")
print("🎉  DREs Quiz is ready to build!")

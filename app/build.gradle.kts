plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("com.google.gms.google-services")
}

android {
    namespace = "com.dresapps.dresquiz"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.dresapps.dresquiz"
        minSdk = 24
        targetSdk = 36
        versionCode = 9
        versionName = "1.6"
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

    buildFeatures { buildConfig = true }
    buildTypes {
        release {
            isMinifyEnabled = true
            val osKey = System.getenv("ONESIGNAL_REST_API_KEY") ?: ""
            buildConfigField("String", "ONESIGNAL_REST_API_KEY", "\"" + osKey + "\"")
                isShrinkResources = true
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
    }
}

dependencies {
    implementation("app.rive:rive-android:11.4.1")
    implementation("androidx.startup:startup-runtime:1.1.1")

    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("com.google.android.material:material:1.11.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
    implementation("androidx.recyclerview:recyclerview:1.3.2")
    implementation(platform("com.google.firebase:firebase-bom:33.7.0"))
    implementation("com.onesignal:OneSignal:5.1.6")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3")
    implementation("com.google.firebase:firebase-messaging-ktx")
    implementation("com.google.firebase:firebase-firestore-ktx")
    implementation("com.google.firebase:firebase-auth-ktx")
    implementation("com.google.android.gms:play-services-auth:21.0.0")
    implementation("com.google.android.gms:play-services-ads:23.0.0")
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.1.5")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
}

package com.dresapps.dresquiz

import android.app.Application
import android.app.Activity
import android.content.Intent
import android.os.Bundle
import app.rive.runtime.kotlin.core.Rive

class DresApplication : Application() {
    private var activityCount = 0

    override fun onCreate() {
        super.onCreate()
        Rive.init(this)
        registerActivityLifecycleCallbacks(object : ActivityLifecycleCallbacks {
            override fun onActivityStarted(a: Activity) {
                activityCount++
                if (activityCount == 1) {
                    startService(Intent(this@DresApplication, MusicService::class.java).apply {
                        action = "RESUME"
                    })
                }
            }
            override fun onActivityStopped(a: Activity) {
                activityCount--
                if (activityCount == 0) {
                    startService(Intent(this@DresApplication, MusicService::class.java).apply {
                        action = "PAUSE"
                    })
                }
            }
            override fun onActivityCreated(a: Activity, b: Bundle?) {}
            override fun onActivityResumed(a: Activity) {}
            override fun onActivityPaused(a: Activity) {}
            override fun onActivitySaveInstanceState(a: Activity, b: Bundle) {}
            override fun onActivityDestroyed(a: Activity) {}
        })
    }
}

package com.dresapps.dresquiz

import android.content.Context
import android.os.Handler
import android.os.Looper
import java.io.OutputStreamWriter
import java.net.HttpURLConnection
import java.net.URL

object SupabaseHelper {
    private const val BASE_URL = "https://ncfeudprexwdvwcnlhtx.supabase.co/rest/v1"
    private const val ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5jZmV1ZHByZXh3ZHZ3Y25saHR4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYxMDU2MzMsImV4cCI6MjA5MTY4MTYzM30.aCcKi8UooIL8nAACb3dWrbESZdYYPR8W-nPygCC7-Lc"

    fun registerUser(email: String, deviceId: String, callback: (Boolean) -> Unit) {
        Thread {
            try {
                val url = URL("$BASE_URL/users")
                val conn = url.openConnection() as HttpURLConnection
                conn.requestMethod = "POST"
                conn.setRequestProperty("Content-Type", "application/json")
                conn.setRequestProperty("apikey", ANON_KEY)
                conn.setRequestProperty("Authorization", "Bearer $ANON_KEY")
                conn.setRequestProperty("Prefer", "resolution=merge-duplicates")
                conn.doOutput = true
                val json = """{"email":"$email","device_id":"$deviceId","is_premium":false}"""
                OutputStreamWriter(conn.outputStream).use { it.write(json); it.flush() }
                val code = conn.responseCode
                conn.disconnect()
                Handler(Looper.getMainLooper()).post { callback(code in 200..299) }
            } catch (e: Exception) {
                Handler(Looper.getMainLooper()).post { callback(false) }
            }
        }.start()
    }

    fun checkPremium(email: String, callback: (Boolean) -> Unit) {
        Thread {
            try {
                val url = URL("$BASE_URL/users?email=eq.$email&select=is_premium")
                val conn = url.openConnection() as HttpURLConnection
                conn.requestMethod = "GET"
                conn.setRequestProperty("apikey", ANON_KEY)
                conn.setRequestProperty("Authorization", "Bearer $ANON_KEY")
                val response = conn.inputStream.bufferedReader().readText()
                conn.disconnect()
                val isPremium = response.contains("\"is_premium\":true")
                Handler(Looper.getMainLooper()).post { callback(isPremium) }
            } catch (e: Exception) {
                Handler(Looper.getMainLooper()).post { callback(false) }
            }
        }.start()
    }

    fun checkPremiumByDevice(deviceId: String, callback: (Boolean) -> Unit) {
        Thread {
            try {
                val url = URL("$BASE_URL/users?device_id=eq.$deviceId&select=is_premium")
                val conn = url.openConnection() as HttpURLConnection
                conn.requestMethod = "GET"
                conn.setRequestProperty("apikey", ANON_KEY)
                conn.setRequestProperty("Authorization", "Bearer $ANON_KEY")
                val response = conn.inputStream.bufferedReader().readText()
                conn.disconnect()
                val isPremium = response.contains("\"is_premium\":true")
                Handler(Looper.getMainLooper()).post { callback(isPremium) }
            } catch (e: Exception) {
                Handler(Looper.getMainLooper()).post { callback(false) }
            }
        }.start()
    }

    fun getDeviceId(ctx: Context): String {
        return android.provider.Settings.Secure.getString(ctx.contentResolver, android.provider.Settings.Secure.ANDROID_ID)
    }
}

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
                val errorBody = try { conn.errorStream?.bufferedReader()?.readText() ?: "" } catch (e: Exception) { "" }
                val successBody = try { conn.inputStream?.bufferedReader()?.readText() ?: "" } catch (e: Exception) { "" }
                android.util.Log.e("DresQuizSupabase", "registerUser code=$code body=$successBody error=$errorBody json=$json")
                conn.disconnect()
                Handler(Looper.getMainLooper()).post { callback(code in 200..299) }
            } catch (e: Exception) {
                android.util.Log.e("DresQuizSupabase", "registerUser EXCEPTION: ${e.javaClass.simpleName}: ${e.message}", e)
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



    fun fetchPlayerScores(name: String, onResult: (List<Map<String, Any>>) -> Unit) {
        Thread {
            try {
                val encoded = java.net.URLEncoder.encode(name, "UTF-8")
                val url = URL("$BASE_URL/scores?name=eq.$encoded&select=score,total,category,level,cheats,pct,time_taken,country&order=created_at.desc")
                val conn = url.openConnection() as java.net.HttpURLConnection
                conn.requestMethod = "GET"
                conn.connectTimeout = 10000
                conn.readTimeout = 10000
                conn.setRequestProperty("apikey", ANON_KEY)
                conn.setRequestProperty("Authorization", "Bearer $ANON_KEY")
                conn.setRequestProperty("Accept", "application/json")
                val body = try {
                    conn.inputStream.bufferedReader().readText()
                } catch (e: Exception) {
                    conn.errorStream?.bufferedReader()?.readText() ?: "[]"
                }
                android.util.Log.d("DresQuiz", "fetchPlayerScores[$name] code=${conn.responseCode} body=${body.take(200)}")
                val list = mutableListOf<Map<String, Any>>()
                try {
                    val arr = org.json.JSONArray(body)
                    for (i in 0 until arr.length()) {
                        val obj = arr.getJSONObject(i)
                        list.add(mapOf(
                            "score"      to obj.optInt("score", 0),
                            "total"      to obj.optInt("total", 15),
                            "category"   to obj.optString("category", ""),
                            "level"      to obj.optInt("level", 1),
                            "cheats"     to obj.optInt("cheats", 0),
                            "pct"        to obj.optInt("pct", 0),
                            "time_taken" to obj.optInt("time_taken", 0),
                            "country"    to obj.optString("country", "")
                        ))
                    }
                } catch (e: Exception) {
                    android.util.Log.e("DresQuiz", "fetchPlayerScores parse error: $e body=$body")
                }
                onResult(list)
            } catch (e: Exception) {
                android.util.Log.e("DresQuiz", "fetchPlayerScores network error: $e")
                onResult(emptyList())
            }
        }.start()
    }
}

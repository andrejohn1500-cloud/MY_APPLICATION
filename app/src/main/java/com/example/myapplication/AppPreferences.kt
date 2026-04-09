package com.example.myapplication

import android.content.Context

object AppPreferences {
    private const val PREFS_NAME = "dres_quiz_prefs"

    private const val KEY_SOUND        = "sound_enabled"
    private const val KEY_MUSIC        = "music_enabled"
    private const val KEY_HAPTICS      = "haptics_enabled"
    private const val KEY_TRACK_INDEX  = "selected_track_index"

    fun isSoundEnabled(context: Context): Boolean =
        getPrefs(context).getBoolean(KEY_SOUND, true)
    fun setSound(context: Context, enabled: Boolean) =
        getPrefs(context).edit().putBoolean(KEY_SOUND, enabled).apply()

    fun isMusicEnabled(context: Context): Boolean =
        getPrefs(context).getBoolean(KEY_MUSIC, true)
    fun setMusic(context: Context, enabled: Boolean) =
        getPrefs(context).edit().putBoolean(KEY_MUSIC, enabled).apply()

    fun isHapticsEnabled(context: Context): Boolean =
        getPrefs(context).getBoolean(KEY_HAPTICS, true)
    fun setHaptics(context: Context, enabled: Boolean) =
        getPrefs(context).edit().putBoolean(KEY_HAPTICS, enabled).apply()

    fun getSelectedTrack(context: Context): Int =
        getPrefs(context).getInt(KEY_TRACK_INDEX, 0)
    fun setSelectedTrack(context: Context, index: Int) =
        getPrefs(context).edit().putInt(KEY_TRACK_INDEX, index).apply()

    private fun getPrefs(context: Context) =
        context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
}

package com.dresapps.dresquiz
import android.content.Context
object AppPreferences {
    private const val PREFS_NAME = "dres_quiz_prefs"
    private const val KEY_SOUND         = "sound_enabled"
    private const val KEY_MUSIC         = "music_enabled"
    private const val KEY_HAPTICS       = "haptics_enabled"
    private const val KEY_TRACK_INDEX   = "selected_track_index"
    private const val KEY_PREMIUM       = "is_premium_unlocked"

    fun isSoundEnabled(ctx: Context) = getPrefs(ctx).getBoolean(KEY_SOUND, true)
    fun setSound(ctx: Context, v: Boolean) = getPrefs(ctx).edit().putBoolean(KEY_SOUND, v).apply()
    fun isMusicEnabled(ctx: Context) = getPrefs(ctx).getBoolean(KEY_MUSIC, true)
    fun setMusic(ctx: Context, v: Boolean) = getPrefs(ctx).edit().putBoolean(KEY_MUSIC, v).apply()
    fun isHapticsEnabled(ctx: Context) = getPrefs(ctx).getBoolean(KEY_HAPTICS, true)
    fun setHaptics(ctx: Context, v: Boolean) = getPrefs(ctx).edit().putBoolean(KEY_HAPTICS, v).apply()
    fun getSelectedTrack(ctx: Context) = getPrefs(ctx).getInt(KEY_TRACK_INDEX, 0)
    fun setSelectedTrack(ctx: Context, i: Int) = getPrefs(ctx).edit().putInt(KEY_TRACK_INDEX, i).apply()

    fun isPremium(ctx: Context) = getPrefs(ctx).getBoolean(KEY_PREMIUM, false)
    fun setPremium(ctx: Context, v: Boolean) = getPrefs(ctx).edit().putBoolean(KEY_PREMIUM, v).apply()

    fun getHighestLevel(ctx: Context, category: String): Int {
        val key = "highest_level_" + category.replace(" ", "_")
        return getPrefs(ctx).getInt(key, 1)
    }
    fun setHighestLevel(ctx: Context, category: String, level: Int) {
        val key = "highest_level_" + category.replace(" ", "_")
        val cur = getHighestLevel(ctx, category)
        if (level > cur) getPrefs(ctx).edit().putInt(key, level).apply()
    }

    fun resetAll(ctx: Context) = getPrefs(ctx).edit().clear().apply()

    private fun getPrefs(ctx: Context) = ctx.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
}

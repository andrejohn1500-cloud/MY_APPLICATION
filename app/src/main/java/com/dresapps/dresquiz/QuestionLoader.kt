package com.dresapps.dresquiz

import android.content.Context
import org.json.JSONObject

object QuestionLoader {

    fun loadQuestions(context: Context, category: String, level: Int): List<Question> {
        val fileName = getCategoryFileName(category, level)
        return try {
            val json = context.assets.open("questions/$fileName")
                .bufferedReader().use { it.readText() }
            parseQuestions(json)
        } catch (e: Exception) {
            emptyList()
        }
    }

    private fun parseQuestions(json: String): List<Question> {
        val result = mutableListOf<Question>()
        val obj = JSONObject(json)
        val category = obj.getString("category")
        val arr = obj.getJSONArray("questions")
        for (i in 0 until arr.length()) {
            val q = arr.getJSONObject(i)
            val options = mutableListOf<String>()
            val opts = q.getJSONArray("options")
            for (j in 0 until opts.length()) options.add(opts.getString(j))
            result.add(Question(
                text = q.getString("q"),
                options = options,
                correctIndex = q.getInt("answer"),
                category = category
            ))
        }
        return result
    }

    private fun getCategoryFileName(category: String, level: Int): String {
        val base = when {
            category.contains("Maths") -> "cxc_maths"
            category.contains("English A") -> "cxc_english_a"
            category.contains("English B") -> "cxc_english_b"
            category.contains("Integrated Science") -> "cxc_integrated_science"
            category.contains("Social Studies") -> "cxc_social_studies"
            category.contains("Geography") -> "cxc_geography"
            category.contains("POB") -> "cxc_pob"
            category.contains("CXC IT") -> "cxc_it"
            category.contains("Office Admin") -> "cxc_office_admin"
            category.contains("Physical Education") -> "cxc_pe"
            category.contains("Caribbean History") -> "caribbean_history"
            category.contains("Science & Tech") -> "science_tech"
            category.contains("Sports") -> "sports"
            category.contains("World Geography") -> "world_geography"
            category.contains("Arts") -> "arts_culture"
            category.contains("Vincy") -> "svg_vincy"
            else -> "caribbean_history"
        }
        return "${base}_l${level}.json"
    }
}

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
    return try {
        val trimmed = json.trim()
        if (trimmed.startsWith("[")) {
            val arr = org.json.JSONArray(trimmed)
            for (i in 0 until arr.length()) {
                val q = arr.getJSONObject(i)
                val options = mutableListOf<String>()
                val opts = q.getJSONArray("options")
                for (j in 0 until opts.length()) options.add(opts.getString(j))
                result.add(Question(
                    text = q.getString("question"),
                    options = options,
                    correctIndex = q.getInt("correctIndex"),
                    category = ""
                ))
            }
        } else {
            val obj = JSONObject(trimmed)
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
        }
        result
    } catch (e: Exception) { result }
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
        category.contains("Agricultural Science") -> "cxc_agricultural_science"
        category.contains("Building Technology") -> "cxc_building_technology"
        category.contains("Clothing") -> "cxc_clothing_textiles"
        category.contains("Food & Nutrition") -> "cxc_food_nutrition"
        category.contains("French") -> "cxc_french"
        category.contains("History") -> "cxc_history"
        category.contains("Human & Social") -> "cxc_human_social_biology"
        category.contains("Music") -> "cxc_music"
        category.contains("Physics") -> "cxc_physics"
        category.contains("Principles of Accounts") -> "cxc_principles_of_accounts"
        category.contains("Religious") -> "cxc_religious_education"
        category.contains("Spanish") -> "cxc_spanish"
        category.contains("TCF") -> "cxc_tcf"
        category.contains("Technical Drawing") -> "cxc_technical_drawing"
        category.contains("Theatre") -> "cxc_theatre_arts"
        category.contains("Tourism") -> "cxc_tourism"
        category.contains("Visual Arts") -> "cxc_visual_arts"
        category.contains("CPEA English") -> "cpea_english"
        category.contains("CPEA Maths") -> "cpea_mathematics"
        category.contains("CPEA Science") -> "cpea_science"
        category.contains("CPEA Social") -> "cpea_social_studies"
        category.contains("SEA Maths") -> "sea_mathematics"
        category.contains("SEA Language") -> "sea_language_arts"
        category.contains("PEP Ability") -> "pep_ability_test"
        category.contains("PEP Maths") -> "pep_mathematics"
        category.contains("PEP Language") -> "pep_language_arts"
        category.contains("Science Tech") -> "science_tech"
        category.contains("CAPE Accounting") -> "cape_accounting"
        category.contains("CAPE Biology") -> "cape_biology"
        category.contains("CAPE Chemistry") -> "cape_chemistry"
        category.contains("CAPE Economics") -> "cape_economics"
        category.contains("CAPE Geography") -> "cape_geography"
        category.contains("CAPE History") -> "cape_history"
        category.contains("CAPE Law") -> "cape_law"
        category.contains("CAPE Maths") -> "cape_mathematics"
        category.contains("CAPE Physics") -> "cape_physics"
        category.contains("CAPE Sociology") -> "cape_sociology"
        category.contains("CVQ Carpentry") -> "cvq_carpentry_joinery"
        category.contains("CVQ Cosmetology") -> "cvq_cosmetology"
        category.contains("CVQ Electrical") -> "cvq_electrical_installation"
        category.contains("CVQ Food") -> "cvq_food_preparation"
        category.contains("CVQ IT") -> "cvq_information_technology"
        category.contains("CVQ Plumbing") -> "cvq_plumbing"
        category.contains("CVQ Welding") -> "cvq_welding_fabrication"
            else -> "caribbean_history"
        }
        return "${base}_l${level}.json"
    }
}

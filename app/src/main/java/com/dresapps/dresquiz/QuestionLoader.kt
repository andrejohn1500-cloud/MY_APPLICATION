package com.dresapps.dresquiz

import android.content.Context
import org.json.JSONObject

object QuestionLoader {

    fun loadQuestions(context: Context, category: String, level: Int): List<Question> {
        val fileName = getCategoryFileName(category, level)
        return try {
            val json = context.assets.open("questions/$fileName")
                .bufferedReader().use { it.readText() }
            val questions = parseQuestions(json)
            if (category.startsWith("CPEA")) {
                questions.map { q ->
                    val trimmed = q.options.take(3).toMutableList()
                    trimmed.add("Not applicable")
                    q.copy(options = trimmed)
                }
            } else {
                questions
            }
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
        val base = when (category) {
            "Caribbean History" -> "caribbean_history"
        "Science & Tech" -> "science_tech"
        "Sports" -> "sports"
        "World Geography" -> "world_geography"
        "Arts & Culture" -> "arts_culture"
        "SVG & Vincy Life" -> "svg_vincy"
        "CXC English A" -> "cxc_english_a"
        "CXC English B" -> "cxc_english_b"
        "CXC Maths" -> "cxc_maths"
        "CXC Integrated Science" -> "cxc_integrated_science"
        "CXC Social Studies" -> "cxc_social_studies"
        "CXC Geography" -> "cxc_geography"
        "CXC POB" -> "cxc_pob"
        "CXC IT" -> "cxc_it"
        "CXC Office Admin" -> "cxc_office_admin"
        "CXC Physical Education" -> "cxc_pe"
        "CXC Agricultural Science" -> "cxc_agricultural_science"
        "CXC Building Technology" -> "cxc_building_technology"
        "CXC Clothing & Textiles" -> "cxc_clothing_textiles"
        "CXC Food & Nutrition" -> "cxc_food_nutrition"
        "CXC French" -> "cxc_french"
        "CXC History" -> "cxc_history"
        "CXC Human & Social Biology" -> "cxc_human_social_biology"
        "CXC Music" -> "cxc_music"
        "CXC Physics" -> "cxc_physics"
        "CXC Principles of Accounts" -> "cxc_principles_of_accounts"
        "CXC Religious Education" -> "cxc_religious_education"
        "CXC Spanish" -> "cxc_spanish"
        "CXC TCF" -> "cxc_tcf"
        "CXC Technical Drawing" -> "cxc_technical_drawing"
        "CXC Theatre Arts" -> "cxc_theatre_arts"
        "CXC Tourism" -> "cxc_tourism"
        "CXC Visual Arts" -> "cxc_visual_arts"
        "CPEA English" -> "cpea_english"
        "CPEA Maths" -> "cpea_mathematics"
        "CPEA Science" -> "cpea_science"
        "CPEA Social Studies" -> "cpea_social_studies"
        "SEA Maths" -> "sea_mathematics"
        "SEA Language Arts" -> "sea_language_arts"
        "PEP Ability Test" -> "pep_ability_test"
        "PEP Maths" -> "pep_mathematics"
        "PEP Language Arts" -> "pep_language_arts"
        "CAPE Accounting" -> "cape_accounting"
        "CAPE Agricultural Science" -> "cape_agricultural_science"
        "CAPE Applied Mathematics" -> "cape_applied_mathematics"
        "CAPE Biology" -> "cape_biology"
        "CAPE Caribbean Studies" -> "cape_caribbean_studies"
        "CAPE Chemistry" -> "cape_chemistry"
        "CAPE Communication Studies" -> "cape_communication_studies"
        "CAPE Computer Science" -> "cape_computer_science"
        "CAPE Economics" -> "cape_economics"
        "CAPE Environmental Science" -> "cape_environmental_science"
        "CAPE French" -> "cape_french"
        "CAPE Geography" -> "cape_geography"
        "CAPE History" -> "cape_history"
        "CAPE Law" -> "cape_law"
        "CAPE Literatures in English" -> "cape_literatures_english"
        "CAPE Management of Business" -> "cape_management_of_business"
        "CAPE Maths" -> "cape_mathematics"
        "CAPE Music" -> "cape_music"
        "CAPE Physics" -> "cape_physics"
        "CAPE Political Science" -> "cape_political_science"
        "CAPE Psychology" -> "cape_psychology"
        "CAPE Sociology" -> "cape_sociology"
        "CAPE Spanish" -> "cape_spanish"
        "CAPE Tourism" -> "cape_tourism"
        "CAPE Visual Arts" -> "cape_visual_arts"
        "CVQ Agricultural Production" -> "cvq_agricultural_production"
        "CVQ Carpentry & Joinery" -> "cvq_carpentry_joinery"
        "CVQ Cosmetology" -> "cvq_cosmetology"
        "CVQ Early Childhood" -> "cvq_early_childhood"
        "CVQ Electrical Installation" -> "cvq_electrical_installation"
        "CVQ Food Preparation" -> "cvq_food_preparation"
        "CVQ Information Technology" -> "cvq_information_technology"
        "CVQ Motor Vehicle" -> "cvq_motor_vehicle"
        "CVQ Plumbing" -> "cvq_plumbing"
        "CVQ Welding & Fabrication" -> "cvq_welding_fabrication"
        else -> "caribbean_history"
        }
        return "${base}_l${level}.json"
    }
}

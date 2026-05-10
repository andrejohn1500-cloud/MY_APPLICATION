import anthropic
import json
import os
import time
import subprocess

key = open(".env").read().strip().split("=",1)[1]
client = anthropic.Anthropic(api_key=key)

SUBJECTS = [
    ("cxc_human_social_biology", "CXC Human and Social Biology"),
    ("cxc_history", "CXC History"),
    ("cxc_spanish", "CXC Spanish"),
    ("cxc_biology", "CXC Biology"),
    ("cxc_chemistry", "CXC Chemistry"),
    ("cxc_physics", "CXC Physics"),
    ("cxc_economics", "CXC Economics"),
    ("cxc_agricultural_science", "CXC Agricultural Science"),
    ("cxc_technical_drawing", "CXC Technical Drawing"),
    ("cxc_food_nutrition", "CXC Food and Nutrition"),
    ("cxc_visual_arts", "CXC Visual Arts"),
    ("cxc_music", "CXC Music"),
    ("cxc_tcf", "CXC Technical and Vocational"),
    ("cxc_religious_education", "CXC Religious Education"),
    ("cxc_french", "CXC French"),
    ("cxc_principles_of_accounts", "CXC Principles of Accounts"),
    ("cxc_theatre_arts", "CXC Theatre Arts"),
    ("cxc_tourism", "CXC Tourism"),
    ("cxc_building_technology", "CXC Building Technology"),
    ("cxc_clothing_textiles", "CXC Clothing and Textiles"),
    ("cape_communication_studies", "CAPE Communication Studies"),
    ("cape_caribbean_studies", "CAPE Caribbean Studies"),
    ("cape_literatures_english", "CAPE Literatures in English"),
    ("cape_sociology", "CAPE Sociology"),
    ("cape_law", "CAPE Law"),
    ("cape_political_science", "CAPE Political Science"),
    ("cape_psychology", "CAPE Psychology"),
    ("cape_economics", "CAPE Economics"),
    ("cape_accounting", "CAPE Accounting"),
    ("cape_management_of_business", "CAPE Management of Business"),
    ("cape_biology", "CAPE Biology"),
    ("cape_chemistry", "CAPE Chemistry"),
    ("cape_physics", "CAPE Physics"),
    ("cape_environmental_science", "CAPE Environmental Science"),
    ("cape_computer_science", "CAPE Computer Science"),
    ("cape_mathematics", "CAPE Mathematics"),
    ("cape_applied_mathematics", "CAPE Applied Mathematics"),
    ("cape_agricultural_science", "CAPE Agricultural Science"),
    ("cape_french", "CAPE French"),
    ("cape_spanish", "CAPE Spanish"),
    ("cape_history", "CAPE History"),
    ("cape_geography", "CAPE Geography"),
    ("cape_tourism", "CAPE Tourism"),
    ("cape_music", "CAPE Music"),
    ("cape_visual_arts", "CAPE Visual Arts"),
    ("cvq_cosmetology", "CVQ Cosmetology"),
    ("cvq_electrical_installation", "CVQ Electrical Installation"),
    ("cvq_plumbing", "CVQ Plumbing"),
    ("cvq_carpentry_joinery", "CVQ Carpentry and Joinery"),
    ("cvq_food_preparation", "CVQ Food Preparation and Cooking"),
    ("cvq_welding_fabrication", "CVQ Welding and Fabrication"),
    ("cvq_motor_vehicle", "CVQ Motor Vehicle Technology"),
    ("cvq_information_technology", "CVQ Information Technology"),
    ("cvq_agricultural_production", "CVQ Agricultural Production"),
    ("cvq_early_childhood", "CVQ Early Childhood Care and Education"),
    ("pep_ability_test", "PEP Ability Test"),
    ("pep_language_arts", "PEP Language Arts"),
    ("pep_mathematics", "PEP Mathematics"),
    ("sea_mathematics", "SEA Mathematics"),
    ("sea_language_arts", "SEA Language Arts"),
    ("cpea_mathematics", "CPEA Mathematics"),
    ("cpea_english", "CPEA English Language"),
    ("cpea_science", "CPEA Science"),
    ("cpea_social_studies", "CPEA Social Studies"),
]

OUTPUT_DIR = "app/src/main/assets/questions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

total = len(SUBJECTS) * 20
done = 0

def git_commit(subject_name):
    try:
        subprocess.run(["git", "add", "-A"], check=True)
        subprocess.run(["git", "commit", "-m", f"Add questions: {subject_name}"], check=True)
        subprocess.run(["git", "push", "origin", "master"], check=True)
        print(f"✅ Committed {subject_name} to GitHub!")
    except Exception as e:
        print(f"Git error: {e}")

for subject_key, subject_name in SUBJECTS:
    subject_done = True
    for level in range(1, 21):
        filename = f"{subject_key}_l{level}.json"
        filepath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(filepath):
            done += 1
            continue
        subject_done = False
        difficulty = "easy" if level <= 3 else "intermediate" if level <= 10 else "advanced"
        prompt = f"""Generate exactly 15 multiple choice questions for {subject_name} Level {level}.
Difficulty: {difficulty}. Cover varied topics from the full {subject_name} syllabus.
Respond ONLY with a valid JSON array, no markdown, no extra text:
[{{"question":"...","options":["A","B","C","D"],"correctIndex":0}}]"""
        try:
            print(f"Generating {subject_name} Level {level}... ({done+1}/{total})")
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=2000,
                messages=[{"role":"user","content":prompt}]
            )
            text = response.content[0].text.strip()
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            questions = json.loads(text)
            with open(filepath, "w") as f:
                json.dump(questions, f, indent=2)
            print(f"Saved {filename}")
            done += 1
            time.sleep(0.3)
        except Exception as e:
            print(f"Error {filename}: {e}")
            time.sleep(2)
    if not subject_done:
        git_commit(subject_name)

print(f"Done! {done}/{total}")

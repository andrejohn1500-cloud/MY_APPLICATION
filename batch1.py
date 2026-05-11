import json, os, random, time
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
PATH = "app/src/main/assets/questions/"

SUBJECTS = [
    ("cxc_english_a", "CXC CSEC English A", [
        "reading comprehension", "summary writing", "narrative writing", "expository writing",
        "argumentative writing", "persuasive writing", "report writing", "letter writing",
        "grammar and usage", "parts of speech", "sentence structure", "punctuation",
        "vocabulary in context", "literary devices", "figurative language", "prose fiction",
        "drama", "poetry analysis", "media and communication", "listening comprehension"
    ]),
    ("cxc_english_b", "CXC CSEC English B", [
        "poetry analysis", "prose fiction", "drama and theatre", "literary devices",
        "figurative language", "characterisation", "theme and setting", "narrative point of view",
        "Caribbean literature", "African literature", "British literature", "American literature",
        "oral tradition", "folk literature", "short story", "novel study",
        "essay writing", "critical analysis", "tone and mood", "symbolism"
    ]),
    ("cxc_mathematics", "CXC CSEC Mathematics", [
        "number theory", "fractions decimals percentages", "ratios and proportions",
        "consumer arithmetic", "sets", "algebraic expressions", "linear equations",
        "simultaneous equations", "quadratic equations", "inequalities", "functions and graphs",
        "geometry and measurement", "circle theorems", "trigonometry", "statistics",
        "probability", "matrices", "vectors", "sequences and series", "mensuration"
    ]),
    ("cxc_integrated_science", "CXC CSEC Integrated Science", [
        "scientific method", "cells and cell processes", "photosynthesis and respiration",
        "human body systems", "reproduction", "genetics and heredity", "ecosystems",
        "food chains and webs", "conservation", "matter and its properties",
        "chemical reactions", "acids bases and salts", "atomic structure",
        "forces and motion", "energy forms and transfer", "electricity and magnetism",
        "waves light and sound", "the earth and atmosphere", "weather and climate",
        "space and the solar system"
    ]),
    ("cxc_social_studies", "CXC CSEC Social Studies", [
        "individual and society", "family and socialisation", "culture and identity",
        "Caribbean history and heritage", "colonialism and its effects",
        "Caribbean integration", "CARICOM", "governance and democracy",
        "citizenship and rights", "human rights", "economic systems",
        "production and consumption", "trade and development", "poverty and inequality",
        "crime and social issues", "environment and sustainable development",
        "population and migration", "health and wellbeing", "media and communication",
        "global issues affecting the Caribbean"
    ]),
]

LEVEL_TIER_MAP = {
    1:0,2:0,3:0,4:0,5:0,
    6:1,7:1,8:1,9:1,10:1,
    11:2,12:2,13:2,14:2,15:2,
    16:3,17:3,18:3,19:3,20:3
}

TIER_LABELS = [
    ("foundation", "basic recall and simple understanding of fundamental concepts"),
    ("intermediate", "application and moderate problem solving"),
    ("advanced", "analysis synthesis and challenging application"),
    ("expert", "complex evaluation critical thinking and highest difficulty"),
]

def already_done(cat_key):
    for lvl in range(1, 21):
        fp = os.path.join(PATH, f"{cat_key}_l{lvl}.json")
        if not os.path.exists(fp):
            return False
        try:
            data = json.load(open(fp))
            if len(data) != 15:
                return False
        except:
            return False
    return True

def generate_tier(subject_name, topics, tier_label, tier_desc, existing):
    prompt = f"""You are an expert question writer for the {subject_name} examination.

Generate exactly 80 unique multiple choice questions based STRICTLY on the official {subject_name} syllabus.

Difficulty: {tier_label} — {tier_desc}

Draw questions from these syllabus topics: {', '.join(topics)}

Rules:
- Every question must come directly from {subject_name} syllabus content
- Cover as many different topics as possible across the 80 questions
- Each question must be completely unique — no repeats
- Each question must have exactly one correct answer and three plausible wrong answers
- Do not use any of these questions: {list(existing)[:10]}

Respond ONLY with a valid JSON array, no markdown, no extra text:
[
  {{
    "question": "Question text?",
    "correct": "Correct answer",
    "wrong": ["Wrong 1", "Wrong 2", "Wrong 3"]
  }}
]"""

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=6000,
                temperature=0.7
            )
            text = response.choices[0].message.content.strip()
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            parsed = json.loads(text)
            fresh = [q for q in parsed if q["question"] not in existing]
            print(f"    {tier_label}: {len(fresh)} fresh questions")
            return fresh
        except Exception as e:
            print(f"    Attempt {attempt+1} failed: {e}")
            time.sleep(3)
    return []

def write_files(cat_key, all_questions):
    quarter = len(all_questions) // 4
    tiers = [
        all_questions[0:quarter],
        all_questions[quarter:quarter*2],
        all_questions[quarter*2:quarter*3],
        all_questions[quarter*3:]
    ]
    used = {0:set(), 1:set(), 2:set(), 3:set()}

    for lvl in range(1, 21):
        tier_idx = LEVEL_TIER_MAP[lvl]
        pool = [q for q in tiers[tier_idx] if q["question"] not in used[tier_idx]]
        random.shuffle(pool)
        selected = pool[:15]
        used[tier_idx].update(q["question"] for q in selected)

        data = []
        for item in selected:
            opts = [item["correct"]] + item["wrong"][:3]
            random.shuffle(opts)
            ci = opts.index(item["correct"])
            data.append({"question": item["question"], "options": opts, "correctIndex": ci})

        out = os.path.join(PATH, f"{cat_key}_l{lvl}.json")
        with open(out, 'w') as f:
            json.dump(data, f, indent=2)

    print(f"  ✅ {cat_key} written — 20 levels x 15 questions")

def run_batch(subjects):
    global_existing = set()
    for cat_key, subject_name, topics in subjects:
        if already_done(cat_key):
            print(f"⏭️  {cat_key} already has 15 questions per level — skipping")
            continue

        print(f"\n📚 Generating: {subject_name}")
        all_questions = []

        for tier_label, tier_desc in TIER_LABELS:
            qs = generate_tier(subject_name, topics, tier_label, tier_desc, global_existing)
            all_questions.extend(qs)
            global_existing.update(q["question"] for q in qs)
            time.sleep(3)

        if len(all_questions) >= 60:
            write_files(cat_key, all_questions)
        else:
            print(f"  ❌ Only {len(all_questions)} questions generated — skipping {cat_key}")

    print("\n✅ Batch 1 complete — committing to GitHub...")
    os.system('git add . && git commit -m "Batch 1: regenerate CXC English A, English B, Mathematics, Integrated Science, Social Studies" && git pull --rebase origin master && git push origin master')
    print("✅ Pushed!")

run_batch(SUBJECTS)

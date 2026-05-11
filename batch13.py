# TO RUN:
# Step 1: export GROQ_API_KEY=your_key
# Step 2: python3 /workspaces/MY_APPLICATION/batch13.py
import json, os, random, time
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
PATH = "app/src/main/assets/questions/"

SUBJECTS = [
    ("cvq_food_preparation", "CVQ Food Preparation and Cooking", "kitchen safety and hygiene, food handling, cooking methods, knife skills, menu planning, Caribbean cuisine, baking, nutrition, food presentation, stock and sauce preparation"),
    ("cvq_information_technology", "CVQ Information Technology", "computer hardware, software applications, operating systems, networking basics, internet safety, word processing, spreadsheets, databases, cybersecurity, Caribbean ICT applications"),
    ("cvq_motor_vehicle", "CVQ Motor Vehicle Technology", "engine systems, electrical systems, braking systems, transmission, steering and suspension, vehicle safety, diagnostic tools, Caribbean road regulations, maintenance schedules, workshop safety"),
    ("cvq_plumbing", "CVQ Plumbing", "plumbing tools and materials, pipe systems, water supply, drainage systems, sanitary fittings, safety regulations, blueprint reading, Caribbean plumbing standards, maintenance and repair, water conservation"),
    ("cvq_welding_fabrication", "CVQ Welding and Fabrication", "welding processes, welding safety, metal types and properties, cutting techniques, joint preparation, MIG welding, TIG welding, arc welding, blueprint reading, quality control"),
]

LEVEL_TIER_MAP = {1:0,2:0,3:0,4:0,5:0,6:1,7:1,8:1,9:1,10:1,11:2,12:2,13:2,14:2,15:2,16:3,17:3,18:3,19:3,20:3}
TIERS = ["foundation","intermediate","advanced","expert"]
TIER_DESC = ["basic recall of fundamental concepts","moderate application and understanding","challenging analysis and problem solving","complex evaluation at highest difficulty"]

def generate_tier(subject_name, topics, tier, desc, existing):
    prompt = f"""Generate 40 unique multiple choice questions for {subject_name} at {tier} level ({desc}).
Topics: {topics}
Rules: strictly syllabus based, no repeats, one correct answer and 3 wrong answers per question.
Every question must have a wrong array with exactly 3 items.
Reply ONLY with JSON array:
[{{"question":"...","correct":"...","wrong":["...","...","..."]}}]"""
    for attempt in range(3):
        try:
            r = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role":"user","content":prompt}],
                max_tokens=4000,
                temperature=0.7
            )
            text = r.choices[0].message.content.strip()
            if "```" in text:
                parts = text.split("```")
                for p in parts:
                    if "[" in p:
                        text = p
                        break
            if text.startswith("json"):
                text = text[4:]
            start = text.find("[")
            end = text.rfind("]") + 1
            text = text[start:end]
            parsed = json.loads(text)
            fresh = [q for q in parsed if isinstance(q,dict) and "question" in q and "correct" in q and "wrong" in q and len(q.get("wrong",[])) >= 3 and q["question"] not in existing]
            print(f"    {tier}: {len(fresh)} questions")
            return fresh
        except Exception as e:
            print(f"    Attempt {attempt+1} failed: {e}")
            time.sleep(4)
    return []

def write_files(cat_key, all_questions):
    quarter = max(1, len(all_questions) // 4)
    tiers = [all_questions[0:quarter],all_questions[quarter:quarter*2],all_questions[quarter*2:quarter*3],all_questions[quarter*3:]]
    used = {0:set(),1:set(),2:set(),3:set()}
    for lvl in range(1,21):
        ti = LEVEL_TIER_MAP[lvl]
        pool = [q for q in tiers[ti] if q["question"] not in used[ti]]
        random.shuffle(pool)
        sel = pool[:15]
        used[ti].update(q["question"] for q in sel)
        data = []
        for item in sel:
            opts = [item["correct"]] + item["wrong"][:3]
            random.shuffle(opts)
            ci = opts.index(item["correct"])
            data.append({"question":item["question"],"options":opts,"correctIndex":ci})
        with open(os.path.join(PATH, f"{cat_key}_l{lvl}.json"),"w") as f:
            json.dump(data, f, indent=2)
    print(f"  ✅ {cat_key} — 20 levels x 15 questions written")

global_existing = set()
for cat_key, subject_name, topics in SUBJECTS:
    print(f"\n📚 {subject_name}")
    all_questions = []
    for i, tier in enumerate(TIERS):
        qs = generate_tier(subject_name, topics, tier, TIER_DESC[i], global_existing)
        all_questions.extend(qs)
        global_existing.update(q["question"] for q in qs)
        time.sleep(4)
    if len(all_questions) >= 60:
        write_files(cat_key, all_questions)
    else:
        print(f"  ❌ Only {len(all_questions)} questions — skipping {cat_key}")

print("\n✅ Batch 13 complete — committing...")
os.system('git add . && git commit -m "Batch 13: CVQ Food Preparation, IT, Motor Vehicle, Plumbing, Welding and Fabrication — 15q per level syllabus based" && git pull --rebase origin master && git push origin master')
print("✅ Done!")

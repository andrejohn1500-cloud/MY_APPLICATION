# TO RUN:
# Step 1: export GROQ_API_KEY=your_key
# Step 2: python3 /workspaces/MY_APPLICATION/batch14.py
import json, os, random, time
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
PATH = "app/src/main/assets/questions/"

SUBJECTS = [
    ("sea_mathematics", "SEA Mathematics Trinidad and Tobago", "number operations, fractions and decimals, percentages, ratio and proportion, measurement, geometry, algebra, statistics, problem solving, consumer arithmetic, patterns and sequences"),
    ("sea_language_arts", "SEA Language Arts Trinidad and Tobago", "reading comprehension, vocabulary, grammar, punctuation, spelling, creative writing, letter writing, summary writing, poetry appreciation, oral language skills"),
    ("pep_ability_test", "PEP Ability Test Jamaica", "verbal reasoning, numerical reasoning, abstract reasoning, logical patterns, spatial reasoning, sequence completion, analogies, classification, problem solving patterns, critical thinking"),
    ("pep_mathematics", "PEP Mathematics Jamaica", "number operations, fractions, decimals, percentages, measurement, geometry, algebra, statistics, problem solving, consumer arithmetic, sets and Venn diagrams"),
    ("pep_language_arts", "PEP Language Arts Jamaica", "reading comprehension, vocabulary in context, grammar, punctuation, creative writing, summary writing, poetry analysis, oral communication, spelling, sentence structure"),
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

print("\n✅ Batch 14 complete — committing...")
os.system('git add . && git commit -m "Batch 14: SEA Mathematics, SEA Language Arts, PEP Ability Test, PEP Mathematics, PEP Language Arts — 15q per level syllabus based" && git pull --rebase origin master && git push origin master')
print("✅ Done!")

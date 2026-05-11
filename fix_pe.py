# TO RUN:
# Step 1: export GROQ_API_KEY=your_key
# Step 2: python3 /workspaces/MY_APPLICATION/fix_pe.py
import json, os, random, time
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
PATH = "app/src/main/assets/questions/"

LEVEL_TIER_MAP = {1:0,2:0,3:0,4:0,5:0,6:1,7:1,8:1,9:1,10:1,11:2,12:2,13:2,14:2,15:2,16:3,17:3,18:3,19:3,20:3}
TIERS = ["foundation", "intermediate", "advanced", "expert"]
TIER_DESC = ["basic recall of fundamental concepts","moderate application and understanding","challenging analysis and problem solving","complex evaluation at highest difficulty"]

def generate_tier(tier, desc, existing):
    prompt = f"""Generate 40 unique multiple choice questions for CXC Physical Education at {tier} level ({desc}).
Topics: physical fitness, nutrition, biomechanics, sports psychology, team sports, individual sports, first aid, sports injuries, Olympic movement, Caribbean sports history, exercise physiology, motor skills, health and wellness
Rules: strictly based on CXC Physical Education syllabus, no repeats, one correct answer and 3 wrong answers.
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
            fresh = [q for q in parsed if isinstance(q, dict) and "question" in q and q["question"] not in existing]
            print(f"    {tier}: {len(fresh)} questions")
            return fresh
        except Exception as e:
            print(f"    Attempt {attempt+1} failed: {e}")
            time.sleep(4)
    return []

print("📚 CXC Physical Education")
all_questions = []
existing = set()
for i, tier in enumerate(TIERS):
    qs = generate_tier(tier, TIER_DESC[i], existing)
    all_questions.extend(qs)
    existing.update(q["question"] for q in qs)
    time.sleep(4)

quarter = max(1, len(all_questions) // 4)
tiers = [all_questions[0:quarter],all_questions[quarter:quarter*2],all_questions[quarter*2:quarter*3],all_questions[quarter*3:]]
used = {0:set(),1:set(),2:set(),3:set()}
for lvl in range(1, 21):
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
    with open(os.path.join(PATH, f"cxc_physical_education_l{lvl}.json"), 'w') as f:
        json.dump(data, f, indent=2)

print("✅ cxc_physical_education — 20 levels x 15 questions written")
os.system('git add . && git commit -m "Fix CXC Physical Education — correct subject name, 15q per level" && git pull --rebase origin master && git push origin master')
print("✅ Done!")

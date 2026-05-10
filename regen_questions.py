import os, json, time
import urllib.request

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
PATH = "app/src/main/assets/questions/"

CATEGORIES = {
    "cxc_tcf": "CXC CSEC Textile Clothing and Fashion",
    "cxc_biology": "CXC CSEC Biology",
    "cxc_chemistry": "CXC CSEC Chemistry",
    "cxc_economics": "CXC CSEC Economics",
    "cxc_theatre_arts": "CXC CSEC Theatre Arts",
    "cxc_visual_arts": "CXC CSEC Visual Arts",
    "sea_language_arts": "SEA Language Arts Trinidad and Tobago primary school",
    "pep_language_arts": "PEP Language Arts Jamaica primary school",
    "cape_applied_mathematics": "CAPE Applied Mathematics",
}

def ask_groq(subject, level):
    prompt = f"""Generate exactly 20 multiple choice questions for {subject}, difficulty level {level} out of 20.
Return ONLY a JSON array, no explanation, no markdown. Format:
[{{"question":"...","options":["A","B","C","D"],"correctIndex":0}},...]
Make sure questions are specific and accurate to the {subject} syllabus."""

    body = json.dumps({
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }).encode()

    req = urllib.request.Request(
        "https://api.groq.com/openai/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(req) as r:
        result = json.loads(r.read())
    return result["choices"][0]["message"]["content"]

for cat, subject in CATEGORIES.items():
    print(f"\n--- {cat} ---")
    for lvl in range(1, 21):
        out = f"{PATH}{cat}_l{lvl}.json"
        try:
            raw = ask_groq(subject, lvl)
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            data = json.loads(raw.strip())
            with open(out, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"  ✅ level {lvl} ({len(data)} questions)")
            time.sleep(1)
        except Exception as e:
            print(f"  ❌ level {lvl}: {e}")
            time.sleep(2)

print("\nDone!")

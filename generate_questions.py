import json, random, os, re

PATH = "app/src/main/assets/questions/"
os.makedirs(PATH, exist_ok=True)

CATEGORIES = {
    "cxc_maths":              ["maths_l1_10.md",          "maths_l11_20.md"],
    "cxc_english_a":          ["english_a_l1_10.md",      "english_a_l11_20.md"],
    "cxc_english_b":          ["english_b_l1_10.md",      "english_b_l11_20.md"],
    "cxc_integrated_science": ["int_science_l1_10.md",    "int_science_l11_20.md"],
    "cxc_social_studies":     ["social_studies_l1_10.md", "social_studies_l11_20.md"],
    "cxc_geography":          ["geography_l1_10.md",      "geography_l11_20.md"],
    "cxc_pob":                ["pob_l1_10.md",            "pob_l11_20.md"],
    "cxc_it":                 ["it_l1_10.md",             "it_l11_20.md"],
    "cxc_office_admin":       ["office_admin_l1_10.md",   "office_admin_l11_20.md"],
    "cxc_pe":                 ["pe_l1_10.md",             "pe_l11_20.md"],
    "caribbean_history":      ["caribbean_history_l1_10.md", "caribbean_history_l11_20.md"],
    "science_tech":           ["science_tech_l1_10.md",   "science_tech_l11_20.md"],
    "sports":                 ["sports_l1_10.md",         "sports_l11_20.md"],
    "world_geography":        ["world_geography_l1_10.md","world_geography_l11_20.md"],
    "arts_culture":           ["arts_culture_l1_10.md",   "arts_culture_l11_20.md"],
    "svg_vincy":              ["svg_vincy_l1_10.md",      "svg_vincy_l11_20.md"],
}

def parse_md(filepath):
    levels = {}
    current_level = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            m = re.match(r'^## Level (\d+)', line)
            if m:
                current_level = int(m.group(1))
                levels[current_level] = []
            elif current_level and re.match(r'^\d+\.', line):
                parts = re.split(r'\s*[→\-]+>\s*', line, 1)
                if len(parts) == 2:
                    q = re.sub(r'^\d+\.\s*', '', parts[0]).strip()
                    a = re.sub(r'\*\*([^*]+)\*\*', r'\1', parts[1]).strip()
                    if q and a:
                        levels[current_level].append((q, a))
    return levels

def make_json(pairs):
    pool = [a for _, a in pairs]
    result = []
    for i, (q, a) in enumerate(pairs):
        wrong = [x for j, x in enumerate(pool) if j != i]
        random.shuffle(wrong)
        opts = [a] + wrong[:3]
        random.shuffle(opts)
        result.append({"question": q, "options": opts, "answer": a})
    return result

total = 0
skipped = []

for cat, files in CATEGORIES.items():
    all_levels = {}
    for fn in files:
        if os.path.exists(fn):
            all_levels.update(parse_md(fn))
        else:
            print(f"  ⚠️  Missing: {fn}")

    for lvl in range(3, 21):
        if lvl in all_levels and len(all_levels[lvl]) >= 4:
            data = make_json(all_levels[lvl])
            out = f"{PATH}{cat}_l{lvl}.json"
            with open(out, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✅ {out} ({len(data)} questions)")
            total += 1
        else:
            skipped.append(f"{cat}_l{lvl}")

print(f"\n🎉 Done! Created {total} files.")
if skipped:
    print(f"⚠️  Skipped {len(skipped)}: {skipped[:5]}{'...' if len(skipped)>5 else ''}")

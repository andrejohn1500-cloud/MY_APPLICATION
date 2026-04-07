import re

path = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Get exact tags from question lists
tags = set(re.findall(r'"([^"]*(?:History|Tech|Sports|Geography|Culture|Vincy)[^"]*?)"\s*\)', content))
print("Exact question tags found:")
for t in sorted(tags):
    print(repr(t))

# Now rebuild routing block using EXACT tag strings
tag_map = {}
for t in tags:
    if 'History' in t:      tag_map[t] = 'caribbeanHistory'
    elif 'Tech' in t:       tag_map[t] = 'scienceTech'
    elif 'Sports' in t:     tag_map[t] = 'sports'
    elif 'Geography' in t:  tag_map[t] = 'worldGeo'
    elif 'Culture' in t:    tag_map[t] = 'artsCulture'
    elif 'Vincy' in t:      tag_map[t] = 'svgVincy'

new_when_lines = '\n'.join(f'        "{k}" -> {v}' for k, v in tag_map.items())
new_block = f'''fun getQuestions(category: String): List<Question> = when (category) {{
{new_when_lines}
        else -> caribbeanHistory
    }}'''

pattern = r'fun getQuestions\(category: String\): List<Question> = when \(category\) \{.*?\}'
new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("\nRouting block written:")
f2 = open(path, encoding='utf-8').read()
start = f2.find('fun getQuestions')
for line in f2[start:start+500].splitlines():
    if '->' in line:
        print(repr(line))

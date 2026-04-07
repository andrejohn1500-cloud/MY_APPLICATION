path = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old_block = '''fun getQuestions(category: String): List<Question> = when (category) {'''

# Find and replace the entire when block
import re
pattern = r'fun getQuestions\(category: String\): List<Question> = when \(category\) \{.*?\}'
replacement = '''fun getQuestions(category: String): List<Question> = when (category) {
        "\U0001f33a Caribbean History" -> caribbeanHistory
        "\u270f\ufe0f Science & Tech"  -> scienceTech
        "\U0001f3c5 Sports"            -> sports
        "\U0001f30d World Geography"   -> worldGeo
        "\U0001f3a8 Arts & Culture"    -> artsCulture
        "\U0001f1fb\U0001f1e8 SVG & Vincy Life" -> svgVincy
        else -> caribbeanHistory
    }'''

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done!")

# Verify
f2 = open(path, encoding="utf-8").read()
start = f2.find("fun getQuestions")
block = f2[start:start+500]
for line in block.splitlines():
    if "->" in line:
        print(repr(line))

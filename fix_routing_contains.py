import re

path = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

new_block = '''fun getQuestions(category: String): List<Question> = when {
        category.contains("Caribbean History") -> caribbeanHistory
        category.contains("Science")           -> scienceTech
        category.contains("Sports")            -> sports
        category.contains("Geography")         -> worldGeo
        category.contains("Arts")              -> artsCulture
        category.contains("Vincy")             -> svgVincy
        else                                   -> caribbeanHistory
    }'''

pattern = r'fun getQuestions\(category: String\): List<Question> = when \(category\) \{.*?\}'
new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done! Verifying...")
f2 = open(path, encoding="utf-8").read()
start = f2.find("fun getQuestions")
print(f2[start:start+400])

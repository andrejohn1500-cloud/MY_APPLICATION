path = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix routing key and question tags - add space after globe emoji
content = content.replace('"🌍World Geography"', '"🌍 World Geography"')

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed! Verifying...")
import re
fixed = open(path, encoding="utf-8").read()
hits = re.findall(r'"[^"]*World Geography[^"]*"', fixed)
for h in set(hits):
    print(repr(h))

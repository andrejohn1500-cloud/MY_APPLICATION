path = "./app/src/main/java/com/example/myapplication/CategoryActivity.kt"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('"🌺  Caribbean History"', '"🌺 Caribbean History"'),
    ('"✏️  Science & Tech"',    '"✏️ Science & Tech"'),
    ('"🏅  Sports"',            '"🏅 Sports"'),
    ('"🌍  World Geography"',   '"🌍World Geography"'),
    ('"🎨  Arts & Culture"',    '"🎨 Arts & Culture"'),
    ('"🇻🇨  SVG & Vincy Life"', '"🇻🇨 SVG & Vincy Life"'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done! Verify:")
import subprocess
result = subprocess.run(['grep', 'Caribbean\|Science\|Sports\|Geography\|Arts\|Vincy', path],
    capture_output=True, text=True)
print(result.stdout)

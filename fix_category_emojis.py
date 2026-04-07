import re

path = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the routing block to match actual question tag emojis
replacements = [
    ('"⚽ Sports"', '"🏅 Sports"'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Verify:")
import subprocess
result = subprocess.run(
    ['grep', '-n', 'Sports\|Caribbean\|Science\|Geography\|Arts\|SVG', path],
    capture_output=True, text=True
)
# Just show the getQuestions block lines
for line in result.stdout.splitlines():
    if '->' in line or 'when' in line:
        print(line)

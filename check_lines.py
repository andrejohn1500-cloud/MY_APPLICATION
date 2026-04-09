filepath = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"
with open(filepath, "r") as f:
    lines = f.readlines()
for i, line in enumerate(lines[260:285], 261):
    print(f"{i}: {line}", end="")

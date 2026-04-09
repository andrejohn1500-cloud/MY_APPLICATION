filepath = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"
with open(filepath, "r") as f:
    lines = f.readlines()
# Print first 20 lines to see data class + first few questions
for i, line in enumerate(lines[:20], 1):
    print(f"{i}: {line}", end="")

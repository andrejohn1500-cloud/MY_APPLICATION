filepath = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"

with open(filepath, "r") as f:
    lines = f.readlines()

# Lines 270 and 271 (index 269 and 270) are stray ) characters
# We need to remove them - they sit between the category mapping block and val cxcEnglishA
new_lines = []
skip_indices = set()

for i, line in enumerate(lines):
    # Line numbers are 1-based in output, so index = line_num - 1
    # Lines 269 and 270 (0-indexed) = line numbers 270 and 271
    if i in (269, 270) and line.strip() in (")", ""):
        print(f"Removing line {i+1}: {repr(line)}")
        skip_indices.add(i)
    else:
        new_lines.append(line)

with open(filepath, "w") as f:
    f.writelines(new_lines)

print(f"Done. Removed {len(skip_indices)} lines.")

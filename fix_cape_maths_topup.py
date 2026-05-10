import json, random, os

PATH = "app/src/main/assets/questions/"

extra_tier3 = [
    ("Find the inverse of f(x) = 2x + 3.", "f⁻¹(x) = (x-3)/2", ["f⁻¹(x) = 2x - 3", "f⁻¹(x) = (x+3)/2", "f⁻¹(x) = 1/(2x+3)"]),
    ("A die is rolled twice. Find P(sum = 7).", "6 favourable outcomes out of 36: P = 6/36 = 1/6", ["P = 1/12", "P = 7/36", "P = 1/36"]),
    ("Find the stationary point of y = x² - 4x + 7.", "dy/dx = 2x - 4 = 0; x = 2; y = 4 - 8 + 7 = 3; stationary point (2,3)", ["(4, 7)", "(-2, 3)", "(2, -3)"]),
    ("Given A = [[1,2],[3,4]] and B = [[5,6],[7,8]], find AB.", "AB = [[1×5+2×7, 1×6+2×8],[3×5+4×7, 3×6+4×8]] = [[19,22],[43,50]]", ["[[5,12],[21,32]]", "[[6,8],[10,12]]", "[[19,22],[41,48]]"]),
    ("The mean of 5 numbers is 12. Four of the numbers are 10, 14, 9, 15. Find the fifth.", "Sum = 5×12 = 60; fifth = 60 - (10+14+9+15) = 60 - 48 = 12", ["10", "14", "8"]),
    ("Find ∫(3x² + 2x) dx.", "x³ + x² + C", ["3x³ + 2x² + C", "6x + 2 + C", "x³ + x + C"]),
    ("Solve: |2x - 3| = 7.", "2x - 3 = 7 gives x = 5; 2x - 3 = -7 gives x = -2; solutions x = 5 or x = -2", ["x = 5 only", "x = 2 or x = -5", "x = -2 only"]),
    ("Find the sum to infinity of the series 1 + 1/3 + 1/9 + ...", "a = 1, r = 1/3; S∞ = 1/(1-1/3) = 1/(2/3) = 3/2", ["S∞ = 3", "S∞ = 1", "S∞ = 2"]),
    ("A straight line has gradient -2 and passes through (1, 4). Find its equation.", "y - 4 = -2(x - 1); y = -2x + 6", ["y = -2x + 2", "y = 2x + 2", "y = -2x - 6"]),
    ("If P(A) = 0.5, P(B) = 0.4 and A and B are mutually exclusive, find P(A∪B).", "P(A∪B) = P(A) + P(B) = 0.5 + 0.4 = 0.9", ["P = 0.2", "P = 0.1", "P = 1.0"]),
]

extra_tier4 = [
    ("A factory produces items where 2% are defective. In a batch of 500, find the expected number of defective items and the standard deviation using binomial distribution.", "E(X) = np = 500×0.02 = 10; Var(X) = np(1-p) = 500×0.02×0.98 = 9.8; SD = √9.8 ≈ 3.13", ["E(X) = 10, SD = 10", "E(X) = 5, SD = 2.5", "E(X) = 100, SD = 9.8"]),
    ("Maximise P = 3x + 5y subject to x + 2y ≤ 12, 2x + y ≤ 10, x ≥ 0, y ≥ 0. Find the optimal solution.", "Vertices: (0,0) P=0; (5,0) P=15; (8/3, 14/3) P=8+70/3≈31.3; (0,6) P=30; maximum at (8/3, 14/3) ≈ 31.3", ["Maximum P = 30 at (0,6)", "Maximum P = 25 at (5,0)", "Maximum P = 36 at (3,5)"]),
    ("Given f(x) = x³ - 6x + 4, find the intervals where f is increasing and decreasing.", "f'(x) = 3x² - 6 = 3(x²-2) = 0 at x = ±√2; increasing for x < -√2 and x > √2; decreasing for -√2 < x < √2", ["Increasing everywhere", "Decreasing for all x > 0", "Increasing only for x > 0"]),
    ("The heights of 1000 students are normally distributed with mean 165cm and SD 8cm. Estimate how many students are taller than 181cm.", "z = (181-165)/8 = 2; P(Z>2) ≈ 0.0228; 1000 × 0.0228 ≈ 23 students", ["About 50 students", "About 100 students", "About 5 students"]),
    ("Solve the matrix equation AX = B where A = [[2,1],[5,3]] and B = [[4],[7]].", "det(A) = 6-5 = 1; A⁻¹ = [[3,-1],[-5,2]]; X = A⁻¹B = [[3×4+(-1)×7],[-5×4+2×7]] = [[5],[-6]]", ["X = [[2],[3]]", "X = [[4],[7]]", "X = [[1],[2]]"]),
    ("A sequence is defined by uₙ₊₁ = 3uₙ - 4 with u₁ = 3. Find u₁, u₂, u₃, u₄ and the general term.", "u₁=3, u₂=5, u₃=11, u₄=29; the sequence is not simply geometric; general term uₙ = 2×3ⁿ⁻¹ + 1 verified by substitution", ["uₙ = 3ⁿ", "uₙ = 2n + 1", "uₙ = 3n - 4"]),
    ("Find the area enclosed between y = x² and y = x + 2.", "Intersections: x²=x+2; x²-x-2=0; (x-2)(x+1)=0; x=-1,2; Area=∫₋₁²(x+2-x²)dx=[x²/2+2x-x³/3]₋₁² = (2+4-8/3)-( 1/2-2+1/3) = 10/3+13/6=9/2", ["Area = 3", "Area = 6", "Area = 4.5 square units"]),
    ("Two vectors are a = 2i + 3j and b = λi + 6j. Find λ if a and b are parallel.", "For parallel vectors a×b = 0; 2×6 - 3×λ = 0; 12 = 3λ; λ = 4", ["λ = 3", "λ = 6", "λ = 2"]),
    ("The probability that machine A produces a faulty item is 0.03 and machine B is 0.05. Machine A produces 60% of output. Find P(item is faulty).", "P(faulty) = P(A)×P(F|A) + P(B)×P(F|B) = 0.6×0.03 + 0.4×0.05 = 0.018 + 0.020 = 0.038", ["P = 0.08", "P = 0.04", "P = 0.015"]),
    ("Sketch and describe the transformation of f(x) = x² to g(x) = -(x-3)² + 4.", "Reflection in x-axis, translation 3 right and 4 up; vertex moves from (0,0) to (3,4); parabola opens downward", ["Translation only, no reflection", "Reflection in y-axis and translation", "Stretch by factor 4 and translation"]),
]

# Load existing files and top up tier3 (levels 11-15) and tier4 (levels 16-20)
for lvl in range(11, 16):
    filepath = f"{PATH}cape_applied_mathematics_l{lvl}.json"
    with open(filepath, 'r') as f:
        existing = json.load(f)
    pool = extra_tier3.copy()
    random.shuffle(pool)
    needed = 20 - len(existing)
    for item in pool[:needed]:
        q, a, wrong = item[0], item[1], item[2]
        opts = [a] + wrong[:3]
        random.shuffle(opts)
        ci = opts.index(a)
        existing.append({"question": q, "options": opts, "correctIndex": ci})
    with open(filepath, 'w') as f:
        json.dump(existing, f, indent=2)
    print(f"✅ level {lvl} topped up to {len(existing)} questions")

for lvl in range(16, 21):
    filepath = f"{PATH}cape_applied_mathematics_l{lvl}.json"
    with open(filepath, 'r') as f:
        existing = json.load(f)
    pool = extra_tier3 + extra_tier4
    random.shuffle(pool)
    needed = 20 - len(existing)
    for item in pool[:needed]:
        q, a, wrong = item[0], item[1], item[2]
        opts = [a] + wrong[:3]
        random.shuffle(opts)
        ci = opts.index(a)
        existing.append({"question": q, "options": opts, "correctIndex": ci})
    with open(filepath, 'w') as f:
        json.dump(existing, f, indent=2)
    print(f"✅ level {lvl} topped up to {len(existing)} questions")

print("\nDone!")

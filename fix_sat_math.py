import json, random, os

PATH = "app/src/main/assets/questions/"
os.makedirs(PATH, exist_ok=True)

tier1 = [
    ("What is the value of 3x + 5 when x = 4?", "17", ["12", "15", "20"]),
    ("What is 25% of 200?", "50", ["25", "75", "100"]),
    ("Simplify: 4(x + 3) - 2x", "2x + 12", ["6x + 12", "2x + 7", "4x + 12"]),
    ("What is the slope of the line y = 3x - 7?", "3", ["-7", "7", "-3"]),
    ("Solve for x: 2x - 6 = 10", "x = 8", ["x = 2", "x = 4", "x = 16"]),
    ("What is the area of a rectangle with length 8 and width 5?", "40", ["26", "13", "30"]),
    ("What is the median of the set {3, 7, 9, 2, 5}?", "5", ["7", "3", "9"]),
    ("If a car travels 60 miles in 2 hours, what is its speed in miles per hour?", "30", ["120", "20", "15"]),
    ("What is the value of 2³?", "8", ["6", "9", "16"]),
    ("Solve: 5x = 35", "x = 7", ["x = 5", "x = 30", "x = 175"]),
    ("What is the perimeter of a square with side length 6?", "24", ["12", "36", "18"]),
    ("What is 15% of 80?", "12", ["8", "15", "18"]),
    ("Which of the following is equivalent to x² - 9?", "(x+3)(x-3)", ["(x-3)²", "(x+9)(x-1)", "(x+3)²"]),
    ("What is the y-intercept of the line y = 2x + 5?", "5", ["2", "-5", "0"]),
    ("A triangle has angles of 90° and 45°. What is the third angle?", "45°", ["90°", "30°", "60°"]),
    ("What is the average of 10, 20, and 30?", "20", ["15", "25", "60"]),
    ("If f(x) = 2x + 1, what is f(3)?", "7", ["5", "6", "8"]),
    ("What is the probability of rolling a 4 on a standard die?", "1/6", ["1/4", "1/3", "4/6"]),
    ("What is the volume of a cube with side length 3?", "27", ["9", "18", "12"]),
    ("Solve: x/4 = 7", "x = 28", ["x = 11", "x = 3", "x = 1.75"]),
]

tier2 = [
    ("If 3x + 2y = 12 and x = 2, what is y?", "3", ["6", "4", "2"]),
    ("What is the solution set of |x - 3| = 5?", "x = 8 or x = -2", ["x = 8 or x = 2", "x = -8 or x = 2", "x = 8 only"]),
    ("A line passes through (0, 4) and (2, 8). What is its equation?", "y = 2x + 4", ["y = 4x + 2", "y = 2x - 4", "y = x + 4"]),
    ("What are the roots of x² - 5x + 6 = 0?", "x = 2 and x = 3", ["x = -2 and x = -3", "x = 1 and x = 6", "x = 5 and x = 1"]),
    ("If a rectangle has area 48 and width 6, what is its perimeter?", "28", ["22", "48", "24"]),
    ("What is the value of (2x - 3)² when x = 4?", "25", ["13", "22", "49"]),
    ("A store marks up an item by 20% then discounts it 20%. What is the net effect?", "4% decrease", ["No change", "4% increase", "2% decrease"]),
    ("Solve the system: x + y = 10 and x - y = 4", "x = 7, y = 3", ["x = 3, y = 7", "x = 6, y = 4", "x = 5, y = 5"]),
    ("What is the equation of a line parallel to y = 3x + 1 passing through (0, -2)?", "y = 3x - 2", ["y = -3x - 2", "y = (1/3)x - 2", "y = 3x + 2"]),
    ("If the ratio of boys to girls is 3:5 and there are 40 students total, how many boys are there?", "15", ["20", "25", "12"]),
    ("What is the value of (x + y)² - (x - y)² simplified?", "4xy", ["2x² + 2y²", "x² - y²", "2xy"]),
    ("A circle has a radius of 5. What is its area?", "25π", ["10π", "5π", "50π"]),
    ("What is the 10th term of the arithmetic sequence 3, 7, 11, 15...?", "39", ["43", "37", "35"]),
    ("If p(x) = x² - 4x + 3, what is p(1)?", "0", ["1", "-1", "2"]),
    ("Two angles are supplementary. One is 70°. What is the other?", "110°", ["20°", "290°", "70°"]),
    ("What is the slope of a line perpendicular to y = (1/2)x + 3?", "-2", ["2", "1/2", "-1/2"]),
    ("Simplify: (x³)(x⁴)", "x⁷", ["x¹²", "x", "2x⁷"]),
    ("A bag has 4 red and 6 blue balls. What is the probability of picking a red ball?", "2/5", ["1/4", "4/10 simplified to 2/4", "3/5"]),
    ("If 40% of a number is 28, what is the number?", "70", ["56", "40", "112"]),
    ("What is the distance between points (1, 2) and (4, 6)?", "5", ["3", "4", "7"]),
]

tier3 = [
    ("If f(x) = x² - 3x and g(x) = 2x + 1, what is f(g(1))?", "3", ["0", "6", "9"]),
    ("What is the sum of an infinite geometric series with first term 8 and ratio 1/2?", "16", ["8", "4", "12"]),
    ("Solve: log₂(x) + log₂(x-2) = 3", "x = 4", ["x = 3", "x = 2", "x = 8"]),
    ("A quadratic has vertex (3, -4) and passes through (5, 0). What is its equation?", "y = (x-3)² - 4", ["y = (x+3)² - 4", "y = (x-3)² + 4", "y = -(x-3)² - 4"]),
    ("In a right triangle, the hypotenuse is 13 and one leg is 5. What is the other leg?", "12", ["8", "10", "11"]),
    ("What is the remainder when x³ - 2x² + x - 5 is divided by (x - 2)?", "-3", ["0", "3", "-5"]),
    ("If sin θ = 3/5 and θ is in the first quadrant, what is cos θ?", "4/5", ["3/4", "5/3", "1/5"]),
    ("How many ways can 5 books be arranged on a shelf?", "120", ["25", "60", "100"]),
    ("What is the value of x if 2^(x+1) = 32?", "x = 4", ["x = 5", "x = 3", "x = 16"]),
    ("A parabola has x-intercepts at x = -1 and x = 5 and passes through (0, -5). What is its equation?", "y = (x+1)(x-5)", ["y = -(x+1)(x-5)", "y = (x-1)(x+5)", "y = (x+1)(x+5)"]),
    ("What is the standard deviation concept measuring?", "How spread out data values are from the mean", ["The middle value in a data set", "The most frequently occurring value", "The difference between the highest and lowest values"]),
    ("Solve: 3^(2x) = 81", "x = 2", ["x = 4", "x = 3", "x = 1"]),
    ("What is the area of an equilateral triangle with side length 6?", "9√3", ["18", "6√3", "12√3"]),
    ("If the mean of 5 numbers is 12 and four of them are 10, 11, 13, 15, what is the fifth?", "11", ["12", "13", "10"]),
    ("What is the domain of f(x) = √(x - 4)?", "x ≥ 4", ["x > 4", "x ≤ 4", "all real numbers"]),
    ("In a data set, the interquartile range (IQR) measures what?", "The spread of the middle 50% of data", ["The range of all data values", "The average of the data", "The difference between mean and median"]),
    ("What is the product of the roots of 2x² - 6x + 4 = 0?", "2", ["3", "-2", "6"]),
    ("A circle equation is (x-2)² + (y+3)² = 25. What is the centre?", "(2, -3)", ["(-2, 3)", "(2, 3)", "(-2, -3)"]),
    ("If P(A) = 0.4 and P(B) = 0.3 and A and B are independent, what is P(A and B)?", "0.12", ["0.7", "0.1", "0.3"]),
    ("What transformation maps f(x) to f(x-3) + 2?", "Shift right 3 and up 2", ["Shift left 3 and up 2", "Shift right 3 and down 2", "Shift left 3 and down 2"]),
]

tier4 = [
    ("A system of equations has no solution. Which best describes the lines?", "They are parallel — same slope, different y-intercepts", ["They are the same line", "They are perpendicular", "They intersect at exactly one point"]),
    ("If f(x) = (x² - 4)/(x - 2), what is the value the function approaches as x approaches 2?", "4", ["0", "2", "undefined with no limit"]),
    ("The graph of y = a·sin(bx + c) + d has amplitude 3, period π, and midline y = 1. What are a and d?", "a = 3, d = 1", ["a = 3, d = 0", "a = 6, d = 1", "a = 1, d = 3"]),
    ("A scatterplot shows a strong positive linear correlation. Which value of r is most consistent with this?", "r = 0.92", ["r = -0.92", "r = 0.2", "r = 0"]),
    ("What is the remainder theorem used for?", "Finding the remainder when a polynomial is divided by (x - a) by evaluating f(a)", ["Factoring quadratic expressions", "Finding zeros of a polynomial graphically", "Simplifying rational expressions"]),
    ("If the discriminant b² - 4ac is negative, what does this mean for the quadratic?", "The quadratic has no real roots — two complex roots", ["Two equal real roots", "Two distinct real roots", "One positive and one negative root"]),
    ("A rational function has a vertical asymptote at x = 3. What does this mean?", "The denominator equals zero at x = 3 and the numerator does not", ["The function equals zero at x = 3", "The function has a maximum at x = 3", "The graph crosses the x-axis at x = 3"]),
    ("In a normally distributed data set, approximately what percentage of data falls within 2 standard deviations of the mean?", "95%", ["68%", "99.7%", "75%"]),
    ("What is the inverse function of f(x) = 3x - 6?", "f⁻¹(x) = (x + 6)/3", ["f⁻¹(x) = (x - 6)/3", "f⁻¹(x) = 3x + 6", "f⁻¹(x) = (3x + 6)"]),
    ("A survey samples 200 students. 60% prefer online learning. What is the margin of error at 95% confidence?", "Approximately ±7%", ["Exactly 0%", "±60%", "±1%"]),
    ("Which best explains why correlation does not imply causation?", "A third variable (confounding variable) may cause both observed variables to change together", ["Correlation coefficients are always inaccurate", "Causation requires a negative correlation", "Correlation only applies to linear relationships"]),
    ("If f(x) = x³ and g(x) = x^(1/3), what is f(g(27))?", "27", ["3", "9", "81"]),
    ("A line of best fit has equation y = 1.5x + 4. What does the slope represent in context?", "For each unit increase in x, y increases by 1.5 units on average", ["The starting value of y when x is unknown", "The maximum value of y", "The correlation between x and y"]),
    ("What is the maximum value of -2x² + 8x - 3?", "5", ["3", "8", "2"]),
    ("Two dice are rolled. What is the probability that the sum equals 7?", "1/6", ["1/12", "7/36", "1/4"]),
    ("A polynomial of degree n has at most how many real zeros?", "n", ["n-1", "2n", "n+1"]),
    ("What is the value of i² where i is the imaginary unit?", "-1", ["1", "i", "0"]),
    ("If log(x) + log(y) = log(12) and x = 3, what is y?", "4", ["9", "36", "3"]),
    ("A function f is even if what condition holds?", "f(-x) = f(x) for all x in the domain", ["f(-x) = -f(x)", "f(x) = f(x+1)", "f(x) is always positive"]),
    ("What is the solution to the inequality (x-1)(x+3) > 0?", "x < -3 or x > 1", ["x > -3 and x < 1", "-3 < x < 1", "x > 1 only"]),
]

all_tiers = [tier1, tier2, tier3, tier4]
level_tier_map = {
    1:0,2:0,3:0,4:0,5:0,
    6:1,7:1,8:1,9:1,10:1,
    11:2,12:2,13:2,14:2,15:2,
    16:3,17:3,18:3,19:3,20:3
}

for lvl in range(1, 21):
    tier_idx = level_tier_map[lvl]
    pool = all_tiers[tier_idx].copy()
    random.shuffle(pool)
    selected = pool[:20] if len(pool) >= 20 else pool
    data = []
    for item in selected:
        q, a, wrong = item[0], item[1], item[2]
        opts = [a] + wrong[:3]
        random.shuffle(opts)
        ci = opts.index(a)
        data.append({"question": q, "options": opts, "correctIndex": ci})
    out = f"{PATH}sat_math_l{lvl}.json"
    with open(out, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ sat_math_l{lvl}.json ({len(data)} q) - Tier {tier_idx+1}")

print("\nDone!")

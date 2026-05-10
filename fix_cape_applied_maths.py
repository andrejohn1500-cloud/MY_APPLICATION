import json, random, os

PATH = "app/src/main/assets/questions/"

tier1 = [
    ("What is a set?", "A well-defined collection of distinct objects", ["A list of numbers in order", "A type of equation", "A graph of a function"]),
    ("What is a subset?", "A set whose elements are all contained in another set", ["A set with more elements than another", "A set with no elements", "A set equal to another set"]),
    ("What is the union of two sets?", "All elements that are in either set A or set B or both", ["Only elements in both sets", "Elements in A but not B", "Elements in B but not A"]),
    ("What is the intersection of two sets?", "Elements that are in both set A and set B", ["All elements in either set", "Elements in A only", "Elements in neither set"]),
    ("What is the complement of a set?", "All elements in the universal set that are not in the set", ["All elements in the set", "The empty set", "The universal set itself"]),
    ("What is a function?", "A relation where each input has exactly one output", ["A relation with multiple outputs for one input", "A type of set", "A graph that crosses the x-axis"]),
    ("What is the domain of a function?", "The set of all possible input values", ["The set of all possible output values", "The maximum value of the function", "The x-intercept of the function"]),
    ("What is the range of a function?", "The set of all possible output values", ["The set of all input values", "The minimum value of the function", "The y-intercept of the function"]),
    ("What is a linear function?", "A function whose graph is a straight line with equation y = mx + c", ["A function whose graph is a curve", "A function with no x-intercept", "A function that only has positive values"]),
    ("What is the gradient of a line?", "The measure of steepness calculated as rise over run", ["The y-intercept of the line", "The x-intercept of the line", "The length of the line"]),
    ("What is a quadratic function?", "A function of the form f(x) = ax² + bx + c where a ≠ 0", ["A function of the form f(x) = mx + c", "A function involving cube roots", "A function with no turning point"]),
    ("What is probability?", "A measure of how likely an event is to occur expressed as a value between 0 and 1", ["The number of times an event occurs", "The ratio of successful outcomes to total trials only", "A measure of data spread"]),
    ("What is a sample space?", "The set of all possible outcomes of an experiment", ["The set of favourable outcomes only", "The probability of an event", "The number of trials in an experiment"]),
    ("What is the mean of a data set?", "The sum of all values divided by the number of values", ["The middle value when data is ordered", "The most frequently occurring value", "The difference between the highest and lowest values"]),
    ("What is the median?", "The middle value when data is arranged in order", ["The average of all values", "The most common value", "The highest minus the lowest value"]),
    ("What is the mode?", "The value that occurs most frequently in a data set", ["The middle value", "The average value", "The range of the data"]),
    ("What is the range of a data set?", "The difference between the highest and lowest values", ["The average of the data", "The middle value", "The most common value"]),
    ("What is a vector?", "A quantity that has both magnitude and direction", ["A quantity with only magnitude", "A type of matrix", "A scalar quantity"]),
    ("What is a scalar?", "A quantity that has only magnitude and no direction", ["A quantity with both magnitude and direction", "A type of vector", "A negative number"]),
    ("What is a matrix?", "A rectangular array of numbers arranged in rows and columns", ["A single number", "A type of graph", "A set of vectors only"]),
    ("What is a factor of a number?", "A number that divides exactly into another number", ["A number added to another", "A number greater than the original", "A decimal part of a number"]),
    ("What is a prime number?", "A number greater than 1 that has only two factors: 1 and itself", ["A number divisible by 2", "A number with more than two factors", "Any odd number"]),
    ("What is an arithmetic sequence?", "A sequence where each term differs from the previous by a constant amount called the common difference", ["A sequence where each term is multiplied by a constant", "A sequence with no pattern", "A sequence of prime numbers"]),
    ("What is a geometric sequence?", "A sequence where each term is multiplied by a constant ratio", ["A sequence with a constant difference between terms", "A sequence of square numbers", "A random sequence of numbers"]),
    ("What is the y-intercept of a graph?", "The point where the graph crosses the y-axis where x = 0", ["The point where the graph crosses the x-axis", "The gradient of the line", "The maximum point of the graph"]),
]

tier2 = [
    ("How do you find the equation of a line given two points?", "Calculate the gradient using m = (y2-y1)/(x2-x1) then substitute into y = mx + c to find c", ["Use the quadratic formula", "Multiply the two coordinates together", "Add the x and y values of both points"]),
    ("What is the quadratic formula?", "x = (-b ± √(b²-4ac)) / 2a for ax² + bx + c = 0", ["x = -b/2a only", "x = b² - 4ac", "x = (a+b)/c"]),
    ("What does the discriminant tell us about a quadratic equation?", "If b²-4ac > 0: two real roots; = 0: one repeated root; < 0: no real roots", ["It gives the value of the roots directly", "It only tells us if the parabola opens up or down", "It measures the gradient of the quadratic"]),
    ("What is conditional probability?", "The probability of event A given that event B has already occurred: P(A|B) = P(A∩B)/P(B)", ["The probability of two independent events", "The probability of either A or B occurring", "The complement of P(A)"]),
    ("What is the addition rule of probability?", "P(A∪B) = P(A) + P(B) - P(A∩B)", ["P(A∪B) = P(A) × P(B)", "P(A∪B) = P(A) + P(B) always", "P(A∪B) = P(A) - P(B)"]),
    ("What is the multiplication rule for independent events?", "P(A∩B) = P(A) × P(B)", ["P(A∩B) = P(A) + P(B)", "P(A∩B) = P(A) - P(B)", "P(A∩B) = P(A) / P(B)"]),
    ("What is a cumulative frequency curve used for?", "To estimate medians, quartiles and percentiles from grouped data", ["To show the mode of a data set", "To compare two data sets directly", "To calculate the mean of grouped data"]),
    ("What is the interquartile range?", "The difference between the upper quartile Q3 and lower quartile Q1", ["The difference between the maximum and minimum values", "The average of the quartiles", "Half of the range"]),
    ("What is standard deviation?", "A measure of how spread out data values are from the mean", ["The average of the data set", "The middle value of the data", "The difference between max and min values"]),
    ("What is a Venn diagram used for?", "To visually represent sets and their relationships including unions intersections and complements", ["To show the frequency of data values", "To plot a linear function", "To represent a probability tree"]),
    ("What is a probability tree diagram?", "A diagram showing all possible outcomes of sequential events and their probabilities", ["A diagram showing set relationships", "A graph of a cumulative frequency", "A bar chart of probability values"]),
    ("What is matrix addition?", "Adding corresponding elements of two matrices of the same dimensions", ["Multiplying rows by columns", "Finding the determinant", "Transposing the matrix"]),
    ("What is the determinant of a 2x2 matrix?", "For matrix [[a,b],[c,d]], the determinant is ad - bc", ["ac + bd", "ab - cd", "a + d"]),
    ("What is the inverse of a 2x2 matrix?", "(1/det) × [[d,-b],[-c,a]] where det = ad-bc", ["The transpose of the matrix", "The matrix with all signs changed", "The matrix divided by its determinant only"]),
    ("What is a position vector?", "A vector that describes the position of a point relative to the origin", ["A vector with no direction", "A unit vector", "A vector showing only magnitude"]),
    ("How do you add two vectors?", "Add corresponding components: if a=(x1,y1) and b=(x2,y2) then a+b=(x1+x2, y1+y2)", ["Multiply the magnitudes", "Add the angles only", "Subtract corresponding components"]),
    ("What is the magnitude of a vector?", "The length of the vector calculated as √(x² + y²) for vector (x,y)", ["The direction of the vector", "The sum of the components", "The product of the components"]),
    ("What is a unit vector?", "A vector with magnitude 1 used to show direction", ["A vector with magnitude 0", "A vector in the positive x direction only", "Any vector divided by 2"]),
    ("What is a linear programming problem?", "An optimisation problem finding the maximum or minimum of a linear objective function subject to linear constraints", ["A problem involving quadratic functions", "A problem with no constraints", "A problem finding the gradient of a line"]),
    ("What defines the feasible region in linear programming?", "The region satisfying all the constraints in the problem", ["The region where the objective function is maximised", "The region outside all constraints", "The x and y axes only"]),
    ("What is differentiation used for?", "To find the rate of change of a function and the gradient at any point", ["To find the area under a curve", "To solve quadratic equations", "To find the inverse of a function"]),
    ("What is integration used for?", "To find the area under a curve and to reverse differentiation", ["To find the gradient at a point", "To find the maximum of a function only", "To solve linear equations"]),
    ("What is the nth term of an arithmetic sequence?", "a + (n-1)d where a is the first term and d is the common difference", ["a × r^(n-1)", "n × a + d", "a + nd"]),
    ("What is the nth term of a geometric sequence?", "a × r^(n-1) where a is the first term and r is the common ratio", ["a + (n-1)d", "a × n + r", "r^n only"]),
    ("What is a scatter diagram used for?", "To show the relationship or correlation between two variables", ["To show the frequency of one variable", "To display data in sectors", "To show cumulative totals"]),
]

tier3 = [
    ("A bag contains 5 red and 3 blue balls. Two balls are drawn without replacement. Find P(both red).", "P = (5/8) × (4/7) = 20/56 = 5/14", ["P = (5/8) × (5/8) = 25/64", "P = 5/8 + 4/7", "P = 10/8"]),
    ("Find the equation of the line passing through (2,3) and (4,7).", "Gradient = (7-3)/(4-2) = 2; y - 3 = 2(x - 2); y = 2x - 1", ["y = 2x + 3", "y = x + 1", "y = 3x - 1"]),
    ("Solve the quadratic equation x² - 5x + 6 = 0.", "x = 2 or x = 3 by factoring (x-2)(x-3) = 0", ["x = -2 or x = -3", "x = 5 or x = 6", "x = 1 or x = 6"]),
    ("The sum of the first n terms of an arithmetic series is Sn = n/2(2a + (n-1)d). Find S10 when a=3 and d=2.", "S10 = 10/2(6 + 18) = 5 × 24 = 120", ["S10 = 100", "S10 = 60", "S10 = 150"]),
    ("A linear programming problem has constraints x + y ≤ 10, x ≥ 2, y ≥ 3. Find the vertices of the feasible region.", "Vertices are (2,3), (7,3) and (2,8) found by solving constraint boundary intersections", ["Vertices are (0,0), (10,0) and (0,10)", "Vertices are (2,2) and (10,10)", "The feasible region has no vertices"]),
    ("Given f(x) = 3x² - 4x + 1, find f'(x).", "f'(x) = 6x - 4", ["f'(x) = 3x - 4", "f'(x) = 6x² - 4", "f'(x) = 9x - 4"]),
    ("Find the area under y = x² between x = 0 and x = 3.", "∫₀³ x² dx = [x³/3]₀³ = 9 - 0 = 9 square units", ["6 square units", "27 square units", "3 square units"]),
    ("Given matrix A = [[2,1],[3,4]], find the determinant and inverse.", "det = 2×4 - 1×3 = 5; inverse = (1/5)[[4,-1],[-3,2]]", ["det = 8; inverse = [[4,1],[3,2]]", "det = 5; inverse = [[4,1],[-3,2]]", "det = 11; no inverse exists"]),
    ("Two events A and B have P(A) = 0.4, P(B) = 0.3, P(A∩B) = 0.1. Find P(A∪B).", "P(A∪B) = 0.4 + 0.3 - 0.1 = 0.6", ["P(A∪B) = 0.4 + 0.3 = 0.7", "P(A∪B) = 0.4 × 0.3 = 0.12", "P(A∪B) = 0.1"]),
    ("In a group of 30 students: 18 study Maths, 15 study Science, 7 study both. How many study neither?", "n(M∪S) = 18 + 15 - 7 = 26; neither = 30 - 26 = 4", ["6 students", "8 students", "2 students"]),
    ("Find the turning point of f(x) = x² - 6x + 11.", "f'(x) = 2x - 6 = 0 gives x = 3; f(3) = 9 - 18 + 11 = 2; turning point is (3, 2) — a minimum", ["Turning point is (6, 11)", "Turning point is (3, 3)", "Turning point is (-3, 2)"]),
    ("A geometric series has first term 4 and common ratio 0.5. Find the sum to infinity.", "S∞ = a/(1-r) = 4/(1-0.5) = 4/0.5 = 8", ["S∞ = 4", "S∞ = 2", "S∞ = 16"]),
    ("Find the correlation coefficient interpretation: r = -0.92.", "Strong negative correlation — as one variable increases the other decreases", ["Weak positive correlation", "No correlation between variables", "Perfect negative correlation where all points lie exactly on a line"]),
    ("Vectors a = (3,4) and b = (1,2). Find |a - b|.", "a - b = (2,2); |a-b| = √(4+4) = √8 = 2√2", ["√5", "5", "√20"]),
    ("The probability that a student passes Maths is 0.7 and passes English is 0.6. If independent, find P(passes both).", "P(M∩E) = 0.7 × 0.6 = 0.42", ["P = 0.7 + 0.6 = 1.3", "P = 0.7 - 0.6 = 0.1", "P = 0.7/0.6"]),
]

tier4 = [
    ("A company manufactures x units of product A and y units of product B. Profit = 5x + 8y. Constraints: 2x + 3y ≤ 120, x + y ≤ 50, x ≥ 0, y ≥ 0. Find the maximum profit.", "Test vertices of feasible region: (0,40): P=320; (30,20): P=310; (50,0): P=250; maximum profit = $320 at x=0, y=40", ["Maximum profit = $400", "Maximum profit = $250 at x=50", "Maximum profit = $310"]),
    ("Prove that the sum of the first n terms of a geometric series is Sn = a(1-rⁿ)/(1-r).", "Let Sn = a + ar + ar² +...+ arⁿ⁻¹; multiply by r: rSn = ar + ar² +...+ arⁿ; subtract: Sn(1-r) = a(1-rⁿ); divide: Sn = a(1-rⁿ)/(1-r)", ["The formula cannot be proven algebraically", "Sn = a(rⁿ-1)/(r-1) is a different formula with no connection", "The proof requires calculus"]),
    ("A random variable X has the following distribution: P(X=1)=0.2, P(X=2)=0.5, P(X=3)=0.3. Find E(X) and Var(X).", "E(X) = 1(0.2)+2(0.5)+3(0.3) = 0.2+1.0+0.9 = 2.1; E(X²) = 1(0.2)+4(0.5)+9(0.3) = 4.9; Var(X) = 4.9 - 2.1² = 4.9 - 4.41 = 0.49", ["E(X) = 2, Var(X) = 1", "E(X) = 2.1, Var(X) = 2.1", "E(X) = 3, Var(X) = 0.5"]),
    ("Given f(x) = x³ - 3x² - 9x + 5, find all stationary points and determine their nature.", "f'(x) = 3x²-6x-9 = 3(x-3)(x+1) = 0; x=3 or x=-1; f''(x)=6x-6; at x=3: f''=12>0 minimum; at x=-1: f''=-12<0 maximum", ["Only one stationary point at x=3", "Stationary points at x=1 and x=-3", "f'(x) cannot be factored"]),
    ("A data set has mean 50 and standard deviation 10. Using normal distribution, find P(40 < X < 60).", "Standardise: z = (40-50)/10 = -1 and z = (60-50)/10 = 1; P(-1 < Z < 1) ≈ 0.6827 or 68.27%", ["P = 95%", "P = 50%", "P = 99.7%"]),
    ("Solve the system using matrices: 2x + y = 7, x + 3y = 11.", "Matrix form: [[2,1],[1,3]][[x],[y]] = [[7],[11]]; det=5; inverse=(1/5)[[3,-1],[-1,2]]; solution: x=2, y=3", ["x=3, y=2", "x=4, y=1", "x=1, y=5"]),
    ("A ball is thrown upward with position s(t) = 20t - 5t². Find the maximum height and the time it takes to reach it.", "s'(t) = 20 - 10t = 0 gives t = 2 seconds; s(2) = 40 - 20 = 20 metres", ["Maximum height = 25m at t=3s", "Maximum height = 20m at t=3s", "Maximum height = 40m at t=2s"]),
    ("In a class of 40 students, 25 play cricket, 20 play football, and 8 play both. A student is chosen at random. Find P(plays cricket but not football).", "Cricket only = 25 - 8 = 17; P = 17/40", ["P = 25/40", "P = 17/32", "P = 8/40"]),
    ("The first three terms of a sequence are 2, 6, 18. Find the sum of the first 8 terms.", "Geometric with a=2, r=3; S8 = 2(3⁸-1)/(3-1) = 2(6561-1)/2 = 6560", ["S8 = 4374", "S8 = 3280", "S8 = 13122"]),
    ("Given vectors p = 3i + 4j and q = i - 2j, find the angle between them.", "cos θ = (p·q)/(|p||q|) = (3-8)/(5×√5) = -5/(5√5) = -1/√5; θ = arccos(-1/√5) ≈ 116.6°", ["θ = 45°", "θ = 63.4°", "θ = 90°"]),
]

all_tiers = [tier1, tier2, tier3, tier4]
level_tier_map = {1:0,2:0,3:0,4:0,5:0,6:1,7:1,8:1,9:1,10:1,11:2,12:2,13:2,14:2,15:2,16:3,17:3,18:3,19:3,20:3}

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
    out = f"{PATH}cape_applied_mathematics_l{lvl}.json"
    with open(out, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ cape_applied_mathematics_l{lvl}.json ({len(data)} questions) - Tier {tier_idx+1}")

print("\nDone!")

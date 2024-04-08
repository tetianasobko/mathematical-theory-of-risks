import math
def calculate_probability(x1, x2):
    return 1 / (x2 - x1)

def U(a, c, x):
    return a * x ** c

def mathematical_expectation(x1, x2, p):
    return (x1 + x2) * p

def expected_usefulness(a, c, x1, x2, p):
    return p * U(a, c, x1) + p * U(a, c, x2)

def certainty_equivalent(expected_usefulness, p):
    return math.sqrt(expected_usefulness / p)

def risk_premium(math_expectation, certainty_equivalent):
    return math_expectation - certainty_equivalent

data = [
    [1, 10, 2.0, 0, 10],
    [2, 20, 3.0, 10, 20],
    [3, 50, 0.1, 20, 30],
    [4, 30, 1.0, 5, 10],
    [5, 45, 0.5, 5, 20],
    [6, 55, 4.0, 5, 30],
    [7, 25, 0.25, 0, 10],
    [8, 65, 5.0, 10, 20],
    [9, 75, 0.4, 20, 30],
    [10, 35, 0.2, 0, 10],
    [11, 95, 1.2, 10, 20],
    [12, 10, 2.5, 20, 30],
    [13, 15, 0.6, 5, 10],
    [14, 85, 3.5, 5, 20]
]

for row in data:
    variant, a, c, x1, x2 = row
    p = calculate_probability(x1, x2)
    math_expectation = mathematical_expectation(x1, x2, p)
    exp_usefulness = expected_usefulness(a, c, x1, x2, p)
    c_equivalent = certainty_equivalent(exp_usefulness, p)
    premium = risk_premium(math_expectation, c_equivalent)

    print("Result for variant ", variant)
    print("Math expectation: ", math_expectation)
    print("Expected usefulness: ", exp_usefulness)
    print("Certainty equivalent: ", c_equivalent)
    print("Risk premium : ", premium)

    if U(a, c, math_expectation) < exp_usefulness:
        print("The person is risky")
    else:
        print("The person is not risky")

    print()
import cmath

def lab_2():
    profit_1 = [40, 30]
    profit_2 = [35, 25]

    probability_1 = [0.4, 0.6]
    probability_2 = [0.8, 0.2]

    math_expectation_1 = profit_1[0] * probability_1[0] + profit_1[1] * probability_1[1]
    math_expectation_2 = profit_2[0] * probability_2[0] + profit_2[1] * probability_2[1]

    print(f"Expected value for outlet №1: {math_expectation_1}")
    print(f"Expected value for outlet №2: {math_expectation_2}")

    variation_1 = probability_1[0] * ((profit_1[0] - math_expectation_1) ** 2) + probability_1[1] * ((profit_1[1] - math_expectation_1) ** 2)
    variation_2 = probability_2[0] * ((profit_2[0] - math_expectation_2) ** 2) + probability_2[1] * ((profit_2[1] - math_expectation_2) ** 2)

    print(f"\nVariation for outlet №1: {variation_1}")
    print(f"Variation for outlet №2: {variation_2}")

    deviation_1 = cmath.sqrt(variation_1)
    deviation_2 = cmath.sqrt(variation_2)

    print(f"\nStandard deviation for outlet №1: {deviation_1.real}")
    print(f"Standard deviation for outlet №2: {deviation_2.real}")

    coefficient_1 = deviation_1.real / abs(math_expectation_1)
    coefficient_2 = deviation_2.real / abs(math_expectation_2)

    print(f"\nCoefficient of variation for outlet №1: {coefficient_1}")
    print(f"Coefficient of variation for outlet №2: {coefficient_2}")

    if deviation_1.real < deviation_2.real:
        print("Choosing to eliminate outlet №2.")
    else:
        print("Choosing to eliminate outlet №1.")

if __name__ == "__main__":
    lab_2()

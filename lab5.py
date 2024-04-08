import numpy as np

# Функціонал оцінювання
F = np.array([
    [3, 6, 5, 6],
    [1, 3, 9, 5],
    [4, 1, 8, 4]
])

# Ймовірності станів економічного середовища
probabilities = np.array([0.2, 0.3, 0.25, 0.25])

# Критерій Ходжеса-Лемана
expected_values = np.dot(F, probabilities)
print("Очікувані вартості за критерієм Ходжеса-Лемана:", expected_values)

# Модифікований критерій
modified_criteria = np.sum(F * probabilities, axis=1)
print("Модифікований критерій:", modified_criteria)

# Найкраще рішення за критерієм Ходжеса-Лемана
best_solution_HL = np.argmin(expected_values)
print("Найкраще рішення за критерієм Ходжеса-Лемана: x", best_solution_HL + 1)

# Найкраще рішення за модифікованим критерієм
best_solution_modified = np.argmin(modified_criteria)
print("Найкраще рішення за модифікованим критерієм: x", best_solution_modified + 1)

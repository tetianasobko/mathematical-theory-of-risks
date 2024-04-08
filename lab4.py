import numpy as np
import math

m_n = np.array([0.5, 0.4, 0.5, 0.5, 0.4, 0.3, 0.4, 0.3, 0.5, 0.3])
sigma_n = np.array([0.2, 0.15, 0.2, 0.2, 0.15, 0.12, 0.15, 0.14, 0.2, 0.13])
m_q = 0.1
x_n = np.array([0.8, 0.6, 1.2, 0.75, 0.7, 1.1, 0.9, 0.7, 0.85, 0.55])
sigma_pn = np.array([0.15, 0.11, 0.15, 0.12, 0.1, 0.05, 0.12, 0.08, 0.1, 0.11])

for i in range(len(x_n)):
    m_p = x_n[i] * m_n[i] + (1 - x_n[i]) * m_q
    sigma_p = x_n[i] * sigma_n[i]
    desired_x_n = math.sqrt(sigma_pn[i]**2 / sigma_n[i]**2)

    
    print(f"Для стовпця {i + 1}:")
    print(f"Норма прибутку: {m_p * 100:.2f}%")
    print(f"Оцінка ризику: {sigma_p * 100:.2f}%")
    print(f"Структура портфеля для досягнення σ_pn = {sigma_pn[i] * 100}%: {desired_x_n * 100:.2f}% ринкових цінних паперів та {100 - desired_x_n * 100:.2f}% державних облігацій.")
    print(f"---")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Настройка шрифтов для русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

# Данные для поразрядной сортировки
sizes = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
radix_actual = [0.024, 0.048, 0.072, 0.093, 0.119, 0.141, 0.164, 0.187, 0.208, 0.231]
radix_expected = [0.024, 0.096, 0.144, 0.192, 0.24, 0.288, 0.356, 0.384, 0.432, 0.48]

# Создание графика
plt.figure(figsize=(12, 7))

# Построение графиков реального и ожидаемого времени
plt.plot(sizes, radix_actual, 'bo-', linewidth=2, markersize=8, label='Реальное время')
plt.plot(sizes, radix_expected, 'r--', linewidth=2, markersize=8, label='Ожидаемое время')

# Настройка осей
plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время выполнения (сек)', fontsize=12)
plt.title('Поразрядная сортировка: Реальное vs Ожидаемое время', fontsize=14, fontweight='bold')

# Добавление сетки
plt.grid(True, linestyle='--', alpha=0.7)

# Расчет коэффициентов масштабирования
actual_slope, actual_intercept, _, _, _ = linregress(sizes, radix_actual)
expected_slope, expected_intercept, _, _, _ = linregress(sizes, radix_expected)

# Добавление информации о масштабировании
plt.text(0.05, 0.95,
         f"Реальное время: ~{actual_slope:.7f} * N + {actual_intercept:.4f}",
         transform=plt.gca().transAxes, fontsize=10, color='blue')

plt.text(0.05, 0.90,
         f"Ожидаемое время: ~{expected_slope:.7f} * N + {expected_intercept:.4f}",
         transform=plt.gca().transAxes, fontsize=10, color='red')

# Добавление легенды
plt.legend(loc='upper left', fontsize=10)

# Отображение графика
plt.tight_layout()
plt.show()

# Вывод формул
print(f"Формула для реального времени: время = {actual_slope:.7f} * N + {actual_intercept:.4f}")
print(f"Формула для ожидаемого времени: время = {expected_slope:.7f} * N + {expected_intercept:.4f}")
import matplotlib.pyplot as plt
import numpy as np

# Настройка шрифтов для русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

# Данные для пузырьковой сортировки
sizes = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
bubble_actual = [3.9, 13.5, 25.1, 43.2, 69.9, 90, 121, 159.3, 202.7, 244.3]
bubble_expected = [3.9, 15.6, 35.1, 62.4, 97.5, 140.4, 191.1, 249.6, 315.9, 390]

# Создание графика
plt.figure(figsize=(12, 7))

# Построение графиков реального и ожидаемого времени
plt.plot(sizes, bubble_actual, 'bo-', linewidth=2, markersize=8, label='Реальное время')
plt.plot(sizes, bubble_expected, 'r--', linewidth=2, markersize=8, label='Ожидаемое время')

# Настройка осей
plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время выполнения (сек)', fontsize=12)
plt.title('Пузырьковая сортировка: Реальное vs Ожидаемое время', fontsize=14, fontweight='bold')

# Добавление сетки
plt.grid(True, linestyle='--', alpha=0.7)

# Расчет коэффициентов масштабирования
actual_coeff = np.polyfit(sizes, bubble_actual, 1)
expected_coeff = np.polyfit(sizes, bubble_expected, 1)

# Добавление информации о масштабировании
plt.text(0.05, 0.95,
         f"Реальное время: ~{actual_coeff[0]:.5f} * N + {actual_coeff[1]:.2f}",
         transform=plt.gca().transAxes, fontsize=10, color='blue')

plt.text(0.05, 0.90,
         f"Ожидаемое время: ~{expected_coeff[0]:.5f} * N + {expected_coeff[1]:.2f}",
         transform=plt.gca().transAxes, fontsize=10, color='red')

# Добавление легенды
plt.legend(loc='upper left', fontsize=10)

# Отображение графика
plt.tight_layout()
plt.show()
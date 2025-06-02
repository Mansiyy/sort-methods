import matplotlib.pyplot as plt
import numpy as np

# Настройка шрифтов для русского языка
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

# Данные для быстрой сортировки
sizes = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
quick_actual = [0.5, 1.2, 2.0, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
quick_expected = [0.5, 1.11, 1.77, 2.45, 3.16, 3.89, 4.64, 5.41, 6.20, 7.01]

# Создание графика
plt.figure(figsize=(12, 7))

# Построение графиков реального и ожидаемого времени
plt.plot(sizes, quick_actual, 'go-', linewidth=2, markersize=8, label='Реальное время')
plt.plot(sizes, quick_expected, 'm--', linewidth=2, markersize=8, label='Ожидаемое время')

# Настройка осей
plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время выполнения (сек)', fontsize=12)
plt.title('Быстрая сортировка: Реальное vs Ожидаемое время', fontsize=14, fontweight='bold')

# Добавление сетки
plt.grid(True, linestyle='--', alpha=0.7)

# Расчет коэффициентов масштабирования (линейная аппроксимация)
actual_coeff = np.polyfit(sizes, quick_actual, 1)
expected_coeff = np.polyfit(sizes, quick_expected, 1)

# Добавление информации о масштабировании
plt.text(0.05, 0.95,
         f"Реальное время: ~{actual_coeff[0]:.5f} * N + {actual_coeff[1]:.2f}",
         transform=plt.gca().transAxes, fontsize=10, color='green')

plt.text(0.05, 0.90,
         f"Ожидаемое время: ~{expected_coeff[0]:.5f} * N + {expected_coeff[1]:.2f}",
         transform=plt.gca().transAxes, fontsize=10, color='magenta')

# Добавление легенды
plt.legend(loc='upper left', fontsize=10)

# Отображение графика
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

sizes = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
insertion_actual = [0.25, 0.9, 2.0, 3.5, 5.5, 8.0, 11.0, 14.5, 18.5, 23.0]
insertion_expected = [0.25 * (i/500)**2 for i in sizes]  # O(N²)

plt.figure(figsize=(12, 7))
plt.plot(sizes, insertion_actual, 'go-', lw=2, ms=8, label='Реальное время')
plt.plot(sizes, insertion_expected, 'r--', lw=2, ms=8, label='Ожидаемое время')

plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время (сек)', fontsize=12)
plt.title('Сортировка вставками: Реальное vs Ожидаемое время', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7)

actual_coeff = np.polyfit(sizes, insertion_actual, 1)
expected_coeff = np.polyfit(sizes, insertion_expected, 1)

plt.text(0.05, 0.95, f"Реальное: {actual_coeff[0]:.5f}*N + {actual_coeff[1]:.2f}",
         transform=plt.gca().transAxes, color='green', fontsize=10)
plt.text(0.05, 0.90, f"Ожидаемое: {expected_coeff[0]:.5f}*N + {expected_coeff[1]:.2f}",
         transform=plt.gca().transAxes, color='red', fontsize=10)

plt.legend()
plt.tight_layout()
plt.show()
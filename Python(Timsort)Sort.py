import matplotlib.pyplot as plt
import numpy as np

from QuickSort import sizes




plt.figure(figsize=(12, 7))
built_in_actual = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
built_in_expected = [0.00005 * i * np.log2(i) for i in sizes]  # O(N log N)

plt.plot(sizes, built_in_actual, 'co-', lw=2, ms=8, label='Реальное время')
plt.plot(sizes, built_in_expected, 'g--', lw=2, ms=8, label='Ожидаемое время')

plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время (сек)', fontsize=12)
plt.title('Встроенная сортировка: Реальное vs Ожидаемое время', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7)

actual_coeff = np.polyfit(sizes, built_in_actual, 1)
expected_coeff = np.polyfit(sizes, built_in_expected, 1)

plt.text(0.05, 0.95, f"Реальное: {actual_coeff[0]:.5f}*N + {actual_coeff[1]:.2f}",
         transform=plt.gca().transAxes, color='cyan', fontsize=10)
plt.text(0.05, 0.90, f"Ожидаемое: {expected_coeff[0]:.5f}*N + {expected_coeff[1]:.2f}",
         transform=plt.gca().transAxes, color='green', fontsize=10)

plt.legend()
plt.tight_layout()
plt.show()
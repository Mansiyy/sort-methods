import matplotlib.pyplot as plt
import numpy as np

from QuickSort import sizes

plt.figure(figsize=(12, 7))
selection_actual = [0.3, 1.0, 2.3, 4.0, 6.5, 9.5, 13.0, 17.0, 21.5, 27.0]
selection_expected = [0.3 * (i/500)**2 for i in sizes]  # O(N²)

plt.plot(sizes, selection_actual, 'bo-', lw=2, ms=8, label='Реальное время')
plt.plot(sizes, selection_expected, 'm--', lw=2, ms=8, label='Ожидаемое время')

plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время (сек)', fontsize=12)
plt.title('Сортировка выбором: Реальное vs Ожидаемое время', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7)

actual_coeff = np.polyfit(sizes, selection_actual, 1)
expected_coeff = np.polyfit(sizes, selection_expected, 1)

plt.text(0.05, 0.95, f"Реальное: {actual_coeff[0]:.5f}*N + {actual_coeff[1]:.2f}",
         transform=plt.gca().transAxes, color='blue', fontsize=10)
plt.text(0.05, 0.90, f"Ожидаемое: {expected_coeff[0]:.5f}*N + {expected_coeff[1]:.2f}",
         transform=plt.gca().transAxes, color='magenta', fontsize=10)

plt.legend()
plt.tight_layout()
plt.show()
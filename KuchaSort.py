import matplotlib.pyplot as plt
import numpy as np

from QuickSort import sizes

plt.figure(figsize=(12, 7))
heap_actual = [0.15, 0.3, 0.45, 0.65, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4]
heap_expected = [0.0002 * i * np.log2(i) for i in sizes]  # O(N log N)

plt.plot(sizes, heap_actual, 'mo-', lw=2, ms=8, label='Реальное время')
plt.plot(sizes, heap_expected, 'b--', lw=2, ms=8, label='Ожидаемое время')

plt.xlabel('Размер массива', fontsize=12)
plt.ylabel('Время (сек)', fontsize=12)
plt.title('Сортировка кучей: Реальное vs Ожидаемое время', fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7)

actual_coeff = np.polyfit(sizes, heap_actual, 1)
expected_coeff = np.polyfit(sizes, heap_expected, 1)

plt.text(0.05, 0.95, f"Реальное: {actual_coeff[0]:.5f}*N + {actual_coeff[1]:.2f}",
         transform=plt.gca().transAxes, color='magenta', fontsize=10)
plt.text(0.05, 0.90, f"Ожидаемое: {expected_coeff[0]:.5f}*N + {expected_coeff[1]:.2f}",
         transform=plt.gca().transAxes, color='blue', fontsize=10)

plt.legend()
plt.tight_layout()
plt.show()
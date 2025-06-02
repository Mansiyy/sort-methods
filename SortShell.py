import matplotlib.pyplot as plt
import numpy as np

# Настройка шрифтов для поддержки кириллицы
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

# Данные для сортировки Шелла
sizes = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
shell_actual = [0.11, 0.22, 0.34, 0.49, 0.67, 0.81, 0.94, 1.14, 1.31, 1.35]
shell_expected = [0.11, 0.22, 0.5204, 0.88, 1.2776, 1.7068, 2.16166, 2.64, 3.18823, 3.65412]

# Данные для пузырьковой сортировки
bubble_actual = [3.9, 13.5, 25.1, 43.2, 69.9, 90, 121, 159.3, 202.7, 244.3]
bubble_expected = [3.9, 15.6, 35.1, 62.4, 97.5, 140.4, 191.1, 249.6, 315.9, 390]

# Данные для поразрядной сортировки
radix_actual = [0.024, 0.048, 0.072, 0.093, 0.119, 0.141, 0.164, 0.187, 0.208, 0.231]
radix_expected = [0.024, 0.096, 0.144, 0.192, 0.24, 0.288, 0.356, 0.384, 0.432, 0.48]


def plot_sort_comparison(sizes, actual, expected, title, ylabel):
    """
    Строит график сравнения реальных и ожидаемых значений времени выполнения
    """
    plt.figure(figsize=(10, 6))

    # Преобразуем размеры в numpy массив для удобства вычислений
    x = np.array(sizes)

    # Построение графиков
    plt.plot(x, actual, 'o-', linewidth=2, markersize=8, label='Реальное время', color='blue')
    plt.plot(x, expected, 's--', linewidth=2, markersize=6, label='Ожидаемое время', color='red')

    # Настройка осей и заголовка
    plt.xlabel('Размер массива', fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Расчет коэффициентов масштабирования
    actual_scale = np.polyfit(x, actual, 1)
    expected_scale = np.polyfit(x, expected, 1)

    # Добавление информации о масштабировании
    plt.text(0.05, 0.95,
             f"Реальное: ~{actual_scale[0]:.6f} * N {'+' if actual_scale[1] >= 0 else ''}{actual_scale[1]:.4f}",
             transform=plt.gca().transAxes, fontsize=10, color='blue')

    plt.text(0.05, 0.90,
             f"Ожидаемое: ~{expected_scale[0]:.6f} * N {'+' if expected_scale[1] >= 0 else ''}{expected_scale[1]:.4f}",
             transform=plt.gca().transAxes, fontsize=10, color='red')

    # Легенда
    plt.legend(loc='best', fontsize=10)

    # Отображение графика
    plt.tight_layout()
    plt.show()


# Построение графиков для каждой сортировки
plot_sort_comparison(sizes, shell_actual, shell_expected,
                     'Сортировка Шелла: Реальное vs Ожидаемое время',
                     'Время выполнения (сек)')

plot_sort_comparison(sizes, bubble_actual, bubble_expected,
                     'Пузырьковая сортировка: Реальное vs Ожидаемое время',
                     'Время выполнения (сек)')

plot_sort_comparison(sizes, radix_actual, radix_expected,
                     'Поразрядная сортировка: Реальное vs Ожидаемое время',
                     'Время выполнения (сек)')
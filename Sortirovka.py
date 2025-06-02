import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import sys

sys.setrecursionlimit(1000000)  # Увеличиваем лимит рекурсии для больших массивов


# ===== АЛГОРИТМЫ СОРТИРОВКИ =====
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def shell_sort(arr):
    n = len(arr)
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if len(arr) == 0:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


# ===== ГЕНЕРАЦИЯ ДАННЫХ =====
def generate_data(size, data_type, order_type):
    if data_type == 'digits':
        arr = [random.randint(0, 9) for _ in range(size)]
    elif data_type == 'integers':
        arr = [random.randint(0, 1000000) for _ in range(size)]  # Только положительные числа для radix
    elif data_type == 'strings':
        arr = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 10))) for _ in range(size)]
    elif data_type == 'dates':
        start = datetime(2000, 1, 1)
        arr = [start + timedelta(days=random.randint(0, 10000)) for _ in range(size)]

    if order_type == 'random':
        return arr
    elif order_type == 'partially_sorted':
        arr.sort()
        for _ in range(max(1, size // 10)):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    elif order_type == 'reverse':
        return sorted(arr, reverse=True)


# ===== ИЗМЕРЕНИЕ ВРЕМЕНИ =====
def measure_performance(sort_func, data):
    def wrapper():
        return sort_func(data.copy())

    time_taken = timeit.timeit(wrapper, number=3)  # Уменьшено до 3 запусков для скорости
    return time_taken / 3


# ===== НАСТРОЙКИ ТЕСТИРОВАНИЯ =====
sizes = [50, 500, 5000, 50000, 500000]
data_types = ['digits', 'integers', 'strings', 'dates']
order_types = ['random', 'reverse', 'partially_sorted']

algorithms = {
    'вставками': insertion_sort,
    'пузырьком': bubble_sort,
    'выбором': selection_sort,
    'Шелла': shell_sort,
    'быстрая': quick_sort,
    'слиянием': merge_sort,
    'кучей': heap_sort,
    'поразрядная': radix_sort,
    'встроенная': sorted
}

results = {alg: {size: 0 for size in sizes} for alg in algorithms}


# ===== ВИЗУАЛИЗАЦИЯ =====
def plot_results(data_type, order_type):
    plt.figure(figsize=(14, 8))
    for alg in algorithms:
        if any(results[alg][size] for size in sizes):
            times = [results[alg][size] for size in sizes]
            plt.plot(sizes, times, marker='o', label=alg)

    plt.xscale('log')
    plt.yscale('log')
    plt.title(f'Сравнение сортировок ({data_type}, {order_type})')
    plt.xlabel('Размер массива')
    plt.ylabel('Время (секунды)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()

    # Сохранение и отображение
    filename = f"{data_type}_{order_type}.png"
    plt.savefig(filename, dpi=150)
    plt.show()
    print(f"График сохранен: {filename}")


# ===== ОСНОВНОЙ ЦИКЛ ТЕСТИРОВАНИЯ =====
if __name__ == "__main__":
    print("Тестирование начато...\n")

    for data_type in data_types:
        for order_type in order_types:
            print(f"Тестирование: {data_type} ({order_type})")
            for size in sizes:
                print(f"Размер: {size}")

                # Пропуск слишком больших массивов для дат
                if size > 10000 and data_type == 'dates':
                    continue

                data = generate_data(size, data_type, order_type)

                for alg_name, alg_func in algorithms.items():
                    # Пропуск медленных алгоритмов для больших размеров
                    if (size > 1000 and alg_name in ['вставками', 'пузырьком', 'выбором']) or \
                            (size > 5000 and alg_name in ['Шелла']) or \
                            (alg_name == 'поразрядная' and data_type not in ['digits', 'integers']):
                        results[alg_name][size] = None
                        continue

                    try:
                        time_taken = measure_performance(alg_func, data)
                        results[alg_name][size] = time_taken
                        print(f"  {alg_name}: {time_taken:.6f} с")
                    except Exception as e:
                        results[alg_name][size] = None
                        print(f"  Ошибка: {e}")
            plot_results(data_type, order_type)
            results = {alg: {size: 0 for size in sizes} for alg in algorithms}  # Сброс результатов для следующего теста
            print("------------------------------")

    print("\nТестирование завершено!")
"""
Порівняльний аналіз алгоритмів сортування за часом виконання
"""

import timeit
import random
from sorting_algorithms import merge_sort, insertion_sort, timsort


def generate_random_data(size):
    """Генерує випадковий список заданого розміру"""
    return [random.randint(0, 10000) for _ in range(size)]


def generate_sorted_data(size):
    """Генерує відсортований список заданого розміру"""
    return list(range(size))


def generate_reverse_sorted_data(size):
    """Генерує список, відсортований у зворотному порядку"""
    return list(range(size, 0, -1))


def generate_nearly_sorted_data(size):
    """Генерує майже відсортований список (90% відсортовано)"""
    data = list(range(size))
    # Перемішуємо 10% елементів
    swaps = size // 10
    for _ in range(swaps):
        i, j = random.randint(0, size - 1), random.randint(0, size - 1)
        data[i], data[j] = data[j], data[i]
    return data


def measure_time(algorithm, data, number=10):
    """
    Вимірює час виконання алгоритму
    
    Args:
        algorithm: функція сортування
        data: дані для сортування
        number: кількість повторень для усереднення
        
    Returns:
        середній час виконання в секундах
    """
    # Створюємо копію даних для кожного виміру
    timer = timeit.Timer(lambda: algorithm(data.copy()))
    time_taken = timer.timeit(number=number) / number
    return time_taken


def run_performance_tests():
    """Виконує повний набір тестів продуктивності"""

    # Розміри наборів даних
    sizes = [100, 1000, 5000, 10000]

    # Алгоритми для тестування
    algorithms = {
        'Merge Sort': merge_sort,
        'Insertion Sort': insertion_sort,
        'Timsort (sorted)': timsort
    }

    # Типи даних
    data_types = {
        'Випадкові дані': generate_random_data,
        'Відсортовані дані': generate_sorted_data,
        'Зворотно відсортовані': generate_reverse_sorted_data,
        'Майже відсортовані': generate_nearly_sorted_data
    }

    print("=" * 100)
    print("ПОРІВНЯЛЬНИЙ АНАЛІЗ АЛГОРИТМІВ СОРТУВАННЯ")
    print("=" * 100)
    print()

    for data_type_name, data_generator in data_types.items():
        print(f"\n{'=' * 100}")
        print(f"ТИП ДАНИХ: {data_type_name}")
        print(f"{'=' * 100}\n")

        # Заголовок таблиці
        print(f"{'Розмір':<15} {'Merge Sort':<20} {'Insertion Sort':<20} {'Timsort':<20}")
        print("-" * 100)

        for size in sizes:
            # Генеруємо дані
            data = data_generator(size)

            # Вимірюємо час для кожного алгоритму
            times = {}
            for alg_name, alg_func in algorithms.items():
                # Для великих масивів пропускаємо insertion sort (занадто повільний)
                if alg_name == 'Insertion Sort' and size > 10000:
                    times[alg_name] = None
                else:
                    # Зменшуємо кількість повторень для великих масивів
                    number = 3 if size >= 5000 else 10
                    times[alg_name] = measure_time(alg_func, data, number=number)

            # Виводимо результати
            merge_time = (
                f"{times['Merge Sort']:.6f} с"
                if times['Merge Sort']
                else "N/A"
            )
            insertion_time = (
                f"{times['Insertion Sort']:.6f} с"
                if times['Insertion Sort']
                else "Занадто повільно"
            )
            timsort_time = (
                f"{times['Timsort (sorted)']:.6f} с"
                if times['Timsort (sorted)']
                else "N/A"
            )

            print(f"{size:<15} {merge_time:<20} {insertion_time:<20} {timsort_time:<20}")

        print()

    # Додатковий тест на дуже великих масивах
    print(f"\n{'=' * 100}")
    print("ТЕСТ НА ВЕЛИКИХ МАСИВАХ (тільки ефективні алгоритми)")
    print(f"{'=' * 100}\n")

    large_sizes = [50000, 100000]
    print(f"{'Розмір':<15} {'Merge Sort':<25} {'Timsort':<25}")
    print("-" * 100)

    for size in large_sizes:
        data = generate_random_data(size)

        merge_time = measure_time(merge_sort, data, number=3)
        timsort_time = measure_time(timsort, data, number=3)

        print(f"{size:<15} {merge_time:.6f} с{' ' * 14} {timsort_time:.6f} с")

    print("\n" + "=" * 100)
    print("ВИСНОВКИ:")
    print("=" * 100)
    print("""
1. Insertion Sort ефективний лише на малих масивах (< 1000 елементів)
2. Merge Sort показує стабільну продуктивність O(n log n) на всіх типах даних
3. Timsort (вбудований sorted) найефективніший у більшості випадків:
   - На випадкових даних: порівнянний з Merge Sort
   - На відсортованих/майже відсортованих: значно швидший (O(n))
   - Оптимізований для реальних даних з частковим порядком
4. Timsort поєднує переваги обох алгоритмів:
   - Використовує Insertion Sort для малих підмасивів
   - Використовує Merge Sort для великих масивів
   - Виявляє та використовує природні впорядковані послідовності
    """)


if __name__ == "__main__":
    # Встановлюємо seed для відтворюваності результатів
    random.seed(42)
    
    run_performance_tests()

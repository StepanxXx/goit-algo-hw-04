"""
Реалізація алгоритмів сортування: злиттям та вставками
"""


def merge_sort(arr):
    """
    Сортування злиттям
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    """
    Сортування злиттям
    """
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    """
    Сортування вставками
    """
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def timsort(arr):
    """
    Timsort
    """
    return sorted(arr)


if __name__ == "__main__":
    # Тестування алгоритмів
    test_data = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 23, 36, 18, 77]

    print("Оригінальний список:", test_data)
    print("Сортування злиттям:", merge_sort(test_data))
    print("Сортування вставками:", insertion_sort(test_data))
    print("Timsort (sorted):", timsort(test_data))

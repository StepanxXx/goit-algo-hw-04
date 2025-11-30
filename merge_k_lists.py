"""
Об'єднання k відсортованих списків у один відсортований список
"""

from sorting_algorithms import merge_sort


def merge_k_lists(lists):
    """
    Об'єднує k відсортованих списків у один відсортований список
    """
    # Об'єднуємо всі списки в один
    merged = []
    for lst in lists:
        merged.extend(lst)
    
    # Сортуємо за допомогою merge_sort

    print("Відсортований список:", merged)
    return merge_sort(merged)


if __name__ == "__main__":
    # Приклад з завдання
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    

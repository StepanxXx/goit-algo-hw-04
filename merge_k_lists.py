"""
Об'єднання k відсортованих списків у один відсортований список
"""

from sorting_algorithms import merge

def merge_k_lists(lists):
    """
    Об'єднує k відсортованих списків у один відсортований список
    """
    merged = lists[0]
    for lst in lists[1:]:
        merged = merge(merged, lst)

    print("Відсортований список:", merged)
    return merged


if __name__ == "__main__":
    # Приклад з завдання
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)

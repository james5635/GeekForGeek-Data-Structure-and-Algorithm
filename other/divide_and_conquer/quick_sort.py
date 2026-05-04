def quick_sort(arr: list[int]) -> list[int]:
    """
    Sort an array using the quick sort algorithm.

    Args:
        arr: List of integers to sort

    Returns:
        A new sorted list
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print(quick_sort(arr))

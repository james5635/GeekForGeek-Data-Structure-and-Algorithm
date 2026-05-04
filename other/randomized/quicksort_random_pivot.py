import random


def quicksort_random_pivot(arr: list[int]) -> list[int]:
    """Quicksort using random pivot selection."""
    if len(arr) <= 1:
        return arr[:]

    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]

    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_idx]
    middle = [x for x in arr if x == pivot]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_idx]

    return quicksort_random_pivot(left) + middle + quicksort_random_pivot(right)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5, 3, 6, 2, 4]
    print(f"Original: {arr}")
    print(f"Sorted:   {quicksort_random_pivot(arr)}")

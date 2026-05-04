def find_max_min(arr: list[int]) -> tuple[int, int]:
    """
    Find the maximum and minimum elements in an array using divide and conquer.

    Args:
        arr: List of integers

    Returns:
        Tuple of (maximum, minimum)
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    return _divide(arr, 0, len(arr) - 1)


def _divide(arr: list[int], low: int, high: int) -> tuple[int, int]:
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[high], arr[low]
        return arr[low], arr[high]

    mid = (low + high) // 2
    max1, min1 = _divide(arr, low, mid)
    max2, min2 = _divide(arr, mid + 1, high)

    return max(max1, max2), min(min1, min2)


if __name__ == "__main__":
    arr = [3, 5, 1, 9, 2, 8, 4]
    maximum, minimum = find_max_min(arr)
    print(f"Max: {maximum}, Min: {minimum}")

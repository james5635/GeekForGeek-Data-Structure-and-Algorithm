def frequency_limited_range(arr: list[int], max_val: int) -> dict[int, int]:
    """
    Find frequency of each element in a limited range array.

    Uses the array itself to store frequencies by adding (n+1) to indices.

    Args:
        arr: List of integers in range [1, max_val]
        max_val: Maximum value in the array

    Returns:
        Dictionary mapping element to its frequency
    """
    if not arr:
        return {}

    n = len(arr)
    offset = max_val + 1

    temp = arr[:]

    for i in range(n):
        idx = temp[i] % offset - 1
        if 0 <= idx < n:
            arr[idx] += offset

    result = {}
    for i in range(n):
        freq = arr[i] // offset
        if freq > 0:
            result[i + 1] = freq

    return result


if __name__ == "__main__":
    arr = [2, 3, 2, 3, 5]
    print(frequency_limited_range(arr, 5))

    arr2 = [1, 2, 2, 3, 1, 1, 4]
    print(frequency_limited_range(arr2, 4))

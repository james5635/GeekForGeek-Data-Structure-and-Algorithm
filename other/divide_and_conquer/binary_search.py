def binary_search(arr: list[int], target: int) -> int:
    """
    Perform binary search on a sorted array.

    Args:
        arr: A sorted list of integers
        target: The value to search for

    Returns:
        The index of target if found, -1 otherwise
    """

    def _search(left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return _search(mid + 1, right)
        return _search(left, mid - 1)

    return _search(0, len(arr) - 1)


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 50, 80]
    print(binary_search(arr, 10))
    print(binary_search(arr, 25))

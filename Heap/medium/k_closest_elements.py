"""
K Closest Elements in Sorted Array - GeeksforGeeks
https://www.geeksforgeeks.org/find-k-closest-elements-given-value/

Problem: Given a sorted array arr[], a number k, and a target value x, return the
k elements from the array that are closest to x (excluding x itself if present).

An element a is closer to x than b if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| AND a > b (prefer larger element on tie)

Time Complexity:
- Naive: O(n*log(n)) using custom sorting
- Better: O(n) using linear search with two pointers
- Expected: O(k + log(n)) using binary search with two pointers

Space Complexity: O(k) for storing results
"""


def print_k_closest_binary_search(arr, k, x):
    """
    Find k closest elements to x using binary search + two pointers.

    Args:
        arr: Sorted list of unique integers
        k: Number of closest elements to find
        x: Target value

    Returns:
        List of k closest elements
    """
    n = len(arr)
    low, high, pos = 0, n - 1, -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            pos = mid
            low = mid + 1
        else:
            high = mid - 1

    left, right = pos, pos + 1

    if right < n and arr[right] == x:
        right += 1

    res = []

    while left >= 0 and right < n and len(res) < k:
        leftDiff = abs(arr[left] - x)
        rightDiff = abs(arr[right] - x)

        if leftDiff < rightDiff:
            res.append(arr[left])
            left -= 1
        else:
            res.append(arr[right])
            right += 1

    while left >= 0 and len(res) < k:
        res.append(arr[left])
        left -= 1

    while right < n and len(res) < k:
        res.append(arr[right])
        right += 1

    return res


def print_k_closest_linear_search(arr, k, x):
    """
    Find k closest elements to x using linear search with two pointers.
    O(n) time complexity.
    """
    n = len(arr)
    i = 0

    while i < n and arr[i] < x:
        i += 1
    left = i - 1
    right = i

    if right < n and arr[right] == x:
        right += 1

    res = []

    while left >= 0 and right < n and len(res) < k:
        leftDiff = abs(arr[left] - x)
        rightDiff = abs(arr[right] - x)

        if leftDiff < rightDiff:
            res.append(arr[left])
            left -= 1
        else:
            res.append(arr[right])
            right += 1

    while left >= 0 and len(res) < k:
        res.append(arr[left])
        left -= 1

    while right < n and len(res) < k:
        res.append(arr[right])
        right += 1

    return res


def print_k_closest_sorting(arr, k, x):
    """
    Find k closest elements to x using custom sorting.
    O(n*log(n)) time complexity.
    """
    arr_copy = arr.copy()
    arr_copy.sort(key=lambda a: (abs(a - x), -a))

    result = []
    count = 0

    for num in arr_copy:
        if num == x:
            continue
        result.append(num)
        count += 1
        if count == k:
            break

    return result


if __name__ == "__main__":
    # Example 1
    arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    k, x = 4, 35
    print("Closest elements:", print_k_closest_binary_search(arr, k, x))
    # Output: [39, 30, 42, 45]

    # Example 2
    arr = [1, 3, 4, 10, 12]
    k, x = 2, 4
    print("Closest elements:", print_k_closest_binary_search(arr, k, x))
    # Output: [3, 1]

"""
Count Distinct Elements in Every Window

Problem: Given an array of integers and a window size k, count the number of
distinct elements in every contiguous subarray (window) of size k.

Approach: Use a sliding window with hash map to count frequencies. Add new element
from right, remove leftmost element, and track distinct count.

Time Complexity: O(n) - single pass through array
Space Complexity: O(k) - at most k elements in window
"""

from collections import defaultdict


def count_distinct_in_windows(arr, k):
    """
    Count distinct elements in every window of size k.

    Args:
        arr: List of integers
        k: Window size

    Returns:
        List of distinct counts for each window
    """
    if not arr or k <= 0 or k > len(arr):
        return []

    freq = defaultdict(int)
    result = []
    distinct_count = 0

    # Process first window
    for i in range(k):
        if freq[arr[i]] == 0:
            distinct_count += 1
        freq[arr[i]] += 1

    result.append(distinct_count)

    # Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element of previous window
        left_elem = arr[i - k]
        freq[left_elem] -= 1
        if freq[left_elem] == 0:
            distinct_count -= 1

        # Add new element
        if freq[arr[i]] == 0:
            distinct_count += 1
        freq[arr[i]] += 1

        result.append(distinct_count)

    return result


def get_distinct_elements_in_windows(arr, k):
    """
    Get the actual distinct elements in each window.

    Args:
        arr: List of integers
        k: Window size

    Returns:
        List of sets containing distinct elements for each window
    """
    if not arr or k <= 0 or k > len(arr):
        return []

    result = []

    for i in range(len(arr) - k + 1):
        window = arr[i : i + k]
        result.append(set(window))

    return result


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [1, 2, 1, 3, 4, 2, 3]
    k1 = 4
    print(f"Array: {arr1}, k: {k1}")
    print(f"Distinct counts: {count_distinct_in_windows(arr1, k1)}")
    print()

    # Test Case 2: All same elements
    arr2 = [1, 1, 1, 1, 1]
    k2 = 3
    print(f"Array: {arr2}, k: {k2}")
    print(f"Distinct counts: {count_distinct_in_windows(arr2, k2)}")
    print()

    # Test Case 3: All distinct elements
    arr3 = [1, 2, 3, 4, 5]
    k3 = 3
    print(f"Array: {arr3}, k: {k3}")
    print(f"Distinct counts: {count_distinct_in_windows(arr3, k3)}")
    print()

    # Test Case 4: k = 1
    arr4 = [1, 2, 1, 3]
    k4 = 1
    print(f"Array: {arr4}, k: {k4}")
    print(f"Distinct counts: {count_distinct_in_windows(arr4, k4)}")
    print()

    # Test Case 5: k equals array length
    arr5 = [1, 2, 3, 4]
    k5 = 4
    print(f"Array: {arr5}, k: {k5}")
    print(f"Distinct counts: {count_distinct_in_windows(arr5, k5)}")
    print()

    # Test Case 6: Empty array
    arr6 = []
    k6 = 3
    print(f"Array: {arr6}, k: {k6}")
    print(f"Distinct counts: {count_distinct_in_windows(arr6, k6)}")
    print()

    # Test Case 7: Negative numbers
    arr7 = [-1, -2, -1, -3, -2]
    k7 = 3
    print(f"Array: {arr7}, k: {k7}")
    print(f"Distinct counts: {count_distinct_in_windows(arr7, k7)}")
    print()

    # Test Case 8: Large window
    arr8 = [1, 2, 3, 4, 5, 6, 7, 8]
    k8 = 5
    print(f"Array: {arr8}, k: {k8}")
    print(f"Distinct counts: {count_distinct_in_windows(arr8, k8)}")

"""
Maximize length of subarray with all equal elements after K operations
Each operation can change any element to any value to maximize consecutive equal elements
Uses sliding window approach with deque
"""

from collections import deque


def max_equal_subarray(arr, k):
    """
    Find maximum length of subarray that can be made equal using k operations

    Approach:
    - If k == 0, return max frequency of any element
    - Use two-pointer sliding window

    Key insight: We want to find the longest subarray where
    (length - frequency_of_most_common_element) <= k
    """
    if not arr:
        return 0

    n = len(arr)

    if k == 0:
        freq = {}
        for val in arr:
            freq[val] = freq.get(val, 0) + 1
        return max(freq.values()) if freq else 0

    max_len = 0
    freq = {}
    left = 0

    for right in range(n):
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        while right - left + 1 - max(freq.values()) > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def max_equal_subarray_with_changes(arr, k):
    """
    Also return which value to use for maximum subarray
    """
    if not arr:
        return 0, None

    n = len(arr)

    if k == 0:
        freq = {}
        for val in arr:
            freq[val] = freq.get(val, 0) + 1
        most_common = max(freq.keys(), key=lambda x: freq[x])
        return max(freq.values()), most_common

    max_len = 0
    best_val = arr[0]
    freq = {}
    left = 0

    for right in range(n):
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        while right - left + 1 - max(freq.values()) > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1

        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_val = max(freq.keys(), key=lambda x: freq[x])

    return max_len, best_val


def main():
    print("=" * 60)
    print("Maximize Length of Subarray with Equal Elements")
    print("=" * 60)

    print("\n--- Test Case 1 ---")
    arr = [2, 2, 4]
    k = 10
    result = max_equal_subarray(arr, k)
    length, val = max_equal_subarray_with_changes(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (change to {val})")
    print(f"Expected: 3")
    print(f"Pass: {result == 3}")

    print("\n--- Test Case 2 ---")
    arr = [2, 4, 8, 5, 9, 6]
    k = 6
    result = max_equal_subarray(arr, k)
    length, val = max_equal_subarray_with_changes(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (change to {val})")
    print(f"Expected: 3")
    print(f"Pass: {result == 3}")

    print("\n--- Test Case 3 ---")
    arr = [1, 2, 3, 4, 5]
    k = 2
    result = max_equal_subarray(arr, k)
    length, val = max_equal_subarray_with_changes(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (change to {val})")
    print(f"Expected: 3")
    print(f"Pass: {result == 3}")

    print("\n--- Test Case 4 ---")
    arr = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    k = 1
    result = max_equal_subarray(arr, k)
    length, val = max_equal_subarray_with_changes(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (change to {val})")
    print(f"Expected: 4")

    print("\n--- Test Case 5 ---")
    arr = [5, 1, 2, 3, 4, 5]
    k = 2
    result = max_equal_subarray(arr, k)
    length, val = max_equal_subarray_with_changes(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (change to {val})")
    print(f"Expected: 5 (change to 5)")

    print("\n--- Test Case 6 ---")
    arr = [1, 2, 3]
    k = 0
    result = max_equal_subarray(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result}")
    print(f"Expected: 1")
    print(f"Pass: {result == 1}")

    print("\n--- Test Case 7 ---")
    arr = []
    k = 5
    result = max_equal_subarray(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result}")
    print(f"Expected: 0")
    print(f"Pass: {result == 0}")


if __name__ == "__main__":
    main()

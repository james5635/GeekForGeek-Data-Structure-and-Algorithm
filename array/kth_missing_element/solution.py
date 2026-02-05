"""
K-th Missing Element in Sorted Array Problem

Problem Description:
Given a sorted array of distinct positive integers and a positive integer k,
find the k-th missing element in the array.

The missing elements are the positive integers that are not present in the array.

Example:
Input: arr = [2, 3, 5, 9, 10], k = 1
Output: 1
Explanation: The missing elements are 1, 4, 6, 7, 8. The 1st missing is 1.

Input: arr = [2, 3, 5, 9, 10], k = 3
Output: 6
Explanation: The 3rd missing element is 6.

Time Complexity: O(log n) using Binary Search
Space Complexity: O(1)

Approach:
- Calculate how many elements are missing before each index
- Use binary search to find the position where k missing elements occur
- missing_before_i = arr[i] - (i + 1) = how many numbers missing from 1 to arr[i]
"""

from typing import List


def find_kth_missing_element(arr: List[int], k: int) -> int:
    """
    Find the k-th missing element in sorted array.

    Args:
        arr: Sorted list of distinct positive integers
        k: Position of missing element to find

    Returns:
        The k-th missing element, or -1 if not found
    """
    if not arr or k <= 0:
        return -1

    n = len(arr)

    # Binary search to find the position
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        # Count of missing elements from 1 to arr[mid]
        # If no missing, arr[mid] should be mid + 1
        missing_before_mid = arr[mid] - (mid + 1)

        if missing_before_mid < k:
            left = mid + 1
        else:
            right = mid - 1

    # After binary search, right points to the largest index
    # where missing count < k, or -1 if all k missing are before arr[0]
    if right == -1:
        # k-th missing is simply k (since we start counting from 1)
        return k

    missing_before_right = arr[right] - (right + 1)
    # k-th missing = arr[right] + (k - missing_before_right)
    return arr[right] + (k - missing_before_right)


def find_kth_missing_element_linear(arr: List[int], k: int) -> int:
    """
    Linear approach for comparison.
    Time: O(n), Space: O(1)
    """
    if not arr or k <= 0:
        return -1

    # Check missing elements before first element
    if k <= arr[0] - 1:
        return k

    # Adjust k for elements before arr[0]
    k -= arr[0] - 1

    # Check gaps between consecutive elements
    for i in range(len(arr) - 1):
        gap = arr[i + 1] - arr[i] - 1
        if k <= gap:
            return arr[i] + k
        k -= gap

    # kth missing is after last element
    return arr[-1] + k


def find_kth_missing_element_simple(arr: List[int], k: int) -> int:
    """
    Simple approach using set.
    Time: O(n + m), Space: O(n) where m is max value
    """
    if not arr or k <= 0:
        return -1

    num_set = set(arr)
    missing_count = 0
    current = 1

    while missing_count < k:
        if current not in num_set:
            missing_count += 1
            if missing_count == k:
                return current
        current += 1

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard example
    arr1 = [2, 3, 5, 9, 10]
    k1 = 1
    result1 = find_kth_missing_element(arr1, k1)
    print(f"Input: {arr1}, k = {k1}")
    print(f"K-th missing: {result1}")
    print(f"Expected: 1")
    print(f"Pass: {result1 == 1}\n")

    # Test Case 2: Another standard example
    arr2 = [2, 3, 5, 9, 10]
    k2 = 3
    result2 = find_kth_missing_element(arr2, k2)
    print(f"Input: {arr2}, k = {k2}")
    print(f"K-th missing: {result2}")
    print(f"Expected: 6")
    print(f"Pass: {result2 == 6}\n")

    # Test Case 3: Missing at the beginning
    arr3 = [4, 7, 9]
    k3 = 3
    result3 = find_kth_missing_element(arr3, k3)
    print(f"Input: {arr3}, k = {k3}")
    print(f"K-th missing: {result3}")
    print(f"Expected: 3")
    print(f"Pass: {result3 == 3}\n")

    # Test Case 4: No missing elements in between
    arr4 = [1, 2, 3, 4, 5]
    k4 = 2
    result4 = find_kth_missing_element(arr4, k4)
    print(f"Input: {arr4}, k = {k4}")
    print(f"K-th missing: {result4}")
    print(f"Expected: 7")
    print(f"Pass: {result4 == 7}\n")

    # Test Case 5: Single element
    arr5 = [5]
    k5 = 2
    result5 = find_kth_missing_element(arr5, k5)
    print(f"Input: {arr5}, k = {k5}")
    print(f"K-th missing: {result5}")
    print(f"Expected: 2")
    print(f"Pass: {result5 == 2}\n")

    # Test Case 6: Empty array
    arr6 = []
    k6 = 1
    result6 = find_kth_missing_element(arr6, k6)
    print(f"Input: {arr6}, k = {k6}")
    print(f"K-th missing: {result6}")
    print(f"Expected: -1")
    print(f"Pass: {result6 == -1}\n")

    # Test Case 7: Large gaps
    arr7 = [1, 10, 20]
    k7 = 5
    result7 = find_kth_missing_element(arr7, k7)
    print(f"Input: {arr7}, k = {k7}")
    print(f"K-th missing: {result7}")
    print(f"Expected: 6")
    print(f"Pass: {result7 == 6}")

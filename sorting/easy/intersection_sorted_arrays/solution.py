"""
Intersection of Two Sorted Arrays

Problem Description:
    Given two sorted arrays a[] and b[], return the intersection of both arrays.
    Intersection contains elements that are common in both arrays.
    The result should not contain duplicates and should be in sorted order.

Example:
    Input: a = [1, 1, 2, 2, 2, 4], b = [2, 2, 4, 4]
    Output: [2, 4]
    Explanation: 2 and 4 are the only common elements in both arrays

Time Complexity: O(n + m) - Linear time using two-pointer technique
Space Complexity: O(min(n, m)) - For the result array (worst case)
"""

from typing import List


def intersection_sorted(a: List[int], b: List[int]) -> List[int]:
    """
    Find intersection of two sorted arrays.

    Args:
        a: First sorted array
        b: Second sorted array

    Returns:
        List containing intersection elements (no duplicates)
    """
    res = []
    m, n = len(a), len(b)
    i, j = 0, 0

    while i < m and j < n:
        # Skip duplicate elements in the first array
        if i > 0 and a[i - 1] == a[i]:
            i += 1
            continue

        # Skip duplicate elements in the second array
        if j > 0 and b[j - 1] == b[j]:
            j += 1
            continue

        # Compare elements
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            # Found common element
            res.append(a[i])
            i += 1
            j += 1

    return res


if __name__ == "__main__":
    # Test Case 1: Basic case with duplicates
    a = [1, 1, 2, 2, 2, 4]
    b = [2, 2, 4, 4]
    print("Test 1:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = intersection_sorted(a, b)
    print(f"Intersection: {result}")
    print()

    # Test Case 2: No common elements
    a = [1, 2]
    b = [3, 4]
    print("Test 2:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = intersection_sorted(a, b)
    print(f"Intersection: {result}")
    print()

    # Test Case 3: All elements common
    a = [1, 2, 3]
    b = [1, 2, 3]
    print("Test 3:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = intersection_sorted(a, b)
    print(f"Intersection: {result}")
    print()

    # Test Case 4: Larger arrays
    a = [3, 5, 10, 10, 10, 15, 15, 20]
    b = [5, 10, 10, 15, 30]
    print("Test 4:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = intersection_sorted(a, b)
    print(f"Intersection: {result}")
    print()

    # Test Case 5: One empty array
    a = []
    b = [1, 2, 3]
    print("Test 5:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = intersection_sorted(a, b)
    print(f"Intersection: {result}")
    print()

    # Test Case 6: Single common element
    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8]
    print("Test 6:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = intersection_sorted(a, b)
    print(f"Intersection: {result}")

"""
Union of Two Sorted Arrays

Problem Description:
    Given two sorted arrays a[] and b[], return the union of both arrays.
    Union contains all distinct elements present in either array.
    The result should be in sorted order.

Example:
    Input: a = [1, 1, 2, 2, 2, 4], b = [2, 2, 4, 4]
    Output: [1, 2, 4]
    Explanation: 1, 2, and 4 are the distinct elements present in either array

Time Complexity: O(n + m) - Linear time using two-pointer technique
Space Complexity: O(n + m) - For the result array (worst case)
"""

from typing import List


def union_sorted(a: List[int], b: List[int]) -> List[int]:
    """
    Find union of two sorted arrays.

    Args:
        a: First sorted array
        b: Second sorted array

    Returns:
        List containing union elements (distinct, sorted)
    """
    res = []
    m, n = len(a), len(b)
    i, j = 0, 0

    while i < m and j < n:
        # Skip duplicates in first array
        if i > 0 and a[i - 1] == a[i]:
            i += 1
            continue

        # Skip duplicates in second array
        if j > 0 and b[j - 1] == b[j]:
            j += 1
            continue

        # Compare and add smaller element
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        elif a[i] > b[j]:
            res.append(b[j])
            j += 1
        else:
            # Equal elements, add only once
            res.append(a[i])
            i += 1
            j += 1

    # Add remaining elements from first array
    while i < m:
        if i == 0 or a[i - 1] != a[i]:
            res.append(a[i])
        i += 1

    # Add remaining elements from second array
    while j < n:
        if j == 0 or b[j - 1] != b[j]:
            res.append(b[j])
        j += 1

    return res


if __name__ == "__main__":
    # Test Case 1: Basic case with duplicates
    a = [1, 1, 2, 2, 2, 4]
    b = [2, 2, 4, 4]
    print("Test 1:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = union_sorted(a, b)
    print(f"Union: {result}")
    print()

    # Test Case 2: Different elements
    a = [3, 5, 10, 10, 10, 15, 15, 20]
    b = [5, 10, 10, 15, 30]
    print("Test 2:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = union_sorted(a, b)
    print(f"Union: {result}")
    print()

    # Test Case 3: No common elements
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("Test 3:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = union_sorted(a, b)
    print(f"Union: {result}")
    print()

    # Test Case 4: All elements same
    a = [1, 2, 3]
    b = [1, 2, 3]
    print("Test 4:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = union_sorted(a, b)
    print(f"Union: {result}")
    print()

    # Test Case 5: One empty array
    a = []
    b = [1, 2, 3]
    print("Test 5:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = union_sorted(a, b)
    print(f"Union: {result}")
    print()

    # Test Case 6: Negative numbers
    a = [-5, -3, 0, 2]
    b = [-3, 1, 2, 5]
    print("Test 6:")
    print(f"a = {a}")
    print(f"b = {b}")
    result = union_sorted(a, b)
    print(f"Union: {result}")

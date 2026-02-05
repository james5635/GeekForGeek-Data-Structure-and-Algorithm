"""
Count Pairs with Difference K

Problem: Given an array of integers and a difference k, count the number of pairs
of elements whose absolute difference equals k.

Approach: Use a hash map to store frequency of elements. For each element,
check if (element + k) and (element - k) exist in the map.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(n) - hash map stores element frequencies
"""


def count_pairs_with_diff_k(arr, k):
    """
    Count pairs with absolute difference k.

    Args:
        arr: List of integers
        k: Target difference

    Returns:
        Number of pairs with absolute difference k
    """
    if k < 0:
        return 0

    freq = {}
    count = 0

    for num in arr:
        if num + k in freq:
            count += freq[num + k]
        if k != 0 and num - k in freq:
            count += freq[num - k]
        freq[num] = freq.get(num, 0) + 1

    return count


if __name__ == "__main__":
    # Test Case 1: Multiple pairs with diff 3
    arr1 = [1, 5, 3, 4, 2]
    k1 = 3
    print(f"Array: {arr1}, k: {k1}")
    print(f"Count of pairs: {count_pairs_with_diff_k(arr1, k1)}")
    print()

    # Test Case 2: No pairs
    arr2 = [1, 2, 3, 4, 5]
    k2 = 10
    print(f"Array: {arr2}, k: {k2}")
    print(f"Count of pairs: {count_pairs_with_diff_k(arr2, k2)}")
    print()

    # Test Case 3: Duplicate elements
    arr3 = [1, 1, 1, 1]
    k3 = 0
    print(f"Array: {arr3}, k: {k3}")
    print(f"Count of pairs: {count_pairs_with_diff_k(arr3, k3)}")
    print()

    # Test Case 4: k = 0 with unique elements
    arr4 = [1, 2, 3]
    k4 = 0
    print(f"Array: {arr4}, k: {k4}")
    print(f"Count of pairs: {count_pairs_with_diff_k(arr4, k4)}")
    print()

    # Test Case 5: Negative numbers
    arr5 = [-1, -2, -3, 1, 2, 3]
    k5 = 2
    print(f"Array: {arr5}, k: {k5}")
    print(f"Count of pairs: {count_pairs_with_diff_k(arr5, k5)}")
    print()

    # Test Case 6: Empty array
    arr6 = []
    k6 = 5
    print(f"Array: {arr6}, k: {k6}")
    print(f"Count of pairs: {count_pairs_with_diff_k(arr6, k6)}")

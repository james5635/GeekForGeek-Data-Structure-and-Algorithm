"""
Count Pairs with Sum Equal to K

Problem: Given an array of integers and a target sum k, count the number of
unique pairs (a, b) such that a + b = k.

Approach: Use a hash map to count frequencies. For each element, check how many
complements exist and handle duplicates carefully.

Time Complexity: O(n) - single pass through array
Space Complexity: O(n) - hash map for frequencies
"""

from collections import defaultdict


def count_pairs_with_sum_k(arr, k):
    """
    Count pairs (a, b) such that a + b = k.

    Args:
        arr: List of integers
        k: Target sum

    Returns:
        Count of valid pairs
    """
    if not arr or len(arr) < 2:
        return 0

    freq = defaultdict(int)
    count = 0

    for num in arr:
        complement = k - num
        count += freq[complement]
        freq[num] += 1

    return count


def count_pairs_unique_indices(arr, k):
    """
    Count pairs with unique indices (i, j) where i < j.

    Args:
        arr: List of integers
        k: Target sum

    Returns:
        Count of valid pairs with unique indices
    """
    return count_pairs_with_sum_k(arr, k)


def get_all_pairs_with_sum_k(arr, k):
    """
    Get all pairs (a, b) such that a + b = k.

    Args:
        arr: List of integers
        k: Target sum

    Returns:
        List of tuples containing pairs
    """
    if not arr or len(arr) < 2:
        return []

    freq = defaultdict(int)
    pairs = []

    for num in arr:
        complement = k - num

        # Add all pairs with this complement
        for _ in range(freq[complement]):
            pairs.append((complement, num))

        freq[num] += 1

    return pairs


def count_pairs_no_duplicates(arr, k):
    """
    Count unique pairs (unique values, not indices).

    Args:
        arr: List of integers
        k: Target sum

    Returns:
        Count of unique value pairs
    """
    if not arr or len(arr) < 2:
        return 0

    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1

    count = 0
    seen = set()

    for num in freq:
        if num in seen:
            continue

        complement = k - num

        if complement == num:
            # Same element pairs, need at least 2 occurrences
            if freq[num] >= 2:
                count += 1
        elif complement in freq and complement not in seen:
            count += 1

        seen.add(num)

    return count


if __name__ == "__main__":
    # Test Case 1: Basic case
    arr1 = [1, 5, 7, -1, 5]
    k1 = 6
    print(f"Array: {arr1}, k: {k1}")
    print(f"Count pairs: {count_pairs_with_sum_k(arr1, k1)}")
    print(f"All pairs: {get_all_pairs_with_sum_k(arr1, k1)}")
    print()

    # Test Case 2: No pairs
    arr2 = [1, 2, 3, 4]
    k2 = 10
    print(f"Array: {arr2}, k: {k2}")
    print(f"Count pairs: {count_pairs_with_sum_k(arr2, k2)}")
    print()

    # Test Case 3: Multiple same pairs
    arr3 = [1, 1, 1, 1]
    k3 = 2
    print(f"Array: {arr3}, k: {k3}")
    print(f"Count pairs: {count_pairs_with_sum_k(arr3, k3)}")
    print(f"All pairs: {get_all_pairs_with_sum_k(arr3, k3)}")
    print()

    # Test Case 4: Negative numbers
    arr4 = [-1, -2, 3, 4, 5]
    k4 = 3
    print(f"Array: {arr4}, k: {k4}")
    print(f"Count pairs: {count_pairs_with_sum_k(arr4, k4)}")
    print()

    # Test Case 5: Zero sum
    arr5 = [0, 0, 0, 0]
    k5 = 0
    print(f"Array: {arr5}, k: {k5}")
    print(f"Count pairs: {count_pairs_with_sum_k(arr5, k5)}")
    print()

    # Test Case 6: Empty array
    arr6 = []
    k6 = 5
    print(f"Array: {arr6}, k: {k6}")
    print(f"Count pairs: {count_pairs_with_sum_k(arr6, k6)}")
    print()

    # Test Case 7: Single element
    arr7 = [5]
    k7 = 10
    print(f"Array: {arr7}, k: {k7}")
    print(f"Count pairs: {count_pairs_with_sum_k(arr7, k7)}")
    print()

    # Test Case 8: Unique value pairs only
    arr8 = [1, 5, 7, -1, 5, 1]
    k8 = 6
    print(f"Array: {arr8}, k: {k8}")
    print(f"Count pairs (indices): {count_pairs_with_sum_k(arr8, k8)}")
    print(f"Count pairs (unique values): {count_pairs_no_duplicates(arr8, k8)}")
    print()

    # Test Case 9: Large array
    arr9 = list(range(1, 101))
    k9 = 101
    print(f"Array: 1 to 100, k: {k9}")
    print(f"Count pairs: {count_pairs_with_sum_k(arr9, k9)}")

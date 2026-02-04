"""
Sorted Subsequence of Size 3

Find a sorted subsequence of size 3 (i < j < k and arr[i] < arr[j] < arr[k]).

Approaches:
1. Naive: Check all triplets - O(n³) time, O(1) space
2. Better: Two arrays - O(n) time, O(n) space
3. Optimal: Single pass - O(n) time, O(1) space
"""


def find_sorted_subsequence_naive(arr):
    """
    Naive approach: Check all possible triplets.

    Time Complexity: O(n³)
    Space Complexity: O(1)

    Args:
        arr: List of integers

    Returns:
        Tuple of 3 indices (i, j, k) or None if not found
    """
    n = len(arr)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] < arr[j] < arr[k]:
                    return (i, j, k)

    return None


def find_sorted_subsequence_two_arrays(arr):
    """
    Better approach: Using smaller and greater arrays.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - smaller[i]: index of element smaller than arr[i] to its left
    - greater[i]: index of element greater than arr[i] to its right
    - Find i where both smaller[i] and greater[i] exist

    Args:
        arr: List of integers

    Returns:
        Tuple of 3 values (arr[i], arr[j], arr[k]) or None
    """
    n = len(arr)
    if n < 3:
        return None

    # smaller[i] stores index of element smaller than arr[i] on left
    smaller = [-1] * n
    min_idx = 0

    for i in range(1, n):
        if arr[i] <= arr[min_idx]:
            min_idx = i
            smaller[i] = -1
        else:
            smaller[i] = min_idx

    # greater[i] stores index of element greater than arr[i] on right
    greater = [-1] * n
    max_idx = n - 1

    for i in range(n - 2, -1, -1):
        if arr[i] >= arr[max_idx]:
            max_idx = i
            greater[i] = -1
        else:
            greater[i] = max_idx

    # Find index with both smaller and greater
    for i in range(n):
        if smaller[i] != -1 and greater[i] != -1:
            return (arr[smaller[i]], arr[i], arr[greater[i]])

    return None


def find_sorted_subsequence_optimal(arr):
    """
    Optimal approach: Single pass with two tracking variables.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Track first and second elements of potential subsequence
    - first: smallest element seen so far
    - second: element greater than first but smallest possible
    - When we find element > second, we have our subsequence

    Args:
        arr: List of integers

    Returns:
        Tuple of 3 values (first, second, third) or None
    """
    n = len(arr)
    if n < 3:
        return None

    first = second = float("inf")

    for num in arr:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            # Found third element greater than both
            return (first, second, num)

    return None


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [12, 11, 10, 5, 6, 2, 30],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [5, 6, 1, 2, 3],
        [1],
        [1, 2],
        [5, 1, 5, 5, 2, 5, 4],
        [3, 2, 1, 1, 2, 3],
    ]

    print("=" * 70)
    print("Sorted Subsequence of Size 3")
    print("=" * 70)
    print("\nFind i < j < k such that arr[i] < arr[j] < arr[k]\n")

    for i, arr in enumerate(test_cases, 1):
        print(f"Test {i}: arr = {arr}")

        naive_result = find_sorted_subsequence_naive(arr)
        two_array_result = find_sorted_subsequence_two_arrays(arr)
        optimal_result = find_sorted_subsequence_optimal(arr)

        print(f"  Naive O(n³):          {naive_result}")
        print(f"  Two Arrays O(n):      {two_array_result}")
        print(f"  Optimal O(1) space:   {optimal_result}")
        print()

    print("=" * 70)
    print("\nOptimal Approach Explanation:")
    print("  - first:  smallest element seen so far")
    print("  - second: element greater than first but smallest possible")
    print("  - When we find num > second, we have our triplet")
    print("\n  This works because we greedily keep the smallest valid pair,")
    print("  maximizing chances of finding a valid third element.")
    print("=" * 70)

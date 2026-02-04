"""
Smallest Subarray with Sum Greater Than X

Given an array of integers and a number x, find the smallest subarray
with sum greater than x.

Approaches:
1. Naive: Try all subarrays - O(n²) time, O(1) space
2. Optimal: Sliding Window - O(n) time, O(1) space
"""


def smallest_subarray_naive(arr, x):
    """
    Naive approach: Try all possible subarrays.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each starting index, extend subarray to the right
    - Track minimum length where sum > x

    Args:
        arr: List of positive integers
        x: Target sum threshold

    Returns:
        Minimum length of subarray with sum > x, or -1 if not found
    """
    n = len(arr)
    min_len = float("inf")

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > x:
                min_len = min(min_len, j - i + 1)
                break  # Further elements will only increase sum

    return min_len if min_len != float("inf") else -1


def smallest_subarray_sliding_window(arr, x):
    """
    Optimal approach: Sliding Window (Two Pointers).

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Use two pointers: start and end
    - Expand window by moving end, add to current_sum
    - When current_sum > x, shrink from start to find smaller window
    - Track minimum length throughout

    Key Insight:
    Since all numbers are positive, when sum exceeds x, we can try
    to shrink from left to potentially find a smaller valid window.

    Args:
        arr: List of positive integers
        x: Target sum threshold

    Returns:
        Minimum length of subarray with sum > x, or -1 if not found
    """
    n = len(arr)
    if n == 0:
        return -1

    min_len = float("inf")
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        # Shrink window while sum is still > x
        while current_sum > x:
            min_len = min(min_len, end - start + 1)
            current_sum -= arr[start]
            start += 1

    return min_len if min_len != float("inf") else -1


def smallest_subarray_with_indices(arr, x):
    """
    Sliding Window with start and end indices.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Returns:
        Tuple of (min_length, start_index, end_index)
    """
    n = len(arr)
    if n == 0:
        return -1, -1, -1

    min_len = float("inf")
    current_sum = 0
    start = 0
    best_start = best_end = -1

    for end in range(n):
        current_sum += arr[end]

        while current_sum > x:
            if end - start + 1 < min_len:
                min_len = end - start + 1
                best_start = start
                best_end = end
            current_sum -= arr[start]
            start += 1

    if min_len == float("inf"):
        return -1, -1, -1

    return min_len, best_start, best_end


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 4, 45, 6, 0, 19], 51),
        ([1, 10, 5, 2, 7], 9),
        ([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280),
        ([1, 2, 4], 8),
        ([5], 3),
        ([5], 10),
        ([1, 2, 3, 4, 5], 10),
    ]

    print("=" * 70)
    print("Smallest Subarray with Sum Greater Than X")
    print("=" * 70)
    print("\nFind minimum length subarray with sum > x.\n")

    for i, (arr, x) in enumerate(test_cases, 1):
        naive_result = smallest_subarray_naive(arr, x)
        sliding_result = smallest_subarray_sliding_window(arr, x)
        indices_result = smallest_subarray_with_indices(arr, x)

        match = "✓" if naive_result == sliding_result == indices_result[0] else "✗"

        print(f"Test {i}: arr = {arr}, x = {x}")
        print(f"  Naive O(n²):              {naive_result}")
        print(f"  Sliding Window O(n):      {sliding_result}")
        if indices_result[0] != -1:
            subarray = arr[indices_result[1] : indices_result[2] + 1]
            subarray_sum = sum(subarray)
            print(
                f"  Subarray:                 {subarray} (sum = {subarray_sum}) {match}"
            )
        else:
            print(f"  Subarray:                 Not found {match}")
        print()

    print("=" * 70)
    print("\nSliding Window Explanation:")
    print("  1. Expand window by moving 'end' pointer")
    print("  2. When sum > x, try to shrink from 'start'")
    print("  3. Track minimum valid window length")
    print("\n  Time: O(n), Space: O(1)")
    print("  Note: Works only for positive numbers")
    print("=" * 70)

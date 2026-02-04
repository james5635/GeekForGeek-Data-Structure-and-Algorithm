"""
Maximum Subarray Sum (Kadane's Algorithm)

Find the largest sum contiguous subarray.

Approaches:
1. Naive: Check all subarrays - O(n²) time, O(1) space
2. Optimal: Kadane's Algorithm - O(n) time, O(1) space
"""


def max_subarray_sum_naive(arr):
    """
    Naive approach: Check all possible subarrays.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each starting index, extend subarray to the right
    - Track maximum sum encountered

    Args:
        arr: List of integers

    Returns:
        Maximum sum of any contiguous subarray
    """
    n = len(arr)
    max_sum = float("-inf")

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_sum_kadane(arr):
    """
    Optimal approach: Kadane's Algorithm.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Initialize max_so_far and max_ending_here with first element
    - For each element, decide whether to:
      a) Extend the existing subarray (max_ending_here + arr[i])
      b) Start new subarray from current element (arr[i])
    - Update max_so_far if max_ending_here is greater

    Key Insight:
    At each position, we track the maximum sum ending at that position.
    Either we extend the previous subarray or start fresh.

    Args:
        arr: List of integers

    Returns:
        Maximum sum of any contiguous subarray
    """
    if not arr:
        return 0

    max_so_far = max_ending_here = arr[0]

    for i in range(1, len(arr)):
        # Either extend existing subarray or start new
        max_ending_here = max(arr[i], max_ending_here + arr[i])

        # Update global maximum
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def max_subarray_sum_kadane_with_indices(arr):
    """
    Kadane's Algorithm with start and end indices.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Returns:
        Tuple of (max_sum, start_index, end_index)
    """
    if not arr:
        return 0, -1, -1

    max_so_far = max_ending_here = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if max_ending_here + arr[i] < arr[i]:
            # Start new subarray
            max_ending_here = arr[i]
            s = i
        else:
            # Extend existing
            max_ending_here += arr[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return max_so_far, start, end


def max_subarray_sum_divide_conquer(arr, left, right):
    """
    Divide and Conquer approach.

    Time Complexity: O(n log n)
    Space Complexity: O(log n) for recursion

    Algorithm:
    - Divide array into two halves
    - Max subarray can be in:
      a) Left half
      b) Right half
      c) Crossing the midpoint

    Args:
        arr: List of integers
        left: Left index
        right: Right index

    Returns:
        Maximum sum of any contiguous subarray
    """
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    # Max in left half
    left_max = max_subarray_sum_divide_conquer(arr, left, mid)

    # Max in right half
    right_max = max_subarray_sum_divide_conquer(arr, mid + 1, right)

    # Max crossing the midpoint
    cross_max = max_crossing_sum(arr, left, mid, right)

    return max(left_max, right_max, cross_max)


def max_crossing_sum(arr, left, mid, right):
    """Helper for divide and conquer approach."""
    # Sum from mid to left
    left_sum = float("-inf")
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]
        left_sum = max(left_sum, current_sum)

    # Sum from mid+1 to right
    right_sum = float("-inf")
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += arr[i]
        right_sum = max(right_sum, current_sum)

    return left_sum + right_sum


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [-2, -3, 4, -1, -2, 1, 5, -3],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [5],
        [-5],
        [1, -1, 1, -1, 1],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    ]

    print("=" * 70)
    print("Maximum Subarray Sum (Kadane's Algorithm)")
    print("=" * 70)
    print("\nFind contiguous subarray with maximum sum.\n")

    for i, arr in enumerate(test_cases, 1):
        naive_result = max_subarray_sum_naive(arr)
        kadane_result = max_subarray_sum_kadane(arr)
        kadane_indices = max_subarray_sum_kadane_with_indices(arr)

        match = "✓" if naive_result == kadane_result == kadane_indices[0] else "✗"

        print(f"Test {i}: arr = {arr}")
        print(f"  Naive O(n²):              {naive_result}")
        print(f"  Kadane's O(n):            {kadane_result}")
        print(
            f"  Kadane's with indices:    sum={kadane_indices[0]}, "
            f"subarray=arr[{kadane_indices[1]}:{kadane_indices[2]}+1] "
            f"= {arr[kadane_indices[1] : kadane_indices[2] + 1]} {match}"
        )
        print()

    print("=" * 70)
    print("\nKadane's Algorithm Explanation:")
    print("  At each position i, decide:")
    print("    - Extend previous subarray: max_ending_here + arr[i]")
    print("    - Start new subarray: arr[i]")
    print("  Keep track of maximum sum seen so far.")
    print("\n  Time: O(n), Space: O(1)")
    print("=" * 70)

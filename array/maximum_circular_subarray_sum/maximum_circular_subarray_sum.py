"""
Maximum Circular Subarray Sum

Given an array arr[] of N integers arranged in a circular fashion.
Find the maximum subarray sum.

Approaches:
1. Naive: O(n²) - Check all circular subarrays
2. Optimal: O(n) - Kadane's for normal and total - min_subarray_sum
"""


def kadane_normal(arr):
    """
    Helper: Kadane's algorithm for normal (non-circular) subarray.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of integers

    Returns:
        Maximum sum of normal subarray
    """
    if not arr:
        return 0

    max_so_far = max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def kadane_inverted(arr):
    """
    Helper: Kadane's algorithm for minimum subarray sum.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of integers

    Returns:
        Minimum sum of subarray
    """
    if not arr:
        return 0

    min_so_far = min_ending_here = arr[0]

    for i in range(1, len(arr)):
        min_ending_here = min(arr[i], min_ending_here + arr[i])
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far


def max_circular_subarray_sum_naive(arr):
    """
    Naive approach: Check all possible circular subarrays.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each starting position
    - Extend subarray considering circular wrapping
    - Track maximum sum

    Args:
        arr: List of integers in circular arrangement

    Returns:
        Maximum circular subarray sum
    """
    n = len(arr)
    if n == 0:
        return 0

    max_sum = float("-inf")

    for i in range(n):
        current_sum = 0
        for j in range(n):
            # Wrap around using modulo
            idx = (i + j) % n
            current_sum += arr[idx]
            max_sum = max(max_sum, current_sum)

    return max_sum


def max_circular_subarray_sum_optimal(arr):
    """
    Optimal approach: Using Kadane's algorithm.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    1. Find max subarray sum using Kadane's (normal case)
    2. Find total sum of array
    3. Find min subarray sum using Kadane's on inverted values
    4. Circular max = total_sum - min_subarray_sum
    5. Result = max(normal_max, circular_max)

    Special Case:
    - If all numbers are negative, return max element

    Args:
        arr: List of integers in circular arrangement

    Returns:
        Maximum circular subarray sum
    """
    n = len(arr)
    if n == 0:
        return 0

    # Case 1: Maximum sum using normal Kadane's (non-circular)
    max_kadane = kadane_normal(arr)

    # Case 2: Maximum sum that includes wrapping
    # Sum of array - minimum subarray sum = maximum circular sum
    total_sum = sum(arr)
    min_kadane = kadane_inverted(arr)

    # If all elements are negative, max_kadane will be the max element
    # and total_sum - min_kadane will be 0 (which is incorrect for all negative)
    # So we need to handle this case
    if max_kadane < 0:
        return max_kadane

    max_circular = total_sum - min_kadane

    # Return maximum of two cases
    return max(max_kadane, max_circular)


def max_circular_subarray_sum_all_approaches(arr):
    """
    Complete solution with all cases handled.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of integers

    Returns:
        Tuple of (normal_max, circular_max, overall_max)
    """
    n = len(arr)
    if n == 0:
        return 0, 0, 0
    if n == 1:
        return arr[0], arr[0], arr[0]

    # Normal Kadane's
    max_kadane = kadane_normal(arr)

    # Total sum
    total_sum = sum(arr)

    # Min subarray sum
    min_kadane = kadane_inverted(arr)

    # All negative case
    if max_kadane < 0:
        return max_kadane, max_kadane, max_kadane

    # Circular case
    max_circular = total_sum - min_kadane

    overall_max = max(max_kadane, max_circular)

    return max_kadane, max_circular, overall_max


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (array, description)
        ([8, -8, 9, -9, 10, -11, 12], "Mixed positive/negative"),
        ([10, -3, -4, 7, 6, 5, -4, -1], "Another mixed case"),
        ([-1, 40, -14, 7, 6, 5, -4, -1], "Starting with negative"),
        ([-1, -2, -3, -4], "All negative"),
        ([1, 2, 3, 4, 5], "All positive"),
        ([5, -2, 3, 4], "Simple case"),
        ([-2], "Single element negative"),
        ([5], "Single element positive"),
        ([8, -1, 3, 4], "Optimal uses circular"),
        ([-8, -1, -3, -4], "All negative small"),
    ]

    print("=" * 70)
    print("Maximum Circular Subarray Sum")
    print("=" * 70)

    for i, (arr, desc) in enumerate(test_cases, 1):
        naive_result = max_circular_subarray_sum_naive(arr)
        optimal_result = max_circular_subarray_sum_optimal(arr)
        normal_kadane, circular, overall = max_circular_subarray_sum_all_approaches(arr)

        match = naive_result == optimal_result

        print(f"\nTest {i}: {desc}")
        print(f"  Array: {arr}")
        print(f"  Naive O(n²):          {naive_result}")
        print(f"  Optimal O(n):         {optimal_result} {'✓' if match else '✗'}")
        print(f"  Normal Kadane:        {normal_kadane}")
        print(f"  Circular (total-min): {circular}")
        print(f"  Overall Maximum:      {overall}")

    print("\n" + "=" * 70)
    print("\nAlgorithm Explanation:")
    print("\n1. Naive Approach O(n²):")
    print("   - For each starting position i")
    print("   - Extend subarray to the right (circular wrapping)")
    print("   - Track maximum sum across all subarrays")
    print("\n2. Optimal Approach O(n):")
    print("   - Case 1: Maximum subarray is non-circular")
    print("     → Use normal Kadane's algorithm")
    print("   - Case 2: Maximum subarray wraps around")
    print("     → Max circular = Total Sum - Minimum Subarray Sum")
    print("   - Result: max(Case 1, Case 2)")
    print("\n3. Special Case - All Negative:")
    print("   - If all numbers are negative, return max element")
    print("   - total_sum - min_kadane would give 0 (wrong)")
    print("\nKey Insight: Circular max = Total - Minimum subarray")
    print("=" * 70)

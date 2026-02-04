"""
Subarray with Given Sum (Positive Numbers)

Given an array of positive integers and a target sum,
find a contiguous subarray that sums to the target.

Approaches:
1. Naive: Try all subarrays - O(n²) time, O(1) space
2. Optimal: Sliding Window - O(n) time, O(1) space
"""


def subarray_with_sum_naive(arr, target):
    """
    Naive approach: Try all possible subarrays.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each starting index, extend subarray and check sum
    - Return indices when sum equals target

    Args:
        arr: List of positive integers
        target: Target sum to find

    Returns:
        Tuple of (start_index, end_index) or (-1, -1) if not found
    """
    n = len(arr)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target:
                return i, j
            elif current_sum > target:
                break  # Can't extend further (all positive)

    return -1, -1


def subarray_with_sum_sliding_window(arr, target):
    """
    Optimal approach: Sliding Window.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Maintain a window [start, end]
    - Expand by adding arr[end] to current_sum
    - Shrink from start if current_sum > target
    - Return when current_sum == target

    Key Insight:
    Since all numbers are positive:
    - Adding elements increases sum
    - Removing elements decreases sum
    - We can adjust window size dynamically

    Args:
        arr: List of positive integers
        target: Target sum to find

    Returns:
        Tuple of (start_index, end_index) or (-1, -1) if not found
    """
    n = len(arr)
    if n == 0:
        return -1, -1

    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        # Shrink window while sum exceeds target
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            return start, end

    return -1, -1


def subarray_with_sum_prefix_hash(arr, target):
    """
    Alternative: Prefix Sum with Hash Map (works with negatives too).

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    - Store prefix sums in hash map
    - If prefix_sum - target exists in map, we found subarray
    - This works for arrays with negative numbers too
    """
    prefix_sum = 0
    prefix_map = {0: -1}  # prefix_sum 0 at index -1

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum - target in prefix_map:
            return prefix_map[prefix_sum - target] + 1, i

        prefix_map[prefix_sum] = i

    return -1, -1


def find_all_subarrays_with_sum(arr, target):
    """
    Find all subarrays with given sum.

    Time Complexity: O(n) for positive numbers
    Returns list of (start, end) tuples
    """
    n = len(arr)
    result = []
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1

        if current_sum == target:
            result.append((start, end))

    return result


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 4, 20, 3, 10, 5], 33),
        ([1, 4, 0, 0, 3, 10, 5], 7),
        ([1, 4], 0),
        ([1, 2, 3, 4, 5], 9),
        ([1, 2, 3, 8], 8),
        ([5, 5, 5, 5], 10),
        ([1, 2, 3, 4, 5], 15),
        ([1, 2, 3, 4, 5], 100),
    ]

    print("=" * 70)
    print("Subarray with Given Sum (Positive Numbers)")
    print("=" * 70)
    print("\nFind contiguous subarray with sum equal to target.\n")

    for i, (arr, target) in enumerate(test_cases, 1):
        naive_result = subarray_with_sum_naive(arr, target)
        sliding_result = subarray_with_sum_sliding_window(arr, target)
        hash_result = subarray_with_sum_prefix_hash(arr, target)

        match = "✓" if naive_result == sliding_result == hash_result else "✗"

        print(f"Test {i}: arr = {arr}, target = {target}")
        if sliding_result[0] != -1:
            subarray = arr[sliding_result[0] : sliding_result[1] + 1]
            subarray_sum = sum(subarray)
            print(f"  Subarray found:           indices {sliding_result}")
            print(
                f"  Subarray:                 {subarray} (sum = {subarray_sum}) {match}"
            )
        else:
            print(f"  Result:                   No subarray found {match}")
        print()

    # Test finding all subarrays
    print("=" * 70)
    print("\nAll subarrays with sum = 5 in [1, 2, 3, 4, 5]:")
    all_subarrays = find_all_subarrays_with_sum([1, 2, 3, 4, 5], 5)
    for start, end in all_subarrays:
        subarray = [1, 2, 3, 4, 5][start : end + 1]
        print(f"  indices ({start}, {end}): {subarray}")

    print("\n" + "=" * 70)
    print("\nSliding Window Explanation:")
    print("  1. Expand window by moving 'end' pointer")
    print("  2. If current_sum > target, shrink from 'start'")
    print("  3. If current_sum == target, found the subarray")
    print("\n  Time: O(n), Space: O(1)")
    print("  Note: Only works for positive numbers")
    print("=" * 70)

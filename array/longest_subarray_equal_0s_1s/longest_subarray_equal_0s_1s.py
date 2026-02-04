"""
Longest Subarray with Equal 0s and 1s

Given a binary array, find the length of the longest subarray with
equal number of 0s and 1s.

Approach:
- Convert 0s to -1s
- Use prefix sum with hash map
- Optimal: O(n) time, O(n) space

Key Insight:
If prefix_sum[j] == prefix_sum[i], then subarray (i+1, j) has equal 0s and 1s
"""


def longest_subarray_equal_naive(arr):
    """
    Naive approach: Try all subarrays and count 0s and 1s.

    Time Complexity: O(n²)
    Space Complexity: O(1)

    Algorithm:
    - For each starting index, extend subarray
    - Count 0s and 1s in each subarray
    - Track maximum length where count_0 == count_1

    Args:
        arr: Binary array (0s and 1s)

    Returns:
        Maximum length of subarray with equal 0s and 1s
    """
    n = len(arr)
    max_len = 0

    for i in range(n):
        count_0 = 0
        count_1 = 0
        for j in range(i, n):
            if arr[j] == 0:
                count_0 += 1
            else:
                count_1 += 1

            if count_0 == count_1:
                max_len = max(max_len, j - i + 1)

    return max_len


def longest_subarray_equal_prefix_sum(arr):
    """
    Optimal approach: Prefix Sum with Hash Map.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    1. Convert 0s to -1s (or treat 0 as -1 in calculation)
    2. Compute prefix sum
    3. If prefix_sum[j] == prefix_sum[i], subarray (i+1, j) sums to 0
       → equal number of 0s and 1s
    4. Use hash map to store first occurrence of each prefix sum

    Key Insight:
    - Treat 0 as -1, then equal 0s and 1s means sum = 0
    - If same prefix sum appears at i and j, subarray (i+1, j) has sum = 0

    Args:
        arr: Binary array (0s and 1s)

    Returns:
        Maximum length of subarray with equal 0s and 1s
    """
    n = len(arr)
    if n == 0:
        return 0

    max_len = 0
    prefix_sum = 0
    # Map prefix_sum to its first occurrence index
    prefix_map = {0: -1}  # prefix_sum 0 at index -1

    for i in range(n):
        # Treat 0 as -1, 1 as +1
        prefix_sum += 1 if arr[i] == 1 else -1

        if prefix_sum in prefix_map:
            # Found subarray with equal 0s and 1s
            length = i - prefix_map[prefix_sum]
            max_len = max(max_len, length)
        else:
            # Store first occurrence
            prefix_map[prefix_sum] = i

    return max_len


def longest_subarray_equal_with_indices(arr):
    """
    Prefix Sum approach with start and end indices.

    Returns:
        Tuple of (max_length, start_index, end_index)
    """
    n = len(arr)
    if n == 0:
        return 0, -1, -1

    max_len = 0
    prefix_sum = 0
    prefix_map = {0: -1}
    best_start = best_end = -1

    for i in range(n):
        prefix_sum += 1 if arr[i] == 1 else -1

        if prefix_sum in prefix_map:
            length = i - prefix_map[prefix_sum]
            if length > max_len:
                max_len = length
                best_start = prefix_map[prefix_sum] + 1
                best_end = i
        else:
            prefix_map[prefix_sum] = i

    return max_len, best_start, best_end


def longest_subarray_equal_alternative(arr):
    """
    Alternative: Explicit conversion to -1 and 1.

    Same logic but more explicit transformation.
    """
    n = len(arr)
    if n == 0:
        return 0

    # Convert to -1 and 1
    transformed = [-1 if x == 0 else 1 for x in arr]

    max_len = 0
    prefix_sum = 0
    prefix_map = {0: -1}

    for i in range(n):
        prefix_sum += transformed[i]

        if prefix_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum])
        else:
            prefix_map[prefix_sum] = i

    return max_len


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 1],
        [1, 0],
        [0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0, 1, 1],
        [],
        [0],
        [1],
    ]

    print("=" * 70)
    print("Longest Subarray with Equal 0s and 1s")
    print("=" * 70)
    print("\nFind longest contiguous subarray with equal count of 0s and 1s.\n")

    for i, arr in enumerate(test_cases, 1):
        naive_result = longest_subarray_equal_naive(arr)
        prefix_result = longest_subarray_equal_prefix_sum(arr)
        indices_result = longest_subarray_equal_with_indices(arr)
        alt_result = longest_subarray_equal_alternative(arr)

        match = (
            "✓"
            if naive_result == prefix_result == alt_result == indices_result[0]
            else "✗"
        )

        print(f"Test {i}: arr = {arr}")
        print(f"  Naive O(n²):              {naive_result}")
        print(f"  Prefix Sum O(n):          {prefix_result}")
        if indices_result[0] > 0:
            subarray = arr[indices_result[1] : indices_result[2] + 1]
            count_0 = subarray.count(0)
            count_1 = subarray.count(1)
            print(f"  Subarray:                 {subarray}")
            print(
                f"  Indices:                  ({indices_result[1]}, {indices_result[2]})"
            )
            print(f"  Count 0s:                 {count_0}, Count 1s: {count_1} {match}")
        else:
            print(f"  Result:                   No valid subarray {match}")
        print()

    print("=" * 70)
    print("\nPrefix Sum with Hash Map Explanation:")
    print("  1. Convert: Treat 0 as -1, 1 as +1")
    print("  2. Compute prefix sum at each index")
    print("  3. If prefix_sum repeats at i and j:")
    print("     → Subarray (i+1, j) has sum = 0")
    print("     → Equal number of 0s and 1s")
    print("  4. Use hash map to store first occurrence")
    print("\n  Time: O(n), Space: O(n)")
    print("=" * 70)

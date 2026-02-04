"""
Longest Common Span with Same Sum in Two Binary Arrays

Given two binary arrays of same size, find the longest common span (i, j)
where both arrays have the same sum in the subarray arr1[i..j] and arr2[i..j].

Approach:
- Treat 0 as -1 for both arrays
- Compute difference of prefix sums
- Longest subarray with sum 0 in difference array
- Optimal: O(n) time, O(n) space
"""


def longest_common_span_naive(arr1, arr2):
    """
    Naive approach: Try all subarrays in both arrays.

    Time Complexity: O(n³)
    Space Complexity: O(1)

    Algorithm:
    - For each possible subarray in arr1
    - Check if same subarray in arr2 has same sum
    - Track maximum length

    Args:
        arr1: First binary array
        arr2: Second binary array

    Returns:
        Maximum length of common span with same sum
    """
    n = len(arr1)
    max_len = 0

    for i in range(n):
        for j in range(i, n):
            sum1 = sum(arr1[i : j + 1])
            sum2 = sum(arr2[i : j + 1])

            if sum1 == sum2:
                max_len = max(max_len, j - i + 1)

    return max_len


def longest_common_span_prefix_diff(arr1, arr2):
    """
    Optimal approach: Prefix Sum Difference with Hash Map.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Algorithm:
    1. Convert 0s to -1s (or treat 0 as -1)
    2. Compute prefix sum for both arrays
    3. Create difference array: diff[i] = prefix1[i] - prefix2[i]
    4. Find longest subarray in diff with sum 0
       → Same as longest subarray with equal sum in both

    Key Insight:
    If prefix1[j] - prefix1[i] = prefix2[j] - prefix2[i]
    Then prefix1[j] - prefix2[j] = prefix1[i] - prefix2[i]
    So we need to find equal values in the difference of prefix sums

    Args:
        arr1: First binary array
        arr2: Second binary array

    Returns:
        Maximum length of common span with same sum
    """
    n = len(arr1)
    if n == 0 or len(arr2) != n:
        return 0

    max_len = 0
    prefix_sum_diff = 0
    # Map difference value to its first occurrence index
    diff_map = {0: -1}

    for i in range(n):
        # Treat 0 as -1, 1 as +1
        val1 = 1 if arr1[i] == 1 else -1
        val2 = 1 if arr2[i] == 1 else -1

        prefix_sum_diff += val1 - val2

        if prefix_sum_diff in diff_map:
            # Found common span
            length = i - diff_map[prefix_sum_diff]
            max_len = max(max_len, length)
        else:
            # Store first occurrence
            diff_map[prefix_sum_diff] = i

    return max_len


def longest_common_span_with_indices(arr1, arr2):
    """
    Prefix Sum Difference approach with start and end indices.

    Returns:
        Tuple of (max_length, start_index, end_index)
    """
    n = len(arr1)
    if n == 0 or len(arr2) != n:
        return 0, -1, -1

    max_len = 0
    prefix_sum_diff = 0
    diff_map = {0: -1}
    best_start = best_end = -1

    for i in range(n):
        val1 = 1 if arr1[i] == 1 else -1
        val2 = 1 if arr2[i] == 1 else -1

        prefix_sum_diff += val1 - val2

        if prefix_sum_diff in diff_map:
            length = i - diff_map[prefix_sum_diff]
            if length > max_len:
                max_len = length
                best_start = diff_map[prefix_sum_diff] + 1
                best_end = i
        else:
            diff_map[prefix_sum_diff] = i

    return max_len, best_start, best_end


def longest_common_span_alternative(arr1, arr2):
    """
    Alternative: Create explicit difference array first.

    Same logic but more explicit steps.
    """
    n = len(arr1)
    if n == 0 or len(arr2) != n:
        return 0

    # Create difference array (treating 0 as -1)
    diff = []
    for i in range(n):
        val1 = 1 if arr1[i] == 1 else -1
        val2 = 1 if arr2[i] == 1 else -1
        diff.append(val1 - val2)

    # Find longest subarray with sum 0 in diff
    max_len = 0
    prefix_sum = 0
    prefix_map = {0: -1}

    for i in range(n):
        prefix_sum += diff[i]

        if prefix_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum])
        else:
            prefix_map[prefix_sum] = i

    return max_len


def verify_common_span(arr1, arr2, start, end):
    """
    Verify that subarrays arr1[start..end] and arr2[start..end] have same sum.

    Returns:
        True if sums are equal, False otherwise
    """
    if start < 0 or end >= len(arr1) or end >= len(arr2):
        return False

    sum1 = sum(arr1[start : end + 1])
    sum2 = sum(arr2[start : end + 1])

    return sum1 == sum2


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1]),
        ([0, 0, 1, 0], [1, 1, 1, 1]),
        ([0, 0, 0, 0], [1, 1, 1, 1]),
        ([0, 1, 0, 1, 0], [1, 0, 1, 0, 1]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0, 1], [0, 1, 0]),
        ([], []),
        ([1], [0]),
        ([0, 1], [1, 0]),
    ]

    print("=" * 70)
    print("Longest Common Span with Same Sum in Two Binary Arrays")
    print("=" * 70)
    print("\nFind longest span (i, j) where both arrays have same sum in arr[i..j].\n")

    for i, (arr1, arr2) in enumerate(test_cases, 1):
        naive_result = longest_common_span_naive(arr1, arr2)
        prefix_result = longest_common_span_prefix_diff(arr1, arr2)
        indices_result = longest_common_span_with_indices(arr1, arr2)
        alt_result = longest_common_span_alternative(arr1, arr2)

        match = (
            "✓"
            if naive_result == prefix_result == alt_result == indices_result[0]
            else "✗"
        )

        print(f"Test {i}:")
        print(f"  arr1 = {arr1}")
        print(f"  arr2 = {arr2}")
        print(f"  Naive O(n³):              {naive_result}")
        print(f"  Prefix Diff O(n):         {prefix_result}")

        if indices_result[0] > 0:
            subarr1 = arr1[indices_result[1] : indices_result[2] + 1]
            subarr2 = arr2[indices_result[1] : indices_result[2] + 1]
            sum1 = sum(subarr1)
            sum2 = sum(subarr2)
            print(
                f"  Span:                     indices ({indices_result[1]}, {indices_result[2]})"
            )
            print(f"  arr1 span:                {subarr1} (sum = {sum1})")
            print(f"  arr2 span:                {subarr2} (sum = {sum2}) {match}")
        else:
            print(f"  Result:                   No common span found {match}")
        print()

    print("=" * 70)
    print("\nPrefix Sum Difference Explanation:")
    print("  1. Treat 0 as -1 for both arrays")
    print("  2. Compute prefix sum difference: diff[i] = prefix1[i] - prefix2[i]")
    print("  3. If diff[j] == diff[i], then subarrays (i+1, j) have equal sums")
    print("  4. Use hash map to find longest such span")
    print("\n  Key Insight: Equal prefix difference means equal subarray sums")
    print("  Time: O(n), Space: O(n)")
    print("=" * 70)

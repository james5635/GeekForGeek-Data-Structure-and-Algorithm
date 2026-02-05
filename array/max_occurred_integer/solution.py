"""
Maximum Occurred Integer in N Ranges
=====================================

Problem:
    Given n ranges of the form L[i] to R[i], find the maximum occurred integer
    in all these ranges. If multiple integers have the same maximum occurrence,
    return the smallest one.

Approach:
    Use prefix sum technique (difference array).
    For each range [L, R], increment count[L] and decrement count[R+1].
    Then compute prefix sum to get actual frequencies.
    Track the maximum frequency.

Time Complexity: O(n + max_val) where n is number of ranges, max_val is max range value
Space Complexity: O(max_val) for the frequency array
"""


def max_occurred_integer(L, R):
    """
    Find maximum occurred integer in given ranges.

    Args:
        L: List of left boundaries of ranges
        R: List of right boundaries of ranges

    Returns:
        Integer with maximum occurrence
    """
    n = len(L)
    if n == 0:
        return None

    # Find maximum value to size array
    max_val = max(R)

    # Difference array
    freq = [0] * (max_val + 2)

    # Apply difference array technique
    for i in range(n):
        freq[L[i]] += 1
        freq[R[i] + 1] -= 1

    # Compute prefix sum and find maximum
    max_count = freq[0]
    result = 0

    for i in range(1, max_val + 1):
        freq[i] += freq[i - 1]
        if freq[i] > max_count:
            max_count = freq[i]
            result = i

    return result


def max_occurred_with_count(L, R):
    """
    Return both the integer and its occurrence count.
    """
    n = len(L)
    if n == 0:
        return None, 0

    max_val = max(R)
    freq = [0] * (max_val + 2)

    for i in range(n):
        freq[L[i]] += 1
        freq[R[i] + 1] -= 1

    max_count = freq[0]
    result = 0

    for i in range(1, max_val + 1):
        freq[i] += freq[i - 1]
        if freq[i] > max_count:
            max_count = freq[i]
            result = i

    return result, max_count


if __name__ == "__main__":
    # Test Case 1: Basic case
    L = [1, 4, 3, 1]
    R = [15, 8, 5, 4]
    result = max_occurred_integer(L, R)
    print(f"Test 1: {result}")  # Expected: 4 (appears in all 4 ranges)

    # Test Case 2: Overlapping ranges
    L = [1, 2, 3]
    R = [3, 5, 7]
    result = max_occurred_integer(L, R)
    print(f"Test 2: {result}")  # Expected: 3 (appears in all 3 ranges)

    # Test Case 3: Single range
    L = [1]
    R = [10]
    result = max_occurred_integer(L, R)
    print(f"Test 3: {result}")  # Expected: 1 (smallest in range)

    # Test Case 4: Non-overlapping ranges
    L = [1, 5, 9]
    R = [3, 7, 11]
    result = max_occurred_integer(L, R)
    print(f"Test 4: {result}")  # Expected: 1 (or 5 or 9, all appear once)

    # Test Case 5: All same range
    L = [1, 1, 1, 1]
    R = [5, 5, 5, 5]
    result = max_occurred_integer(L, R)
    result_count = max_occurred_with_count(L, R)
    print(f"Test 5: {result}, Count: {result_count}")  # Expected: 1 with count 4

    # Test Case 6: Large ranges
    L = [1, 1, 1]
    R = [100, 100, 100]
    result = max_occurred_integer(L, R)
    print(f"Test 6: {result}")  # Expected: 1

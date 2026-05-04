"""
Maximum value of Sum(i*arr[i]) with array rotations allowed.

Given an array arr[], find the maximum possible value of the expression
i*arr[i] after rotating the array any number of times (including zero).

In each rotation, every element shifts one position to the right, and
the last element moves to the front.

Algorithm:
    The key insight is that we can compute the sum for the next rotation
    from the previous rotation without recalculating from scratch.

    Let R_j be the sum after j rotations:
        R_j = R_{j-1} + totalSum - n * arr[n-j]

    Where totalSum is the sum of all array elements.

    This allows us to find the maximum in O(n) time instead of O(n^2).

Time Complexity: O(n)
Space Complexity: O(1)
"""


def max_rotate_sum(arr):
    """Find the maximum value of Sum(i*arr[i]) after any number of rotations.

    Args:
        arr: List of integers

    Returns:
        Maximum possible value of Sum(i*arr[i]) across all rotations
    """
    n = len(arr)
    if n == 0:
        return 0

    total_sum = 0
    curr_val = 0

    for i in range(n):
        total_sum += arr[i]
        curr_val += i * arr[i]

    max_val = curr_val

    for j in range(1, n):
        curr_val = curr_val + total_sum - n * arr[n - j]
        max_val = max(max_val, curr_val)

    return max_val


if __name__ == "__main__":
    test_cases = [
        ([4, 3, 2, 6, 1, 5], 60),
        ([8, 3, 1, 2], 29),
        ([10, 1, 2, 7, 9, 3], 105),
        ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 330),
        ([1, 2, 3], 8),
        ([5], 0),
        ([], 0),
    ]

    for arr, expected in test_cases:
        result = max_rotate_sum(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: arr={arr}, expected={expected}, got={result}")

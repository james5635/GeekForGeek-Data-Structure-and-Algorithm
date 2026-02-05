"""
Find a Repeating and a Missing Number

Problem Description:
Given an unsorted array of size n with distinct elements in range [1, n],
find one repeating number and one missing number.

Example:
    Input: [4, 3, 6, 2, 1, 1]
    Output: (1, 5)  # 1 is repeating, 5 is missing

Time Complexity: O(n)
Space Complexity: O(1)

Approach: Mathematical equations using sum and sum of squares
    Let x = repeating number, y = missing number
    Sum difference: x - y = sum(arr) - n*(n+1)/2
    Squares difference: x² - y² = sum(arr²) - n*(n+1)(2n+1)/6
    Solve: x + y = (x² - y²) / (x - y)
    Then: x = (diff_sum + diff_squares/diff_sum) / 2
          y = x - diff_sum
"""


def find_repeating_and_missing(arr):
    """
    Find one repeating and one missing number in array.

    Args:
        arr: List of integers from 1 to n with one repeat and one missing

    Returns:
        Tuple of (repeating_number, missing_number)
    """
    n = len(arr)

    # Calculate expected sums
    expected_sum = n * (n + 1) // 2
    expected_square_sum = n * (n + 1) * (2 * n + 1) // 6

    # Calculate actual sums
    actual_sum = sum(arr)
    actual_square_sum = sum(x * x for x in arr)

    # x - y = diff_sum (repeating - missing)
    diff_sum = actual_sum - expected_sum

    # x² - y² = diff_square_sum
    diff_square_sum = actual_square_sum - expected_square_sum

    # x + y = (x² - y²) / (x - y)
    sum_xy = diff_square_sum // diff_sum

    # Solving: x = (diff_sum + sum_xy) / 2
    repeating = (diff_sum + sum_xy) // 2
    missing = sum_xy - repeating

    return (repeating, missing)


def find_repeating_and_missing_xor(arr):
    """
    Find repeating and missing using XOR.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of integers from 1 to n with one repeat and one missing

    Returns:
        Tuple of (repeating_number, missing_number)
    """
    n = len(arr)

    # XOR all elements and all numbers from 1 to n
    xor_result = 0
    for num in arr:
        xor_result ^= num
    for i in range(1, n + 1):
        xor_result ^= i

    # xor_result = x ^ y (repeating ^ missing)
    # Find rightmost set bit
    rightmost_bit = xor_result & -xor_result

    # Divide into two groups based on rightmost set bit
    x = 0
    for num in arr:
        if num & rightmost_bit:
            x ^= num
    for i in range(1, n + 1):
        if i & rightmost_bit:
            x ^= i

    y = xor_result ^ x

    # Determine which is repeating and which is missing
    # Count occurrences in original array
    x_count = sum(1 for num in arr if num == x)

    if x_count > 1:
        return (x, y)
    else:
        return (y, x)


def test_find_repeating_and_missing():
    """Test cases for find_repeating_and_missing."""
    # Test case 1: Basic example
    arr1 = [4, 3, 6, 2, 1, 1]
    assert find_repeating_and_missing(arr1) == (1, 5)
    assert find_repeating_and_missing_xor(arr1) == (1, 5)

    # Test case 2: Missing smallest, repeating largest
    arr2 = [1, 2, 3, 3, 5]
    assert find_repeating_and_missing(arr2) == (3, 4)
    assert find_repeating_and_missing_xor(arr2) == (3, 4)

    # Test case 3: Simple case
    arr3 = [1, 1]
    assert find_repeating_and_missing(arr3) == (1, 2)
    assert find_repeating_and_missing_xor(arr3) == (1, 2)

    # Test case 4: Missing first element
    arr4 = [2, 2, 3, 4, 5]
    assert find_repeating_and_missing(arr4) == (2, 1)
    assert find_repeating_and_missing_xor(arr4) == (2, 1)

    # Test case 5: Larger array
    arr5 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 10]
    assert find_repeating_and_missing(arr5) == (10, 7)
    assert find_repeating_and_missing_xor(arr5) == (10, 7)

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_repeating_and_missing()

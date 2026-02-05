"""
Find the Missing Number

Problem Description:
Given an array of size n-1 containing distinct numbers from 1 to n,
find the missing number in the range.

Example:
    Input: [1, 2, 4, 6, 3, 7, 8], n = 8
    Output: 5

Time Complexity: O(n)
Space Complexity: O(1)

Approach: Mathematical formula using sum of first n natural numbers
    Missing number = n*(n+1)//2 - sum(array)
"""


def find_missing_number(arr, n):
    """
    Find the missing number in array of size n-1 containing 1 to n.

    Args:
        arr: List of integers from 1 to n with one missing number
        n: The maximum number in the range

    Returns:
        The missing number
    """
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


def find_missing_number_xor(arr, n):
    """
    Find missing number using XOR approach.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: List of integers from 1 to n with one missing number
        n: The maximum number in the range

    Returns:
        The missing number
    """
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i

    xor_arr = 0
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr


def test_find_missing_number():
    """Test cases for find_missing_number."""
    # Test case 1: Basic example
    arr1 = [1, 2, 4, 6, 3, 7, 8]
    n1 = 8
    assert find_missing_number(arr1, n1) == 5
    assert find_missing_number_xor(arr1, n1) == 5

    # Test case 2: Missing first element
    arr2 = [2, 3, 4, 5]
    n2 = 5
    assert find_missing_number(arr2, n2) == 1
    assert find_missing_number_xor(arr2, n2) == 1

    # Test case 3: Missing last element
    arr3 = [1, 2, 3, 4]
    n3 = 5
    assert find_missing_number(arr3, n3) == 5
    assert find_missing_number_xor(arr3, n3) == 5

    # Test case 4: Single element (n=2, missing 1)
    arr4 = [2]
    n4 = 2
    assert find_missing_number(arr4, n4) == 1
    assert find_missing_number_xor(arr4, n4) == 1

    # Test case 5: Single element (n=2, missing 2)
    arr5 = [1]
    n5 = 2
    assert find_missing_number(arr5, n5) == 2
    assert find_missing_number_xor(arr5, n5) == 2

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_missing_number()

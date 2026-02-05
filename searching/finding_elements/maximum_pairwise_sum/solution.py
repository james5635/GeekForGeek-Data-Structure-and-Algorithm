"""
Maximum Pairwise Sum in Array

Problem:
Given an array of n integers, find the maximum pairwise sum.
This is simply the sum of the two largest elements.

Examples:
Input: [12, 34, 10, 6, 40]
Output: 74 (40 + 34)

Input: [10, 20, 30]
Output: 50 (30 + 20)

Input: [5, 5, 5]
Output: 10 (5 + 5)

Approach:
Single pass - Find first and second largest elements in one traversal,
then return their sum.

Time Complexity: O(n)
Space Complexity: O(1)

Reference:
https://www.geeksforgeeks.org/dsa/maximum-pairwise-sum-array/
"""


def maximum_pairwise_sum(arr):
    """
    Find maximum sum of any two elements in array.

    Args:
        arr: List of integers (size >= 2)

    Returns:
        Maximum pairwise sum

    Raises:
        ValueError: If array has fewer than 2 elements
    """
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")

    # Initialize first and second largest
    if arr[0] > arr[1]:
        first, second = arr[0], arr[1]
    else:
        first, second = arr[1], arr[0]

    # Find two largest elements
    for num in arr[2:]:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num

    return first + second


def maximum_pairwise_sum_simple(arr):
    """
    Simpler but O(n log n) approach using sorting.
    """
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")

    sorted_arr = sorted(arr, reverse=True)
    return sorted_arr[0] + sorted_arr[1]


def test_maximum_pairwise_sum():
    """Test cases for maximum pairwise sum."""
    # Test case 1: Basic
    assert maximum_pairwise_sum([12, 34, 10, 6, 40]) == 74

    # Test case 2: Three elements
    assert maximum_pairwise_sum([10, 20, 30]) == 50

    # Test case 3: All same
    assert maximum_pairwise_sum([5, 5, 5]) == 10

    # Test case 4: Two elements
    assert maximum_pairwise_sum([10, 20]) == 30

    # Test case 5: Negative numbers
    assert maximum_pairwise_sum([-10, -5, -20]) == -15

    # Test case 6: Mixed positive and negative
    assert maximum_pairwise_sum([-10, 5, -3, 8, 0]) == 13

    # Test case 7: Large numbers
    assert maximum_pairwise_sum([1000000, 999999, 1]) == 1999999

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [12, 34, 10, 6, 40]
    print(f"Array: {arr}")
    print(f"Maximum pairwise sum: {maximum_pairwise_sum(arr)}")

    # Run tests
    test_maximum_pairwise_sum()

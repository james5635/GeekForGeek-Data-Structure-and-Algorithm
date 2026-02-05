"""
Second Largest Element in Array

Problem:
Given an array of integers, find the second largest element.
If no such element exists, return -1.

Examples:
Input: [12, 35, 1, 10, 34, 1]
Output: 34

Input: [10, 10, 10]
Output: -1

Input: [10]
Output: -1

Approach:
Single pass - Maintain first and second largest. Update them
when a larger element is found or when current element is
between first and second.

Time Complexity: O(n)
Space Complexity: O(1)

Reference:
https://www.geeksforgeeks.org/dsa/second-largest-element-in-array/
"""


def find_second_largest(arr):
    """
    Find the second largest element in an array.

    Args:
        arr: List of integers

    Returns:
        Second largest element, or -1 if not exists
    """
    if len(arr) < 2:
        return -1

    first = second = float("-inf")

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float("-inf") else -1


def test_find_second_largest():
    """Test cases for find_second_largest function."""
    # Test case 1: Basic case
    assert find_second_largest([12, 35, 1, 10, 34, 1]) == 34

    # Test case 2: All same elements
    assert find_second_largest([10, 10, 10]) == -1

    # Test case 3: Single element
    assert find_second_largest([10]) == -1

    # Test case 4: Two elements
    assert find_second_largest([5, 10]) == 5

    # Test case 5: Negative numbers
    assert find_second_largest([-10, -5, -20]) == -10

    # Test case 6: Duplicates of largest
    assert find_second_largest([5, 5, 5, 3]) == 3

    # Test case 7: Sorted array
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

    # Test case 8: Reverse sorted
    assert find_second_largest([5, 4, 3, 2, 1]) == 4

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [12, 35, 1, 10, 34, 1]
    print(f"Array: {arr}")
    result = find_second_largest(arr)
    print(f"Second largest: {result}")

    # Run tests
    test_find_second_largest()

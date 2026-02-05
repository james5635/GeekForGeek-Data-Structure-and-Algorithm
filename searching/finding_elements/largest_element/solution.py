"""
Largest Element in Array

Problem:
Given an array arr[], find the largest element in the array.

Examples:
Input: [10, 20, 4]
Output: 20

Input: [20, 10, 20, 4, 100]
Output: 100

Approach:
Linear search - Initialize max with first element and iterate through
array updating max when a larger element is found.

Time Complexity: O(n)
Space Complexity: O(1)

Reference:
https://www.geeksforgeeks.org/dsa/program-find-largest-element-in-an-array/
"""


def find_largest_element(arr):
    """
    Find the largest element in an array.

    Args:
        arr: List of integers

    Returns:
        The largest element in the array

    Raises:
        ValueError: If array is empty
    """
    if not arr:
        raise ValueError("Array cannot be empty")

    max_element = arr[0]

    for num in arr[1:]:
        if num > max_element:
            max_element = num

    return max_element


def test_find_largest_element():
    """Test cases for find_largest_element function."""
    # Test case 1: Basic case
    assert find_largest_element([10, 20, 4]) == 20

    # Test case 2: With duplicates
    assert find_largest_element([20, 10, 20, 4, 100]) == 100

    # Test case 3: Single element
    assert find_largest_element([5]) == 5

    # Test case 4: Negative numbers
    assert find_largest_element([-10, -5, -20]) == -5

    # Test case 5: Mixed positive and negative
    assert find_largest_element([-10, 5, -3, 8, 0]) == 8

    # Test case 6: All same elements
    assert find_largest_element([7, 7, 7, 7]) == 7

    # Test case 7: Large array
    assert find_largest_element(list(range(1000000))) == 999999

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [10, 20, 4, 45, 99]
    print(f"Array: {arr}")
    print(f"Largest element: {find_largest_element(arr)}")

    # Run tests
    test_find_largest_element()

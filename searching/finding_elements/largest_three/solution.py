"""
Find the Largest Three Elements in an Array

Problem:
Given an array of integers, find the largest three elements.
If array size is less than 3, return all elements in descending order.

Examples:
Input: [10, 4, 3, 50, 23, 90]
Output: [90, 50, 23]

Input: [10, 4]
Output: [10, 4]

Approach:
Single pass - Maintain first, second, and third largest.
Update them when a larger element is found.

Time Complexity: O(n)
Space Complexity: O(1)

Reference:
https://www.geeksforgeeks.org/dsa/find-the-largest-three-elements-in-an-array/
"""


def find_largest_three(arr):
    """
    Find the three largest elements in an array.

    Args:
        arr: List of integers

    Returns:
        List of up to 3 largest elements in descending order
    """
    n = len(arr)

    if n == 0:
        return []

    if n == 1:
        return [arr[0]]

    if n == 2:
        return sorted(arr, reverse=True)

    first = second = third = float("-inf")

    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num

    result = []
    if first != float("-inf"):
        result.append(first)
    if second != float("-inf"):
        result.append(second)
    if third != float("-inf"):
        result.append(third)

    return result


def test_find_largest_three():
    """Test cases for find_largest_three function."""
    # Test case 1: Basic case
    assert find_largest_three([10, 4, 3, 50, 23, 90]) == [90, 50, 23]

    # Test case 2: Two elements
    assert find_largest_three([10, 4]) == [10, 4]

    # Test case 3: Single element
    assert find_largest_three([10]) == [10]

    # Test case 4: All same elements
    assert find_largest_three([5, 5, 5]) == [5]

    # Test case 5: Negative numbers
    assert find_largest_three([-10, -5, -20, -3]) == [-3, -5, -10]

    # Test case 6: Duplicates
    assert find_largest_three([10, 10, 9, 8]) == [10, 9, 8]

    # Test case 7: Exactly three elements
    assert find_largest_three([3, 1, 2]) == [3, 2, 1]

    # Test case 8: More than 3 duplicates of largest
    assert find_largest_three([10, 10, 10, 5, 3]) == [10, 5, 3]

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [10, 4, 3, 50, 23, 90]
    print(f"Array: {arr}")
    result = find_largest_three(arr)
    print(f"Largest three: {result}")

    # Run tests
    test_find_largest_three()

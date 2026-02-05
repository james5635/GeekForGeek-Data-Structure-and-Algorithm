"""
First Repeating Element

Problem Description:
Given an array of integers, find the first repeating element in it.
The first repeating element means the element that occurs more than once
and whose index of first occurrence is smallest.

Example:
    Input: [10, 5, 3, 4, 3, 5, 6]
    Output: 5
    Explanation: Both 5 and 3 repeat, but 5 occurs first at index 1.

Time Complexity: O(n)
Space Complexity: O(n)

Approach: Use hash set to track seen elements while iterating
"""


def first_repeating_element(arr):
    """
    Find the first repeating element in the array.
    The first repeating element is the one with the smallest index of first occurrence.

    Args:
        arr: List of integers

    Returns:
        The first repeating element, or -1 if no repeating element exists
    """
    # Track first occurrence index of each element
    first_index = {}
    min_first_idx = float("inf")

    for i, num in enumerate(arr):
        if num in first_index:
            # This element repeats, check if it has smaller first occurrence
            min_first_idx = min(min_first_idx, first_index[num])
        else:
            first_index[num] = i

    return arr[min_first_idx] if min_first_idx != float("inf") else -1


def first_repeating_element_with_index(arr):
    """
    Find first repeating element with smallest index of first occurrence.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Args:
        arr: List of integers

    Returns:
        First repeating element, or -1 if no repeating element
    """
    min_index = float("inf")
    index_map = {}

    for i, num in enumerate(arr):
        if num in index_map:
            min_index = min(min_index, index_map[num])
        else:
            index_map[num] = i

    return arr[min_index] if min_index != float("inf") else -1


def test_first_repeating_element():
    """Test cases for first_repeating_element."""
    # Test case 1: Basic example
    arr1 = [10, 5, 3, 4, 3, 5, 6]
    assert first_repeating_element(arr1) == 5
    assert first_repeating_element_with_index(arr1) == 5

    # Test case 2: No repeating element
    arr2 = [1, 2, 3, 4, 5]
    assert first_repeating_element(arr2) == -1
    assert first_repeating_element_with_index(arr2) == -1

    # Test case 3: First element repeats
    arr3 = [1, 2, 3, 1, 4, 5]
    assert first_repeating_element(arr3) == 1
    assert first_repeating_element_with_index(arr3) == 1

    # Test case 4: Adjacent repeating elements
    arr4 = [1, 2, 2, 3, 4]
    assert first_repeating_element(arr4) == 2
    assert first_repeating_element_with_index(arr4) == 2

    # Test case 5: Last element repeats first
    arr5 = [5, 4, 3, 2, 1, 5]
    assert first_repeating_element(arr5) == 5
    assert first_repeating_element_with_index(arr5) == 5

    # Test case 6: Empty array
    arr6 = []
    assert first_repeating_element(arr6) == -1
    assert first_repeating_element_with_index(arr6) == -1

    print("All test cases passed!")


if __name__ == "__main__":
    test_first_repeating_element()

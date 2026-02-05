"""
Sort Elements by Frequency

Problem Description:
    Given an array of integers, sort the array according to frequency of elements.
    That is, elements that have higher frequency come first.
    If frequencies of two elements are same, then smaller number comes first.

Time Complexity: O(n log n)
- Counting frequencies: O(n)
- Sorting: O(n log n)

Space Complexity: O(n)
- Dictionary to store frequencies: O(n)
- Result array: O(n)

Example:
    Input: arr = [2, 5, 2, 8, 5, 6, 8, 8]
    Output: [8, 8, 8, 2, 2, 5, 5, 6]
    Explanation: 8 occurs 3 times, 2 occurs 2 times, 5 occurs 2 times, 6 occurs 1 time.
    8 comes first, then 2 (smaller than 5), then 5, then 6.

Approach:
    1. Count frequency of each element using a dictionary
    2. Sort the array using a custom comparator that:
       - First compares by frequency (descending)
       - Then by value (ascending) if frequencies are equal
"""

from collections import Counter
from typing import List


def sort_by_frequency(arr: List[int]) -> List[int]:
    """
    Sort array elements by frequency in descending order.
    If frequency is same, sort by value in ascending order.

    Args:
        arr: List of integers

    Returns:
        List sorted by frequency
    """
    if not arr:
        return []

    # Count frequency of each element
    freq = Counter(arr)

    # Sort by frequency (descending), then by value (ascending)
    return sorted(arr, key=lambda x: (-freq[x], x))


def sort_by_frequency_alternative(arr: List[int]) -> List[int]:
    """
    Alternative implementation using Counter's most_common method.

    Args:
        arr: List of integers

    Returns:
        List sorted by frequency
    """
    if not arr:
        return []

    freq = Counter(arr)

    # Sort items by frequency (descending), then by value (ascending)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Build result array
    result = []
    for num, count in sorted_items:
        result.extend([num] * count)

    return result


# Test cases
def test_sort_by_frequency():
    """Test cases for sort_by_frequency function."""
    # Test case 1: Basic example
    arr1 = [2, 5, 2, 8, 5, 6, 8, 8]
    result1 = sort_by_frequency(arr1)
    assert result1 == [8, 8, 8, 2, 2, 5, 5, 6], f"Test 1 failed: {result1}"

    # Test case 2: All same elements
    arr2 = [1, 1, 1, 1]
    result2 = sort_by_frequency(arr2)
    assert result2 == [1, 1, 1, 1], f"Test 2 failed: {result2}"

    # Test case 3: All unique elements
    arr3 = [3, 1, 2, 4]
    result3 = sort_by_frequency(arr3)
    assert result3 == [1, 2, 3, 4], f"Test 3 failed: {result3}"

    # Test case 4: Empty array
    arr4 = []
    result4 = sort_by_frequency(arr4)
    assert result4 == [], f"Test 4 failed: {result4}"

    # Test case 5: Single element
    arr5 = [5]
    result5 = sort_by_frequency(arr5)
    assert result5 == [5], f"Test 5 failed: {result5}"

    # Test case 6: Same frequency - smaller number first
    arr6 = [3, 1, 2, 2, 1]
    result6 = sort_by_frequency(arr6)
    assert result6 == [1, 1, 2, 2, 3], f"Test 6 failed: {result6}"

    # Test case 7: Negative numbers
    arr7 = [-1, -1, 2, 2, 2, -1]
    result7 = sort_by_frequency(arr7)
    assert result7 == [-1, -1, -1, 2, 2, 2], f"Test 7 failed: {result7}"

    # Test case 8: Mixed with alternative method
    arr8 = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
    result8a = sort_by_frequency(arr8)
    result8b = sort_by_frequency_alternative(arr8)
    assert result8a == result8b, f"Test 8 failed: methods differ"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_sort_by_frequency()

    # Example usage
    arr = [2, 5, 2, 8, 5, 6, 8, 8]
    print(f"Original: {arr}")
    print(f"Sorted by frequency: {sort_by_frequency(arr)}")

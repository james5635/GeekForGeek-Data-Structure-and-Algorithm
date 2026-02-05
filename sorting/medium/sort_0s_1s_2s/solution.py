"""
Sort an Array of 0s, 1s, and 2s (Dutch National Flag Problem)

Problem Description:
    Given an array containing only 0s, 1s, and 2s, sort the array in-place
    such that all 0s come first, then all 1s, then all 2s.

Time Complexity: O(n)
- Single pass through array: O(n)

Space Complexity: O(1)
- In-place sorting
- Only using three pointers

Example:
    Input: arr = [0, 1, 2, 0, 1, 2]
    Output: [0, 0, 1, 1, 2, 2]

    Input: arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

Approach:
    Dutch National Flag Algorithm:
    1. low: boundary of 0s region (elements before low are 0)
    2. mid: current element being examined
    3. high: boundary of 2s region (elements after high are 2)

    Rules:
    - arr[0...low-1] = 0
    - arr[low...mid-1] = 1
    - arr[mid...high] = unknown (being examined)
    - arr[high+1...n-1] = 2
"""

from typing import List


def sort_012(arr: List[int]) -> List[int]:
    """
    Sort array of 0s, 1s, and 2s using Dutch National Flag algorithm.

    Args:
        arr: List containing only 0s, 1s, and 2s

    Returns:
        Sorted array

    Raises:
        ValueError: If array contains values other than 0, 1, or 2
    """
    if not arr:
        return arr

    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            # Swap with low pointer and move both forward
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # Already in correct position, just move mid
            mid += 1
        elif arr[mid] == 2:
            # Swap with high pointer and move high backward
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            # Don't increment mid, need to check swapped element
        else:
            raise ValueError(
                f"Invalid value {arr[mid]} in array. Only 0, 1, 2 allowed."
            )

    return arr


def sort_012_counting(arr: List[int]) -> List[int]:
    """
    Alternative implementation using counting method.

    Args:
        arr: List containing only 0s, 1s, and 2s

    Returns:
        Sorted array
    """
    if not arr:
        return arr

    # Count occurrences
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)

    # Reconstruct array
    return [0] * count_0 + [1] * count_1 + [2] * count_2


def verify_sorted_012(arr: List[int]) -> bool:
    """
    Verify if array is sorted correctly (all 0s, then 1s, then 2s).

    Args:
        arr: List to verify

    Returns:
        True if correctly sorted
    """
    seen_one = False
    seen_two = False

    for num in arr:
        if num == 0:
            if seen_one or seen_two:
                return False
        elif num == 1:
            if seen_two:
                return False
            seen_one = True
        elif num == 2:
            seen_two = True
        else:
            return False

    return True


# Test cases
def test_sort_012():
    """Test cases for sort_012 function."""
    # Test case 1: Basic example
    arr1 = [0, 1, 2, 0, 1, 2]
    result1 = sort_012(arr1.copy())
    assert result1 == [0, 0, 1, 1, 2, 2], f"Test 1 failed: {result1}"

    # Test case 2: Another example
    arr2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    result2 = sort_012(arr2.copy())
    assert verify_sorted_012(result2), f"Test 2 failed: {result2}"
    assert sorted(arr2) == result2, f"Test 2 content failed"

    # Test case 3: All 0s
    arr3 = [0, 0, 0, 0]
    result3 = sort_012(arr3.copy())
    assert result3 == [0, 0, 0, 0], f"Test 3 failed: {result3}"

    # Test case 4: All 1s
    arr4 = [1, 1, 1, 1]
    result4 = sort_012(arr4.copy())
    assert result4 == [1, 1, 1, 1], f"Test 4 failed: {result4}"

    # Test case 5: All 2s
    arr5 = [2, 2, 2, 2]
    result5 = sort_012(arr5.copy())
    assert result5 == [2, 2, 2, 2], f"Test 5 failed: {result5}"

    # Test case 6: Empty array
    arr6 = []
    result6 = sort_012(arr6.copy())
    assert result6 == [], f"Test 6 failed: {result6}"

    # Test case 7: Single element
    arr7 = [1]
    result7 = sort_012(arr7.copy())
    assert result7 == [1], f"Test 7 failed: {result7}"

    # Test case 8: Two elements
    arr8 = [2, 0]
    result8 = sort_012(arr8.copy())
    assert result8 == [0, 2], f"Test 8 failed: {result8}"

    # Test case 9: Compare with counting method
    arr9 = [2, 0, 2, 1, 1, 0, 1, 2, 0, 1, 0, 2]
    result9a = sort_012(arr9.copy())
    result9b = sort_012_counting(arr9.copy())
    assert result9a == result9b, f"Test 9 failed: methods differ"

    # Test case 10: Already sorted
    arr10 = [0, 0, 1, 1, 2, 2]
    result10 = sort_012(arr10.copy())
    assert result10 == [0, 0, 1, 1, 2, 2], f"Test 10 failed: {result10}"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_sort_012()

    # Example usage
    arr = [0, 1, 2, 0, 1, 2, 1, 0, 2, 1, 0]
    print(f"Original: {arr}")
    print(f"Sorted: {sort_012(arr.copy())}")

"""
Find a Peak Element

Problem:
Given an array where no two adjacent elements are same, find the
index of a peak element. An element is a peak if it's strictly
greater than its neighbors. First and last elements only need
one neighbor to compare.

Examples:
Input: [1, 2, 4, 5, 7, 8, 3]
Output: 5 (element 8, since 7 < 8 > 3)

Input: [10, 20, 15, 2, 23, 90, 80]
Output: 1 or 5 (20 or 90)

Approach:
Binary Search - If mid element is greater than both neighbors,
it's a peak. Otherwise, move to the side with greater neighbor.

Time Complexity: O(log n)
Space Complexity: O(1)

Reference:
https://www.geeksforgeeks.org/dsa/find-a-peak-in-a-given-array/
"""


def find_peak_element(arr):
    """
    Find index of a peak element in array.

    Args:
        arr: List of integers where no two adjacent elements are same

    Returns:
        Index of any peak element
    """
    n = len(arr)

    if n == 0:
        return -1

    if n == 1:
        return 0

    # Check if first element is peak
    if arr[0] > arr[1]:
        return 0

    # Check if last element is peak
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    # Binary search in middle section
    left, right = 1, n - 2

    while left <= right:
        mid = left + (right - left) // 2

        # Check if mid is peak
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        # Move to the side with greater element
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_peak_linear(arr):
    """
    Linear search approach - O(n).
    """
    n = len(arr)

    for i in range(n):
        is_peak = True

        if i > 0 and arr[i] <= arr[i - 1]:
            is_peak = False

        if i < n - 1 and arr[i] <= arr[i + 1]:
            is_peak = False

        if is_peak:
            return i

    return -1


def find_all_peaks(arr):
    """
    Find all peak elements in array.
    """
    n = len(arr)
    peaks = []

    for i in range(n):
        is_peak = True

        if i > 0 and arr[i] <= arr[i - 1]:
            is_peak = False

        if i < n - 1 and arr[i] <= arr[i + 1]:
            is_peak = False

        if is_peak:
            peaks.append(i)

    return peaks


def test_find_peak_element():
    """Test cases for find_peak_element function."""
    # Test case 1: Single peak in middle
    assert find_peak_element([1, 2, 4, 5, 7, 8, 3]) == 5

    # Test case 2: Multiple peaks
    result = find_peak_element([10, 20, 15, 2, 23, 90, 80])
    assert result in [1, 5]

    # Test case 3: First element is peak
    assert find_peak_element([10, 5, 3]) == 0

    # Test case 4: Last element is peak
    assert find_peak_element([1, 3, 5, 10]) == 3

    # Test case 5: Single element
    assert find_peak_element([5]) == 0

    # Test case 6: Two elements
    assert find_peak_element([1, 2]) == 1
    assert find_peak_element([2, 1]) == 0

    # Test case 7: Mountain array
    assert find_peak_element([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 4

    # Test all peaks
    assert find_all_peaks([10, 20, 15, 2, 23, 90, 80]) == [1, 5]

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 4, 5, 7, 8, 3]
    print(f"Array: {arr}")
    idx = find_peak_element(arr)
    print(f"Peak element found at index {idx}: {arr[idx]}")

    # Find all peaks
    arr2 = [10, 20, 15, 2, 23, 90, 80]
    print(f"\nArray: {arr2}")
    print(f"All peaks: {find_all_peaks(arr2)}")

    # Run tests
    test_find_peak_element()

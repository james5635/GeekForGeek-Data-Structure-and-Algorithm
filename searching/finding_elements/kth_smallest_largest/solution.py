"""
Kth Smallest/Largest Element in Unsorted Array

Problem:
Given an integer array and k, find the kth smallest element.
k is always smaller than the size of the array.

Examples:
Input: [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5 (4th smallest)

Input: [7, 10, 4, 3, 20, 15], k = 3
Output: 7 (3rd smallest)

Approach:
QuickSelect - Using partition from QuickSort. Average O(n) time.
Or Max Heap - O(n log k) time. This implementation uses QuickSelect.

Time Complexity: O(n) average, O(n^2) worst case
Space Complexity: O(1) auxiliary (in-place)

Reference:
https://www.geeksforgeeks.org/dsa/kth-smallest-largest-element-in-unsorted-array/
"""

import random


def partition(arr, left, right):
    """
    Partition array using last element as pivot.
    Places all elements <= pivot to the left.
    """
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_select(arr, left, right, k):
    """
    Find kth smallest element using QuickSelect.
    k is 0-indexed (0 means smallest).
    """
    if left <= right:
        pivot_idx = partition(arr, left, right)

        if pivot_idx == k:
            return arr[pivot_idx]
        elif pivot_idx > k:
            return quick_select(arr, left, pivot_idx - 1, k)
        else:
            return quick_select(arr, pivot_idx + 1, right, k)

    return None


def find_kth_smallest(arr, k):
    """
    Find kth smallest element (1-indexed).

    Args:
        arr: List of integers
        k: Position (1-based) of element to find

    Returns:
        kth smallest element
    """
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid input")

    # Create a copy to avoid modifying original
    arr_copy = arr.copy()
    return quick_select(arr_copy, 0, len(arr_copy) - 1, k - 1)


def find_kth_largest(arr, k):
    """
    Find kth largest element (1-indexed).

    Args:
        arr: List of integers
        k: Position (1-based) of largest element to find

    Returns:
        kth largest element
    """
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid input")

    # kth largest is (n-k+1)th smallest
    return find_kth_smallest(arr, len(arr) - k + 1)


def test_kth_element():
    """Test cases for kth smallest/largest functions."""
    # Test case 1: 4th smallest
    assert find_kth_smallest([10, 5, 4, 3, 48, 6, 2, 33, 53, 10], 4) == 5

    # Test case 2: 3rd smallest
    assert find_kth_smallest([7, 10, 4, 3, 20, 15], 3) == 7

    # Test case 3: 1st smallest
    assert find_kth_smallest([3, 2, 1, 5, 6, 4], 1) == 1

    # Test case 4: kth largest
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    # Test case 5: 1st largest
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 1) == 6

    # Test case 6: With duplicates
    assert find_kth_smallest([3, 3, 3, 1, 2], 2) == 2

    # Test case 7: Two elements
    assert find_kth_smallest([2, 1], 1) == 1
    assert find_kth_smallest([2, 1], 2) == 2

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k = 4
    print(f"Array: {arr}")
    print(f"k = {k}")
    print(f"Kth smallest: {find_kth_smallest(arr, k)}")
    print(f"Kth largest: {find_kth_largest(arr, k)}")

    # Run tests
    test_kth_element()

"""
K Largest Elements in an Array

Problem:
Given an array arr[] and an integer k, find k largest elements in the array.
Elements in the output should be in decreasing order.

Examples:
Input: [1, 23, 12, 9, 30, 2, 50], k = 3
Output: [50, 30, 23]

Input: [11, 5, 12, 9, 44, 17, 2], k = 2
Output: [44, 17]

Approach:
Min Heap - Maintain a min heap of size k. For elements after first k,
if element is larger than heap top, replace top. Finally, extract all
from heap and reverse for descending order.

Time Complexity: O(n log k)
Space Complexity: O(k)

Reference:
https://www.geeksforgeeks.org/dsa/k-largestor-smallest-elements-in-an-array/
"""

import heapq


def find_k_largest(arr, k):
    """
    Find k largest elements in an array.

    Args:
        arr: List of integers
        k: Number of largest elements to find

    Returns:
        List of k largest elements in descending order
    """
    if k <= 0:
        return []

    if k >= len(arr):
        return sorted(arr, reverse=True)

    # Create min heap with first k elements
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    # Process remaining elements
    for num in arr[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    # Extract and reverse for descending order
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap))

    result.reverse()
    return result


def find_k_largest_sorting(arr, k):
    """
    Alternative using sorting - O(n log n).
    """
    if k <= 0:
        return []

    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[:k]


def test_find_k_largest():
    """Test cases for find_k_largest function."""
    # Test case 1: Basic case
    assert find_k_largest([1, 23, 12, 9, 30, 2, 50], 3) == [50, 30, 23]

    # Test case 2: Different k
    assert find_k_largest([11, 5, 12, 9, 44, 17, 2], 2) == [44, 17]

    # Test case 3: k = 1
    assert find_k_largest([3, 2, 1, 5, 6, 4], 1) == [6]

    # Test case 4: k equals array size
    assert find_k_largest([1, 2, 3], 3) == [3, 2, 1]

    # Test case 5: k = 0
    assert find_k_largest([1, 2, 3], 0) == []

    # Test case 6: With duplicates
    assert find_k_largest([3, 2, 1, 5, 6, 4, 6], 3) == [6, 6, 5]

    # Test case 7: Negative numbers
    assert find_k_largest([-1, -5, -3, -2], 2) == [-1, -2]

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    print(f"Array: {arr}")
    print(f"k = {k}")
    print(f"K largest elements: {find_k_largest(arr, k)}")

    # Run tests
    test_find_k_largest()

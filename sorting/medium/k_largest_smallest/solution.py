"""
K Largest/Smallest Elements in an Array

Given an array and integer k, find k largest (or smallest) elements.
Elements should be returned in decreasing order for largest,
increasing order for smallest.

Algorithms:
1. Sorting: O(n log n) - Sort and take first/last k elements
2. Min/Max Heap: O(n log k) - Use heap of size k
3. Quick Select: O(n) average - Partition-based selection

Time Complexity: O(n log k) for heap approach (most efficient)
Space Complexity: O(k) for heap
"""

import heapq
import random


def k_largest_sorting(arr, k):
    """
    Find k largest elements using sorting.

    Args:
        arr: List of integers
        k: Number of largest elements to find

    Returns:
        list: k largest elements in descending order
    """
    if not arr or k <= 0:
        return []

    if k >= len(arr):
        return sorted(arr, reverse=True)

    # Sort in descending order and take first k
    return sorted(arr, reverse=True)[:k]


def k_smallest_sorting(arr, k):
    """
    Find k smallest elements using sorting.

    Args:
        arr: List of integers
        k: Number of smallest elements to find

    Returns:
        list: k smallest elements in ascending order
    """
    if not arr or k <= 0:
        return []

    if k >= len(arr):
        return sorted(arr)

    return sorted(arr)[:k]


def k_largest_heap(arr, k):
    """
    Find k largest elements using min-heap.

    Args:
        arr: List of integers
        k: Number of largest elements to find

    Returns:
        list: k largest elements in descending order
    """
    if not arr or k <= 0:
        return []

    if k >= len(arr):
        return sorted(arr, reverse=True)

    # Create min-heap with first k elements
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    # Process remaining elements
    for i in range(k, len(arr)):
        if arr[i] > min_heap[0]:
            heapq.heapreplace(min_heap, arr[i])

    # Return in descending order
    return sorted(min_heap, reverse=True)


def k_smallest_heap(arr, k):
    """
    Find k smallest elements using max-heap (simulated with negative values).

    Args:
        arr: List of integers
        k: Number of smallest elements to find

    Returns:
        list: k smallest elements in ascending order
    """
    if not arr or k <= 0:
        return []

    if k >= len(arr):
        return sorted(arr)

    # Create max-heap (using negative values) with first k elements
    max_heap = [-x for x in arr[:k]]
    heapq.heapify(max_heap)

    # Process remaining elements
    for i in range(k, len(arr)):
        if -arr[i] > max_heap[0]:  # arr[i] < -max_heap[0]
            heapq.heapreplace(max_heap, -arr[i])

    # Convert back and return in ascending order
    return sorted([-x for x in max_heap])


def partition(arr, left, right):
    """Partition array for quick select."""
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] >= pivot:  # For k largest (descending order)
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_select(arr, left, right, k):
    """Quick select to find k largest elements."""
    if left <= right:
        pivot_idx = partition(arr, left, right)

        # Count elements in left part (which are >= pivot)
        left_count = pivot_idx - left + 1

        if left_count == k:
            return
        elif left_count > k:
            quick_select(arr, left, pivot_idx - 1, k)
        else:
            quick_select(arr, pivot_idx + 1, right, k - left_count)


def k_largest_quickselect(arr, k):
    """
    Find k largest elements using Quick Select.

    Args:
        arr: List of integers
        k: Number of largest elements to find

    Returns:
        list: k largest elements in descending order
    """
    if not arr or k <= 0:
        return []

    if k >= len(arr):
        return sorted(arr, reverse=True)

    arr_copy = arr[:]
    quick_select(arr_copy, 0, len(arr_copy) - 1, k)

    # First k elements are the largest
    result = arr_copy[:k]
    return sorted(result, reverse=True)


def test_k_largest_smallest():
    """Test cases for k largest/smallest elements."""
    # Test Case 1: Basic case - k largest
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    result = k_largest_heap(arr, k)
    expected = [50, 30, 23]
    assert result == expected, f"Test 1 failed: Expected {expected}, got {result}"
    print("Test 1 passed: k largest (heap)")

    # Test Case 2: Basic case - k smallest
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    result = k_smallest_heap(arr, k)
    expected = [1, 2, 9]
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("Test 2 passed: k smallest (heap)")

    # Test Case 3: k = 1 (maximum/minimum)
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 1
    result = k_largest_heap(arr, k)
    assert result == [50], f"Test 3a failed: Expected [50], got {result}"
    result = k_smallest_heap(arr, k)
    assert result == [1], f"Test 3b failed: Expected [1], got {result}"
    print("Test 3 passed: k = 1")

    # Test Case 4: k = n (all elements)
    arr = [3, 1, 4, 1, 5]
    k = 5
    result = k_largest_heap(arr, k)
    expected = [5, 4, 3, 1, 1]
    assert result == expected, f"Test 4a failed: Expected {expected}, got {result}"
    result = k_smallest_heap(arr, k)
    expected = [1, 1, 3, 4, 5]
    assert result == expected, f"Test 4b failed: Expected {expected}, got {result}"
    print("Test 4 passed: k = n")

    # Test Case 5: Empty array
    arr = []
    k = 3
    result = k_largest_heap(arr, k)
    assert result == [], f"Test 5 failed: Expected [], got {result}"
    print("Test 5 passed: Empty array")

    # Test Case 6: k = 0
    arr = [1, 2, 3]
    k = 0
    result = k_largest_heap(arr, k)
    assert result == [], f"Test 6 failed: Expected [], got {result}"
    print("Test 6 passed: k = 0")

    # Test Case 7: Array with duplicates
    arr = [5, 5, 5, 1, 1, 1]
    k = 3
    result = k_largest_heap(arr, k)
    expected = [5, 5, 5]
    assert result == expected, f"Test 7 failed: Expected {expected}, got {result}"
    print("Test 7 passed: Array with duplicates")

    # Test Case 8: With negative numbers
    arr = [-5, -2, 0, 3, -10, 8]
    k = 3
    result = k_largest_heap(arr, k)
    expected = [8, 3, 0]
    assert result == expected, f"Test 8a failed: Expected {expected}, got {result}"
    result = k_smallest_heap(arr, k)
    expected = [-10, -5, -2]
    assert result == expected, f"Test 8b failed: Expected {expected}, got {result}"
    print("Test 8 passed: With negative numbers")

    # Test Case 9: Quick select approach
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    result = k_largest_quickselect(arr, k)
    expected = [50, 30, 23]
    assert result == expected, f"Test 9 failed: Expected {expected}, got {result}"
    print("Test 9 passed: Quick select approach")

    # Test Case 10: All approaches give same result
    import random

    for _ in range(10):
        arr = [random.randint(-50, 50) for _ in range(20)]
        k = random.randint(1, 15)

        result1 = k_largest_sorting(arr, k)
        result2 = k_largest_heap(arr, k)
        result3 = k_largest_quickselect(arr, k)

        assert result1 == result2 == result3, (
            f"Test 10 failed: Approaches differ for k={k}"
        )
    print("Test 10 passed: All approaches consistent")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_k_largest_smallest()

    # Example usage
    print("\nExample 1 (K Largest):")
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    result = k_largest_heap(arr, k)
    print(f"Array: {arr}")
    print(f"k = {k}")
    print(f"{k} largest elements: {result}")

    print("\nExample 2 (K Smallest):")
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    result = k_smallest_heap(arr, k)
    print(f"Array: {arr}")
    print(f"k = {k}")
    print(f"{k} smallest elements: {result}")

    print("\nExample 3 (Comparison of approaches):")
    arr = [12, 3, 5, 7, 19, 1, 8, 15]
    k = 4
    print(f"Array: {arr}")
    print(f"k = {k}")
    print(f"Sorting approach:     {k_largest_sorting(arr, k)}")
    print(f"Heap approach:        {k_largest_heap(arr, k)}")
    print(f"Quick Select approach:{k_largest_quickselect(arr, k)}")

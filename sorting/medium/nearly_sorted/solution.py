"""
Nearly Sorted Algorithm (Sort a K-Sorted Array)

Given an array where every element is at most k positions away from its correct
sorted position, sort the array efficiently.

Algorithm:
1. Use a min-heap of size k+1
2. Insert first k+1 elements into the heap
3. For each remaining element, pop min from heap, add to result, and push new element
4. Pop remaining elements from heap

Time Complexity: O(n log k) - Each of n elements requires heap operations
Space Complexity: O(k) - Min heap stores at most k+1 elements
"""

import heapq


def sort_nearly_sorted(arr, k):
    """
    Sort a k-sorted array using min-heap.

    Args:
        arr: List of integers where each element is at most k positions
             away from its sorted position
        k: Maximum displacement of any element from its sorted position

    Returns:
        list: Sorted array
    """
    if not arr:
        return []

    n = len(arr)

    # Min-heap to store k+1 elements
    min_heap = []

    # Push first k+1 elements into heap
    for i in range(min(k + 1, n)):
        heapq.heappush(min_heap, arr[i])

    result = []
    index = 0

    # Process remaining elements
    for i in range(k + 1, n):
        # Pop minimum and add to result
        result.append(heapq.heappop(min_heap))
        # Push next element
        heapq.heappush(min_heap, arr[i])
        index += 1

    # Pop remaining elements from heap
    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


def sort_nearly_sorted_inplace(arr, k):
    """
    In-place version that modifies the original array.

    Args:
        arr: List of integers where each element is at most k positions
             away from its sorted position
        k: Maximum displacement of any element from its sorted position
    """
    if not arr:
        return

    n = len(arr)

    # Min-heap to store k+1 elements
    min_heap = []

    # Push first k+1 elements into heap
    for i in range(min(k + 1, n)):
        heapq.heappush(min_heap, arr[i])

    index = 0

    # Process remaining elements
    for i in range(k + 1, n):
        # Pop minimum and place in array
        arr[index] = heapq.heappop(min_heap)
        # Push next element
        heapq.heappush(min_heap, arr[i])
        index += 1

    # Pop remaining elements from heap
    while min_heap:
        arr[index] = heapq.heappop(min_heap)
        index += 1


def test_sort_nearly_sorted():
    """Test cases for nearly sorted array algorithm."""
    # Test Case 1: Basic case from problem
    arr = [2, 3, 1, 4]
    k = 2
    result = sort_nearly_sorted(arr, k)
    expected = [1, 2, 3, 4]
    assert result == expected, f"Test 1 failed: Expected {expected}, got {result}"
    print("Test 1 passed: Basic case")

    # Test Case 2: Larger array
    arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10]
    k = 2
    result = sort_nearly_sorted(arr, k)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("Test 2 passed: Larger array")

    # Test Case 3: k = 0 (already sorted)
    arr = [1, 2, 3, 4, 5]
    k = 0
    result = sort_nearly_sorted(arr, k)
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Test 3 failed: Expected {expected}, got {result}"
    print("Test 3 passed: Already sorted (k=0)")

    # Test Case 4: k = n-1 (can be completely unsorted)
    arr = [5, 4, 3, 2, 1]
    k = 4
    result = sort_nearly_sorted(arr, k)
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Test 4 failed: Expected {expected}, got {result}"
    print("Test 4 passed: Completely unsorted (k=n-1)")

    # Test Case 5: Empty array
    arr = []
    k = 2
    result = sort_nearly_sorted(arr, k)
    expected = []
    assert result == expected, f"Test 5 failed: Expected {expected}, got {result}"
    print("Test 5 passed: Empty array")

    # Test Case 6: Single element
    arr = [5]
    k = 2
    result = sort_nearly_sorted(arr, k)
    expected = [5]
    assert result == expected, f"Test 6 failed: Expected {expected}, got {result}"
    print("Test 6 passed: Single element")

    # Test Case 7: Array with duplicates
    arr = [3, 1, 2, 1, 3, 2]
    k = 2
    result = sort_nearly_sorted(arr, k)
    expected = [1, 1, 2, 2, 3, 3]
    assert result == expected, f"Test 7 failed: Expected {expected}, got {result}"
    print("Test 7 passed: Array with duplicates")

    # Test Case 8: In-place sorting
    arr = [2, 3, 1, 4]
    k = 2
    sort_nearly_sorted_inplace(arr, k)
    expected = [1, 2, 3, 4]
    assert arr == expected, f"Test 8 failed: Expected {expected}, got {arr}"
    print("Test 8 passed: In-place sorting")

    # Test Case 9: Verify k-sorted property
    # After sorting, each element should be at most k positions from original
    original = [2, 3, 1, 4]
    k = 2
    sorted_arr = sort_nearly_sorted(original, k)
    for i, val in enumerate(sorted_arr):
        original_pos = original.index(val)
        assert abs(i - original_pos) <= k, (
            f"Element {val} moved from position {original_pos} to {i}, distance = {abs(i - original_pos)} > k={k}"
        )
    print("Test 9 passed: Verify k-sorted property")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_sort_nearly_sorted()

    # Example usage
    print("\nExample 1:")
    arr = [2, 3, 1, 4]
    k = 2
    result = sort_nearly_sorted(arr, k)
    print(f"Input array: {arr}")
    print(f"k = {k}")
    print(f"Sorted: {result}")

    print("\nExample 2:")
    arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10]
    k = 2
    result = sort_nearly_sorted(arr, k)
    print(f"Input array: {arr}")
    print(f"Sorted: {result}")

"""
Merge K Sorted Arrays

Given a 2D matrix where each row is a sorted array, merge all arrays into a single
sorted array containing all elements.

Algorithm:
1. Use a min-heap to efficiently merge k sorted arrays
2. Push first element of each array into heap along with array and element indices
3. Pop minimum element, add to result, and push next element from same array
4. Repeat until heap is empty

Time Complexity: O(n log k) where n is total elements and k is number of arrays
Space Complexity: O(k) for the min-heap
"""

import heapq


def merge_k_sorted_arrays(mat):
    """
    Merge k sorted arrays into a single sorted array.

    Args:
        mat: 2D list where each row is a sorted array

    Returns:
        list: A single sorted array containing all elements
    """
    if not mat:
        return []

    k = len(mat)
    result = []

    # Min-heap: (value, array_index, element_index)
    min_heap = []

    # Push first element of each array into heap
    for i in range(k):
        if len(mat[i]) > 0:
            heapq.heappush(min_heap, (mat[i][0], i, 0))

    # Merge elements
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        # Push next element from the same array
        next_idx = elem_idx + 1
        if next_idx < len(mat[arr_idx]):
            heapq.heappush(min_heap, (mat[arr_idx][next_idx], arr_idx, next_idx))

    return result


def merge_k_sorted_arrays_divide_conquer(mat):
    """
    Alternative approach using divide and conquer (merge sort style).

    Args:
        mat: 2D list where each row is a sorted array

    Returns:
        list: A single sorted array containing all elements
    """
    if not mat:
        return []

    def merge_two_arrays(a, b):
        """Merge two sorted arrays."""
        result = []
        i = j = 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        # Add remaining elements
        result.extend(a[i:])
        result.extend(b[j:])
        return result

    def merge_recursive(arrays, left, right):
        """Recursively merge arrays from left to right index."""
        if left == right:
            return arrays[left]

        mid = (left + right) // 2
        left_merged = merge_recursive(arrays, left, mid)
        right_merged = merge_recursive(arrays, mid + 1, right)

        return merge_two_arrays(left_merged, right_merged)

    return merge_recursive(mat, 0, len(mat) - 1)


def test_merge_k_sorted_arrays():
    """Test cases for merge k sorted arrays algorithm."""
    # Test Case 1: Basic case
    mat = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
    result = merge_k_sorted_arrays(mat)
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert result == expected, f"Test 1 failed: Expected {expected}, got {result}"
    print("Test 1 passed: Basic case")

    # Test Case 2: Arrays with duplicates
    mat = [[1, 2, 3, 4], [2, 2, 3, 4], [5, 5, 6, 6], [7, 8, 9, 9]]
    result = merge_k_sorted_arrays(mat)
    expected = [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9]
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("Test 2 passed: Arrays with duplicates")

    # Test Case 3: Single array
    mat = [[1, 2, 3]]
    result = merge_k_sorted_arrays(mat)
    expected = [1, 2, 3]
    assert result == expected, f"Test 3 failed: Expected {expected}, got {result}"
    print("Test 3 passed: Single array")

    # Test Case 4: Empty arrays
    mat = [[], [1], []]
    result = merge_k_sorted_arrays(mat)
    expected = [1]
    assert result == expected, f"Test 4 failed: Expected {expected}, got {result}"
    print("Test 4 passed: Empty arrays")

    # Test Case 5: Single element arrays
    mat = [[5], [3], [1], [4], [2]]
    result = merge_k_sorted_arrays(mat)
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Test 5 failed: Expected {expected}, got {result}"
    print("Test 5 passed: Single element arrays")

    # Test Case 6: Test divide and conquer approach
    mat = [[1, 3, 5], [2, 4, 6], [0, 7, 8]]
    result = merge_k_sorted_arrays_divide_conquer(mat)
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert result == expected, f"Test 6 failed: Expected {expected}, got {result}"
    print("Test 6 passed: Divide and conquer approach")

    # Test Case 7: Large number of arrays
    mat = [[i] for i in range(100, 0, -1)]
    result = merge_k_sorted_arrays(mat)
    expected = list(range(1, 101))
    assert result == expected, f"Test 7 failed: Expected sorted 1-100"
    print("Test 7 passed: Large number of arrays")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_merge_k_sorted_arrays()

    # Example usage
    print("\nExample 1 (Min-Heap approach):")
    mat = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
    result = merge_k_sorted_arrays(mat)
    print(f"Input: {mat}")
    print(f"Merged: {result}")

    print("\nExample 2 (Divide and Conquer):")
    result = merge_k_sorted_arrays_divide_conquer(mat)
    print(f"Merged: {result}")

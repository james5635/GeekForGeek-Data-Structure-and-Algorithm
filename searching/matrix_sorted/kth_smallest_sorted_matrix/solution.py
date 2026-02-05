"""
Kth Smallest Element in a Row-Column Wise Sorted Matrix

Problem Description:
Given a n x n matrix where each row and column is sorted in ascending order,
find the kth smallest element in the matrix.

Example:
    Input: matrix = [[10, 20, 30, 40],
                     [15, 25, 35, 45],
                     [24, 29, 37, 48],
                     [32, 33, 39, 50]]
           k = 7
    Output: 30

Time Complexity: O(n log(max-min))
Space Complexity: O(1)

Approach: Binary search on value range
    Use binary search between min and max element
    Count elements <= mid to determine search direction
"""

import heapq


def kth_smallest_binary_search(matrix, k):
    """
    Find kth smallest using binary search on value range.

    Args:
        matrix: n x n sorted matrix
        k: Position of element to find (1-based)

    Returns:
        The kth smallest element
    """
    n = len(matrix)

    def count_less_equal(mid):
        """Count elements <= mid in the matrix."""
        count = 0
        row, col = n - 1, 0  # Start from bottom-left

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1  # All elements above are also <= mid
                col += 1
            else:
                row -= 1

        return count

    low, high = matrix[0][0], matrix[n - 1][n - 1]

    while low < high:
        mid = low + (high - low) // 2
        count = count_less_equal(mid)

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low


def kth_smallest_heap(matrix, k):
    """
    Find kth smallest using min heap.

    Time Complexity: O(k log n)
    Space Complexity: O(n)

    Args:
        matrix: n x n sorted matrix
        k: Position of element to find (1-based)

    Returns:
        The kth smallest element
    """
    n = len(matrix)
    min_heap = []

    # Push first column elements
    for i in range(min(n, k)):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))

    count = 0
    result = 0

    while min_heap and count < k:
        val, row, col = heapq.heappop(min_heap)
        result = val
        count += 1

        if col + 1 < n:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

    return result


def test_kth_smallest():
    """Test cases for kth smallest in sorted matrix."""
    # Test case 1: Basic 4x4 matrix
    matrix1 = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
    assert kth_smallest_binary_search(matrix1, 7) == 30
    assert kth_smallest_heap(matrix1, 7) == 30

    # Test case 2: 3x3 matrix
    matrix2 = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    assert kth_smallest_binary_search(matrix2, 8) == 13
    assert kth_smallest_heap(matrix2, 8) == 13

    # Test case 3: k = 1 (smallest element)
    assert kth_smallest_binary_search(matrix2, 1) == 1
    assert kth_smallest_heap(matrix2, 1) == 1

    # Test case 4: k = n*n (largest element)
    assert kth_smallest_binary_search(matrix2, 9) == 15
    assert kth_smallest_heap(matrix2, 9) == 15

    # Test case 5: 2x2 matrix
    matrix3 = [[1, 2], [1, 3]]
    assert kth_smallest_binary_search(matrix3, 2) == 1
    assert kth_smallest_heap(matrix3, 2) == 1

    # Test case 6: Single element
    matrix4 = [[1]]
    assert kth_smallest_binary_search(matrix4, 1) == 1
    assert kth_smallest_heap(matrix4, 1) == 1

    print("All test cases passed!")


if __name__ == "__main__":
    test_kth_smallest()

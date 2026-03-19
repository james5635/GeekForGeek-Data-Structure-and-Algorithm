def findMedian(matrix, R, C):
    """
    Find median in a row-wise sorted matrix
    Args:
        matrix: 2D list representing the matrix
        R: Number of rows
        C: Number of columns
    Returns:
        Median value
    """
    # Initialize min and max as the minimum and maximum elements in the matrix
    min_element = matrix[0][0]
    max_element = matrix[0][C - 1]

    for i in range(1, R):
        # Update min_element
        if matrix[i][0] < min_element:
            min_element = matrix[i][0]
        # Update max_element
        if matrix[i][C - 1] > max_element:
            max_element = matrix[i][C - 1]

    # For odd number of elements, median is at position (R*C)//2
    # For even number of elements, we can take the lower median
    desired = (R * C + 1) // 2

    while min_element < max_element:
        mid = min_element + (max_element - min_element) // 2
        # Count of elements smaller than or equal to mid
        count = 0
        for i in range(R):
            # Find the first element greater than mid in row i
            # Using binary search since each row is sorted
            left, right = 0, C - 1
            while left <= right:
                mid_idx = left + (right - left) // 2
                if matrix[i][mid_idx] <= mid:
                    left = mid_idx + 1
                else:
                    right = mid_idx - 1
            count += left

        if count < desired:
            min_element = mid + 1
        else:
            max_element = mid

    return min_element


def test_findMedian():
    # Test case 1
    matrix1 = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    R1, C1 = 3, 3
    print(f"Test 1 - Matrix: {matrix1}")
    print(f"Median: {findMedian(matrix1, R1, C1)}")
    print(f"Expected: 5")
    print()

    # Test case 2
    matrix2 = [[1, 3, 4], [2, 5, 6], [7, 8, 9]]
    R2, C2 = 3, 3
    print(f"Test 2 - Matrix: {matrix2}")
    print(f"Median: {findMedian(matrix2, R2, C2)}")
    print(f"Expected: 5")
    print()

    # Test case 3 - Even number of elements
    matrix3 = [[1, 2], [3, 4]]
    R3, C3 = 2, 2
    print(f"Test 3 - Matrix: {matrix3}")
    print(f"Median: {findMedian(matrix3, R3, C3)}")
    print(f"Expected: 2 (lower median for even elements)")
    print()


if __name__ == "__main__":
    test_findMedian()

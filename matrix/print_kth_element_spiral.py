def findK(matrix, n, m, k):
    """
    Find the kth element obtained while traversing the matrix in spiral form
    Args:
        matrix: 2D list representing the matrix
        n: Number of rows
        m: Number of columns
        k: Position of element to find (1-indexed)
    Returns:
        The kth element in spiral traversal
    """
    if not matrix or not matrix[0] or k <= 0:
        return None

    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    count = 0

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for j in range(left, right + 1):
            count += 1
            if count == k:
                return matrix[top][j]
        top += 1

        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            count += 1
            if count == k:
                return matrix[i][right]
        right -= 1

        # Traverse from right to left along the bottom row
        if top <= bottom:
            for j in range(right, left - 1, -1):
                count += 1
                if count == k:
                    return matrix[bottom][j]
            bottom -= 1

        # Traverse from bottom to top along the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                count += 1
                if count == k:
                    return matrix[i][left]
            left += 1

    # If k is out of bounds
    return None


def test_findK():
    # Test case 1
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    n1, m1 = 4, 4
    k1 = 6
    print(f"Test 1 - Matrix:")
    for row in matrix1:
        print(row)
    print(f"k = {k1}")
    result1 = findK(matrix1, n1, m1, k1)
    print(f"kth element: {result1}")
    print(f"Expected: 12")
    print()

    # Test case 2
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n2, m2 = 3, 3
    k2 = 4
    print(f"Test 2 - Matrix:")
    for row in matrix2:
        print(row)
    print(f"k = {k2}")
    result2 = findK(matrix2, n2, m2, k2)
    print(f"kth element: {result2}")
    print(f"Expected: 6")
    print()

    # Test case 3 - Last element
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n3, m3 = 3, 3
    k3 = 9
    print(f"Test 3 - Matrix:")
    for row in matrix3:
        print(row)
    print(f"k = {k3}")
    result3 = findK(matrix3, n3, m3, k3)
    print(f"kth element: {result3}")
    print(f"Expected: 5")
    print()

    # Test case 4 - First element
    matrix4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n4, m4 = 3, 3
    k4 = 1
    print(f"Test 4 - Matrix:")
    for row in matrix4:
        print(row)
    print(f"k = {k4}")
    result4 = findK(matrix4, n4, m4, k4)
    print(f"kth element: {result4}")
    print(f"Expected: 1")
    print()


if __name__ == "__main__":
    test_findK()

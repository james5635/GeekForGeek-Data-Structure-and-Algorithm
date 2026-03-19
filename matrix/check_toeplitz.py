def is_toeplitz(matrix):
    """
    Check if a given matrix is Toeplitz.
    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
    """
    if not matrix or not matrix[0]:
        return True  # Empty matrix is considered Toeplitz

    rows = len(matrix)
    cols = len(matrix[0])

    # Check each diagonal starting from the first row
    for col in range(cols):
        val = matrix[0][col]
        row, col_idx = 0, col
        while row < rows and col_idx < cols:
            if matrix[row][col_idx] != val:
                return False
            row += 1
            col_idx += 1

    # Check each diagonal starting from the first column (excluding the first row)
    for row in range(1, rows):
        val = matrix[row][0]
        row_idx, col = row, 0
        while row_idx < rows and col < cols:
            if matrix[row_idx][col] != val:
                return False
            row_idx += 1
            col += 1

    return True


# Test cases
if __name__ == "__main__":
    # Test case 1: Toeplitz matrix
    matrix1 = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print("Matrix1 is Toeplitz:", is_toeplitz(matrix1))  # Expected: True

    # Test case 2: Non-Toeplitz matrix
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    print("Matrix2 is Toeplitz:", is_toeplitz(matrix2))  # Expected: False

    # Test case 3: Single element matrix
    matrix3 = [[5]]
    print("Matrix3 is Toeplitz:", is_toeplitz(matrix3))  # Expected: True

    # Test case 4: Single row matrix
    matrix4 = [[1, 2, 3, 4]]
    print("Matrix4 is Toeplitz:", is_toeplitz(matrix4))  # Expected: True

    # Test case 5: Single column matrix
    matrix5 = [[1], [2], [3]]
    print("Matrix5 is Toeplitz:", is_toeplitz(matrix5))  # Expected: True

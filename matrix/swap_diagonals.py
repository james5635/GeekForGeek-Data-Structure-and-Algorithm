def swap_diagonals(matrix):
    """
    Swap the major and minor diagonals of a square matrix.
    The matrix is modified in-place.
    Assumes the matrix is square (n x n).
    """
    n = len(matrix)
    # Swap elements of the two diagonals
    for i in range(n):
        # Swap the i-th element of major diagonal with the i-th element of minor diagonal
        # Major diagonal: (i, i)
        # Minor diagonal: (i, n-1-i)
        matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]


# Test cases
if __name__ == "__main__":
    # Test case 1: 3x3 matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original matrix:")
    for row in matrix1:
        print(row)
    swap_diagonals(matrix1)
    print("\nAfter swapping diagonals:")
    for row in matrix1:
        print(row)
    # Expected:
    # [3, 2, 1]
    # [4, 5, 6]
    # [9, 8, 7]

    # Test case 2: 4x4 matrix
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("\nOriginal matrix:")
    for row in matrix2:
        print(row)
    swap_diagonals(matrix2)
    print("\nAfter swapping diagonals:")
    for row in matrix2:
        print(row)
    # Expected:
    # [4, 2, 3, 1]
    # [5, 7, 6, 8]
    # [9, 11, 10, 12]
    # [16, 14, 15, 13]

    # Test case 3: 1x1 matrix
    matrix3 = [[5]]
    print("\nOriginal matrix:")
    for row in matrix3:
        print(row)
    swap_diagonals(matrix3)
    print("\nAfter swapping diagonals:")
    for row in matrix3:
        print(row)
    # Expected: [[5]] (no change)

def rotate_matrix_90_clockwise(matrix):
    """
    Rotate a given n x n matrix by 90 degrees clockwise without using extra space.

    Approach:
    1. Transpose the matrix (swap elements across the diagonal)
    2. Reverse each row

    Args:
        matrix: 2D list representing the matrix

    Returns:
        None (modifies matrix in-place)
    """
    if not matrix or not matrix[0]:
        return

    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


def rotate_matrix_90_counterclockwise(matrix):
    """
    Rotate a given n x n matrix by 90 degrees counterclockwise without using extra space.

    Approach:
    1. Transpose the matrix (swap elements across the diagonal)
    2. Reverse each column

    Args:
        matrix: 2D list representing the matrix

    Returns:
        None (modifies matrix in-place)
    """
    if not matrix or not matrix[0]:
        return

    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each column
    for j in range(n):
        for i in range(n // 2):
            matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: 3x3 matrix
    print("Test 1: 3x3 matrix rotation")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original matrix:")
    print_matrix(matrix1)

    rotate_matrix_90_clockwise(matrix1)
    print("After 90° clockwise rotation:")
    print_matrix(matrix1)

    # Reset matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_matrix_90_counterclockwise(matrix1)
    print("After 90° counterclockwise rotation:")
    print_matrix(matrix1)

    # Test case 2: 4x4 matrix
    print("Test 2: 4x4 matrix rotation")
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Original matrix:")
    print_matrix(matrix2)

    rotate_matrix_90_clockwise(matrix2)
    print("After 90° clockwise rotation:")
    print_matrix(matrix2)

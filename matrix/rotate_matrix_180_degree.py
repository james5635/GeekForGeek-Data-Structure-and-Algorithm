def rotate_matrix_180(matrix):
    """
    Rotate a given n x n matrix by 180 degrees without using extra space.

    Approach:
    1. Reverse each row of the matrix
    2. Reverse the entire matrix (i.e., reverse the order of rows)

    Args:
        matrix: 2D list representing the matrix

    Returns:
        None (modifies matrix in-place)
    """
    if not matrix or not matrix[0]:
        return

    n = len(matrix)

    # Step 1: Reverse each row
    for i in range(n):
        left, right = 0, n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1

    # Step 2: Reverse the entire matrix (reverse rows)
    top, bottom = 0, n - 1
    while top < bottom:
        matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
        top += 1
        bottom -= 1


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

    rotate_matrix_180(matrix1)
    print("After 180° rotation:")
    print_matrix(matrix1)

    # Test case 2: 4x4 matrix
    print("Test 2: 4x4 matrix rotation")
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Original matrix:")
    print_matrix(matrix2)

    rotate_matrix_180(matrix2)
    print("After 180° rotation:")
    print_matrix(matrix2)

    # Test case 3: 1x1 matrix
    print("Test 3: 1x1 matrix")
    matrix3 = [[42]]
    print("Original matrix:")
    print_matrix(matrix3)

    rotate_matrix_180(matrix3)
    print("After 180° rotation:")
    print_matrix(matrix3)

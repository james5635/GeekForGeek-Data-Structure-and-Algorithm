def get_matrix_minor(matrix, i, j):
    """
    Get the minor of a matrix after removing row i and column j.
    """
    return [row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])]


def determinant(matrix):
    """
    Calculate the determinant of a square matrix using recursive cofactor expansion.
    """
    # Check if matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("Determinant can only be calculated for square matrices")

    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Base case for 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # Recursive case: expand along first row
    det = 0
    for col in range(len(matrix[0])):
        # Calculate cofactor
        minor = get_matrix_minor(matrix, 0, col)
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(minor)
        det += cofactor

    return det


# Test cases
if __name__ == "__main__":
    # Test case 1: 2x2 matrix
    matrix1 = [[1, 2], [3, 4]]
    print(determinant(matrix1))  # Expected: 1*4 - 2*3 = -2

    # Test case 2: 3x3 matrix
    matrix2 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    print(determinant(matrix2))  # Expected: -306

    # Test case 3: 4x4 matrix
    matrix3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(determinant(matrix3))  # Expected: 0 (singular matrix)

    # Test case 4: Identity matrix
    matrix4 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(determinant(matrix4))  # Expected: 1

    # Test case 5: 1x1 matrix
    matrix5 = [[5]]
    print(determinant(matrix5))  # Expected: 5

    # Test case 6: Non-square matrix (should raise error)
    try:
        matrix6 = [[1, 2, 3], [4, 5, 6]]
        determinant(matrix6)
    except ValueError as e:
        print(
            f"Error: {e}"
        )  # Expected: Determinant can only be calculated for square matrices

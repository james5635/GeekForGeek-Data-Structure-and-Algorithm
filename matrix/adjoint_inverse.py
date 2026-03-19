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


def matrix_of_cofactors(matrix):
    """
    Calculate the cofactor matrix of a square matrix.
    """
    if len(matrix) != len(matrix[0]):
        raise ValueError("Cofactor matrix can only be calculated for square matrices")

    n = len(matrix)
    cofactor_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # Get minor
            minor = get_matrix_minor(matrix, i, j)
            # Calculate cofactor
            cofactor_matrix[i][j] = ((-1) ** (i + j)) * determinant(minor)

    return cofactor_matrix


def transpose_matrix(matrix):
    """
    Transpose a matrix (swap rows and columns).
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Create transposed matrix with dimensions cols x rows
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


def adjoint(matrix):
    """
    Calculate the adjoint (adjugate) of a matrix.
    The adjoint is the transpose of the cofactor matrix.
    """
    cofactor_mat = matrix_of_cofactors(matrix)
    adj_mat = transpose_matrix(cofactor_mat)
    return adj_mat


def inverse(matrix):
    """
    Calculate the inverse of a matrix using the formula:
    A^(-1) = (1/det(A)) * adj(A)
    """
    det = determinant(matrix)

    if det == 0:
        raise ValueError(
            "Inverse does not exist for singular matrices (determinant = 0)"
        )

    adj = adjoint(matrix)
    n = len(matrix)

    # Divide each element of adjoint by determinant
    inv = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            inv[i][j] = adj[i][j] / det

    return inv


# Test cases
if __name__ == "__main__":
    # Test case 1: 2x2 matrix
    matrix1 = [[4, 7], [2, 6]]
    print("Original matrix:", matrix1)
    print("Determinant:", determinant(matrix1))  # Expected: 4*6 - 7*2 = 10
    print("Adjoint:", adjoint(matrix1))  # Expected: [[6, -7], [-2, 4]]
    print("Inverse:", inverse(matrix1))  # Expected: [[0.6, -0.7], [-0.2, 0.4]]
    print()

    # Test case 2: 3x3 matrix
    matrix2 = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    print("Original matrix:", matrix2)
    print("Determinant:", determinant(matrix2))  # Expected: 1
    print("Adjoint:", adjoint(matrix2))
    print("Inverse:", inverse(matrix2))
    print()

    # Test case 3: Identity matrix
    matrix3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("Original matrix:", matrix3)
    print("Determinant:", determinant(matrix3))  # Expected: 1
    print("Adjoint:", adjoint(matrix3))  # Expected: same as original
    print("Inverse:", inverse(matrix3))  # Expected: same as original
    print()

    # Test case 4: Singular matrix (should raise error for inverse)
    matrix4 = [[1, 2], [2, 4]]  # Determinant = 0
    print("Original matrix:", matrix4)
    print("Determinant:", determinant(matrix4))  # Expected: 0
    try:
        print("Inverse:", inverse(matrix4))
    except ValueError as e:
        print(f"Error: {e}")  # Expected: Inverse does not exist for singular matrices

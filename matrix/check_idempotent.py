def matrix_multiply(A, B):
    """
    Multiply two matrices A and B.
    Assumes the number of columns in A equals the number of rows in B.
    """
    n = len(A)  # rows of A
    m = len(A[0])  # columns of A
    p = len(B[0])  # columns of B
    # Initialize result matrix with zeros
    result = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
    return result


def is_idempotent(matrix):
    """
    Check if a given square matrix is idempotent.
    A matrix is idempotent if matrix * matrix = matrix.
    """
    n = len(matrix)
    # Check if it's square
    for row in matrix:
        if len(row) != n:
            return False

    # Compute matrix squared
    squared = matrix_multiply(matrix, matrix)

    # Check if squared equals matrix
    for i in range(n):
        for j in range(n):
            if squared[i][j] != matrix[i][j]:
                return False
    return True


# Test cases
if __name__ == "__main__":
    # Example 1: Identity matrix (idempotent)
    matrix1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("Identity matrix is idempotent:", is_idempotent(matrix1))  # Expected: True

    # Example 2: A non-idempotent matrix
    matrix2 = [[1, 2], [3, 4]]
    print(
        "Matrix [[1,2],[3,4]] is idempotent:", is_idempotent(matrix2)
    )  # Expected: False

    # Example 3: Another idempotent matrix (projection matrix)
    matrix3 = [[2, -2, -4], [-1, 3, 4], [1, -2, -3]]
    print(
        "Matrix [[2,-2,-4],[-1,3,4],[1,-2,-3]] is idempotent:", is_idempotent(matrix3)
    )  # Expected: True

    # Example 4: 2x2 idempotent matrix
    matrix4 = [[3, -6], [1, -2]]
    print(
        "Matrix [[3,-6],[1,-2]] is idempotent:", is_idempotent(matrix4)
    )  # Expected: True

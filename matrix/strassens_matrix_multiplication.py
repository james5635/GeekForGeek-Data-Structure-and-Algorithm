import numpy as np


def add_matrix(A, B):
    """Add two matrices"""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result


def subtract_matrix(A, B):
    """Subtract matrix B from matrix A"""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]
    return result


def split_matrix(M):
    """Split a matrix into quarters"""
    n = len(M)
    mid = n // 2

    # Top-left
    A = [row[:mid] for row in M[:mid]]
    # Top-right
    B = [row[mid:] for row in M[:mid]]
    # Bottom-left
    C = [row[:mid] for row in M[mid:]]
    # Bottom-right
    D = [row[mid:] for row in M[mid:]]

    return A, B, C, D


def strassen_matrix_multiply(A, B):
    """
    Strassen's Matrix Multiplication algorithm
    Args:
        A: First square matrix (n x n)
        B: Second square matrix (n x n)
    Returns:
        Result of matrix multiplication A x B
    """
    # Base case: 1x1 matrix
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    # Split matrices into quarters
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Calculate the 7 products recursively
    # P1 = A11 * (B12 - B22)
    B12_minus_B22 = subtract_matrix(B12, B22)
    P1 = strassen_matrix_multiply(A11, B12_minus_B22)

    # P2 = (A11 + A12) * B22
    A11_plus_A12 = add_matrix(A11, A12)
    P2 = strassen_matrix_multiply(A11_plus_A12, B22)

    # P3 = (A21 + A22) * B11
    A21_plus_A22 = add_matrix(A21, A22)
    P3 = strassen_matrix_multiply(A21_plus_A22, B11)

    # P4 = A22 * (B21 - B11)
    B21_minus_B11 = subtract_matrix(B21, B11)
    P4 = strassen_matrix_multiply(A22, B21_minus_B11)

    # P5 = (A11 + A22) * (B11 + B22)
    A11_plus_A22 = add_matrix(A11, A22)
    B11_plus_B22 = add_matrix(B11, B22)
    P5 = strassen_matrix_multiply(A11_plus_A22, B11_plus_B22)

    # P6 = (A12 - A22) * (B21 + B22)
    A12_minus_A22 = subtract_matrix(A12, A22)
    B21_plus_B22 = add_matrix(B21, B22)
    P6 = strassen_matrix_multiply(A12_minus_A22, B21_plus_B22)

    # P7 = (A11 - A21) * (B11 + B12)
    A11_minus_A21 = subtract_matrix(A11, A21)
    B11_plus_B12 = add_matrix(B11, B12)
    P7 = strassen_matrix_multiply(A11_minus_A21, B11_plus_B12)

    # Calculate the four quadrants of the result matrix
    # C11 = P5 + P4 - P2 + P6
    P5_plus_P4 = add_matrix(P5, P4)
    P2_negated = [[-elem for elem in row] for row in P2]
    P5_plus_P4_minus_P2 = add_matrix(P5_plus_P4, P2_negated)
    C11 = add_matrix(P5_plus_P4_minus_P2, P6)

    # C12 = P1 + P2
    C12 = add_matrix(P1, P2)

    # C21 = P3 + P4
    C21 = add_matrix(P3, P4)

    # C22 = P5 + P1 - P3 - P7
    P5_plus_P1 = add_matrix(P5, P1)
    P3_negated = [[-elem for elem in row] for row in P3]
    P7_negated = [[-elem for elem in row] for row in P7]
    P5_plus_P1_minus_P3 = add_matrix(P5_plus_P1, P3_negated)
    C22 = subtract_matrix(P5_plus_P1_minus_P3, P7)

    # Combine quadrants into a single matrix
    n = len(A)
    mid = n // 2
    C = [[0] * n for _ in range(n)]

    # Copy C11 to top-left
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]

    # Copy C12 to top-right
    for i in range(mid):
        for j in range(mid, n):
            C[i][j] = C12[i][j - mid]

    # Copy C21 to bottom-left
    for i in range(mid, n):
        for j in range(mid):
            C[i][j] = C21[i - mid][j]

    # Copy C22 to bottom-right
    for i in range(mid, n):
        for j in range(mid, n):
            C[i][j] = C22[i - mid][j - mid]

    return C


def test_strassen_matrix_multiply():
    # Test case 1: 2x2 matrices
    A1 = [[1, 2], [3, 4]]
    B1 = [[5, 6], [7, 8]]
    print("Test 1 - 2x2 Matrices:")
    print("A:", A1)
    print("B:", B1)
    result1 = strassen_matrix_multiply(A1, B1)
    print("Result (Strassen):", result1)
    # Expected: [[1*5+2*7, 1*6+2*8], [3*5+4*7, 3*6+4*8]] = [[19, 22], [43, 50]]
    expected1 = [[19, 22], [43, 50]]
    print("Expected:", expected1)
    print()

    # Test case 2: 4x4 matrices
    A2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    B2 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]  # Identity matrix
    print("Test 2 - 4x4 Matrices (A * I):")
    print("A:", A2)
    print("B (Identity):", B2)
    result2 = strassen_matrix_multiply(A2, B2)
    print("Result (Strassen):", result2)
    print("Expected: Same as A")
    print()

    # Test case 3: Another 2x2
    A3 = [[2, 3], [4, 5]]
    B3 = [[1, 2], [3, 4]]
    print("Test 3 - 2x2 Matrices:")
    print("A:", A3)
    print("B:", B3)
    result3 = strassen_matrix_multiply(A3, B3)
    print("Result (Strassen):", result3)
    # Expected: [[2*1+3*3, 2*2+3*4], [4*1+5*3, 4*2+5*4]] = [[11, 16], [19, 28]]
    expected3 = [[11, 16], [19, 28]]
    print("Expected:", expected3)
    print()


if __name__ == "__main__":
    test_strassen_matrix_multiply()

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


# Test cases
if __name__ == "__main__":
    # Test case 1: 3x3 matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed1 = transpose_matrix(matrix1)
    print(transposed1)  # Expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    # Test case 2: 2x3 matrix
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    transposed2 = transpose_matrix(matrix2)
    print(transposed2)  # Expected: [[1, 4], [2, 5], [3, 6]]

    # Test case 3: 3x2 matrix
    matrix3 = [[1, 2], [3, 4], [5, 6]]
    transposed3 = transpose_matrix(matrix3)
    print(transposed3)  # Expected: [[1, 3, 5], [2, 4, 6]]

    # Test case 4: Square matrix
    matrix4 = [[1, 2], [3, 4]]
    transposed4 = transpose_matrix(matrix4)
    print(transposed4)  # Expected: [[1, 3], [2, 4]]

    # Test case 5: Single row
    matrix5 = [[1, 2, 3, 4]]
    transposed5 = transpose_matrix(matrix5)
    print(transposed5)  # Expected: [[1], [2], [3], [4]]

    # Test case 6: Single column
    matrix6 = [[1], [2], [3]]
    transposed6 = transpose_matrix(matrix6)
    print(transposed6)  # Expected: [[1, 2, 3]]

    # Test case 7: Empty matrix
    print(transpose_matrix([]))  # Expected: []
    print(transpose_matrix([[]]))  # Expected: []

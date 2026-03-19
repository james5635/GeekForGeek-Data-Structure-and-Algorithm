def modifyBooleanMatrix(matrix):
    """
    Modify a boolean matrix such that if a cell matrix[i][j] is 1,
    then all the cells in its ith row and jth column become 1.
    Args:
        matrix: 2D list of booleans or integers (0/1)
    Returns:
        Modified matrix
    """
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    # Create temporary arrays to store row and column flags
    row_flag = [False] * rows
    col_flag = [False] * cols

    # First pass: identify which rows and columns need to be modified
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_flag[i] = True
                col_flag[j] = True

    # Second pass: modify the matrix based on flags
    for i in range(rows):
        for j in range(cols):
            if row_flag[i] or col_flag[j]:
                matrix[i][j] = 1

    return matrix


def test_boolean_matrix():
    # Test case 1
    matrix1 = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(f"Test 1 - Original Matrix:")
    for row in matrix1:
        print(row)
    result1 = modifyBooleanMatrix(
        [row[:] for row in matrix1]
    )  # Copy to preserve original
    print(f"Modified Matrix:")
    for row in result1:
        print(row)
    print()

    # Test case 2
    matrix2 = [[0, 0, 0], [0, 0, 1]]
    print(f"Test 2 - Original Matrix:")
    for row in matrix2:
        print(row)
    result2 = modifyBooleanMatrix([row[:] for row in matrix2])
    print(f"Modified Matrix:")
    for row in result2:
        print(row)
    print()

    # Test case 3
    matrix3 = [[1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]]
    print(f"Test 3 - Original Matrix:")
    for row in matrix3:
        print(row)
    result3 = modifyBooleanMatrix([row[:] for row in matrix3])
    print(f"Modified Matrix:")
    for row in result3:
        print(row)
    print()


if __name__ == "__main__":
    test_boolean_matrix()

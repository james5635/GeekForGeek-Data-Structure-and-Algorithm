def add_matrices(matrix1, matrix2):
    """
    Add two matrices of the same dimensions.
    Returns the resulting matrix.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")

    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: 2x2 matrices
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    result = add_matrices(m1, m2)
    print(result)  # Expected: [[6, 8], [10, 12]]

    # Test case 2: 3x3 matrices
    m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m4 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    result2 = add_matrices(m3, m4)
    print(result2)  # Expected: [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

    # Test case 3: Single element matrices
    m5 = [[5]]
    m6 = [[3]]
    result3 = add_matrices(m5, m6)
    print(result3)  # Expected: [[8]]

    # Test case 4: Different dimensions (should raise error)
    try:
        m7 = [[1, 2], [3, 4]]
        m8 = [[1, 2, 3], [4, 5, 6]]
        add_matrices(m7, m8)
    except ValueError as e:
        print(f"Error: {e}")  # Expected: Matrices must have the same dimensions

def print_boundary_elements(matrix):
    """
    Print the boundary elements of a given matrix.
    The matrix is a 2D list with R rows and C columns.
    Boundary elements are those in the first row, last row, first column, and last column.
    """
    if not matrix or not matrix[0]:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    # Print first row
    for j in range(cols):
        print(matrix[0][j], end=" ")

    # Print last column (excluding first and last row)
    for i in range(1, rows - 1):
        print(matrix[i][cols - 1], end=" ")

    # Print last row (if there is more than one row)
    if rows > 1:
        for j in range(cols - 1, -1, -1):
            print(matrix[rows - 1][j], end=" ")

    # Print first column (excluding first and last row, and if there is more than one column)
    if cols > 1:
        for i in range(rows - 2, 0, -1):
            print(matrix[i][0], end=" ")


# Alternatively, we can return a list of boundary elements for testing.
def get_boundary_elements(matrix):
    """
    Return the boundary elements of a given matrix as a list.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # First row
    for j in range(cols):
        result.append(matrix[0][j])

    # Last column (excluding first and last row)
    for i in range(1, rows - 1):
        result.append(matrix[i][cols - 1])

    # Last row (if there is more than one row) in reverse
    if rows > 1:
        for j in range(cols - 1, -1, -1):
            result.append(matrix[rows - 1][j])

    # First column (excluding first and last row) in reverse, if there is more than one column
    if cols > 1:
        for i in range(rows - 2, 0, -1):
            result.append(matrix[i][0])

    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: 4x4 matrix
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Boundary elements (as list):", get_boundary_elements(matrix1))
    # Expected: [1,2,3,4,8,12,16,15,14,13,9,5]

    # Test case 2: 3x3 matrix
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Boundary elements (as list):", get_boundary_elements(matrix2))
    # Expected: [1,2,3,6,9,8,7,4]

    # Test case 3: 1x1 matrix
    matrix3 = [[5]]
    print("Boundary elements (as list):", get_boundary_elements(matrix3))
    # Expected: [5]

    # Test case 4: 1x4 matrix
    matrix4 = [[1, 2, 3, 4]]
    print("Boundary elements (as list):", get_boundary_elements(matrix4))
    # Expected: [1,2,3,4]

    # Test case 5: 4x1 matrix
    matrix5 = [[1], [2], [3], [4]]
    print("Boundary elements (as list):", get_boundary_elements(matrix5))
    # Expected: [1,2,3,4]

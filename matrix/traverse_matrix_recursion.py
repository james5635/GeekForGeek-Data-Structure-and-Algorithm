def traverse_matrix_recursion(matrix, row=0, col=0):
    """
    Traverse a matrix using recursion and return elements in row-major order.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # Base case: if we've processed all rows
    if row >= rows:
        return []

    # If we've reached end of current row, move to next row
    if col >= cols:
        return traverse_matrix_recursion(matrix, row + 1, 0)

    # Current element plus recursion for next column
    return [matrix[row][col]] + traverse_matrix_recursion(matrix, row, col + 1)


# Test cases
if __name__ == "__main__":
    # Test case 1: 3x3 matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = traverse_matrix_recursion(matrix1)
    print(result1)  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test case 2: 2x2 matrix
    matrix2 = [[1, 2], [3, 4]]
    result2 = traverse_matrix_recursion(matrix2)
    print(result2)  # Expected: [1, 2, 3, 4]

    # Test case 3: Single row
    matrix3 = [[1, 2, 3, 4]]
    result3 = traverse_matrix_recursion(matrix3)
    print(result3)  # Expected: [1, 2, 3, 4]

    # Test case 4: Single column
    matrix4 = [[1], [2], [3]]
    result4 = traverse_matrix_recursion(matrix4)
    print(result4)  # Expected: [1, 2, 3]

    # Test case 5: Empty matrix
    result5 = traverse_matrix_recursion([])
    print(result5)  # Expected: []

    # Test case 6: Matrix with empty row
    result6 = traverse_matrix_recursion([[]])
    print(result6)  # Expected: []

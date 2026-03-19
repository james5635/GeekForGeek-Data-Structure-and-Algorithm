def sort_matrix(matrix):
    """
    Sort all elements of a matrix in ascending order and reshape to original dimensions.
    """
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    # Flatten the matrix
    flat = [element for row in matrix for element in row]

    # Sort the flattened list
    flat.sort()

    # Reshape back to original dimensions
    sorted_matrix = []
    for i in range(rows):
        sorted_matrix.append(flat[i * cols : (i + 1) * cols])

    return sorted_matrix


# Test cases
if __name__ == "__main__":
    # Test case 1: 3x3 matrix
    matrix1 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    sorted1 = sort_matrix(matrix1)
    print(sorted1)  # Expected: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Test case 2: 2x2 matrix
    matrix2 = [[4, 3], [2, 1]]
    sorted2 = sort_matrix(matrix2)
    print(sorted2)  # Expected: [[1, 2], [3, 4]]

    # Test case 3: Single row
    matrix3 = [[5, 1, 3, 2, 4]]
    sorted3 = sort_matrix(matrix3)
    print(sorted3)  # Expected: [[1, 2, 3, 4, 5]]

    # Test case 4: Single column
    matrix4 = [[5], [1], [3], [2], [4]]
    sorted4 = sort_matrix(matrix4)
    print(sorted4)  # Expected: [[1], [2], [3], [4], [5]]

    # Test case 5: Empty matrix
    print(sort_matrix([]))  # Expected: []
    print(sort_matrix([[]]))  # Expected: [[]]

def count_transformations_to_equal(mat1, mat2):
    """
    Find the number of transformations required to make two matrices equal.
    A transformation is defined as changing a single element in either matrix.

    Args:
        mat1: First matrix (2D list)
        mat2: Second matrix (2D list)

    Returns:
        int: Number of transformations required, or -1 if matrices have different dimensions
    """
    # Check if matrices have same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return -1

    rows = len(mat1)
    cols = len(mat1[0])
    transformations = 0

    # Count positions where elements differ
    for i in range(rows):
        for j in range(cols):
            if mat1[i][j] != mat2[i][j]:
                transformations += 1

    return transformations


def count_transformations_to_equal_with_operations(mat1, mat2):
    """
    Find the number of transformations and show what needs to be changed.

    Args:
        mat1: First matrix (2D list)
        mat2: Second matrix (2D list)

    Returns:
        tuple: (number_of_transformations, list_of_changes)
               where list_of_changes contains tuples ((i,j), value_from_mat1, value_from_mat2)
    """
    # Check if matrices have same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return -1, []

    rows = len(mat1)
    cols = len(mat1[0])
    transformations = 0
    changes = []

    # Count positions where elements differ
    for i in range(rows):
        for j in range(cols):
            if mat1[i][j] != mat2[i][j]:
                transformations += 1
                changes.append(((i, j), mat1[i][j], mat2[i][j]))

    return transformations, changes


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Equal matrices
    print("Test 1: Equal matrices")
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matrix 1:")
    print_matrix(mat1)
    print("Matrix 2:")
    print_matrix(mat2)

    result = count_transformations_to_equal(mat1, mat2)
    print(f"Number of transformations required: {result}")
    print()

    # Test case 2: Different matrices
    print("Test 2: Different matrices")
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[1, 2, 4], [4, 5, 6], [7, 8, 9]]

    print("Matrix 1:")
    print_matrix(mat1)
    print("Matrix 2:")
    print_matrix(mat2)

    result, changes = count_transformations_to_equal_with_operations(mat1, mat2)
    print(f"Number of transformations required: {result}")
    print("Changes needed:")
    for pos, val1, val2 in changes:
        print(f"  Position {pos}: {val1} -> {val2}")
    print()

    # Test case 3: Completely different
    print("Test 3: Completely different matrices")
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]

    print("Matrix 1:")
    print_matrix(mat1)
    print("Matrix 2:")
    print_matrix(mat2)

    result, changes = count_transformations_to_equal_with_operations(mat1, mat2)
    print(f"Number of transformations required: {result}")
    print("Changes needed:")
    for pos, val1, val2 in changes:
        print(f"  Position {pos}: {val1} -> {val2}")
    print()

    # Test case 4: Different dimensions
    print("Test 4: Different dimensions")
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[1, 2], [3, 4], [5, 6]]

    print("Matrix 1:")
    print_matrix(mat1)
    print("Matrix 2:")
    print_matrix(mat2)

    result = count_transformations_to_equal(mat1, mat2)
    print(
        f"Number of transformations required: {result} (Expected: -1 for different dimensions)"
    )
    print()

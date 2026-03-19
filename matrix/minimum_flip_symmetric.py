def min_flip_to_make_symmetric(matrix):
    """
    Find the minimum number of flips required to make a binary matrix symmetric.
    A matrix is symmetric if matrix[i][j] == matrix[j][i] for all i, j.

    Args:
        matrix: 2D list of 0s and 1s (binary matrix)

    Returns:
        int: Minimum number of flips required
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # For a matrix to be symmetric, it must be square
    if rows != cols:
        return -1  # Cannot make non-square matrix symmetric in the usual sense

    flips = 0
    # Only need to check elements above or below the diagonal
    # Comparing matrix[i][j] with matrix[j][i] for i < j
    for i in range(rows):
        for j in range(
            i + 1, cols
        ):  # Start from i+1 to avoid double counting and diagonal
            if matrix[i][j] != matrix[j][i]:
                flips += 1  # One flip needed to make them equal

    return flips


def min_flip_to_make_symmetric_with_details(matrix):
    """
    Find the minimum number of flips and show which elements need to be flipped.

    Args:
        matrix: 2D list of 0s and 1s (binary matrix)

    Returns:
        tuple: (minimum_flips, list_of_positions_to_flip)
    """
    if not matrix or not matrix[0]:
        return 0, []

    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        return -1, []

    flips = 0
    positions = []

    # Only need to check elements above or below the diagonal
    for i in range(rows):
        for j in range(i + 1, cols):
            if matrix[i][j] != matrix[j][i]:
                flips += 1
                # We can flip either position; let's choose to flip the lower triangle
                positions.append(
                    (j, i)
                )  # Position (j,i) needs to be flipped to match (i,j)

    return flips, positions


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Already symmetric matrix
    print("Test 1: Already symmetric matrix")
    matrix1 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

    print("Matrix:")
    print_matrix(matrix1)

    result1 = min_flip_to_make_symmetric(matrix1)
    result1_details, positions1 = min_flip_to_make_symmetric_with_details(matrix1)

    print(f"Minimum flips required: {result1}")
    print(f"Minimum flips required (with details): {result1_details}")
    if positions1:
        print("Positions to flip (row, col):")
        for pos in positions1:
            print(f"  {pos}")
    print()

    # Test case 2: Needs flips
    print("Test 2: Matrix needing flips")
    matrix2 = [[1, 0, 1], [1, 1, 0], [0, 0, 1]]

    print("Matrix:")
    print_matrix(matrix2)

    result2 = min_flip_to_make_symmetric(matrix2)
    result2_details, positions2 = min_flip_to_make_symmetric_with_details(matrix2)

    print(f"Minimum flips required: {result2}")
    print(f"Minimum flips required (with details): {result2_details}")
    if positions2:
        print("Positions to flip (row, col):")
        for pos in positions2:
            print(
                f"  {pos} (flip matrix[{pos[0]}][{pos[1]}] from {matrix2[pos[0]][pos[1]]} to {matrix2[pos[1]][pos[0]]})"
            )
    print()

    # Test case 3: All zeros except one mismatch
    print("Test 3: Simple mismatch")
    matrix3 = [[0, 1], [0, 0]]

    print("Matrix:")
    print_matrix(matrix3)

    result3 = min_flip_to_make_symmetric(matrix3)
    result3_details, positions3 = min_flip_to_make_symmetric_with_details(matrix3)

    print(f"Minimum flips required: {result3}")
    print(f"Minimum flips required (with details): {result3_details}")
    if positions3:
        print("Positions to flip (row, col):")
        for pos in positions3:
            print(
                f"  {pos} (flip matrix[{pos[0]}][{pos[1]}] from {matrix3[pos[0]][pos[1]]} to {matrix3[pos[1]][pos[0]]})"
            )
    print()

    # Test case 4: Non-square matrix
    print("Test 4: Non-square matrix")
    matrix4 = [[1, 0, 1], [0, 1, 0]]

    print("Matrix:")
    print_matrix(matrix4)

    result4 = min_flip_to_make_symmetric(matrix4)
    print(f"Minimum flips required: {result4} (Expected: -1 for non-square matrix)")
    print()

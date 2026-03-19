def largest_subsquare_surrounded_by_X(matrix):
    """
    Find the size of the largest subsquare surrounded by 'X' in a given matrix.

    Args:
        matrix: 2D list of characters containing only 'X' and 'O'

    Returns:
        int: Size (side length) of the largest subsquare surrounded by 'X'
             Returns 0 if no such square exists
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Create auxiliary arrays to store horizontal and vertical counts of consecutive 'X's
    hor = [[0] * cols for _ in range(rows)]
    ver = [[0] * cols for _ in range(rows)]

    # Fill hor and ver arrays
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "X":
                hor[i][j] = 1 if j == 0 else hor[i][j - 1] + 1
                ver[i][j] = 1 if i == 0 else ver[i - 1][j] + 1
            else:
                hor[i][j] = 0
                ver[i][j] = 0

    max_size = 0

    # Start from bottom-right corner and move towards top-left
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            # Find the smaller of hor[i][j] and ver[i][j]
            small = min(hor[i][j], ver[i][j])

            # Check for decreasing sizes until we find a valid square or exceed current max
            while small > max_size:
                # Check if left vertical line and top horizontal line are sufficient
                # Left vertical line: at column (j - small + 1), from row (i - small + 1) to i
                # Top horizontal line: at row (i - small + 1), from column (j - small + 1) to j
                if ver[i][j - small + 1] >= small and hor[i - small + 1][j] >= small:
                    max_size = small
                small -= 1

    return max_size


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: All X matrix
    print("Test 1: 3x3 all X matrix")
    matrix1 = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
    print("Matrix:")
    print_matrix(matrix1)
    result = largest_subsquare_surrounded_by_X(matrix1)
    print(f"Largest subsquare surrounded by X: {result}")
    print()

    # Test case 2: Example from GeeksforGeeks
    print("Test 2: Example from GeeksforGeeks")
    matrix2 = [
        ["X", "O", "X", "X", "X", "X"],
        ["X", "O", "X", "X", "O", "X"],
        ["X", "X", "X", "O", "O", "X"],
        ["O", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "O", "X", "O"],
        ["O", "O", "X", "O", "O", "O"],
    ]
    print("Matrix:")
    print_matrix(matrix2)
    result = largest_subsquare_surrounded_by_X(matrix2)
    print(f"Largest subsquare surrounded by X: {result} (Expected: 4)")
    print()

    # Test case 3: No X
    print("Test 3: Matrix with no X")
    matrix3 = [["O", "O"], ["O", "O"]]
    print("Matrix:")
    print_matrix(matrix3)
    result = largest_subsquare_surrounded_by_X(matrix3)
    print(f"Largest subsquare surrounded by X: {result}")
    print()

    # Test case 4: Single X
    print("Test 4: Single X")
    matrix4 = [["X"]]
    print("Matrix:")
    print_matrix(matrix4)
    result = largest_subsquare_surrounded_by_X(matrix4)
    print(f"Largest subsquare surrounded by X: {result}")
    print()

    # Test case 5: 2x2 with border X but interior O (should still count as surrounded by X)
    print("Test 5: 2x2 with border X")
    matrix5 = [["X", "X"], ["X", "X"]]
    print("Matrix:")
    print_matrix(matrix5)
    result = largest_subsquare_surrounded_by_X(matrix5)
    print(f"Largest subsquare surrounded by X: {result}")
    print()

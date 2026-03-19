def is_magic_square(matrix):
    """
    Check if a given matrix is a magic square.
    A magic square is an n x n matrix of distinct positive integers from 1 to n²
    where the sum of any row, column, or diagonal is always the same number.

    Args:
        matrix: 2D list of integers

    Returns:
        bool: True if matrix is a magic square, False otherwise
    """
    if not matrix or not matrix[0]:
        return False

    n = len(matrix)

    # Check if it's a square matrix
    for row in matrix:
        if len(row) != n:
            return False

    # Calculate the expected sum (sum of first row)
    expected_sum = sum(matrix[0])

    # Check all rows
    for i in range(n):
        if sum(matrix[i]) != expected_sum:
            return False

    # Check all columns
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != expected_sum:
            return False

    # Check main diagonal
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    if main_diag_sum != expected_sum:
        return False

    # Check secondary diagonal
    secondary_diag_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if secondary_diag_sum != expected_sum:
        return False

    # Check if all numbers from 1 to n² are present exactly once
    flat_list = [num for row in matrix for num in row]
    expected_numbers = set(range(1, n * n + 1))
    actual_numbers = set(flat_list)

    if actual_numbers != expected_numbers:
        return False

    # Check for duplicates (though set comparison above should catch this)
    if len(flat_list) != len(set(flat_list)):
        return False

    return True


def generate_magic_square_odd(n):
    """
    Generate a magic square of odd order using the Siamese method.

    Args:
        n: Odd integer representing the size of the matrix

    Returns:
        2D list representing the magic square
    """
    if n % 2 == 0:
        raise ValueError("This method only works for odd-order magic squares")

    # Initialize matrix with zeros
    magic_square = [[0] * n for _ in range(n)]

    # Start position for number 1
    i, j = 0, n // 2

    # Fill the magic square
    for num in range(1, n * n + 1):
        magic_square[i][j] = num

        # Calculate next position
        next_i, next_j = (i - 1) % n, (j + 1) % n

        # If the cell is already filled, move down instead
        if magic_square[next_i][next_j] != 0:
            i = (i + 1) % n
        else:
            i, j = next_i, next_j

    return magic_square


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(f"{elem:2d}" for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Known magic square (3x3)
    print("Test 1: 3x3 magic square")
    matrix1 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

    print("Matrix:")
    print_matrix(matrix1)
    result1 = is_magic_square(matrix1)
    print(f"Is magic square: {result1} (Expected: True)")
    print()

    # Test case 2: Another magic square (3x3)
    print("Test 2: Another 3x3 magic square")
    matrix2 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

    print("Matrix:")
    print_matrix(matrix2)
    result2 = is_magic_square(matrix2)
    print(f"Is magic square: {result2} (Expected: True)")
    print()

    # Test case 3: Not a magic square
    print("Test 3: Not a magic square")
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matrix:")
    print_matrix(matrix3)
    result3 = is_magic_square(matrix3)
    print(f"Is magic square: {result3} (Expected: False)")
    print()

    # Test case 4: Not a square matrix
    print("Test 4: Not a square matrix")
    matrix4 = [[1, 2, 3], [4, 5, 6]]

    print("Matrix:")
    print_matrix(matrix4)
    result4 = is_magic_square(matrix4)
    print(f"Is magic square: {result4} (Expected: False)")
    print()

    # Test case 5: Generate magic square using Siamese method
    print("Test 5: Generate 5x5 magic square using Siamese method")
    try:
        generated = generate_magic_square_odd(5)
        print("Generated 5x5 magic square:")
        print_matrix(generated)
        result5 = is_magic_square(generated)
        print(f"Is generated square magic: {result5} (Expected: True)")
    except ValueError as e:
        print(f"Error: {e}")
    print()

    # Test case 6: Try to generate even order magic square (should fail)
    print("Test 6: Try to generate 4x4 magic square using Siamese method")
    try:
        generated = generate_magic_square_odd(4)
        print("Generated 4x4 magic square:")
        print_matrix(generated)
    except ValueError as e:
        print(f"Expected error: {e}")
    print()

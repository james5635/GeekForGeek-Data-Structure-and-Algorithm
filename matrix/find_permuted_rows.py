def find_permuted_rows(matrix, row):
    """
    Find all rows in a matrix that are permutations of a given row.

    Args:
        matrix: 2D list of integers
        row: Index of the row to check permutations against

    Returns:
        List of row indices that are permutations of the given row
    """
    if not matrix or not matrix[0] or row < 0 or row >= len(matrix):
        return []

    cols = len(matrix[0])
    target_row = matrix[row]

    # Create frequency map for the target row
    from collections import Counter

    target_freq = Counter(target_row)

    result = []

    # Check each row
    for i in range(len(matrix)):
        if i == row:
            continue  # Skip the same row

        # Check if current row is permutation of target row
        if Counter(matrix[i]) == target_freq:
            result.append(i)

    return result


def find_permuted_rows_optimized(matrix, row):
    """
    Optimized version using sorting instead of Counter for better performance
    when rows are long but number of distinct elements is small.

    Args:
        matrix: 2D list of integers
        row: Index of the row to check permutations against

    Returns:
        List of row indices that are permutations of the given row
    """
    if not matrix or not matrix[0] or row < 0 or row >= len(matrix):
        return []

    target_row = sorted(matrix[row])
    result = []

    # Check each row
    for i in range(len(matrix)):
        if i == row:
            continue  # Skip the same row

        # Check if current row is permutation of target row
        if sorted(matrix[i]) == target_row:
            result.append(i)

    return result


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Example with permutations
    print("Test 1: Matrix with permuted rows")
    matrix1 = [[1, 2, 3, 4], [4, 3, 2, 1], [2, 1, 4, 3], [5, 6, 7, 8]]
    row_to_check = 0

    print("Matrix:")
    print_matrix(matrix1)
    print(f"Checking permutations of row {row_to_check}: {matrix1[row_to_check]}")

    result1 = find_permuted_rows(matrix1, row_to_check)
    result1_opt = find_permuted_rows_optimized(matrix1, row_to_check)

    print(f"Permuted rows (using Counter): {result1}")
    print(f"Permuted rows (using sorting): {result1_opt}")
    print()

    # Test case 2: No permutations
    print("Test 2: No permuted rows")
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row_to_check = 0

    print("Matrix:")
    print_matrix(matrix2)
    print(f"Checking permutations of row {row_to_check}: {matrix2[row_to_check]}")

    result2 = find_permuted_rows(matrix2, row_to_check)
    result2_opt = find_permuted_rows_optimized(matrix2, row_to_check)

    print(f"Permuted rows (using Counter): {result2}")
    print(f"Permuted rows (using sorting): {result2_opt}")
    print()

    # Test case 3: All rows are permutations
    print("Test 3: All rows are permutations")
    matrix3 = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    row_to_check = 0

    print("Matrix:")
    print_matrix(matrix3)
    print(f"Checking permutations of row {row_to_check}: {matrix3[row_to_check]}")

    result3 = find_permuted_rows(matrix3, row_to_check)
    result3_opt = find_permuted_rows_optimized(matrix3, row_to_check)

    print(f"Permuted rows (using Counter): {result3}")
    print(f"Permuted rows (using sorting): {result3_opt}")
    print()

    # Test case 4: With duplicate elements
    print("Test 4: Matrix with duplicate elements")
    matrix4 = [[1, 2, 2, 3], [3, 2, 1, 2], [2, 1, 2, 3], [4, 5, 6, 7]]
    row_to_check = 0

    print("Matrix:")
    print_matrix(matrix4)
    print(f"Checking permutations of row {row_to_check}: {matrix4[row_to_check]}")

    result4 = find_permuted_rows(matrix4, row_to_check)
    result4_opt = find_permuted_rows_optimized(matrix4, row_to_check)

    print(f"Permuted rows (using Counter): {result4}")
    print(f"Permuted rows (using sorting): {result4_opt}")
    print()

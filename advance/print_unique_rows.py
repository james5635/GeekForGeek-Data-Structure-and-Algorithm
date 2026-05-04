"""
Print Unique Rows in a Binary Matrix

Given a binary matrix, print all unique rows of the given matrix.

Approach: Use a HashSet to store string representations of each row.
If a row is already in the set, skip it. Otherwise, print it and add to the set.

Time Complexity: O(ROW * COL)
Auxiliary Space: O(ROW * COL)

Source: https://www.geeksforgeeks.org/dsa/print-unique-rows/
"""


def find_unique_rows(matrix):
    """Print all unique rows in a given binary matrix.

    Args:
        matrix: A 2D list of binary values (0s and 1s).
    """
    if not matrix or not matrix[0]:
        return

    seen = set()
    row_count = len(matrix)
    col_count = len(matrix[0])

    for i in range(row_count):
        row_str = "".join(str(val) for val in matrix[i])
        if row_str not in seen:
            seen.add(row_str)
            print(" ".join(str(val) for val in matrix[i]))


def find_unique_rows_return(matrix):
    """Return a list of unique rows in a given binary matrix.

    Args:
        matrix: A 2D list of binary values (0s and 1s).

    Returns:
        A list of unique rows (each row is a list of integers).
    """
    if not matrix or not matrix[0]:
        return []

    seen = set()
    unique_rows = []

    for row in matrix:
        row_str = "".join(str(val) for val in row)
        if row_str not in seen:
            seen.add(row_str)
            unique_rows.append(row)

    return unique_rows


if __name__ == "__main__":
    print("Test Case 1:")
    mat1 = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0],
    ]
    print("Input matrix:")
    for row in mat1:
        print(row)
    print("Unique rows:")
    find_unique_rows(mat1)

    print("\nTest Case 2:")
    mat2 = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]
    print("Input matrix:")
    for row in mat2:
        print(row)
    print("Unique rows:")
    find_unique_rows(mat2)

    print("\nTest Case 3 (using return function):")
    mat3 = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
    ]
    unique = find_unique_rows_return(mat3)
    print("Unique rows returned:")
    for row in unique:
        print(row)

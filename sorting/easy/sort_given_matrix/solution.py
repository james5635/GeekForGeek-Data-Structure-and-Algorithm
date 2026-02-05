"""
Sort Given Matrix

Problem Description:
    Given a n x n matrix, sort the matrix row-wise and column-wise.
    After sorting, all rows and columns should be in non-decreasing order.

Algorithm:
    - Approach 1: Flatten, sort, and rebuild
        1. Extract all elements from matrix into a 1D array
        2. Sort the 1D array
        3. Fill matrix back in row-major order

    - Approach 2: Sort each row, then sort each column (not optimal)

Time Complexity: O(n² log(n²)) = O(n² log n)
    - Flattening: O(n²)
    - Sorting n² elements: O(n² log(n²))
    - Rebuilding: O(n²)

Space Complexity: O(n²)
    - For storing the flattened array
"""


def sort_matrix_flatten(matrix):
    """
    Sort matrix by flattening, sorting, and rebuilding.

    Args:
        matrix: n x n 2D list

    Returns:
        list: Sorted n x n matrix
    """
    if not matrix or not matrix[0]:
        return matrix

    n = len(matrix)

    # Flatten matrix
    flat = []
    for row in matrix:
        flat.extend(row)

    # Sort flattened array
    flat.sort()

    # Rebuild matrix
    sorted_matrix = []
    for i in range(n):
        row = flat[i * n : (i + 1) * n]
        sorted_matrix.append(row)

    return sorted_matrix


def sort_matrix_snake_pattern(matrix):
    """
    Sort matrix in snake pattern (alternating row directions).
    First row left-to-right, second row right-to-left, etc.

    Args:
        matrix: n x n 2D list

    Returns:
        list: Matrix sorted in snake pattern
    """
    if not matrix or not matrix[0]:
        return matrix

    n = len(matrix)

    # Flatten and sort
    flat = []
    for row in matrix:
        flat.extend(row)
    flat.sort()

    # Rebuild in snake pattern
    sorted_matrix = []
    idx = 0
    for i in range(n):
        if i % 2 == 0:
            # Left to right
            sorted_matrix.append(flat[idx : idx + n])
        else:
            # Right to left
            sorted_matrix.append(flat[idx : idx + n][::-1])
        idx += n

    return sorted_matrix


def print_matrix(matrix, title=""):
    """Helper function to print matrix."""
    if title:
        print(title)
    for row in matrix:
        print(row)
    print()


if __name__ == "__main__":
    # Test Case 1: 3x3 matrix
    matrix1 = [[5, 4, 7], [1, 3, 8], [2, 9, 6]]
    print("Test Case 1: 3x3 Matrix")
    print_matrix(matrix1, "Original:")
    print_matrix(sort_matrix_flatten(matrix1), "Sorted:")

    # Test Case 2: 2x2 matrix
    matrix2 = [[4, 1], [3, 2]]
    print("Test Case 2: 2x2 Matrix")
    print_matrix(matrix2, "Original:")
    print_matrix(sort_matrix_flatten(matrix2), "Sorted:")

    # Test Case 3: 4x4 matrix
    matrix3 = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    print("Test Case 3: 4x4 Matrix")
    print_matrix(matrix3, "Original:")
    print_matrix(sort_matrix_flatten(matrix3), "Sorted:")

    # Test Case 4: Single element
    matrix4 = [[5]]
    print("Test Case 4: 1x1 Matrix")
    print_matrix(matrix4, "Original:")
    print_matrix(sort_matrix_flatten(matrix4), "Sorted:")

    # Test Case 5: Snake pattern
    matrix5 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    print("Test Case 5: Snake Pattern")
    print_matrix(matrix5, "Original:")
    print_matrix(sort_matrix_snake_pattern(matrix5), "Snake Pattern Sorted:")

    # Test Case 6: Already sorted
    matrix6 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Test Case 6: Already Sorted")
    print_matrix(matrix6, "Original:")
    print_matrix(sort_matrix_flatten(matrix6), "Sorted:")

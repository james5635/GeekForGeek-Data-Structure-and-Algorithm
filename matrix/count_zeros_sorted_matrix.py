def count_zeros_in_sorted_matrix(matrix):
    """
    Count zeros in a row-wise and column-wise sorted binary matrix.

    Approach:
    Start from top-right corner and move:
    - If current element is 0, then all elements in current column below it are also 0
      (since column-wise sorted), so add (number of rows - current row) to count and move left
    - If current element is 1, then move down (since we need to find 0s)

    Args:
        matrix: 2D list of 0s and 1s, sorted row-wise and column-wise

    Returns:
        int: Count of zeros in the matrix
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from top-right corner
    row = 0
    col = cols - 1
    count = 0

    while row < rows and col >= 0:
        if matrix[row][col] == 0:
            # All elements below in this column are 0 (column-wise sorted)
            count += (
                col + 1
            )  # Add all elements from column 0 to current col in this row
            row += 1  # Move down
        else:
            # Current element is 1, move left to find 0s
            col -= 1

    return count


def count_zeros_brute_force(matrix):
    """Brute force approach for verification"""
    if not matrix or not matrix[0]:
        return 0

    count = 0
    for row in matrix:
        count += row.count(0)
    return count


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Example matrix
    print("Test 1: Example matrix")
    matrix1 = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    print("Matrix:")
    print_matrix(matrix1)
    result = count_zeros_in_sorted_matrix(matrix1)
    brute_result = count_zeros_brute_force(matrix1)
    print(f"Count of zeros (optimized): {result}")
    print(f"Count of zeros (brute force): {brute_result}")
    print(f"Match: {result == brute_result}")
    print()

    # Test case 2: All zeros
    print("Test 2: All zeros matrix")
    matrix2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print("Matrix:")
    print_matrix(matrix2)
    result = count_zeros_in_sorted_matrix(matrix2)
    brute_result = count_zeros_brute_force(matrix2)
    print(f"Count of zeros (optimized): {result}")
    print(f"Count of zeros (brute force): {brute_result}")
    print(f"Match: {result == brute_result}")
    print()

    # Test case 3: All ones
    print("Test 3: All ones matrix")
    matrix3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print("Matrix:")
    print_matrix(matrix3)
    result = count_zeros_in_sorted_matrix(matrix3)
    brute_result = count_zeros_brute_force(matrix3)
    print(f"Count of zeros (optimized): {result}")
    print(f"Count of zeros (brute force): {brute_result}")
    print(f"Match: {result == brute_result}")
    print()

    # Test case 4: Single element
    print("Test 4: Single element matrix (0)")
    matrix4 = [[0]]
    print("Matrix:")
    print_matrix(matrix4)
    result = count_zeros_in_sorted_matrix(matrix4)
    brute_result = count_zeros_brute_force(matrix4)
    print(f"Count of zeros (optimized): {result}")
    print(f"Count of zeros (brute force): {brute_result}")
    print(f"Match: {result == brute_result}")
    print()

    # Test case 5: Single element
    print("Test 5: Single element matrix (1)")
    matrix5 = [[1]]
    print("Matrix:")
    print_matrix(matrix5)
    result = count_zeros_in_sorted_matrix(matrix5)
    brute_result = count_zeros_brute_force(matrix5)
    print(f"Count of zeros (optimized): {result}")
    print(f"Count of zeros (brute force): {brute_result}")
    print(f"Match: {result == brute_result}")
    print()

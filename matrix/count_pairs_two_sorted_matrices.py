def count_pairs_two_sorted_matrices(mat1, mat2, n, x):
    """
    Count pairs from two sorted matrices such that sum of pair equals given value x.
    Each matrix is sorted row-wise and column-wise.

    Approach:
    Use two-pointer technique: start from top-right of mat1 and bottom-left of mat2
    or vice versa, depending on the sorting order.

    Args:
        mat1: First n x n matrix (sorted row-wise and column-wise)
        mat2: Second n x n matrix (sorted row-wise and column-wise)
        n: Dimension of matrices
        x: Target sum

    Returns:
        int: Count of pairs with sum equal to x
    """
    # Start from top-right of mat1 and bottom-left of mat2
    i = 0  # Row index for mat1 (start from top)
    j = n - 1  # Column index for mat1 (start from right)
    count = 0

    # For mat2, start from bottom-left
    row2 = n - 1  # Row index for mat2 (start from bottom)
    col2 = 0  # Column index for mat2 (start from left)

    while i < n and j >= 0 and row2 >= 0 and col2 < n:
        current_sum = mat1[i][j] + mat2[row2][col2]

        if current_sum == x:
            count += 1
            # Move to next elements in both matrices
            j -= 1  # Move left in mat1
            row2 -= 1  # Move up in mat2
        elif current_sum < x:
            # Need larger sum, move to larger value in mat1 or mat2
            # Since mat1 is sorted, moving down increases value
            # Since mat2 is sorted, moving right increases value
            # We'll move in mat1 first (down), if not possible then in mat2 (right)
            if i + 1 < n:
                i += 1  # Move down in mat1
            else:
                col2 += 1  # Move right in mat2
        else:  # current_sum > x
            # Need smaller sum, move to smaller value
            # Since mat1 is sorted, moving left decreases value
            # Since mat2 is sorted, moving up decreases value
            if j - 1 >= 0:
                j -= 1  # Move left in mat1
            else:
                row2 -= 1  # Move up in mat2

    return count


def count_pairs_two_sorted_matrices_alternative(mat1, mat2, n, x):
    """
    Alternative approach: Flatten matrices and use two-pointer technique.
    Less space efficient but easier to understand.

    Args:
        mat1: First n x n matrix
        mat2: Second n x n matrix
        n: Dimension of matrices
        x: Target sum

    Returns:
        int: Count of pairs with sum equal to x
    """
    # Flatten both matrices
    flat1 = []
    flat2 = []

    for i in range(n):
        for j in range(n):
            flat1.append(mat1[i][j])
            flat2.append(mat2[i][j])

    # Sort both flattened arrays
    flat1.sort()
    flat2.sort()

    # Two-pointer technique
    left = 0
    right = len(flat2) - 1
    count = 0

    while left < len(flat1) and right >= 0:
        current_sum = flat1[left] + flat2[right]

        if current_sum == x:
            count += 1
            left += 1
            right -= 1
        elif current_sum < x:
            left += 1
        else:  # current_sum > x
            right -= 1

    return count


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Example from GeeksforGeeks
    print("Test 1: Example matrices")
    mat1 = [[1, 3, 5, 7], [2, 4, 6, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    mat2 = [[2, 4, 6, 8], [1, 3, 5, 7], [10, 11, 12, 13], [9, 10, 11, 12]]
    n = 4
    x = 21

    print("Matrix 1:")
    print_matrix(mat1)
    print("Matrix 2:")
    print_matrix(mat2)
    print(f"Target sum: {x}")

    result1 = count_pairs_two_sorted_matrices(mat1, mat2, n, x)
    result2 = count_pairs_two_sorted_matrices_alternative(mat1, mat2, n, x)
    print(f"Count of pairs with sum {x} (method 1): {result1}")
    print(f"Count of pairs with sum {x} (method 2): {result2}")
    print()

    # Test case 2: Simple case
    print("Test 2: Simple matrices")
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[1, 2], [3, 4]]
    n = 2
    x = 5

    print("Matrix 1:")
    print_matrix(mat1)
    print("Matrix 2:")
    print_matrix(mat2)
    print(f"Target sum: {x}")

    result1 = count_pairs_two_sorted_matrices(mat1, mat2, n, x)
    result2 = count_pairs_two_sorted_matrices_alternative(mat1, mat2, n, x)
    print(f"Count of pairs with sum {x} (method 1): {result1}")
    print(f"Count of pairs with sum {x} (method 2): {result2}")
    print()

    # Test case 3: No pairs
    print("Test 3: No pairs")
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    n = 2
    x = 20

    print("Matrix 1:")
    print_matrix(mat1)
    print("Matrix 2:")
    print_matrix(mat2)
    print(f"Target sum: {x}")

    result1 = count_pairs_two_sorted_matrices(mat1, mat2, n, x)
    result2 = count_pairs_two_sorted_matrices_alternative(mat1, mat2, n, x)
    print(f"Count of pairs with sum {x} (method 1): {result1}")
    print(f"Count of pairs with sum {x} (method 2): {result2}")
    print()

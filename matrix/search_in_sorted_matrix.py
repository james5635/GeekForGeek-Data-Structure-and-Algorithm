def search_in_sorted_matrix(matrix, target):
    """
    Search for a target value in a row-wise and column-wise sorted matrix.
    Returns True if found, False otherwise.
    Algorithm: Start from top-right corner and move based on comparison.
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    # Start from top-right corner
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False


# Test cases
if __name__ == "__main__":
    # Test case 1: Element present
    matrix1 = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    print(search_in_sorted_matrix(matrix1, 29))  # Expected: True

    # Test case 2: Element not present
    print(search_in_sorted_matrix(matrix1, 28))  # Expected: False

    # Test case 3: Element at corner
    print(search_in_sorted_matrix(matrix1, 10))  # Expected: True
    print(search_in_sorted_matrix(matrix1, 50))  # Expected: True

    # Test case 4: Single element matrix
    matrix2 = [[5]]
    print(search_in_sorted_matrix(matrix2, 5))  # Expected: True
    print(search_in_sorted_matrix(matrix2, 3))  # Expected: False

    # Test case 5: Empty matrix
    print(search_in_sorted_matrix([], 5))  # Expected: False
    print(search_in_sorted_matrix([[]], 5))  # Expected: False

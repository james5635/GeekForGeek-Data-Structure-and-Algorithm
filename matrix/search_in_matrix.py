def search_in_matrix(matrix, target):
    """
    Search for a target value in a 2D matrix.
    Returns True if found, False otherwise.
    """
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    return False


# Test cases
if __name__ == "__main__":
    # Test case 1: Element present
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(search_in_matrix(matrix1, 5))  # Expected: True

    # Test case 2: Element not present
    print(search_in_matrix(matrix1, 10))  # Expected: False

    # Test case 3: Empty matrix
    print(search_in_matrix([], 5))  # Expected: False

    # Test case 4: Single element matrix
    matrix2 = [[5]]
    print(search_in_matrix(matrix2, 5))  # Expected: True
    print(search_in_matrix(matrix2, 3))  # Expected: False

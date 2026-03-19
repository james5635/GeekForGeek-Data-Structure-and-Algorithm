def rotate_matrix_elements(matrix):
    """
    Rotate the elements of a matrix in clockwise direction.
    The rotation is done layer by layer (like peeling an onion).
    For each layer, elements are rotated by one position clockwise.
    Modifies the matrix in-place.
    """
    if not matrix or not matrix[0]:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    # Process each layer
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    while top < bottom and left < right:
        # Store the first element of next row (this will replace the first element of current row)
        prev = matrix[top + 1][left]

        # Move elements of top row one step right
        for i in range(left, right + 1):
            curr = matrix[top][i]
            matrix[top][i] = prev
            prev = curr
        top += 1

        # Move elements of right column one step downwards
        for i in range(top, bottom + 1):
            curr = matrix[i][right]
            matrix[i][right] = prev
            prev = curr
        right -= 1

        # Move elements of bottom row one step left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                curr = matrix[bottom][i]
                matrix[bottom][i] = prev
                prev = curr
            bottom -= 1

        # Move elements of left column one step upwards
        if left <= right:
            for i in range(bottom, top - 1, -1):
                curr = matrix[i][left]
                matrix[i][left] = prev
                prev = curr
            left += 1


# Alternative: return a new rotated matrix
def rotate_matrix_elements_new(matrix):
    """
    Return a new matrix with elements rotated clockwise by one position.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    # Create a copy of the matrix
    result = [row[:] for row in matrix]

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    while top < bottom and left < right:
        # Store the first element of next row
        prev = result[top + 1][left]

        # Move elements of top row one step right
        for i in range(left, right + 1):
            curr = result[top][i]
            result[top][i] = prev
            prev = curr
        top += 1

        # Move elements of right column one step downwards
        for i in range(top, bottom + 1):
            curr = result[i][right]
            result[i][right] = prev
            prev = curr
        right -= 1

        # Move elements of bottom row one step left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                curr = result[bottom][i]
                result[bottom][i] = prev
                prev = curr
            bottom -= 1

        # Move elements of left column one step upwards
        if left <= right:
            for i in range(bottom, top - 1, -1):
                curr = result[i][left]
                result[i][left] = prev
                prev = curr
            left += 1

    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: 4x4 matrix
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Original matrix:")
    for row in matrix1:
        print(row)

    rotate_matrix_elements(matrix1)
    print("\nRotated matrix (in-place):")
    for row in matrix1:
        print(row)
    # Expected:
    # [5, 1, 2, 3]
    # [9, 10, 6, 4]
    # [13, 11, 7, 8]
    # [14, 15, 16, 12]

    # Test case 2: 3x3 matrix
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("\n\nOriginal matrix:")
    for row in matrix2:
        print(row)

    rotated2 = rotate_matrix_elements_new(matrix2)
    print("\nRotated matrix (new):")
    for row in rotated2:
        print(row)
    # Expected:
    # [4, 1, 2]
    # [7, 5, 3]
    # [8, 9, 6]

    # Test case 3: 1x1 matrix
    matrix3 = [[5]]
    print("\n\nOriginal matrix:")
    for row in matrix3:
        print(row)

    rotate_matrix_elements(matrix3)
    print("\nRotated matrix (in-place):")
    for row in matrix3:
        print(row)
    # Expected: [[5]] (no change)

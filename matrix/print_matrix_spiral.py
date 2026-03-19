def spiral_order(matrix):
    """
    Return the elements of the matrix in spiral order.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from right to left along the bottom row
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        # Traverse from bottom to top along the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# For printing, we can print the list
def print_spiral(matrix):
    """
    Print the matrix in spiral form.
    """
    result = spiral_order(matrix)
    print(" ".join(map(str, result)))


# Test cases
if __name__ == "__main__":
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Spiral order:")
    result1 = spiral_order(matrix1)
    expected1 = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    print(result1)
    assert result1 == expected1, f"Expected {expected1}, got {result1}"

    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Spiral order:")
    result2 = spiral_order(matrix2)
    expected2 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(result2)
    assert result2 == expected2, f"Expected {expected2}, got {result2}"

    matrix3 = [[1]]
    print("Spiral order:")
    result3 = spiral_order(matrix3)
    expected3 = [1]
    print(result3)
    assert result3 == expected3, f"Expected {expected3}, got {result3}"

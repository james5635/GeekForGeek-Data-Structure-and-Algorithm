def print_zigzag(matrix):
    """
    Print the given matrix in zig-zag fashion.
    Zig-zag fashion:
        First row left to right,
        second row right to left,
        third row left to right, and so on.
    Returns a list of elements in zig-zag order for testing.
    """
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for i in range(rows):
        if i % 2 == 0:
            # Even row: left to right
            for j in range(cols):
                result.append(matrix[i][j])
        else:
            # Odd row: right to left
            for j in range(cols - 1, -1, -1):
                result.append(matrix[i][j])

    # For printing, we can print the result
    print(" ".join(map(str, result)))
    return result


# Test cases
if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Zig-zag order:")
    result1 = print_zigzag(matrix1)
    expected1 = [1, 2, 3, 6, 5, 4, 7, 8, 9]
    assert result1 == expected1, f"Expected {expected1}, got {result1}"

    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print("Zig-zag order:")
    result2 = print_zigzag(matrix2)
    expected2 = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12]
    assert result2 == expected2, f"Expected {expected2}, got {result2}"

    matrix3 = [[1]]
    print("Zig-zag order:")
    result3 = print_zigzag(matrix3)
    expected3 = [1]
    assert result3 == expected3, f"Expected {expected3}, got {result3}"

def max_size_submatrix_all_1s(matrix):
    """
    Find the maximum size sub-matrix with all 1s in a binary matrix.

    Approach:
    1. Create an auxiliary matrix where each cell contains the number of consecutive 1s
       above it (including itself)
    2. For each row, treat it as a histogram and find the largest rectangle area
    3. The maximum area found is the answer

    Args:
        matrix: 2D list of 0s and 1s

    Returns:
        int: Size (area) of the maximum sub-matrix with all 1s
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Create auxiliary matrix
    aux = [[0] * cols for _ in range(rows)]

    # Fill first row
    for j in range(cols):
        aux[0][j] = matrix[0][j]

    # Fill remaining rows
    for i in range(1, rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                aux[i][j] = aux[i - 1][j] + 1
            else:
                aux[i][j] = 0

    # Function to find maximum area in histogram
    def max_histogram_area(heights):
        stack = []
        max_area = 0
        index = 0

        while index < len(heights):
            if not stack or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = heights[top_of_stack] * (
                    (index - stack[-1] - 1) if stack else index
                )
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(max_area, area)

        return max_area

    # Find maximum area for each row
    max_area = 0
    for i in range(rows):
        area = max_histogram_area(aux[i])
        max_area = max(max_area, area)

    return max_area


def max_size_submatrix_all_1s_dp(matrix):
    """
    Alternative DP approach:
    dp[i][j] represents the side length of the maximum square ending at (i, j)

    Args:
        matrix: 2D list of 0s and 1s

    Returns:
        int: Size (area) of the maximum sub-matrix with all 1s
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Create DP table
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    # Initialize first row and column
    for i in range(rows):
        dp[i][0] = matrix[i][0]
        max_side = max(max_side, dp[i][0])

    for j in range(cols):
        dp[0][j] = matrix[0][j]
        max_side = max(max_side, dp[0][j])

    # Fill DP table
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
            else:
                dp[i][j] = 0

    return max_side * max_side  # Return area


def print_matrix(matrix):
    """Helper function to print the matrix"""
    for row in matrix:
        print(" ".join(str(elem) for elem in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: Example matrix
    print("Test 1: Example matrix")
    matrix1 = [[0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
    print("Matrix:")
    print_matrix(matrix1)

    result1 = max_size_submatrix_all_1s(matrix1)
    result2 = max_size_submatrix_all_1s_dp(matrix1)
    print(f"Maximum size sub-matrix with all 1s (histogram method): {result1}")
    print(f"Maximum size sub-matrix with all 1s (DP method): {result2}")
    print()

    # Test case 2: All 1s matrix
    print("Test 2: All 1s matrix")
    matrix2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print("Matrix:")
    print_matrix(matrix2)

    result1 = max_size_submatrix_all_1s(matrix2)
    result2 = max_size_submatrix_all_1s_dp(matrix2)
    print(f"Maximum size sub-matrix with all 1s (histogram method): {result1}")
    print(f"Maximum size sub-matrix with all 1s (DP method): {result2}")
    print()

    # Test case 3: All 0s matrix
    print("Test 3: All 0s matrix")
    matrix3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print("Matrix:")
    print_matrix(matrix3)

    result1 = max_size_submatrix_all_1s(matrix3)
    result2 = max_size_submatrix_all_1s_dp(matrix3)
    print(f"Maximum size sub-matrix with all 1s (histogram method): {result1}")
    print(f"Maximum size sub-matrix with all 1s (DP method): {result2}")
    print()

    # Test case 4: Single 1
    print("Test 4: Single 1")
    matrix4 = [[1]]
    print("Matrix:")
    print_matrix(matrix4)

    result1 = max_size_submatrix_all_1s(matrix4)
    result2 = max_size_submatrix_all_1s_dp(matrix4)
    print(f"Maximum size sub-matrix with all 1s (histogram method): {result1}")
    print(f"Maximum size sub-matrix with all 1s (DP method): {result2}")
    print()

    # Test case 5: Single 0
    print("Test 5: Single 0")
    matrix5 = [[0]]
    print("Matrix:")
    print_matrix(matrix5)

    result1 = max_size_submatrix_all_1s(matrix5)
    result2 = max_size_submatrix_all_1s_dp(matrix5)
    print(f"Maximum size sub-matrix with all 1s (histogram method): {result1}")
    print(f"Maximum size sub-matrix with all 1s (DP method): {result2}")
    print()

def maxSumRectangle(matrix):
    """
    Find the maximum sum rectangle in a 2D matrix
    Args:
        matrix: 2D list of integers
    Returns:
        Maximum sum of any rectangle in the matrix
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float("-inf")

    # Consider all possible left and right column pairs
    for left in range(cols):
        # Create a temporary array to store row sums between left and right columns
        temp = [0] * rows

        for right in range(left, cols):
            # Update the temporary array with current column values
            for i in range(rows):
                temp[i] += matrix[i][right]

            # Find the maximum sum subarray in temp using Kadane's algorithm
            # Handle all negative case properly
            max_ending_here = 0
            max_so_far = float("-inf")

            for i in range(rows):
                max_ending_here = max_ending_here + temp[i]
                if max_sum < max_ending_here:
                    max_sum = max_ending_here
                if max_ending_here < 0:
                    max_ending_here = 0

    return max_sum


def test_maxSumRectangle():
    # Test case 1
    matrix1 = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6],
    ]
    print("Test 1 - Matrix:")
    for row in matrix1:
        print(row)
    result1 = maxSumRectangle(matrix1)
    print(f"Maximum sum rectangle: {result1}")
    print(f"Expected: 29 (from rectangle [3,8,10,1] and [-4,-1,1,7])")
    print()

    # Test case 2 - All negative
    matrix2 = [[-1, -2], [-3, -4]]
    print("Test 2 - Matrix:")
    for row in matrix2:
        print(row)
    result2 = maxSumRectangle(matrix2)
    print(f"Maximum sum rectangle: {result2}")
    print(f"Expected: -1")
    print()

    # Test case 3 - All positive
    matrix3 = [[1, 2], [3, 4]]
    print("Test 3 - Matrix:")
    for row in matrix3:
        print(row)
    result3 = maxSumRectangle(matrix3)
    print(f"Maximum sum rectangle: {result3}")
    print(f"Expected: 10 (entire matrix)")
    print()

    # Test case 4
    matrix4 = [[0, -2, -7, 0], [9, 2, -6, 2], [-4, 1, -4, 1], [-1, 8, 0, -2]]
    print("Test 4 - Matrix:")
    for row in matrix4:
        print(row)
    result4 = maxSumRectangle(matrix4)
    print(f"Maximum sum rectangle: {result4}")
    print(f"Expected: 15")
    print()


if __name__ == "__main__":
    test_maxSumRectangle()

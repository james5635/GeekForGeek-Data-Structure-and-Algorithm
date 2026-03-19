def printMaxSumSub(mat, k):
    """
    Print maximum sum square sub-matrix of given size k
    Args:
        mat: 2D list representing the matrix
        k: size of sub-matrix
    Returns:
        None (prints the maximum sum sub-matrix)
    """
    if not mat or not mat[0] or k <= 0:
        print("Invalid input")
        return

    rows = len(mat)
    cols = len(mat[0])

    if k > rows or k > cols:
        print("Invalid size")
        return

    # Preprocess: compute sum of all vertical strips of size k x 1
    # strip_sum[i][j] will store sum of elements from mat[i][j] to mat[i+k-1][j]
    strip_sum = [[0] * cols for _ in range(rows - k + 1)]

    for j in range(cols):
        # Calculate sum of first k x 1 rectangle in this column
        sum_val = 0
        for i in range(k):
            sum_val += mat[i][j]
        strip_sum[0][j] = sum_val

        # Calculate sum of remaining rectangles
        for i in range(1, rows - k + 1):
            sum_val += mat[i + k - 1][j] - mat[i - 1][j]
            strip_sum[i][j] = sum_val

    # Now calculate sum of k x k squares using strip_sum
    max_sum = float("-inf")
    max_pos = (0, 0)  # To store the top-left position of the max sum sub-matrix
    # Initialize to (0, 0) - will be updated in loops since we validated k <= rows and k <= cols

    for i in range(rows - k + 1):
        # Calculate sum of first k x k sub-matrix in this row
        sum_val = 0
        for j in range(k):
            sum_val += strip_sum[i][j]

        if sum_val > max_sum:
            max_sum = sum_val
            max_pos = (i, 0)

        # Calculate sum of remaining sub-matrices in this row
        for j in range(1, cols - k + 1):
            sum_val += strip_sum[i][j + k - 1] - strip_sum[i][j - 1]
            if sum_val > max_sum:
                max_sum = sum_val
                max_pos = (i, j)

    # Print the maximum sum sub-matrix
    print(f"Maximum sum: {max_sum}")
    print("Sub-matrix:")
    for i in range(max_pos[0], max_pos[0] + k):
        for j in range(max_pos[1], max_pos[1] + k):
            print(mat[i][j], end=" ")
        print()


def test_printMaxSumSub():
    # Test case 1
    mat1 = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5],
    ]
    k1 = 3
    print(f"Test 1 - Matrix:")
    for row in mat1:
        print(row)
    print(f"k = {k1}")
    printMaxSumSub(mat1, k1)
    print()

    # Test case 2
    mat2 = [
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
    ]
    k2 = 2
    print(f"Test 2 - Matrix:")
    for row in mat2:
        print(row)
    print(f"k = {k2}")
    printMaxSumSub(mat2, k2)
    print()


if __name__ == "__main__":
    test_printMaxSumSub()

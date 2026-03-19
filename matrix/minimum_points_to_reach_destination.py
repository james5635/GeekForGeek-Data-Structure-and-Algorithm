def minPoints(grid, n, m):
    """
    Minimum initial points to reach destination
    Args:
        grid: 2D list representing the grid with points (can be negative)
        n: Number of rows
        m: Number of columns
    Returns:
        Minimum initial points required to reach (n-1, m-1) from (0, 0)
    """
    # Create a DP table to store minimum points needed at each cell
    # dp[i][j] represents the minimum points needed to reach destination from cell (i, j)
    dp = [[0] * m for _ in range(n)]

    # Initialize the destination cell
    # We need at least 1 point to be alive at the destination
    dp[n - 1][m - 1] = max(1, 1 - grid[n - 1][m - 1])

    # Fill last row
    for j in range(m - 2, -1, -1):
        dp[n - 1][j] = max(1, dp[n - 1][j + 1] - grid[n - 1][j])

    # Fill last column
    for i in range(n - 2, -1, -1):
        dp[i][m - 1] = max(1, dp[i + 1][m - 1] - grid[i][m - 1])

    # Fill the rest of the table
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            # Minimum points needed on exit from (i, j)
            min_points_on_exit = min(dp[i + 1][j], dp[i][j + 1])
            # Minimum points needed to enter (i, j)
            dp[i][j] = max(1, min_points_on_exit - grid[i][j])

    return dp[0][0]


def test_minPoints():
    # Test case 1
    grid1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    n1, m1 = 3, 3
    print(f"Test 1 - Grid:")
    for row in grid1:
        print(row)
    result1 = minPoints(grid1, n1, m1)
    print(f"Minimum initial points required: {result1}")
    print(f"Expected: 7")
    print()

    # Test case 2
    grid2 = [[0, 0, 0], [0, 0, 0]]
    n2, m2 = 2, 3
    print(f"Test 2 - Grid:")
    for row in grid2:
        print(row)
    result2 = minPoints(grid2, n2, m2)
    print(f"Minimum initial points required: {result2}")
    print(f"Expected: 1")
    print()

    # Test case 3
    grid3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n3, m3 = 3, 3
    print(f"Test 3 - Grid:")
    for row in grid3:
        print(row)
    result3 = minPoints(grid3, n3, m3)
    print(f"Minimum initial points required: {result3}")
    print(f"Expected: 1")
    print()

    # Test case 4 - All negative
    grid4 = [[-1, -2, -3], [-4, -5, -6]]
    n4, m4 = 2, 3
    print(f"Test 4 - Grid:")
    for row in grid4:
        print(row)
    result4 = minPoints(grid4, n4, m4)
    print(f"Minimum initial points required: {result4}")
    print(f"Expected: 13")
    print()


if __name__ == "__main__":
    test_minPoints()

"""
Min Cost Path - Dynamic Programming

Given a 2D matrix cost[][], where each cell represents the cost of traversing
through that position, determine the minimum cost required to reach the
bottom-right cell (m-1, n-1) starting from the top-left cell (0,0).

From any cell (i, j), you can move:
- Right: (i, j+1)
- Down: (i+1, j)
- Diagonal: (i+1, j+1)

Time Complexity: O(m * n)
Space Complexity: O(n) with space optimization
"""


def min_cost(cost):
    """
    Find the minimum cost path from top-left to bottom-right.

    Args:
        cost: 2D list representing the cost matrix

    Returns:
        Minimum cost to reach bottom-right cell
    """
    m = len(cost)
    n = len(cost[0])
    dp = [0] * n

    # Initialize base cell
    dp[0] = cost[0][0]

    # Fill the first row
    for j in range(1, n):
        dp[j] = dp[j - 1] + cost[0][j]

    # Fill the rest of the rows
    for i in range(1, m):
        prev = dp[0]

        # Update first column
        dp[0] = dp[0] + cost[i][0]

        for j in range(1, n):
            temp = dp[j]
            # Update dp[j] using minimum of top, left, and diagonal
            dp[j] = cost[i][j] + min(dp[j], dp[j - 1], prev)
            prev = temp

    return dp[n - 1]


def min_cost_dp_table(cost):
    """
    Find minimum cost path using 2D DP table (more intuitive approach).

    Args:
        cost: 2D list representing the cost matrix

    Returns:
        Minimum cost to reach bottom-right cell
    """
    m = len(cost)
    n = len(cost[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize base cell
    dp[0][0] = cost[0][0]

    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + cost[0][j]

    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + cost[i][0]

    # Fill the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = cost[i][j] + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    # Test case 1
    cost1 = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    result1 = min_cost(cost1)
    result1_table = min_cost_dp_table(cost1)
    print(f"Test 1 - 3x3 matrix:")
    print(f"Cost matrix: {cost1}")
    print(f"Minimum cost (space optimized): {result1}")
    print(f"Minimum cost (DP table): {result1_table}")
    print(f"Expected: 8")
    print(f"Both methods match: {result1 == result1_table == 8}\n")

    # Test case 2
    cost2 = [[1, 2], [3, 4]]
    result2 = min_cost(cost2)
    print(f"Test 2 - 2x2 matrix:")
    print(f"Cost matrix: {cost2}")
    print(f"Minimum cost: {result2}")
    print(f"Expected: 5 (diagonal: 1->4)\n")

    # Test case 3 - Single row
    cost3 = [[1, 5, 2, 7]]
    result3 = min_cost(cost3)
    print(f"Test 3 - Single row:")
    print(f"Cost matrix: {cost3}")
    print(f"Minimum cost: {result3}")
    print(f"Expected: 15\n")

    # Test case 4 - Single column
    cost4 = [[1], [5], [2], [7]]
    result4 = min_cost(cost4)
    print(f"Test 4 - Single column:")
    print(f"Cost matrix: {cost4}")
    print(f"Minimum cost: {result4}")
    print(f"Expected: 15")

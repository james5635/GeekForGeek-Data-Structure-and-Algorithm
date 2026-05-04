"""
0/1 Knapsack Problem (DP-10)

Given weights and values of n items, put these items into a knapsack of
capacity W to get the maximum total value. Each item can either be included
completely or not at all (no fractional items allowed).

This implementation uses the space-optimized dynamic programming approach.

Time Complexity: O(n * W)
Space Complexity: O(W)

Source: https://www.geeksforgeeks.org/dsa/0-1-knapsack-problem-dp-10/
"""


def knapsack(capacity, values, weights):
    """
    Find the maximum value that can be put in a knapsack of given capacity.

    Args:
        capacity: Maximum weight capacity of the knapsack
        values: List of integers representing item values
        weights: List of integers representing item weights

    Returns:
        int: Maximum value that can be achieved without exceeding capacity
    """
    dp = [0] * (capacity + 1)

    for i in range(1, len(weights) + 1):
        for j in range(capacity, weights[i - 1] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i - 1]] + values[i - 1])

    return dp[capacity]


if __name__ == "__main__":
    print("=== 0/1 Knapsack Problem ===\n")

    values = [1, 2, 3]
    weights = [4, 5, 1]
    W = 4
    result = knapsack(W, values, weights)
    print(f"Input: W = {W}, values = {values}, weights = {weights}")
    print(f"Output: {result}")
    print(f"Explanation: Select item with weight 1 and value 3\n")

    values = [1, 2, 3]
    weights = [4, 5, 6]
    W = 3
    result = knapsack(W, values, weights)
    print(f"Input: W = {W}, values = {values}, weights = {weights}")
    print(f"Output: {result}")
    print(f"Explanation: All item weights exceed knapsack capacity\n")

    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    result = knapsack(W, values, weights)
    print(f"Input: W = {W}, values = {values}, weights = {weights}")
    print(f"Output: {result}")
    print(f"Explanation: Select all items (10+20+30=50, value=60+100+120=280)\n")

    values = [10, 40, 30, 50]
    weights = [5, 4, 6, 3]
    W = 10
    result = knapsack(W, values, weights)
    print(f"Input: W = {W}, values = {values}, weights = {weights}")
    print(f"Output: {result}")
    print(
        f"Explanation: Select items with weights 4, 3, and 3 not possible; optimal selection gives {result}\n"
    )

    values = [15, 20, 25, 30]
    weights = [2, 3, 4, 5]
    W = 8
    result = knapsack(W, values, weights)
    print(f"Input: W = {W}, values = {values}, weights = {weights}")
    print(f"Output: {result}")
    print(
        f"Explanation: Select items with weights 3, 5 or 2, 3, and not possible for 4; optimal is {result}\n"
    )

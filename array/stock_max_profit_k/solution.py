"""
Stock Buy Sell - Maximum Profit with At Most K Transactions Problem

Problem Description:
Given stock prices for n days and an integer k, find the maximum profit that can be
made by buying and selling a stock at most k times.

Constraints:
- You cannot engage in multiple transactions simultaneously
- You must sell before buying again

Example:
Input: prices = [10, 22, 5, 75, 65, 80], k = 2
Output: 87
Explanation:
- Buy at 10, sell at 22 (profit = 12)
- Buy at 5, sell at 80 (profit = 75)
- Total profit = 12 + 75 = 87

Time Complexity: O(n*k) using Dynamic Programming
Space Complexity: O(n*k) can be optimized to O(n)

Approach:
- dp[i][j] = max profit using at most i transactions up to day j
- State transition considers either doing nothing or selling on day j
"""

from typing import List


def max_profit_k_transactions(prices: List[int], k: int) -> int:
    """
    Calculate maximum profit with at most k transactions.

    Args:
        prices: List of stock prices for each day
        k: Maximum number of transactions allowed

    Returns:
        Maximum profit achievable
    """
    if not prices or k == 0:
        return 0

    n = len(prices)

    # Optimization: If k >= n//2, we can make unlimited transactions
    # This reduces to simple peak-valley problem
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # dp[t][d] = max profit with at most t transactions up to day d
    dp = [[0] * n for _ in range(k + 1)]

    for t in range(1, k + 1):
        max_diff = -prices[0]  # max of dp[t-1][m] - prices[m] for m < d

        for d in range(1, n):
            # Option 1: Don't sell on day d
            # Option 2: Sell on day d (bought at some m < d)
            # dp[t][d] = max(dp[t][d-1], prices[d] + max_{m<d}(dp[t-1][m] - prices[m]))
            dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
            max_diff = max(max_diff, dp[t - 1][d] - prices[d])

    return dp[k][n - 1]


def max_profit_k_transactions_space_optimized(prices: List[int], k: int) -> int:
    """
    Space optimized version using O(n) space.
    """
    if not prices or k == 0:
        return 0

    n = len(prices)

    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # Space optimization: we only need previous row
    prev = [0] * n
    curr = [0] * n

    for t in range(1, k + 1):
        max_diff = -prices[0]

        for d in range(1, n):
            curr[d] = max(curr[d - 1], prices[d] + max_diff)
            max_diff = max(max_diff, prev[d] - prices[d])

        prev, curr = curr, prev  # Swap references
        curr = [0] * n  # Reset curr

    return prev[n - 1]


def max_profit_k_transactions_1d(prices: List[int], k: int) -> int:
    """
    Most space efficient version using single array.
    """
    if not prices or k == 0:
        return 0

    n = len(prices)

    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # dp[j] = max profit with current transaction count up to day j
    dp = [0] * n

    for t in range(k):
        max_val = -prices[0]
        prev = 0

        for d in range(1, n):
            temp = dp[d]
            dp[d] = max(dp[d], prices[d] + max_val)
            max_val = max(max_val, prev - prices[d])
            prev = temp

    return dp[n - 1]


if __name__ == "__main__":
    # Test Case 1: Standard example
    prices1 = [10, 22, 5, 75, 65, 80]
    k1 = 2
    result1 = max_profit_k_transactions(prices1, k1)
    print(f"Prices: {prices1}, k = {k1}")
    print(f"Max profit: {result1}")
    print(f"Expected: 87")
    print(f"Pass: {result1 == 87}\n")

    # Test Case 2: Decreasing prices
    prices2 = [100, 90, 80, 70, 60]
    k2 = 2
    result2 = max_profit_k_transactions(prices2, k2)
    print(f"Prices: {prices2}, k = {k2}")
    print(f"Max profit: {result2}")
    print(f"Expected: 0")
    print(f"Pass: {result2 == 0}\n")

    # Test Case 3: Single transaction optimal
    prices3 = [1, 5, 3, 8, 4, 9]
    k3 = 1
    result3 = max_profit_k_transactions(prices3, k3)
    print(f"Prices: {prices3}, k = {k3}")
    print(f"Max profit: {result3}")
    print(f"Expected: 8 (buy at 1, sell at 9)")
    print(f"Pass: {result3 == 8}\n")

    # Test Case 4: k larger than n//2 (unlimited transactions)
    prices4 = [1, 2, 3, 4, 5]
    k4 = 10
    result4 = max_profit_k_transactions(prices4, k4)
    print(f"Prices: {prices4}, k = {k4}")
    print(f"Max profit: {result4}")
    print(f"Expected: 4")
    print(f"Pass: {result4 == 4}\n")

    # Test Case 5: Empty prices
    prices5 = []
    k5 = 2
    result5 = max_profit_k_transactions(prices5, k5)
    print(f"Prices: {prices5}, k = {k5}")
    print(f"Max profit: {result5}")
    print(f"Expected: 0")
    print(f"Pass: {result5 == 0}\n")

    # Test Case 6: Single day
    prices6 = [50]
    k6 = 1
    result6 = max_profit_k_transactions(prices6, k6)
    print(f"Prices: {prices6}, k = {k6}")
    print(f"Max profit: {result6}")
    print(f"Expected: 0")
    print(f"Pass: {result6 == 0}\n")

    # Test Case 7: k = 0
    prices7 = [1, 2, 3, 4, 5]
    k7 = 0
    result7 = max_profit_k_transactions(prices7, k7)
    print(f"Prices: {prices7}, k = {k7}")
    print(f"Max profit: {result7}")
    print(f"Expected: 0")
    print(f"Pass: {result7 == 0}\n")

    # Test Case 8: Multiple peaks and valleys
    prices8 = [3, 2, 6, 5, 0, 3]
    k8 = 2
    result8 = max_profit_k_transactions(prices8, k8)
    print(f"Prices: {prices8}, k = {k8}")
    print(f"Max profit: {result8}")
    print(f"Expected: 7")
    print(f"Pass: {result8 == 7}")

"""
Coin Change - Count Ways to Make Sum (DP-7)

Given an array of coin denominations and a target sum, find the number of ways
to make the sum using different combinations of coins. Each coin can be used
an infinite number of times.

This implementation uses the space-optimized dynamic programming approach.

Time Complexity: O(n * sum)
Space Complexity: O(sum)

Source: https://www.geeksforgeeks.org/dsa/coin-change-dp-7/
"""


def count_coin_change(coins, target_sum):
    """
    Count the number of ways to make target_sum using given coin denominations.

    Args:
        coins: List of integers representing coin denominations
        target_sum: The target sum to achieve

    Returns:
        int: Number of ways to make the target sum
    """
    n = len(coins)

    dp = [0] * (target_sum + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(coins[i], target_sum + 1):
            dp[j] += dp[j - coins[i]]

    return dp[target_sum]


if __name__ == "__main__":
    print("=== Coin Change Problem ===\n")

    coins = [1, 2, 3]
    target = 4
    result = count_coin_change(coins, target)
    print(f"Input: coins = {coins}, sum = {target}")
    print(f"Output: {result}")
    print(f"Explanation: Solutions are [1,1,1,1], [1,1,2], [2,2], [1,3]\n")

    coins = [2, 5, 3, 6]
    target = 10
    result = count_coin_change(coins, target)
    print(f"Input: coins = {coins}, sum = {target}")
    print(f"Output: {result}")
    print(
        f"Explanation: Solutions are [2,2,2,2,2], [2,2,3,3], [2,2,6], [2,3,5], [5,5]\n"
    )

    coins = [1, 2, 3]
    target = 5
    result = count_coin_change(coins, target)
    print(f"Input: coins = {coins}, sum = {target}")
    print(f"Output: {result}\n")

    coins = [2]
    target = 3
    result = count_coin_change(coins, target)
    print(f"Input: coins = {coins}, sum = {target}")
    print(f"Output: {result}")
    print(f"Explanation: Cannot make 3 using only coin of value 2\n")

    coins = [1]
    target = 0
    result = count_coin_change(coins, target)
    print(f"Input: coins = {coins}, sum = {target}")
    print(f"Output: {result}")
    print(f"Explanation: One way to make sum 0 - choose nothing\n")

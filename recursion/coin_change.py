"""
Coin Change Problem - Count Ways to Make Sum

Given an integer array coins[] representing different denominations of currency
and an integer sum. Find the number of ways to make sum by using different
combinations from coins[]. Assume infinite supply of each coin type.

Examples:
- sum = 4, coins = [1, 2, 3] -> 4 ways: [1,1,1,1], [1,1,2], [2,2], [1,3]
- sum = 10, coins = [2, 5, 3, 6] -> 5 ways

Approach (Naive Recursive):
For each coin, we have two choices:
1. Include the coin: Reduce sum by coin value, same coins available
2. Exclude the coin: Same sum, move to next coin

Recurrence:
count(coins, n, sum) = count(coins, n, sum - coins[n-1]) + count(coins, n-1, sum)

Time Complexity: O(2^sum)
Auxiliary Space: O(sum)
"""


def count_recur(coins, n, sum_val):
    """
    Recursive helper function to count ways.

    Args:
        coins: List of coin denominations
        n: Number of coins to consider
        sum_val: Target sum to achieve

    Returns:
        int: Number of ways to make the sum
    """
    # If sum is 0 then there is 1 solution (choose nothing)
    if sum_val == 0:
        return 1

    # If sum is negative or no coins left, no solution
    if sum_val < 0 or n == 0:
        return 0

    # Count is sum of solutions:
    # (i) including coins[n-1] (ii) excluding coins[n-1]
    return count_recur(coins, n, sum_val - coins[n - 1]) + count_recur(
        coins, n - 1, sum_val
    )


def count_ways(coins, sum_val):
    """
    Main function to count number of ways to make sum.

    Args:
        coins: List of coin denominations
        sum_val: Target sum

    Returns:
        int: Number of ways to make the sum
    """
    return count_recur(coins, len(coins), sum_val)


def main():
    # Test Case 1
    coins1 = [1, 2, 3]
    sum1 = 4
    result1 = count_ways(coins1, sum1)
    print(f"Coins: {coins1}")
    print(f"Sum: {sum1}")
    print(f"Number of ways: {result1}")
    print(f"Expected: 4")
    print("Ways: [1,1,1,1], [1,1,2], [2,2], [1,3]")
    print()

    # Test Case 2
    coins2 = [2, 5, 3, 6]
    sum2 = 10
    result2 = count_ways(coins2, sum2)
    print(f"Coins: {coins2}")
    print(f"Sum: {sum2}")
    print(f"Number of ways: {result2}")
    print(f"Expected: 5")
    print()

    # Test Case 3
    coins3 = [1, 2, 3]
    sum3 = 5
    result3 = count_ways(coins3, sum3)
    print(f"Coins: {coins3}")
    print(f"Sum: {sum3}")
    print(f"Number of ways: {result3}")
    print(f"Expected: 5")
    print()

    # Test Case 4 - Edge case: sum = 0
    coins4 = [1, 2, 3]
    sum4 = 0
    result4 = count_ways(coins4, sum4)
    print(f"Coins: {coins4}")
    print(f"Sum: {sum4}")
    print(f"Number of ways: {result4}")
    print(f"Expected: 1 (empty set)")


if __name__ == "__main__":
    main()

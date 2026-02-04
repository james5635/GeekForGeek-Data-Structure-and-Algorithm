"""
Stock Buy Sell - Multiple Transactions

Find maximum profit with multiple buy-sell transactions allowed.

Approaches:
1. Naive: Recursive - O(2^n) time
2. Better: Local minima/maxima - O(n) time
3. Optimal: Accumulate all positive differences - O(n) time
"""


def max_profit_recursive(prices, start, end):
    """
    Naive recursive approach.

    Time Complexity: O(2^n)
    Space Complexity: O(n) for recursion stack

    Algorithm:
    - For each possible buy day, try all possible sell days
    - Recursively find max profit for remaining days
    - Return maximum of all possibilities

    Args:
        prices: List of stock prices
        start: Starting index
        end: Ending index

    Returns:
        Maximum profit possible
    """
    if end <= start:
        return 0

    profit = 0

    # Try buying on each day
    for i in range(start, end):
        # Try selling on each day after buying
        for j in range(i + 1, end + 1):
            if prices[j] > prices[i]:
                # Calculate profit for this transaction
                current_profit = prices[j] - prices[i]

                # Add profit from remaining transactions
                remaining_profit = max_profit_recursive(prices, j + 1, end)

                # Update max profit
                profit = max(profit, current_profit + remaining_profit)

    return profit


def max_profit_local_minmax(prices):
    """
    Better approach: Find local minima and maxima.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
    - Find local minima (valley) - buy point
    - Find local maxima (peak) - sell point after valley
    - Add profit of each valley-peak pair

    Args:
        prices: List of stock prices

    Returns:
        Maximum profit possible
    """
    n = len(prices)
    if n < 2:
        return 0

    profit = 0
    i = 0

    while i < n - 1:
        # Find local minima (valley)
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1

        if i >= n - 1:
            break

        buy = prices[i]
        i += 1

        # Find local maxima (peak)
        while i < n and prices[i] >= prices[i - 1]:
            i += 1

        sell = prices[i - 1]
        profit += sell - buy

    return profit


def max_profit_optimal(prices):
    """
    Optimal approach: Accumulate all positive differences.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Key Insight:
    Instead of finding peaks and valleys, just add all positive differences
    between consecutive days. This is equivalent to buying at local minima
    and selling at local maxima.

    Example: [1, 5, 3, 8]
    - Buy at 1, sell at 5: profit = 4
    - Buy at 3, sell at 8: profit = 5
    - Total: 9

    Same as: (5-1) + (8-3) = 4 + 5 = 9

    Args:
        prices: List of stock prices

    Returns:
        Maximum profit possible
    """
    profit = 0

    for i in range(1, len(prices)):
        # If price increased, add the difference to profit
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


if __name__ == "__main__":
    # Test cases
    test_cases = [
        [100, 180, 260, 310, 40, 535, 695],
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [],
        [1, 2],
        [2, 1],
        [3, 3, 5, 0, 0, 3, 1, 4],
    ]

    print("=" * 70)
    print("Stock Buy Sell - Multiple Transactions")
    print("=" * 70)
    print("\nMultiple transactions allowed (buy, sell, buy, sell, ...)\n")

    for i, prices in enumerate(test_cases, 1):
        print(f"Test {i}: prices = {prices}")

        if len(prices) <= 10:  # Only run recursive for small inputs
            recursive_result = max_profit_recursive(prices, 0, len(prices) - 1)
            print(f"  Recursive O(2^n):    {recursive_result}")
        else:
            print(f"  Recursive O(2^n):    (skipped for large input)")

        local_minmax_result = max_profit_local_minmax(prices)
        optimal_result = max_profit_optimal(prices)

        match = "✓" if local_minmax_result == optimal_result else "✗"

        print(f"  Local Min/Max O(n):  {local_minmax_result}")
        print(f"  Optimal O(n):        {optimal_result} {match}")
        print()

    print("=" * 70)
    print("\nOptimal Approach Explanation:")
    print("  Instead of finding all peaks and valleys,")
    print("  simply add all positive differences between consecutive days.")
    print("  This works because: (peak - valley) = sum of all step increases")
    print("=" * 70)

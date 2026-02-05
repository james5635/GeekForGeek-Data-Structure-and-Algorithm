"""
Stock Buy Sell - Maximum Profit with At Most 2 Transactions Problem

Problem Description:
Given an array representing prices of stock on different days, find the maximum
profit that can be earned by buying and selling a stock at most twice.

Constraints:
- A stock must be bought before it can be sold
- Second transaction can only start after first is complete

Example:
Input: prices = [10, 22, 5, 75, 65, 80]
Output: 87
Explanation:
- First transaction: Buy at 10, sell at 22 (profit = 12)
- Second transaction: Buy at 5, sell at 80 (profit = 75)
- Total: 87

Time Complexity: O(n) - single pass
Space Complexity: O(1) - constant space

Approach:
Track four states:
- first_buy: max profit after first buy (minimized cost)
- first_sell: max profit after first sell
- second_buy: max profit after second buy
- second_sell: max profit after second sell
"""

from typing import List


def max_profit_twice(prices: List[int]) -> int:
    """
    Calculate maximum profit with at most 2 transactions.

    Args:
        prices: List of stock prices for each day

    Returns:
        Maximum profit achievable with at most 2 transactions
    """
    if not prices or len(prices) < 2:
        return 0

    # Initialize states
    # first_buy: maximum profit after buying first stock (negative = cost)
    first_buy = float("-inf")
    # first_sell: maximum profit after selling first stock
    first_sell = 0
    # second_buy: maximum profit after buying second stock
    second_buy = float("-inf")
    # second_sell: maximum profit after selling second stock
    second_sell = 0

    for price in prices:
        # Update in reverse order of dependency
        # second_sell depends on second_buy
        second_sell = max(second_sell, second_buy + price)

        # second_buy depends on first_sell
        second_buy = max(second_buy, first_sell - price)

        # first_sell depends on first_buy
        first_sell = max(first_sell, first_buy + price)

        # first_buy is just -price (we want minimum cost)
        first_buy = max(first_buy, -price)

    return int(second_sell)


def max_profit_twice_dp(prices: List[int]) -> int:
    """
    Alternative DP approach using forward and backward passes.
    Time: O(n), Space: O(n)
    """
    if not prices or len(prices) < 2:
        return 0

    n = len(prices)

    # left[i] = max profit from one transaction in prices[0..i]
    left = [0] * n
    min_price = prices[0]

    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left[i] = max(left[i - 1], prices[i] - min_price)

    # right[i] = max profit from one transaction in prices[i..n-1]
    right = [0] * n
    max_price = prices[n - 1]

    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        right[i] = max(right[i + 1], max_price - prices[i])

    # Maximum profit with at most 2 transactions
    max_profit = 0
    for i in range(n):
        # left[i] = profit from first transaction ending at or before i
        # right[i] = profit from second transaction starting at or after i
        max_profit = max(max_profit, left[i] + right[i])

    return max_profit


def max_profit_twice_divide_conquer(prices: List[int]) -> int:
    """
    Divide and conquer approach.
    Time: O(n log n), Space: O(log n)
    """
    if not prices or len(prices) < 2:
        return 0

    def helper(prices: List[int], left: int, right: int) -> int:
        if left >= right:
            return 0

        if right - left == 1:
            return max(0, prices[right] - prices[left])

        mid = (left + right) // 2

        # Case 1: Both transactions in left half
        left_profit = helper(prices, left, mid)

        # Case 2: Both transactions in right half
        right_profit = helper(prices, mid + 1, right)

        # Case 3: One transaction in each half
        # Find min in left half and max in right half
        min_left = min(prices[left : mid + 1])
        max_right = max(prices[mid + 1 : right + 1])
        cross_profit = max(0, max_right - min_left)

        return max(left_profit, right_profit, cross_profit)

    return helper(prices, 0, len(prices) - 1)


if __name__ == "__main__":
    # Test Case 1: Standard example
    prices1 = [10, 22, 5, 75, 65, 80]
    result1 = max_profit_twice(prices1)
    print(f"Prices: {prices1}")
    print(f"Max profit (2 transactions): {result1}")
    print(f"Expected: 87")
    print(f"Pass: {result1 == 87}\n")

    # Test Case 2: Single increasing sequence
    prices2 = [1, 2, 3, 4, 5]
    result2 = max_profit_twice(prices2)
    print(f"Prices: {prices2}")
    print(f"Max profit (2 transactions): {result2}")
    print(f"Expected: 4")
    print(f"Pass: {result2 == 4}\n")

    # Test Case 3: Decreasing prices
    prices3 = [5, 4, 3, 2, 1]
    result3 = max_profit_twice(prices3)
    print(f"Prices: {prices3}")
    print(f"Max profit (2 transactions): {result3}")
    print(f"Expected: 0")
    print(f"Pass: {result3 == 0}\n")

    # Test Case 4: Two separate increasing sequences
    prices4 = [3, 3, 5, 0, 0, 3, 1, 4]
    result4 = max_profit_twice(prices4)
    print(f"Prices: {prices4}")
    print(f"Max profit (2 transactions): {result4}")
    print(f"Expected: 6")
    print(f"Pass: {result4 == 6}\n")

    # Test Case 5: Empty array
    prices5 = []
    result5 = max_profit_twice(prices5)
    print(f"Prices: {prices5}")
    print(f"Max profit (2 transactions): {result5}")
    print(f"Expected: 0")
    print(f"Pass: {result5 == 0}\n")

    # Test Case 6: Single element
    prices6 = [5]
    result6 = max_profit_twice(prices6)
    print(f"Prices: {prices6}")
    print(f"Max profit (2 transactions): {result6}")
    print(f"Expected: 0")
    print(f"Pass: {result6 == 0}\n")

    # Test Case 7: Two elements
    prices7 = [1, 2]
    result7 = max_profit_twice(prices7)
    print(f"Prices: {prices7}")
    print(f"Max profit (2 transactions): {result7}")
    print(f"Expected: 1")
    print(f"Pass: {result7 == 1}\n")

    # Test Case 8: Multiple valleys and peaks
    prices8 = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    result8 = max_profit_twice(prices8)
    print(f"Prices: {prices8}")
    print(f"Max profit (2 transactions): {result8}")
    print(f"Expected: 13")
    print(f"Pass: {result8 == 13}")

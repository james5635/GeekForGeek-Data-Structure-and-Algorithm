# Stock Buy Sell - Maximum Profit with K Transactions

## Problem Description

Given stock prices for n days and an integer k, find the maximum profit that can be made by buying and selling a stock at most k times.

**Constraints:**
- You cannot engage in multiple transactions simultaneously
- You must sell before buying again

**Example:**
```
Input: prices = [10, 22, 5, 75, 65, 80], k = 2
Output: 87

Explanation:
- Buy at 10, sell at 22 (profit = 12)
- Buy at 5, sell at 80 (profit = 75)
- Total profit = 12 + 75 = 87
```

## Algorithm

**Approach:** Dynamic Programming

**Key Insight:** 
- `dp[t][d]` = max profit using at most t transactions up to day d
- State transition considers either doing nothing or selling on day d
- `dp[t][d] = max(dp[t][d-1], prices[d] + max_{m<d}(dp[t-1][m] - prices[m]))`

**Optimization:** If k >= n/2, treat as unlimited transactions (simple peak-valley).

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| DP (2D) | O(n × k) | O(n × k) |
| DP (Space Optimized) | O(n × k) | O(n) |
| DP (1D) | O(n × k) | O(n) |
| Unlimited Transactions | O(n) | O(1) |

## Functions

### `max_profit_k_transactions(prices, k)`
Calculate maximum profit with at most k transactions.

**Parameters:**
- `prices`: List of stock prices for each day
- `k`: Maximum number of transactions allowed

**Returns:**
- Maximum profit achievable

### `max_profit_k_transactions_space_optimized(prices, k)`
Space optimized version using O(n) space.

### `max_profit_k_transactions_1d(prices, k)`
Most space efficient version using single array.

## Usage

```python
from solution import max_profit_k_transactions

prices = [10, 22, 5, 75, 65, 80]
k = 2
profit = max_profit_k_transactions(prices, k)
print(profit)  # 87
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Transaction Limit**: When k >= n/2, it's equivalent to unlimited transactions
2. **DP State**: Track maximum profit for each transaction count and day
3. **Space Optimization**: Only need previous row of DP table
4. **max_diff Trick**: Track `max(dp[t-1][m] - prices[m])` to avoid inner loop

## References

- [GeeksForGeeks - Maximum Profit by Buying and Selling Stock at Most K Times](https://www.geeksforgeeks.org/dsa/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/)

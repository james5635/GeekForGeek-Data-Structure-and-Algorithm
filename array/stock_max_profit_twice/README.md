# Stock Buy Sell - Maximum Profit with At Most 2 Transactions

## Problem Description

Given an array representing prices of stock on different days, find the maximum profit that can be earned by buying and selling a stock at most twice.

**Constraints:**
- A stock must be bought before it can be sold
- Second transaction can only start after first is complete

**Example:**
```
Input: prices = [10, 22, 5, 75, 65, 80]
Output: 87

Explanation:
- First transaction: Buy at 10, sell at 22 (profit = 12)
- Second transaction: Buy at 5, sell at 80 (profit = 75)
- Total: 87
```

## Algorithms

### 1. State Machine (Optimal)
**Time:** O(n), **Space:** O(1)

Track four states:
- `first_buy`: max profit after first buy (minimized cost, so negative)
- `first_sell`: max profit after first sell
- `second_buy`: max profit after second buy
- `second_sell`: max profit after second sell

### 2. DP with Forward/Backward Pass
**Time:** O(n), **Space:** O(n)

Compute max profit for one transaction in [0..i] and [i..n-1], then combine.

### 3. Divide and Conquer
**Time:** O(n log n), **Space:** O(log n)

Divide array and consider transactions in left, right, or across both halves.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| State Machine | O(n) | O(1) |
| DP (Two Pass) | O(n) | O(n) |
| Divide and Conquer | O(n log n) | O(log n) |

## Functions

### `max_profit_twice(prices)`
Calculate maximum profit with at most 2 transactions using state machine.

**Parameters:**
- `prices`: List of stock prices for each day

**Returns:**
- Maximum profit achievable with at most 2 transactions

### `max_profit_twice_dp(prices)`
Alternative DP approach using forward and backward passes.

### `max_profit_twice_divide_conquer(prices)`
Divide and conquer approach.

## Usage

```python
from solution import max_profit_twice

prices = [3, 3, 5, 0, 0, 3, 1, 4]
profit = max_profit_twice(prices)
print(profit)  # 6
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **State Tracking**: Track best outcome after each buy/sell operation
2. **Update Order**: Update states in reverse order of dependency
3. **Optimal Substructure**: Each state depends only on previous states
4. **Constant Space**: Only need to track 4 values, not entire DP table

## References

- [GeeksForGeeks - Maximum Profit by Buying and Selling Stock at Most Twice](https://www.geeksforgeeks.org/dsa/maximum-profit-by-buying-and-selling-a-share-at-most-twice/)

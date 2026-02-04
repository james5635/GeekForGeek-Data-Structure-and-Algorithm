# Stock Buy Sell - Multiple Transactions

Given an array `price[]` of length `n` where `price[i]` denotes the price of a stock on day `i`, find the maximum profit you can achieve by buying and selling stocks with multiple transactions allowed. You can complete as many transactions as you like, but you must sell the stock before you buy again.

## Problem Statement

Find the maximum profit by buying and selling stocks multiple times, with the constraint that you cannot hold more than one stock at a time (must sell before buying again).

### Examples

**Input:** `price[] = [100, 180, 260, 310, 40, 535, 695]`  
**Output:** `865`  
**Explanation:** 
- Buy at 100, sell at 310: Profit = 210
- Buy at 40, sell at 695: Profit = 655
- Total Profit = 210 + 655 = 865

**Input:** `price[] = [7, 1, 5, 3, 6, 4]`  
**Output:** `7`  
**Explanation:**
- Buy at 1, sell at 5: Profit = 4
- Buy at 3, sell at 6: Profit = 3
- Total Profit = 4 + 3 = 7

**Input:** `price[] = [5, 4, 3, 2, 1]`  
**Output:** `0`  
**Explanation:** No profitable transaction possible (prices only decreasing)

## Algorithm Approaches

### 1. Naive Approach - Recursive
- **File:** `stock_buy_sell_multiple.py`
- **Time Complexity:** O(2^n)
- **Space Complexity:** O(n) for recursion stack
- **Description:** 
  - Try all possible buy-sell combinations recursively
  - For each buy day, try all possible sell days after it
  - Recursively calculate profit for remaining days
  - Return maximum profit found

### 2. Better Approach - Local Minima and Maxima
- **File:** `stock_buy_sell_multiple.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Find local minima (valley) - this is a buy point
  - Find the next local maxima (peak) after the valley - this is a sell point
  - Add the difference (peak - valley) to total profit
  - Continue until end of array

### 3. Optimal Approach - Accumulate Positive Differences
- **File:** `stock_buy_sell_multiple.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Simply add all positive differences between consecutive days
  - This is equivalent to buying every day and selling the next day when profitable
  - Mathematically: sum of (price[i] - price[i-1]) for all price[i] > price[i-1]

## Usage

```bash
python stock_buy_sell_multiple.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Practical Use |
|----------|----------------|------------------|---------------|
| Recursive | O(2^n) | O(n) | Educational only |
| Local Min/Max | O(n) | O(1) | Good for understanding peaks/valleys |
| Optimal | O(n) | O(1) | Most practical solution |

## Key Insights

- **Optimal Strategy:** The optimal solution is to capture every upward movement
- **Equivalence:** Adding all positive differences equals finding all peaks and valleys
- **No Overlap:** Selling and buying on the same day doesn't change profit
- **Greedy Works:** Greedy approach (take all profits) is optimal for this problem

## Mathematical Proof

The sum of all positive differences equals the sum of all (peak - valley) pairs:

```
[1, 5, 3, 8]
Positive differences: (5-1) + (8-3) = 4 + 5 = 9
Peak-Valley pairs: (5-1) + (8-3) = 9

Both approaches give the same result because:
(peak - valley) = sum of all consecutive increases from valley to peak
```

## Edge Cases

- Empty array or single element: returns 0
- Strictly decreasing prices: returns 0
- Strictly increasing prices: returns (last - first)
- Same price consecutive days: no profit, no loss

## References

- [GeeksforGeeks - Stock Buy Sell to Maximize Profit](https://www.geeksforgeeks.org/stock-buy-sell/)

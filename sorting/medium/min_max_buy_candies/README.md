# Find Minimum and Maximum Amount to Buy N Candies

## Problem Statement

A shop sells candies at a discount. For every candy you buy, you can take `k` candies for free. Given the prices of each candy, the number of candies `n` to buy, and `k` (free candies per purchase), find:
1. Minimum amount to spend to buy `n` candies
2. Maximum amount to spend to buy `n` candies

## Examples

**Example 1:**
```
Input: prices = [3, 2, 1, 4], n = 4, k = 2
Output: (min=5, max=5)

Explanation:
MINIMUM: Sort [1, 2, 3, 4]
  - Buy 1 (cheapest), get 2 and 3 free
  - Still need 1 more candy, buy 4
  - Total = 1 + 4 = 5

MAXIMUM: Sort [4, 3, 2, 1]
  - Buy 4 (most expensive), get 3 and 2 free
  - Still need 1 more candy, buy 1
  - Total = 4 + 1 = 5
```

**Example 2:**
```
Input: prices = [1, 2, 3, 4, 5, 6, 7, 8], n = 5, k = 2
Output: (min=5, max=13)

Explanation:
MINIMUM: [1, 2, 3, 4, 5, 6, 7, 8]
  - Buy 1, get 2,3 free (3 candies)
  - Buy 4, get 5,6 free (now have 6, but only need 5)
  - Total = 1 + 4 = 5

MAXIMUM: [8, 7, 6, 5, 4, 3, 2, 1]
  - Buy 8, get 7,6 free (3 candies)
  - Buy 5, get 4,3 free (now have 6, but only need 5)
  - Total = 8 + 5 = 13
```

## Approach

### Greedy Strategy

**For Minimum Amount:**
1. Sort prices in **ascending** order
2. Always buy the **cheapest** available candy
3. Get next `k` candies free
4. Repeat until we have `n` candies

**For Maximum Amount:**
1. Sort prices in **descending** order
2. Always buy the **most expensive** available candy
3. Get next `k` candies free
4. Repeat until we have `n` candies

### Why Greedy Works
- For minimum: Buying cheap candies first minimizes cost, and getting expensive ones free maximizes savings
- For maximum: Buying expensive candies first maximizes cost, and getting cheap ones free minimizes savings

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Sorting: O(n log n)
  - Greedy selection: O(n)
- **Space Complexity:** O(1) auxiliary
  - Sorting: O(log n) to O(n)
  - Only tracking total cost

## Implementation

```python
def find_min_amount(prices, n, k):
    prices.sort()
    total = 0
    bought = 0
    i = 0
    
    while bought < n:
        total += prices[i]
        bought += 1
        i += k + 1  # Skip k free candies
    
    return total

def find_max_amount(prices, n, k):
    prices.sort(reverse=True)
    total = 0
    bought = 0
    i = 0
    
    while bought < n:
        total += prices[i]
        bought += 1
        i += k + 1  # Skip k free candies
    
    return total
```

## Edge Cases

- **k = 0:** No free candies, must buy all n candies
- **k ≥ n-1:** Buy one candy, get all others free
- **n = 1:** Just buy the cheapest/most expensive
- **All same prices:** Min = Max
- **Not enough candies:** Raise error

## Applications

- Shopping optimization
- Discount strategy analysis
- Resource allocation with benefits

## Reference

- [GeeksforGeeks - Find Minimum Maximum Amount to Buy N Candies](https://www.geeksforgeeks.org/dsa/find-minimum-maximum-amount-buy-n-candies/)
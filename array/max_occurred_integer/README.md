# Maximum Occurred Integer in N Ranges

## Problem Description

Given n ranges of the form L[i] to R[i], find the maximum occurred integer in all these ranges. If multiple integers have the same maximum occurrence, return the smallest one.

**Example:**
```
Input: L = [1, 2, 3], R = [3, 5, 7]
Ranges: [1,3], [2,5], [3,7]

Output: 3

Explanation: Integer 3 occurs in all 3 ranges (highest frequency).
```

## Algorithm

**Approach:** Prefix Sum / Difference Array

**Key Insight:** Instead of iterating through each range and counting, use difference array technique:
1. Increment count at L[i]
2. Decrement count at R[i] + 1
3. Compute prefix sum to get actual frequencies
4. Track maximum frequency

**Steps:**
1. Create frequency array of size max(R) + 2
2. For each range [L, R]: freq[L]++, freq[R+1]--
3. Compute prefix sum
4. Find index with maximum value

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Difference Array | O(n + MAX) | O(MAX) |
| Brute Force | O(n × MAX) | O(MAX) |

Where MAX = maximum value in ranges, n = number of ranges

## Functions

### `max_occurred_integer(L, R)`
Find maximum occurred integer in given ranges.

**Parameters:**
- `L`: List of left boundaries of ranges
- `R`: List of right boundaries of ranges

**Returns:**
- Integer with maximum occurrence, or None if no ranges

### `max_occurred_with_count(L, R)`
Return both the integer and its occurrence count.

**Returns:**
- Tuple of (integer, count)

## Usage

```python
from solution import max_occurred_integer

L = [1, 2, 3]
R = [3, 5, 7]
result = max_occurred_integer(L, R)
print(result)  # 3
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Difference Array**: Efficient technique for range updates
2. **Prefix Sum**: Converts difference array to actual frequencies
3. **Range Overlap**: Automatically handles overlapping ranges
4. **Space Trade-off**: Uses O(MAX) space but O(n + MAX) time

## References

- [GeeksForGeeks - Maximum Occurred Integer in N Ranges](https://www.geeksforgeeks.org/dsa/maximum-occurred-integer-n-ranges/)

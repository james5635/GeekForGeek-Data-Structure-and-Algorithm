# Range Sum Query using Sparse Table

## Problem Description

Given a static array and multiple range sum queries, answer each query efficiently. While sparse tables are typically used for idempotent operations (min, max), this implementation demonstrates range sum using alternative approaches.

**Example:**
```
Array: [1, 3, 5, 7, 9, 11]
Query: sum(1, 4)
Result: 3 + 5 + 7 + 9 = 24
```

## Algorithm

Since sum is not idempotent, we use:
1. **Prefix Sum Approach:** Precompute prefix sums, answer queries in O(1)
2. **Sparse Table with Overlap:** Demonstrates why sparse tables don't work well for sum

**Prefix Sum Method:**
- `prefix[i]` = sum of arr[0..i-1]
- Range sum [L, R] = prefix[R+1] - prefix[L]

## Complexity Analysis

| Approach | Preprocessing | Query | Space |
|----------|--------------|-------|-------|
| Prefix Sum | O(N) | O(1) | O(N) |
| Sparse Table | O(N log N) | O(log N) | O(N log N) |
| Segment Tree | O(N) | O(log N) | O(N) |

## Classes and Functions

### `RangeSumQuery`
Range sum query using prefix sum (optimal for static arrays).

**Methods:**
- `__init__(arr)`: Initialize with array
- `query(left, right)`: Get sum of range [left, right]

### `RangeSumSparseTable`
Alternative using sparse table (for educational purposes).

## Usage

```python
from solution import RangeSumQuery

arr = [1, 3, 5, 7, 9, 11]
rsq = RangeSumQuery(arr)

# Query sum from index 1 to 4
result = rsq.query(1, 4)
print(result)  # 24

# Query sum of entire array
result = rsq.query(0, 5)
print(result)  # 36
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Best Approach:** Prefix sum is optimal for static range sum queries
2. **Sparse Table Limitation:** Sum is not idempotent, making sparse table less efficient
3. **Space vs Time:** Prefix sum offers best space-time tradeoff
4. **Static Only:** No updates allowed without rebuilding

## References

- [GeeksForGeeks - Range Sum Query using Sparse Table](https://www.geeksforgeeks.org/dsa/range-sum-query-using-sparse-table/)

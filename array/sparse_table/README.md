# Sparse Table

## Problem Description

A Sparse Table is a data structure that allows answering static range queries (such as Range Minimum Query - RMQ) in O(1) time after O(n log n) preprocessing. It is particularly useful when the array is static (no updates) and there are many queries to answer.

**Example:**
```
Array: [7, 2, 3, 0, 5, 10, 3, 12, 18]
Query: min(2, 7)
Result: min([3, 0, 5, 10, 3, 12]) = 0
```

## Algorithm

1. Build a table where `table[i][j]` stores the minimum of range starting at i with length 2^j
2. `table[i][j] = min(table[i][j-1], table[i + 2^(j-1)][j-1])`
3. For query [L, R], find k = floor(log2(R - L + 1))
4. Result = min(table[L][k], table[R - 2^k + 1][k])

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Preprocessing | O(N log N) | O(N log N) |
| Query | O(1) | O(1) |
| Update | Not supported | - |

## Classes and Functions

### `SparseTable`
Sparse Table data structure for Range Minimum Query (RMQ).

**Methods:**
- `__init__(arr)`: Initialize sparse table from array
- `query(left, right)`: Get minimum in range [left, right]
- `query_idempotent(left, right)`: Alternative query for idempotent functions

**Note:** This implementation is for RMQ, but sparse tables can be built for any idempotent function (min, max, gcd).

## Usage

```python
from solution import SparseTable

arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
st = SparseTable(arr)

# Query minimum from index 2 to 7
result = st.query(2, 7)
print(result)  # 0

# Query minimum from index 0 to 4
result = st.query(0, 4)
print(result)  # 0
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Static Only:** Cannot handle updates - rebuild required
2. **Idempotent Functions:** Only works for functions where f(a, a) = a (min, max, gcd)
3. **O(1) Query:** Fastest possible query time for static RMQ
4. **Overlapping Ranges:** Uses overlapping intervals to cover any range

## Applications

- Range Minimum/Maximum Query
- Range GCD Query
- Lowest Common Ancestor (LCA) preprocessing
- Static array analysis

## References

- [GeeksForGeeks - Sparse Table](https://www.geeksforgeeks.org/dsa/sparse-table/)

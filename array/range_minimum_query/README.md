# Range Minimum Query (RMQ) for Static Array

## Problem Description

Given a static array and multiple range minimum queries, find the minimum element in a given range [L, R] efficiently.

**Example:**
```
Array: [7, 2, 3, 0, 5, 10, 3, 12, 18]
Query 1: min(2, 5) -> min([3, 0, 5, 10]) = 0
Query 2: min(0, 3) -> min([7, 2, 3, 0]) = 0
Query 3: min(4, 8) -> min([5, 10, 3, 12, 18]) = 3
```

## Algorithms

### 1. Sparse Table (Optimal for Static)
- Preprocessing: O(N log N)
- Query: O(1)
- Space: O(N log N)

### 2. Segment Tree
- Preprocessing: O(N)
- Query: O(log N)
- Space: O(N)
- Supports updates

### 3. Square Root Decomposition
- Preprocessing: O(N)
- Query: O(√N)
- Space: O(√N)

## Complexity Analysis

| Approach | Preprocessing | Query | Space | Updates |
|----------|--------------|-------|-------|---------|
| Sparse Table | O(N log N) | O(1) | O(N log N) | No |
| Segment Tree | O(N) | O(log N) | O(N) | O(log N) |
| Sqrt Decomposition | O(N) | O(√N) | O(√N) | O(1) |

## Classes and Functions

### `RangeMinimumQuery`
RMQ using sparse table for O(1) queries.

**Methods:**
- `__init__(arr)`: Initialize RMQ structure
- `query(left, right)`: Get minimum in range [left, right]

### `SegmentTreeRMQ`
RMQ using segment tree (supports updates).

**Methods:**
- `__init__(arr)`: Initialize segment tree
- `query(left, right)`: Get minimum in range
- `update(index, value)`: Update element at index

## Usage

```python
from solution import RangeMinimumQuery

arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
rmq = RangeMinimumQuery(arr)

# Query minimum from index 2 to 5
result = rmq.query(2, 5)
print(result)  # 0

# Query minimum from index 4 to 8
result = rmq.query(4, 8)
print(result)  # 3
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Choose Based on Needs:**
   - Static array, many queries → Sparse Table
   - Need updates → Segment Tree
   - Simple implementation → Sqrt Decomposition

2. **Sparse Table Power:** True O(1) query for static arrays
3. **Idempotent Property:** RMQ works because min(a, a) = a
4. **Preprocessing Tradeoff:** O(N log N) preprocessing for O(1) queries

## References

- [GeeksForGeeks - Range Minimum Query for Static Array](https://www.geeksforgeeks.org/dsa/range-minimum-query-for-static-array/)

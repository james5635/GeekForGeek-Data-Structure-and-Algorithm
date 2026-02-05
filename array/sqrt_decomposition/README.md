# Square Root Decomposition

## Problem Description

Square root decomposition is a technique to preprocess an array to answer range queries efficiently. The array is divided into blocks of size √N, allowing range queries to be answered by combining complete blocks and individual elements from partial blocks.

**Example:**
```
Array: [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
Query: sum(2, 7)
Block size: √10 ≈ 3
Blocks: [1,5,2], [4,6,1], [3,5,7], [10]
Result: sum elements 2,3,4,5,6,7 = 2+4+6+1+3+5 = 21
```

## Algorithm

1. Divide array into blocks of size √N
2. Precompute sum (or other aggregate) for each block
3. For query [L, R]:
   - Sum complete blocks fully contained in [L, R]
   - Sum individual elements in partial blocks at boundaries

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Preprocessing | O(N) | O(N) |
| Query | O(√N) | O(√N) block array |
| Point Update | O(1) | O(1) |

## Classes and Functions

### `SqrtDecomposition`
Square Root Decomposition data structure for range sum queries.

**Methods:**
- `__init__(arr)`: Initialize structure from array
- `query(left, right)`: Get sum of range [left, right]
- `update(index, value)`: Update element at index to value

## Usage

```python
from solution import SqrtDecomposition

arr = [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
sqrt_dec = SqrtDecomposition(arr)

# Query sum from index 2 to 7
result = sqrt_dec.query(2, 7)
print(result)  # 21

# Update element at index 3
sqrt_dec.update(3, 10)
result = sqrt_dec.query(2, 7)
print(result)  # 27
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Block Size:** √N is optimal for balancing preprocessing and query time
2. **Hybrid Approach:** Combines precomputed block values with element-level access
3. **Easy Updates:** Point updates are O(1) unlike segment trees
4. **Static/Dynamic:** Works for both static queries and point updates

## Comparison with Other Structures

| Structure | Preprocessing | Query | Update |
|-----------|--------------|-------|--------|
| Sqrt Decomposition | O(N) | O(√N) | O(1) |
| Segment Tree | O(N) | O(log N) | O(log N) |
| Sparse Table | O(N log N) | O(1) | Not supported |

## References

- [GeeksForGeeks - Square Root Decomposition](https://www.geeksforgeeks.org/dsa/square-root-decomposition-set-1-introduction/)

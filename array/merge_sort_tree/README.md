# Merge Sort Tree for Range Order Statistics

## Problem Description

Given a static array and queries to find the k-th smallest element in a subarray [L, R]. The merge sort tree is a segment tree where each node stores a sorted list of elements in its range.

**Example:**
```
Array: [3, 2, 5, 1, 8, 9]
Query 1: kth_smallest(1, 5, 2) 
         Subarray: [2, 5, 1, 8, 9]
         Sorted: [1, 2, 5, 8, 9]
         2nd smallest = 2

Query 2: kth_smallest(0, 3, 3)
         Subarray: [3, 2, 5, 1]
         Sorted: [1, 2, 3, 5]
         3rd smallest = 3
```

## Algorithm

1. Build a segment tree where each node stores a sorted list of its range
2. For query [L, R, k], traverse the tree and merge relevant sorted lists
3. Use binary search to find k-th smallest in O(log²N) time

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Build | O(N log N) | O(N log N) |
| Query (naive) | O(log² N) | O(log N) |
| Query (optimized) | O(log N) | O(log N) |

## Classes and Functions

### `MergeSortTree`
Merge sort tree for range order statistics.

**Methods:**
- `__init__(arr)`: Initialize merge sort tree
- `query_kth_smallest(left, right, k)`: Find k-th smallest in range [left, right]
- `count_less_equal(left, right, x)`: Count elements ≤ x in range
- `query_range_sorted(left, right)`: Get sorted list of range

## Usage

```python
from solution import MergeSortTree

arr = [3, 2, 5, 1, 8, 9]
mst = MergeSortTree(arr)

# Find 2nd smallest from index 1 to 5
result = mst.query_kth_smallest(1, 5, 2)
print(result)  # 2

# Find 3rd smallest from index 0 to 3
result = mst.query_kth_smallest(0, 3, 3)
print(result)  # 3
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Space-Intensive:** O(N log N) space for storing sorted lists
2. **Binary Search:** Use binary search on value to find k-th smallest
3. **Static Only:** Building is expensive, not suitable for dynamic arrays
4. **Order Statistics:** Can answer percentile, median queries easily

## Applications

- Finding median in range
- Finding k-th order statistic
- Counting elements in range less than X
- Range percentile queries

## References

- [GeeksForGeeks - Merge Sort Tree for Range Order Statistics](https://www.geeksforgeeks.org/dsa/merge-sort-tree-for-range-order-statistics/)

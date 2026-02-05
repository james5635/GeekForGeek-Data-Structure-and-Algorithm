# MO's Algorithm (Query Square Root Decomposition)

## Problem Description

MO's algorithm is used to efficiently answer range queries on a static array. It works by sorting queries in a specific order to minimize pointer movements, achieving O((N + Q) × √N) complexity for answering Q queries on an array of size N.

This implementation demonstrates range sum queries, but the technique can be applied to various other query types (XOR, frequency counting, etc.).

**Example:**
```
Array: [1, 1, 2, 1, 3, 4, 5, 2, 8]
Queries: [(0, 4), (1, 3), (2, 4)]
Results: [8, 4, 6]
```

## Algorithm

1. Divide array into blocks of size √N
2. Sort queries by block index of left endpoint, then by right endpoint
3. Process queries in sorted order, maintaining current range
4. Add/remove elements from current range as pointers move

**Key Insight:** By sorting queries in a specific Hilbert curve-like order, we minimize the total pointer movement across all queries.

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Preprocessing | O(1) | O(Q) |
| Query Processing (total) | O((N + Q) × √N) | O(1) auxiliary |
| Per query (amortized) | O(√N) | O(1) |

Where N = array size, Q = number of queries

## Classes and Functions

### `Query`
Represents a query with left, right indices and original index.

### `mo_algorithm(arr, queries)`
Process range sum queries using MO's algorithm.

**Parameters:**
- `arr`: Input array
- `queries`: List of (left, right) tuples (0-indexed, inclusive)

**Returns:**
- List of results for each query in original order

## Usage

```python
from solution import mo_algorithm

arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
queries = [(0, 4), (1, 3), (2, 4)]
results = mo_algorithm(arr, queries)
print(results)  # [8, 4, 6]
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Query Ordering:** Sort queries by (L/√N, R) to minimize pointer movement
2. **Efficient Updates:** Only add/remove elements at boundaries when moving between queries
3. **Offline Processing:** All queries must be known in advance
4. **Versatile:** Can be adapted for various query types (sum, XOR, mode, etc.)

## Applications

- Range sum/min/max queries
- Frequency-based queries (mode, distinct count)
- XOR range queries
- DQUERY (distinct elements in range)

## References

- [GeeksForGeeks - MO's Algorithm](https://www.geeksforgeeks.org/dsa/mos-algorithm-query-square-root-decomposition-set-1-introduction/)

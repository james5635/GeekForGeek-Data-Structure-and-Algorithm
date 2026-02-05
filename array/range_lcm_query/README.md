# Range LCM Queries

## Problem Description

Given a static array and multiple range LCM (Least Common Multiple) queries, find the LCM of all elements in a given range [L, R] efficiently.

**Example:**
```
Array: [2, 3, 4, 6, 8, 12]
Query 1: lcm(1, 3) -> lcm(3, 4, 6) = 12
Query 2: lcm(0, 2) -> lcm(2, 3, 4) = 12
Query 3: lcm(3, 5) -> lcm(6, 8, 12) = 24
```

## Algorithm

**Segment Tree Approach:**
1. Build a segment tree where each node stores LCM of its range
2. For query [L, R], combine results from O(log N) nodes
3. LCM of two numbers: `lcm(a, b) = (a * b) // gcd(a, b)`

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Preprocessing | O(N) | O(N) |
| Query | O(log N) | O(log N) stack |
| Update | O(log N) | O(log N) |

## Classes and Functions

### `RangeLCMQuery`
Range LCM query using segment tree.

**Methods:**
- `__init__(arr)`: Initialize segment tree
- `query(left, right)`: Get LCM of range [left, right]
- `update(index, value)`: Update element at index

### Helper Functions
- `gcd(a, b)`: Calculate GCD using Euclidean algorithm
- `lcm(a, b)`: Calculate LCM using GCD

## Usage

```python
from solution import RangeLCMQuery

arr = [2, 3, 4, 6, 8, 12]
lcm_query = RangeLCMQuery(arr)

# Query LCM from index 1 to 3
result = lcm_query.query(1, 3)
print(result)  # 12

# Query LCM from index 3 to 5
result = lcm_query.query(3, 5)
print(result)  # 24
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **LCM Overflow:** Can overflow quickly, use Python's arbitrary precision integers
2. **GCD Foundation:** Efficient LCM relies on efficient GCD
3. **Associative Property:** LCM(a, LCM(b, c)) = LCM(LCM(a, b), c)
4. **Segment Tree Fit:** Perfect for segment tree due to associative property

## Mathematical Foundation

```
lcm(a, b) = |a × b| / gcd(a, b)
```

For range LCM:
```
lcm(arr[L..R]) = lcm(arr[L], lcm(arr[L+1], ... lcm(arr[R-1], arr[R])...))
```

## References

- [GeeksForGeeks - Range LCM Queries](https://www.geeksforgeeks.org/dsa/range-lcm-queries/)

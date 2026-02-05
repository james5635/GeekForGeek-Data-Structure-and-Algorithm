# 4Sum - Find Four Elements that Sum to Given Value

## Problem Description

Given an array and a target sum, find all unique quadruplets (i, j, k, l) such that arr[i] + arr[j] + arr[k] + arr[l] = target and all indices are distinct. Each quadruplet should be unique (no duplicates).

**Example:**
```
Input: arr = [1, 0, -1, 0, -2, 2], target = 0
Output: [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]

Explanation: All these quadruplets sum to 0.
```

## Algorithm

**Approach:** Sorting + Two Nested Loops + Two Pointers

**Steps:**
1. Sort the array
2. Use two nested loops to fix first two elements (i, j)
3. Skip duplicates at each level
4. Use two pointers for remaining two elements
5. Skip duplicates when moving pointers
6. Collect all valid quadruplets

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Sorting + Two Loops + Two Pointers | O(n³) | O(1) extra |
| Brute Force | O(n⁴) | O(1) |
| Hash Map | O(n²) avg | O(n²) |

## Functions

### `four_sum(arr, target)`
Find all unique quadruplets with sum equal to target.

**Parameters:**
- `arr`: Input array of integers
- `target`: Target sum value

**Returns:**
- List of unique quadruplets (each as a tuple) that sum to target

### `has_four_sum(arr, target)`
Check if there exists any quadruplet with given sum.

**Returns:**
- Boolean indicating existence

## Usage

```python
from solution import four_sum

arr = [1, 0, -1, 0, -2, 2]
target = 0
result = four_sum(arr, target)
print(result)  # [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Extension of 3Sum**: Same approach with one more nested loop
2. **Duplicate Handling**: Skip at all four levels (i, j, left, right)
3. **Time Complexity**: O(n³) is the best we can do without extra space
4. **Early Pruning**: Can skip some iterations with bounds checking

## References

- [GeeksForGeeks - Find Four Elements that Sum to Given Value](https://www.geeksforgeeks.org/dsa/find-four-elements-that-sum-to-a-given-value-set-2/)

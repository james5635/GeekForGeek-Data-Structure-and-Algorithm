# Distinct Quadruplets with Sum Equal to Given Value

## Problem Description

Given an array and a target sum, find all distinct quadruplets (unique sets of four elements) that sum to the target. Similar to 4Sum but with emphasis on distinct quadruplets.

**Example:**
```
Input: arr = [1, 2, 3, 4, 5, 6, 7, 8], target = 18
Output: Multiple quadruplets like (1, 2, 7, 8), (1, 3, 6, 8), etc.

Explanation: Find all unique combinations of 4 elements that sum to 18.
```

## Algorithm

**Approach:** Sorting + Two Nested Loops + Two Pointers

**Steps:**
1. Sort the array
2. Use two nested loops for first two elements
3. Skip duplicates at each level
4. Use two-pointer technique for remaining elements
5. Collect all valid quadruplets

**Difference from 4Sum:** Same algorithm, emphasis on handling duplicates correctly.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Sorting + Two Loops + Two Pointers | O(n³) | O(1) extra |
| Hash Map | O(n²) avg | O(n²) |

## Functions

### `find_distinct_quadruplets(arr, target)`
Find all distinct quadruplets with sum equal to target.

**Parameters:**
- `arr`: Input array of integers
- `target`: Target sum value

**Returns:**
- List of distinct quadruplets (each as a tuple) that sum to target

### `count_distinct_quadruplets(arr, target)`
Count the number of distinct quadruplets with given sum.

## Usage

```python
from solution import find_distinct_quadruplets

arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 18
result = find_distinct_quadruplets(arr, target)
print(result)
# [(1, 2, 7, 8), (1, 3, 6, 8), (1, 4, 5, 8), ...]
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Distinct vs Unique**: Emphasis on avoiding duplicate quadruplets
2. **Sorting Required**: Enables duplicate detection
3. **Skip Duplicates**: At i, j, left, and right levels
4. **Multiple Solutions**: Often many valid quadruplets exist

## References

- [GeeksForGeeks - Find All Distinct Quadruplets that Sum Up to Given Value](https://www.geeksforgeeks.org/dsa/find-all-distinct-quadruplets-in-an-array-that-sum-up-to-a-given-value/)

# 3Sum Zero - Find Triplets with Sum Equal to Zero

## Problem Description

Given an array, find all unique triplets (i, j, k) such that arr[i] + arr[j] + arr[k] = 0 and i, j, k are distinct. This is a special case of the 3Sum problem with target = 0.

**Example:**
```
Input: [-1, 0, 1, 2, -1, -4]
Output: [(-1, -1, 2), (-1, 0, 1)]

Explanation:
- -1 + (-1) + 2 = 0
- -1 + 0 + 1 = 0
```

## Algorithm

**Approach:** Sorting + Two Pointers

**Steps:**
1. Sort the array
2. For each element at index i:
   - Skip positive numbers (can't form sum = 0 with positive first element)
   - Skip duplicates
   - Use two pointers to find pairs that sum to -arr[i]
   - Skip duplicates when moving pointers
3. Collect all valid triplets

**Key Optimization:** Since array is sorted, once arr[i] > 0, we can break (all remaining elements are positive).

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Sorting + Two Pointers | O(n²) | O(1) extra |
| Brute Force | O(n³) | O(1) |
| Hash Set | O(n²) | O(n) |

## Functions

### `three_sum_zero(arr)`
Find all unique triplets with sum equal to zero.

**Parameters:**
- `arr`: Input array of integers

**Returns:**
- List of unique triplets (each as a tuple) that sum to zero

### `has_three_sum_zero(arr)`
Check if there exists any triplet with sum zero.

**Returns:**
- Boolean indicating existence

## Usage

```python
from solution import three_sum_zero

arr = [-1, 0, 1, 2, -1, -4]
result = three_sum_zero(arr)
print(result)  # [(-1, -1, 2), (-1, 0, 1)]

# Check existence
exists = has_three_sum_zero(arr)
print(exists)  # True
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Early Termination**: If arr[i] > 0, break (can't make sum = 0)
2. **Skip Duplicates**: Essential to get unique triplets
3. **Sorted Array**: Enables efficient two-pointer search
4. **Target = 0**: Special case allows early termination on positive numbers

## References

- [GeeksForGeeks - Find Triplets in Array Whose Sum Equal to Zero](https://www.geeksforgeeks.org/dsa/find-triplets-array-whose-sum-equal-zero/)

# Unique Triplets with Given Sum

## Problem Description

Given an array and a target sum, find all unique triplets in the array that sum up to the given value. Each triplet should be unique (no duplicates).

**Example:**
```
Input: arr = [1, 2, 3, 4, 5], target = 9
Output: [(1, 3, 5), (2, 3, 4)]

Explanation: 
- 1 + 3 + 5 = 9
- 2 + 3 + 4 = 9
```

## Algorithm

**Approach:** Sorting + Two Pointers

**Steps:**
1. Sort the array
2. For each element at index i:
   - Skip duplicates
   - Use two pointers (left, right) to find pairs that sum to target - arr[i]
   - Skip duplicates when moving pointers
3. Collect all valid triplets

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Sorting + Two Pointers | O(n²) | O(1) extra |
| Brute Force | O(n³) | O(1) |
| Hash Set | O(n²) | O(n) |

## Functions

### `find_unique_triplets_sum(arr, target)`
Find all unique triplets with sum equal to target.

**Parameters:**
- `arr`: Input array of integers
- `target`: Target sum value

**Returns:**
- List of unique triplets (each as a tuple) that sum to target

### `count_unique_triplets(arr, target)`
Count the number of unique triplets with given sum.

## Usage

```python
from solution import find_unique_triplets_sum

arr = [1, 2, 3, 4, 5]
target = 9
result = find_unique_triplets_sum(arr, target)
print(result)  # [(1, 3, 5), (2, 3, 4)]
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Sorting First**: Enables two-pointer technique
2. **Skip Duplicates**: Check arr[i] == arr[i-1] to avoid duplicate triplets
3. **Two Pointers**: After fixing one element, find pair in O(n) time
4. **Early Termination**: Can break early in some cases

## References

- [GeeksForGeeks - Unique Triplets with Sum Equal to Given Value](https://www.geeksforgeeks.org/dsa/unique-triplets-sum-given-value/)

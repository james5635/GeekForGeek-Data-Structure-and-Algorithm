# Four Elements that Sum to a Given Value

## Problem Statement
Given an array arr[] of n integers and a target sum, find four elements in the array that sum up to the target value. Return all unique quadruplets.

## Examples
- Input: arr[] = [1, 0, -1, 0, -2, 2], target = 0
  - Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

- Input: arr[] = [2, 2, 2, 2, 2], target = 8
  - Output: [[2, 2, 2, 2]]

## Approaches

### 1. Sorting + Two Pointers (Optimal)
1. Sort the array - O(n log n)
2. Use two nested loops for first two elements
3. Use two pointers for remaining two elements
4. Skip duplicates at each level
5. **Time Complexity**: O(n³)
6. **Space Complexity**: O(1) auxiliary

### 2. Hash Map
1. Store all pairs and their sums in hash map
2. For each pair, check if target - sum exists
3. **Time Complexity**: O(n²)
4. **Space Complexity**: O(n²)

### 3. Brute Force
1. Check all combinations of 4 elements
2. **Time Complexity**: O(n⁴)
3. **Space Complexity**: O(1)

## Algorithm Steps (Two Pointer)
```
Sort array
For i from 0 to n-4:
    Skip if duplicate
    For j from i+1 to n-3:
        Skip if duplicate
        left = j + 1, right = n - 1
        While left < right:
            sum = arr[i] + arr[j] + arr[left] + arr[right]
            Process based on sum comparison
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Best For |
|----------|----------------|------------------|----------|
| Two Pointer | O(n³) | O(1) aux | General use, memory constrained |
| Hash Map | O(n²) | O(n²) | When memory available, faster |
| Brute Force | O(n⁴) | O(1) | Only for very small n |

## Key Insights
- Early termination significantly improves practical performance
- Duplicate skipping requires checking at each level
- Two-pointer approach scales better for large n due to better cache locality

# Unique Triplets with Given Sum

## Problem Statement
Given an array arr[] of n integers and a target sum, find all unique combinations of three elements in the array that sum up to the target. The triplets should be unique (no duplicates) and each triplet should be sorted in ascending order.

## Examples
- Input: arr[] = [1, 2, 3, 4, 5], target = 9
  - Output: [[1, 3, 5], [2, 3, 4]]

- Input: arr[] = [0, -1, 2, -3, 1], target = 0
  - Output: [[-3, 1, 2], [-1, 0, 1]]

- Input: arr[] = [1, 1, 1, 1], target = 3
  - Output: [[1, 1, 1]]

## Approaches

### 1. Sorting + Two Pointers (Optimal)
1. Sort the array - O(n log n)
2. For each element i, use two pointers (left, right) to find pairs
3. Skip duplicates to ensure unique triplets
4. **Time Complexity**: O(n²)
5. **Space Complexity**: O(1) auxiliary

### 2. Hash Set
1. For each pair, check if target - sum exists in hash set
2. Use set to avoid duplicates
3. **Time Complexity**: O(n²)
4. **Space Complexity**: O(n)

### 3. Binary Search
1. Sort the array
2. For each pair, binary search for the third element
3. **Time Complexity**: O(n² log n)
4. **Space Complexity**: O(1)

## Algorithm Steps (Two Pointer)
```
Sort array
For i from 0 to n-3:
    If i > 0 and arr[i] == arr[i-1]: skip (duplicate)
    left = i + 1, right = n - 1
    While left < right:
        sum = arr[i] + arr[left] + arr[right]
        If sum == target:
            Add triplet to result
            Skip duplicates for left and right
            left++, right--
        Else if sum < target: left++
        Else: right--
```

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Two Pointer | O(n²) | O(1) aux | Best for general use |
| Hash Set | O(n²) | O(n) | Simpler but more space |
| Binary Search | O(n² log n) | O(1) | Not recommended |

## Key Insights
- Sorting enables two-pointer technique
- Duplicate skipping is crucial for uniqueness
- Early termination can optimize for large arrays

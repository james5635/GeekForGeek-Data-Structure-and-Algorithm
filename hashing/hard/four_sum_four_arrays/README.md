# 4Sum from Four Sorted Arrays

## Problem Description

Given four sorted arrays A, B, C, D of size n each, find the count of quadruples (i, j, k, l) such that:
```
A[i] + B[j] + C[k] + D[l] = 0
```

## Examples

- **Input**:  
  A = [-1, 2], B = [-2, 1]  
  C = [1, 2], D = [2, -1]  
  **Output**: 2  
  **Explanation**: The valid quadruples are: [-1, -2, 2, 1] and [2, 1, 1, -4]

## Approach

### Hash Map Method (O(n²))

1. **Store Pair Sums**: Create a hash map of all possible sums from pairs in A and B
2. **Count Complements**: For each pair in C and D, check if the negative of their sum exists in the hash map
3. **Accumulate Count**: Add the frequency of the complement sum to the result

## Complexity Analysis

- **Time Complexity**: O(n²)
  - O(n²) to compute all pair sums from A and B
  - O(n²) to check all pairs from C and D
  
- **Space Complexity**: O(n²) for the hash map

## Why Hashing Works

Since we need `A[i] + B[j] + C[k] + D[l] = 0`, we can rewrite it as:
```
A[i] + B[j] = -(C[k] + D[l])
```

By storing all `A[i] + B[j]` values and their frequencies in a hash map, we can quickly check for each `C[k] + D[l]` if the required complement exists.

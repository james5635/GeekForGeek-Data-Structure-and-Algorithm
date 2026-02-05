# Count Quadruplets with Given Sum

## Problem Description

Given an array `arr[]` and an integer `target`, find the count of all quadruplets (i, j, k, l) such that `arr[i] + arr[j] + arr[k] + arr[l] == target`.

## Examples

- **Input**: arr = [1, 0, -1, 0, -2, 2], target = 0  
  **Output**: 3  
  **Explanation**: The quadruplets are: [1,0,-1,0], [2,-2,0,0], [1,-1,-2,2]

## Approaches

### 1. Brute Force (O(n^4))
Check all possible combinations of 4 elements.

### 2. Hashing Approach (O(n^2))
- Store all pair sums in a hash map
- For each new pair, check if `target - current_sum` exists

### 3. Two Pointers (O(n^3))
- Sort the array first
- Use two nested loops for first two elements
- Use two pointers for the remaining sum

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n^4) | O(1) |
| Hashing | O(n^2) | O(n^2) |
| Two Pointers | O(n^3) | O(1) |

## Key Insight

The hashing approach reduces time complexity by trading space. Instead of iterating through all 4 elements, we compute pair sums and use the hash map to find complementary pairs.

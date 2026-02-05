# Four Elements Sum (4Sum)

## Problem Description

Given an array `arr[]` and an integer `target`, find all unique quadruplets in the array which sum up to the target value. The solution set must not contain duplicate quadruplets.

## Examples

- **Input**: arr = [1, 0, -1, 0, -2, 2], target = 0  
  **Output**: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

## Approaches

### 1. Hashing Approach (O(n^2))
- Store all pair sums in a hash map
- For each pair, check if `target - current_sum` exists
- Handle duplicate indices carefully

### 2. Two Pointers (O(n^3))
- Sort the array first
- Use two nested loops for first two elements
- Use two pointers for the remaining elements
- Skip duplicates to avoid repeated quadruplets

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Hashing | O(n^2) average, O(n^3) worst | O(n^2) |
| Two Pointers | O(n^3) | O(1) excluding result |

## Key Points

- Sorting helps in skipping duplicates efficiently
- Early termination conditions can optimize performance
- Must ensure all four indices are distinct

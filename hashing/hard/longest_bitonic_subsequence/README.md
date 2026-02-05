# Longest Strictly Bitonic Subsequence

## Problem Description

Given an array `arr[]`, find the length of the longest **strictly** bitonic subsequence. A bitonic subsequence is a sequence that:
1. First increases (strictly)
2. Then decreases (strictly)
3. Has at least one element in both parts

## Examples

- **Input**: arr = [1, 2, 5, 3, 2]  
  **Output**: 5  
  **Explanation**: The entire array is bitonic: 1 < 2 < 5 > 3 > 2

- **Input**: arr = [1, 11, 2, 10, 4, 5, 2, 1]  
  **Output**: 6  
  **Explanation**: One possible subsequence: [1, 2, 10, 5, 2, 1]

## Approach

### Dynamic Programming

1. **LIS from Left**: Calculate longest increasing subsequence ending at each position
2. **LDS from Right**: Calculate longest decreasing subsequence starting at each position
3. **Combine**: For each position as peak, `bitonic_length = LIS[i] + LDS[i] - 1`

## Complexity Analysis

- **Time Complexity**: O(n²) - nested loops for LIS and LDS
- **Space Complexity**: O(n) - for DP arrays

## Key Points

- Strictly bitonic means no equal adjacent elements
- Must have both increasing and decreasing parts (length at least 2)
- Single element or monotonic arrays have no valid bitonic subsequence

## Variations

1. **Non-strictly bitonic**: Allow equal elements
2. **Find the subsequence**: Reconstruct the actual sequence using parent pointers
3. **Count bitonic subsequences**: Use DP with counting

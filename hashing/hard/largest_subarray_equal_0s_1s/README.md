# Largest Subarray with Equal 0s and 1s

## Problem Description

Given a binary array containing only 0s and 1s, find the length of the largest subarray with equal number of 0s and 1s.

## Examples

- **Input**: arr = [1, 0, 1, 1, 1, 0, 0]  
  **Output**: 6  
  **Explanation**: Subarray [0, 5] has three 0s and three 1s

- **Input**: arr = [0, 0, 1, 1, 0]  
  **Output**: 4  
  **Explanation**: Subarrays [0, 3] or [1, 4] both have two 0s and two 1s

## Approach

### Prefix Sum with Hash Map

1. **Transform**: Replace all 0s with -1s
2. **Prefix Sum**: Calculate running sum as we traverse
3. **Hash Map**: Store first occurrence of each prefix sum
4. **Detect**: When prefix sum repeats, subarray between indices has sum 0 (equal 0s and 1s)

## Key Insight

After replacing 0s with -1s:
- Prefix sum = 0 means equal 0s and 1s from start
- Same prefix sum at indices i and j means subarray (i+1, j) has equal 0s and 1s

## Complexity Analysis

- **Time Complexity**: O(n) - single pass through array
- **Space Complexity**: O(n) - for hash map

## Why This Works

If prefix sum is the same at two different positions, the elements between them must sum to 0, meaning equal numbers of 1s and -1s (original 0s).

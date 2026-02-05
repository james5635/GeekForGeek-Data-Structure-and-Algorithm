# Find All Triplets with Zero Sum

## Problem Statement
Given an array arr[], find all unique triplets {i, j, k} such that arr[i] + arr[j] + arr[k] = 0 and i < j < k.

## Approach
Use sorting with two-pointer technique:
1. Sort the array while preserving original indices
2. Fix one element, use two pointers to find pair with sum = -fixed element
3. Skip duplicates to avoid duplicate triplets
4. Return sorted indices of each triplet

## Complexity
- **Time**: O(N^2) - Outer loop + two pointers
- **Space**: O(1) excluding output space (or O(N) for indexed array)

## Example
```
Input: arr[] = [0, -1, 2, -3, 1]
Output: [[0, 1, 4], [2, 3, 4]]
Explanation: 
- arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
- arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0
```

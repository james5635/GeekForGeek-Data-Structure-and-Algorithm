# Subarray with 0 Sum

## Problem Statement
Given an array of positive and negative numbers, find if there is a subarray (of size at least one) with sum equal to 0.

## Approach
Use prefix sum with hash set:
- Track cumulative sum as we iterate
- If prefix sum repeats at indices i and j, subarray (i+1 to j) has sum 0
- Also check if prefix sum becomes 0 at any point

## Complexity
- **Time**: O(N) - Single pass through array
- **Space**: O(N) - Hash set for prefix sums

## Example
```
Input: {4, 2, -3, 1, 6}
Output: True
Explanation: Subarray [2, -3, 1] from index 1 to 3 has sum 0
```

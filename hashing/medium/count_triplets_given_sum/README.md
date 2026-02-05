# Count Triplets with Given Sum

## Problem Statement
Given an array arr[] and a target value, find the count of triplets having sum equal to the given target.

## Approach
Use hashing with two-pointer technique:
1. Fix one element
2. Use hash set to find pairs with sum = (target - fixed element)
3. For sorted arrays, use two-pointer technique for better handling of duplicates

## Complexity
- **Time**: O(N^2) - Fix one element, find pair in remaining
- **Space**: O(N) - Hash set for storing elements

## Example
```
Input: arr[] = [0, -1, 2, -3, 1], target = -2
Output: 2
Triplets: (0, -3, 1) and (-1, 2, -3)
```

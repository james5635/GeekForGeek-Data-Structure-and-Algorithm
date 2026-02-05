# Longest Consecutive Subsequence

## Problem Statement
Given an array of integers, find the length of the longest subsequence where elements are consecutive integers (can be in any order).

## Approach
**Optimized Hashing Approach**:
1. Insert all elements into a hash set for O(1) lookup
2. For each element, check if it's the start of a sequence (element-1 not in set)
3. If it's a start, count consecutive elements
4. Track and return maximum length found

## Complexity
- **Time**: O(N) - Each element visited at most twice
- **Space**: O(N) - Hash set storage

## Example
```
Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: Longest consecutive subsequence is [1, 2, 3, 4, 5, 6]
```

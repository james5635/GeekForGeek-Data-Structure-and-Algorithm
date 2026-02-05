# Pair with Given Sum

## Problem

Given an array of integers and a target sum, check if there exists a pair of elements in the array whose sum equals the target sum.

## Approach

Use a hash set to store visited elements. For each element, check if `(target - element)` exists in the set. If found, a pair exists. Otherwise, add the current element to the set.

## Complexity

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(n) - hash set stores visited elements

## Example

```
Input: arr = [1, 4, 45, 6, 10, -8], target = 16
Output: True (pair: 6 + 10 = 16)
```

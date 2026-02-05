# Count Pairs with Given Sum

## Problem

Given an array of integers and a target sum, count the number of pairs of elements whose sum equals the target sum.

## Approach

Use a hash map to store frequency of elements. For each element, check how many times `(target - element)` has appeared before and add to count. This ensures we count each pair only once.

## Complexity

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(n) - hash map stores element frequencies

## Example

```
Input: arr = [1, 5, 7, -1, 5], target = 6
Output: 3
Explanation: Pairs are (1, 5), (1, 5), (7, -1)
```

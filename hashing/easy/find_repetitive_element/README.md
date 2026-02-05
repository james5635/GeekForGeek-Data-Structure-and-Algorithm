# Find Repetitive Element

## Problem

Given an array of n+1 integers where each integer is between 1 and n (inclusive), find the repetitive element. There is only one repeated number.

## Approach

**Hash Set Approach:** Use a hash set to track visited elements. Return the first element that is already in the set.

**XOR Approach:** XOR all elements from 1 to n, then XOR with all array elements. The result is the repetitive element (O(1) space).

## Complexity

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** 
  - Hash Set: O(n)
  - XOR: O(1)

## Example

```
Input: arr = [1, 2, 3, 3, 4]
Output: 3
```

# Minimum Removals to Make Array Elements Unique

## Problem

Given two arrays, find the minimum number of elements to remove from both arrays such that there is no common element between the resulting arrays.

## Approach

Find common elements between both arrays. For each common element, we need to remove all occurrences from one of the arrays. Choose to remove from the array with fewer occurrences to minimize total removals.

## Complexity

- **Time Complexity:** O(n + m) where n and m are array sizes
- **Space Complexity:** O(n + m) - frequency maps

## Example

```
Input: arr1 = [1, 2, 3, 4], arr2 = [2, 4, 5, 6]
Output: 2
Explanation: Remove 2 and 4 from either array
```

# Count Pairs with Difference K

## Problem

Given an array of integers and a difference k, count the number of pairs of elements whose absolute difference equals k.

## Approach

Use a hash map to store frequency of elements. For each element, check if `(element + k)` and `(element - k)` exist in the map. Special handling for k=0 to avoid counting same element twice.

## Complexity

- **Time Complexity:** O(n) - single pass through the array
- **Space Complexity:** O(n) - hash map stores element frequencies

## Example

```
Input: arr = [1, 5, 3, 4, 2], k = 3
Output: 2
Explanation: Pairs are (1, 4) and (5, 2)
```

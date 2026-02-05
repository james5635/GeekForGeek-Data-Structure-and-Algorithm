# Find Missing Elements in Range

## Problem

Given an array of distinct elements and a range [low, high], find all missing elements in the range that are not present in the array.

## Approach

Use a hash set for O(1) lookup. Iterate through the range [low, high] and check which elements are missing from the set.

## Complexity

- **Time Complexity:** O(n + (high-low+1)) where n is array size
- **Space Complexity:** O(n) - hash set stores array elements

## Example

```
Input: arr = [10, 12, 11, 15], low = 10, high = 15
Output: [13, 14]
```

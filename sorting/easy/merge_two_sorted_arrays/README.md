# Merge Two Sorted Arrays

## Problem Description

Given two sorted arrays `arr1[]` of size n and `arr2[]` of size m, merge these two arrays such that:
- The first n smallest elements of the combined sorted array are stored in `arr1[]`
- The remaining m largest elements are stored in `arr2[]`
- Both arrays remain sorted in non-decreasing order

## Algorithm

1. Use a temporary array to store the merged result
2. Apply two-pointer technique to merge both arrays in sorted order
3. Copy first n elements back to arr1 and remaining m elements to arr2

## Complexity Analysis

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(n + m) | O(n + m) |
| Average | O(n + m) | O(n + m) |
| Worst | O(n + m) | O(n + m) |

## Example

```
Input:  arr1 = [1, 3, 5, 7], arr2 = [2, 4, 6, 8]
Output: arr1 = [1, 2, 3, 4], arr2 = [5, 6, 7, 8]
```

## Key Points

- Two-pointer technique ensures optimal O(n+m) time complexity
- The algorithm handles duplicates correctly
- Space required for the temporary merged array
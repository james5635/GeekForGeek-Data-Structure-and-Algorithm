# Intersection of Two Sorted Arrays

## Problem Description

Given two sorted arrays `a[]` and `b[]`, return the intersection of both arrays. Intersection contains elements that are common in both arrays. The result should not contain duplicates and should be in sorted order.

## Algorithm

1. Initialize two pointers at the start of both arrays
2. Skip duplicates in both arrays
3. Compare elements at both pointers:
   - If a[i] < b[j], move pointer i
   - If a[i] > b[j], move pointer j
   - If equal, add to result and move both pointers
4. Return the result array

## Complexity Analysis

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(min(n, m)) | O(1) |
| Average | O(n + m) | O(min(n, m)) |
| Worst | O(n + m) | O(min(n, m)) |

## Example

```
Input:  a = [1, 1, 2, 2, 2, 4], b = [2, 2, 4, 4]
Output: [2, 4]
```

## Key Points

- Similar to merge step of merge sort
- Automatically handles duplicates
- Efficient two-pointer approach
- Result contains only unique elements
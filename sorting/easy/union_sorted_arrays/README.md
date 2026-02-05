# Union of Two Sorted Arrays

## Problem Description

Given two sorted arrays `a[]` and `b[]`, return the union of both arrays. Union contains all distinct elements present in either array. The result should be in sorted order.

## Algorithm

1. Initialize two pointers at the start of both arrays
2. Skip duplicates in both arrays
3. Compare elements at both pointers:
   - If a[i] < b[j], add a[i] to result and move i
   - If a[i] > b[j], add b[j] to result and move j
   - If equal, add once and move both
4. Add remaining elements from both arrays (skipping duplicates)
5. Return the result array

## Complexity Analysis

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(n + m) | O(n + m) |
| Average | O(n + m) | O(n + m) |
| Worst | O(n + m) | O(n + m) |

## Example

```
Input:  a = [1, 1, 2, 2, 2, 4], b = [2, 2, 4, 4]
Output: [1, 2, 4]
```

## Key Points

- Similar to merge step of merge sort
- Handles duplicates correctly
- Result contains only distinct elements
- Maintains sorted order
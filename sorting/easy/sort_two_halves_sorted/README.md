# Sort Array When Two Halves are Sorted

## Problem Description

Given an integer array `arr[]` whose first k elements and remaining n-k elements are each sorted, merge these two sorted halves into a single fully sorted array.

Note: There doesn't exist more than two sorted halves in an array.

## Algorithm

1. Find the split point where the first sorted half ends (where arr[i] > arr[i+1])
2. If no split point found, array is already sorted
3. Apply merge technique to combine both sorted halves
4. Return the merged sorted array

## Complexity Analysis

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(n) | O(n) |
| Average | O(n) | O(n) |
| Worst | O(n) | O(n) |

## Example

```
Input:  [2, 3, 8, -1, 7, 10]
Output: [-1, 2, 3, 7, 8, 10]
```

## Key Points

- First find the split index by scanning for first descending pair
- Uses merge technique from merge sort
- More efficient than sorting the entire array (O(n log n))
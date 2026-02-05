# Sort a Singly Linked List

## Problem Description

Given a singly linked list, sort it in non-decreasing order.

## Algorithm

This implementation uses **Merge Sort**, which is the most efficient and suitable algorithm for linked lists:

1. **Divide**: Split the list into two halves using slow/fast pointer technique
2. **Conquer**: Recursively sort both halves
3. **Combine**: Merge the two sorted halves

Why Merge Sort for Linked Lists?
- Guaranteed O(n log n) time complexity
- Stable sort
- No extra space needed for merging (unlike arrays)
- Sequential access pattern suits linked list traversal

## Complexity Analysis

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst | O(n log n) | O(log n) |

Space complexity is O(log n) due to recursion stack.

## Example

```
Input:  10 -> 30 -> 20 -> 5
Output: 5 -> 10 -> 20 -> 30
```

## Key Points

- Merge sort is preferred over quicksort for linked lists
- No random access needed
- Efficient memory usage
- Stable sorting algorithm
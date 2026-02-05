# Check if Array is Sorted

## Problem Statement
Given an array of size n, determine if the array is sorted in ascending order.

## Approach
### Iterative Approach
Traverse the array once, comparing each element with the next. If any element is greater than the next one, the array is not sorted.

### Recursive Approach
Recursively check if each element is less than or equal to the next element.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Iterative | O(n) | O(1) |
| Recursive | O(n) | O(n) - due to call stack |

## Key Points
- Handles edge cases: empty array, single element
- Works with duplicate values
- Both ascending and strictly ascending can be checked
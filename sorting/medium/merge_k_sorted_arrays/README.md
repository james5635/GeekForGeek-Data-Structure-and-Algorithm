# Merge K Sorted Arrays

## Problem Description

Given a 2D matrix where each row is a sorted array in non-decreasing order, merge all arrays into a single sorted array containing all elements.

## Examples

### Example 1
- **Input:** `[[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]`
- **Output:** `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`
- **Explanation:** Merging all elements and sorting them

### Example 2
- **Input:** `[[1, 2, 3, 4], [2, 2, 3, 4], [5, 5, 6, 6], [7, 8, 9, 9]]`
- **Output:** `[1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9]`

## Approaches

### Approach 1: Using Min-Heap (Recommended)

1. Create a min-heap and push the first element of each array along with array and element indices
2. Pop the minimum element from heap and add to result
3. Push the next element from the same array (if exists)
4. Repeat until heap is empty

**Time Complexity:** O(n log k) where n is total elements, k is number of arrays
**Space Complexity:** O(k) for the heap

### Approach 2: Divide and Conquer

1. Recursively divide the k arrays into two halves
2. Merge each half separately
3. Merge the two merged halves
4. Base case: single array

**Time Complexity:** O(n log k)
**Space Complexity:** O(n) for recursion stack and temporary arrays

### Approach 3: Naive (Sorting)

1. Flatten all arrays into one
2. Sort the combined array

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

## Comparison

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| Min-Heap | O(n log k) | O(k) | Different sized arrays, real-time streaming |
| Divide & Conquer | O(n log k) | O(n) | Equal sized arrays, parallel processing |
| Naive Sort | O(n log n) | O(n) | Simple implementation, small inputs |

## References

- [GeeksforGeeks - Merge K Sorted Arrays](https://www.geeksforgeeks.org/dsa/merge-k-sorted-arrays/)

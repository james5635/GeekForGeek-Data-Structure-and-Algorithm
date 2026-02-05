# Minimum Length Unsorted Subarray

## Problem Description

Given an unsorted array `arr[]`, find the subarray `arr[s...e]` such that sorting this subarray makes the whole array sorted.

If the given array is already sorted, return `[0, 0]`.

## Examples

### Example 1
- **Input:** `[10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]`
- **Output:** `(3, 8)`
- **Explanation:** Sorting the subarray `[30, 25, 40, 32, 31, 35]` makes the entire array sorted

### Example 2
- **Input:** `[0, 1, 15, 25, 6, 7, 30, 40, 50]`
- **Output:** `(2, 5)`
- **Explanation:** Sorting the subarray `[15, 25, 6, 7]` makes the entire array sorted

### Example 3
- **Input:** `[30, 20, 10]`
- **Output:** `(0, 2)`
- **Explanation:** The entire array needs to be sorted

## Algorithm

### Optimal O(n) Approach

1. **Find candidate unsorted subarray:**
   - Scan from left to right to find first element greater than its next element (left boundary)
   - Scan from right to left to find first element smaller than its previous element (right boundary)

2. **Check if sorting this subarray makes array sorted:**
   - Find minimum and maximum in the subarray
   - Extend left boundary: Find first element from left greater than subarray minimum
   - Extend right boundary: Find first element from right smaller than subarray maximum

3. **Return the final boundaries**

## Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Naive (Sorting) | O(n log n) | O(n) |
| Stack-based | O(n) | O(n) |
| **Optimal** | **O(n)** | **O(1)** |

## Key Insights

- The unsorted subarray is bounded by the first "out of order" elements from both ends
- However, the subarray might need to be extended if:
  - Elements before it are greater than the subarray's minimum
  - Elements after it are smaller than the subarray's maximum
- Finding min/max in the candidate subarray and comparing with outside elements is crucial

## References

- [GeeksforGeeks - Minimum Length Unsorted Subarray](https://www.geeksforgeeks.org/dsa/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/)

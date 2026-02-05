# Sort Array Containing 1 to N Values

## Problem Description

Given an array containing elements from 1 to n (where n is the array size), sort the array efficiently. We are not allowed to simply copy the numbers from 1 to n.

## Examples

### Example 1
- **Input:** `[2, 1, 3]`
- **Output:** `[1, 2, 3]`

### Example 2
- **Input:** `[3, 2, 5, 6, 1, 4]`
- **Output:** `[1, 2, 3, 4, 5, 6]`

## Algorithm

### Cycle Sort Approach (Optimal)

**Key Insight:** Each element `x` belongs at index `x-1`.

**Steps:**
1. Iterate through the array
2. For each element, if it's not at its correct position (`index != value - 1`), swap it with the element at its correct position
3. If element is already at correct position, move to next
4. Repeat until all elements are in place

**Why O(n)?**
- Each element is swapped at most once to reach its correct position
- Total swaps ≤ n
- If no swap needed, we increment pointer
- Total operations ≤ 2n = O(n)

## Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Standard Sort | O(n log n) | O(1) or O(n) |
| Counting Sort | O(n) | O(n) |
| **Cycle Sort** | **O(n)** | **O(1)** |

## Why This is Special

- **O(n) time:** Better than comparison-based sorts
- **O(1) space:** No extra memory needed
- **In-place:** Modifies original array
- **Minimum swaps:** Each element moves at most once

## References

- [GeeksforGeeks - Sort array containing 1 to n values](https://www.geeksforgeeks.org/dsa/sort-array-contain-1-n-values/)

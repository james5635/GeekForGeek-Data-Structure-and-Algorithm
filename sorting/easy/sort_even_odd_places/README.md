# Sort Even Increasing Odd Decreasing

## Problem Statement
Given an array, rearrange it such that:
- Elements at even indices (0, 2, 4, ...) are sorted in **increasing** order
- Elements at odd indices (1, 3, 5, ...) are sorted in **decreasing** order

## Approach
1. Extract all elements at even indices into one list
2. Extract all elements at odd indices into another list
3. Sort even list in ascending order
4. Sort odd list in descending order
5. Rebuild the array by interleaving the sorted lists

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Extract | O(n) | O(n) |
| Sort | O(n log n) | O(1) or O(n) |
| Rebuild | O(n) | O(1) |
| **Total** | **O(n log n)** | **O(n)** |

## Key Points
- Position parity (even/odd) is maintained
- Only the ordering within each group changes
- Original relative positions between even and odd indices are preserved
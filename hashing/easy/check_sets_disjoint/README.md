# Check Two Sets Disjoint

## Problem Statement

Given two sets represented by two arrays, check if the two sets are disjoint. Two sets are disjoint if they have no elements in common.

## Examples

- **Input:** arr1[] = {12, 34, 11, 9, 3}, arr2[] = {2, 1, 3, 5}  
  **Output:** false (3 is common)

- **Input:** arr1[] = {12, 34, 11, 9, 3}, arr2[] = {7, 2, 1, 5}  
  **Output:** true (no common elements)

## Approach

1. **Hash Set Method:** Insert all elements of the first array into a hash set, then iterate through the second array to check if any element exists in the set.

2. **Optimized Method:** Use the smaller array to create the hash set to minimize space usage.

## Complexity Analysis

- **Time Complexity:** O(m + n) where m and n are sizes of the arrays
- **Space Complexity:** O(min(m, n)) for the optimized version

## Files

- `solution.py` - Contains implementation with test cases

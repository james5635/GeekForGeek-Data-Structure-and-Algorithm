# Array is Subset of Another Array

## Problem Statement

Given two arrays `arr1[]` and `arr2[]` of size m and n respectively, determine whether `arr2[]` is a subset of `arr1[]`. Array `arr2[]` is considered a subset of `arr1[]` if all elements of `arr2[]` are present in `arr1[]`.

## Examples

- **Input:** arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}  
  **Output:** true

- **Input:** arr1[] = {1, 2, 3, 4, 5}, arr2[] = {2, 3, 6}  
  **Output:** false

## Approach

1. **Hash Set Method:** Insert all elements of `arr1[]` into a hash set, then iterate through `arr2[]` to check if each element exists in the set.

2. **Counter Method:** Use hash map to count frequencies, useful when duplicates matter.

## Complexity Analysis

- **Time Complexity:** O(m + n) where m and n are sizes of the arrays
- **Space Complexity:** O(m) for storing elements in hash set

## Files

- `solution.py` - Contains implementation with test cases

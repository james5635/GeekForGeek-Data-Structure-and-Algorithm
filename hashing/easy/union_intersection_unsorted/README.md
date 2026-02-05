# Union and Intersection of Two Unsorted Arrays

## Problem Statement

Given two unsorted arrays, find their union and intersection:
- **Union**: All distinct elements from both arrays
- **Intersection**: Common elements between both arrays

## Examples

- **Input:** arr1[] = {3, 8, 2, 10, 5}, arr2[] = {7, 2, 10, 9, 3}  
  **Output:**  
  - Union: {2, 3, 5, 7, 8, 9, 10}  
  - Intersection: {2, 3, 10}

## Approach

Use **hash sets** for O(1) lookups:

**For Union:**
- Convert both arrays to sets
- Use set union operation (`|`) to get all distinct elements
- Time: O(m + n)

**For Intersection:**
- Convert first array to set for lookups
- Iterate through second array and check membership
- Or use set intersection operation (`&`)
- Time: O(m + n)

## Complexity Analysis

- **Time Complexity:** O(m + n) where m and n are sizes of the arrays
- **Space Complexity:** O(m + n) for storing elements in hash sets

## Files

- `solution.py` - Contains implementation with test cases

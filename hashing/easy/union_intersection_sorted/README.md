# Union and Intersection of Two Sorted Arrays

## Problem Statement

Given two sorted arrays, find their union and intersection:
- **Union**: All distinct elements from both arrays
- **Intersection**: Common elements between both arrays

## Examples

- **Input:** arr1[] = {1, 3, 4, 5, 7}, arr2[] = {2, 3, 5, 6}  
  **Output:**  
  - Union: {1, 2, 3, 4, 5, 6, 7}  
  - Intersection: {3, 5}

## Approach

Use the **two-pointer technique** to traverse both sorted arrays simultaneously:

**For Union:**
- Compare elements at both pointers
- Add the smaller element to union and advance that pointer
- If equal, add once and advance both pointers
- Handle duplicates by skipping consecutive same elements

**For Intersection:**
- Compare elements at both pointers
- If equal, add to intersection and advance both
- If not equal, advance pointer pointing to smaller element

## Complexity Analysis

- **Time Complexity:** O(m + n) where m and n are sizes of the arrays
- **Space Complexity:** O(m + n) for storing union and intersection results

## Files

- `solution.py` - Contains implementation with test cases

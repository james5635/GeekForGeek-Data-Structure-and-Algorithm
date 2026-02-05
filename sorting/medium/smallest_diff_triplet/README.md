# Smallest Difference Triplet

## Problem Description

Given three arrays of same size, find a triplet such that the difference between the maximum and minimum element in that triplet is minimum of all the triplets. A triplet should have one number from each of the three given arrays.

If there are multiple triplets with the same minimum difference, return the one with the smallest sum of its elements.

## Examples

### Example 1
- **Input:** 
  - arr1 = [5, 2, 8]
  - arr2 = [10, 7, 12]
  - arr3 = [9, 14, 6]
- **Output:** (7, 6, 5) or any permutation
- **Explanation:** The triplet has minimum difference of 2 (7-5=2)

### Example 2
- **Input:**
  - arr1 = [15, 12, 18, 9]
  - arr2 = [10, 17, 13, 8]
  - arr3 = [14, 16, 11, 5]
- **Output:** (11, 10, 9) or any permutation
- **Explanation:** The triplet has minimum difference of 2

## Approach

### Efficient Approach - Sorting + Three Pointers

1. Sort all three arrays in non-decreasing order
2. Initialize three pointers, one for each array at index 0
3. Calculate the current triplet's max, min, and difference
4. Track the triplet with minimum difference
5. Increment the pointer pointing to the smallest element
6. Repeat until any pointer reaches the end

**Why it works:** By always moving the pointer of the smallest element, we try to reduce the difference between max and min. This greedy approach ensures we explore all potentially better triplets.

## Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n³) | O(1) |
| Sorting + 3 Pointers | O(n log n) | O(1) |

## Key Points

- Sorting enables efficient traversal
- Three-pointer technique is optimal for finding closest triplets
- If multiple triplets have same min difference, pick the one with smallest sum
- Can handle negative numbers and duplicates

## References

- [GeeksforGeeks - Smallest Difference Triplet](https://www.geeksforgeeks.org/dsa/smallest-difference-triplet-from-three-arrays/)

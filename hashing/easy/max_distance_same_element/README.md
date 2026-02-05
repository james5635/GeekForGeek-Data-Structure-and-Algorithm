# Maximum Distance Between Two Occurrences of Same Element

## Problem Statement

Given an array with repeated elements, find the maximum distance between two occurrences of the same element. The distance is measured as the difference between the indices.

## Examples

- **Input:** arr[] = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2}  
  **Output:** 10  
  **Explanation:** Maximum distance for element 2 is 11 - 1 = 10 (first occurrence at index 1 and last at index 11)

## Approach

Use a hash map to store the first occurrence index of each element. As we iterate through the array:
- If element is not in the map, store its index as first occurrence
- If element is already in the map, calculate distance and update maximum if needed

## Complexity Analysis

- **Time Complexity:** O(n) where n is the size of the array
- **Space Complexity:** O(n) for storing first occurrences in the hash map

## Files

- `solution.py` - Contains implementation with test cases

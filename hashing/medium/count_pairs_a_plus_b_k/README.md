# Count Pairs with Sum Equal to K

## Problem Statement

Given an array of integers and a target sum k, count the number of pairs (a, b) such that a + b = k.

## Examples

- **Input:** arr[] = {1, 5, 7, -1, 5}, k = 6  
  **Output:** 3  
  **Explanation:** Pairs are (1, 5), (1, 5), (7, -1)

- **Input:** arr[] = {1, 1, 1, 1}, k = 2  
  **Output:** 6  
  **Explanation:** All pairs of 1s: C(4,2) = 6

## Approach

1. **Hash Map:** Store frequency of each element
2. **Count Complements:** For each element, count how many (k - element) exist
3. **Handle Duplicates:** Carefully count pairs with same values

## Complexity Analysis

- **Time Complexity:** O(n) where n is array size
- **Space Complexity:** O(n) for hash map

## Files

- `solution.py` - Contains implementation with test cases

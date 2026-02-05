# Kth Distinct Element in Array

## Problem Statement

Given an array of integers and a number k, find the kth distinct element in the array. Distinct elements are those that appear exactly once in the array.

## Examples

- **Input:** arr[] = {1, 2, 1, 3, 4, 2, 5}, k = 2  
  **Output:** 3  
  **Explanation:** Distinct elements in order: 3, 4, 5. 2nd distinct is 3.

- **Input:** arr[] = {1, 2, 2, 3, 3, 4}, k = 1  
  **Output:** 1  
  **Explanation:** First distinct element is 1

## Approach

1. **Frequency Count:** Use hash map to count occurrences of each element
2. **Traverse Array:** Find kth element with frequency exactly 1
3. **Maintain Order:** Elements are considered in order of first appearance

## Complexity Analysis

- **Time Complexity:** O(n) where n is array size
- **Space Complexity:** O(n) for hash map

## Files

- `solution.py` - Contains implementation with test cases

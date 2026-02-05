# Count Distinct Elements in Every Window

## Problem Statement

Given an array of integers and a window size k, count the number of distinct elements in every contiguous subarray (window) of size k.

## Examples

- **Input:** arr[] = {1, 2, 1, 3, 4, 2, 3}, k = 4  
  **Output:** 3 4 4 3  
  **Explanation:** 
  - Window 1: {1, 2, 1, 3} -> 3 distinct
  - Window 2: {2, 1, 3, 4} -> 4 distinct
  - Window 3: {1, 3, 4, 2} -> 4 distinct
  - Window 4: {3, 4, 2, 3} -> 3 distinct

## Approach

1. **Sliding Window:** Use a hash map to maintain frequency count of elements in current window
2. **Track Distinct Count:** Maintain a counter for distinct elements
3. **Slide Window:** Remove leftmost element and add new right element, updating counts

## Complexity Analysis

- **Time Complexity:** O(n) where n is array size
- **Space Complexity:** O(k) for storing at most k elements

## Files

- `solution.py` - Contains implementation with test cases

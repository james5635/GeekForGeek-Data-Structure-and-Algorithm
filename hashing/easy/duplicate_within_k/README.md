# Duplicate Within K Distance

## Problem Statement

Given an unsorted array that may contain duplicates, check if the array contains any duplicate elements within a distance of k. In other words, check if there are two identical elements at indices i and j where |i - j| <= k.

## Examples

- **Input:** arr[] = {1, 2, 3, 4, 1, 2, 3, 4}, k = 3  
  **Output:** false  
  **Explanation:** All duplicates are more than k distance away.

- **Input:** arr[] = {1, 2, 3, 1, 4, 5}, k = 3  
  **Output:** true  
  **Explanation:** Element 1 repeats at index 0 and index 3 (distance = 3 <= k)

## Approach

Use a hash set (sliding window) to keep track of elements in the current window of size k:
1. Maintain a window of at most k elements using a hash set
2. Slide the window through the array
3. If current element is already in the window, duplicate found
4. Remove element that falls outside the window as we progress

## Complexity Analysis

- **Time Complexity:** O(n) where n is the size of the array
- **Space Complexity:** O(k) for maintaining the window of size k

## Files

- `solution.py` - Contains implementation with test cases

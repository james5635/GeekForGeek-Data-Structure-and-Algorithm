# Smallest Subarray with K Distinct Elements

## Problem Statement

Given an array of integers and a number k, find the smallest subarray that contains exactly k distinct elements.

## Examples

- **Input:** arr[] = {1, 2, 1, 3, 4, 2, 3}, k = 3  
  **Output:** [1, 3, 4] or [4, 2, 3] (length 3)  
  **Explanation:** Smallest subarrays with exactly 3 distinct elements

- **Input:** arr[] = {1, 2, 3, 4, 5}, k = 3  
  **Output:** [1, 2, 3]  
  **Explanation:** Subarray from index 0 to 2

## Approach

1. **Sliding Window:** Use two pointers to maintain a window
2. **Hash Map:** Track frequency of elements in current window
3. **Shrink Window:** When we have k distinct, try to minimize window size

## Complexity Analysis

- **Time Complexity:** O(n) where n is array size
- **Space Complexity:** O(k) for storing at most k distinct elements

## Files

- `solution.py` - Contains implementation with test cases

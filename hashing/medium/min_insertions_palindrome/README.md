# Minimum Insertions to Form Longest Palindrome

## Problem Statement

Given a string, find the minimum number of insertions needed to make it a palindrome. Characters can be inserted at any position.

## Examples

- **Input:** "abcd"  
  **Output:** 3  
  **Explanation:** Insert 'd', 'c', 'b' at beginning or 'b', 'c', 'd' at end

- **Input:** "abba"  
  **Output:** 0  
  **Explanation:** Already a palindrome

## Approach

1. **Longest Palindromic Subsequence (LPS):** Find the longest subsequence that is a palindrome
2. **Min Insertions:** Minimum insertions = length - LPS length
3. **Dynamic Programming:** Use DP to find LPS in O(n^2) time

## Complexity Analysis

- **Time Complexity:** O(n^2) where n is string length
- **Space Complexity:** O(n^2) for DP table

## Files

- `solution.py` - Contains implementation with test cases

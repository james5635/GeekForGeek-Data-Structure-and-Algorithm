# Palindrome String

## Problem
Check if a given string is a palindrome. A palindrome reads the same forwards and backwards.

## Approach
Use two pointers - one at the start and one at the end. Compare characters and move pointers towards the center until they meet or a mismatch is found.

## Complexity
- **Time Complexity:** O(n) where n is the length of the string
- **Space Complexity:** O(1) for two-pointer approach, O(n) for slicing approach

## Files
- `solution.py` - Contains the implementation with test cases
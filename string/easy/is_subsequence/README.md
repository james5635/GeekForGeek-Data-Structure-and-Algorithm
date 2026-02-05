# Is Subsequence

## Problem
Given two strings str1 and str2, check if str1 is a subsequence of str2. A subsequence appears in the same relative order but not necessarily contiguous.

## Approach
Use two pointers - one for each string. Traverse str2 and match characters with str1. If all characters of str1 are found in order, it's a subsequence.

## Complexity
- **Time Complexity:** O(n) where n is the length of str2
- **Space Complexity:** O(1)

## Files
- `solution.py` - Contains the implementation with test cases
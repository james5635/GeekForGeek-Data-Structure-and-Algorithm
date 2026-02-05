# Check Anagram

## Problem
Given two strings, check whether they are anagrams of each other. Two strings are anagrams if they contain the same characters with the same frequency.

## Approach
Compare character frequencies in both strings. If they match exactly, the strings are anagrams. This can be done using Counter, sorting, or manual counting.

## Complexity
- **Time Complexity:** O(n) for counting approach, O(n log n) for sorting approach
- **Space Complexity:** O(1) - fixed size for character counts

## Files
- `solution.py` - Contains the implementation with test cases
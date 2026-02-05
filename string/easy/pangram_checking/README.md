# Pangram Checking

## Problem
Check if a given sentence is a pangram. A pangram is a sentence containing every letter of the English alphabet at least once.

## Approach
Convert the sentence to lowercase and collect all alphabetic characters in a set. If the set contains all 26 letters, it's a pangram.

## Complexity
- **Time Complexity:** O(n) where n is the length of the string
- **Space Complexity:** O(1) - at most 26 characters in the set

## Files
- `solution.py` - Contains the implementation with test cases
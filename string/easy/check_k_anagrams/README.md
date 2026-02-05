# Check K-Anagrams

## Problem
Two strings are called k-anagrams if they have the same length and can become anagrams by changing at most k characters.

## Approach
Count character frequencies in both strings. The number of changes needed is the sum of absolute differences divided by 2 (since each change fixes one excess and one deficit).

## Complexity
- **Time Complexity:** O(n) where n is the length of the strings
- **Space Complexity:** O(1) - fixed size character frequency array

## Files
- `solution.py` - Contains the implementation with test cases
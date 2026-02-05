# Check if String is Substring of Another

## Problem
Given two strings str1 and str2, check if str1 is a substring of str2.

## Approach
Iterate through str2 and check if str1 matches at each position. If a match is found, return True. If no match after checking all positions, return False.

## Complexity
- **Time Complexity:** O(n × m) where n and m are lengths of str2 and str1
- **Space Complexity:** O(1)

## Files
- `solution.py` - Contains the implementation with test cases
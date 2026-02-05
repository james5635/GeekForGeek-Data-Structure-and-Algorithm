# URLify String

## Problem
Replace all spaces in a string with '%20'. Assume the string has sufficient space at the end to hold additional characters.

## Approach
Iterate through the string up to the true length. Replace each space with '%20' and build the result string.

## Complexity
- **Time Complexity:** O(n) where n is the length of the string
- **Space Complexity:** O(n) for the result string

## Files
- `solution.py` - Contains the implementation with test cases
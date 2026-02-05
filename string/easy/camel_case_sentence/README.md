# Camel Case Sentence

## Problem
Convert a given sentence to camel case format. In camel case, the first word is in lowercase and subsequent words have their first letter capitalized with no spaces.

## Approach
Split the sentence into words. Keep the first word in lowercase, then capitalize the first letter of each remaining word and concatenate them.

## Complexity
- **Time Complexity:** O(n) where n is the length of the string
- **Space Complexity:** O(n) for storing the result

## Files
- `solution.py` - Contains the implementation with test cases
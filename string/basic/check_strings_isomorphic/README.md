# Check if Two Strings are Isomorphic

This program checks if two strings are isomorphic. Two strings are isomorphic if there's a one-to-one mapping between characters of the first string to characters of the second string.

## Algorithm
- Use two dictionaries to track character mappings
- Check if mapping is consistent in both directions
- Return False if any character maps to multiple characters

## Time Complexity
O(n) where n is the length of the strings

## Space Complexity
O(1) - Using fixed size dictionaries
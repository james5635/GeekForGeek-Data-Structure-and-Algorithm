# Count Substrings Start and End with 1

## Problem
Given a binary string, count the number of substrings that start and end with 1.

## Approach
If there are n occurrences of '1', the number of valid substrings is n * (n + 1) / 2. This is because we need to choose 2 positions (start and end) from n positions, plus single character '1's.

## Complexity
- **Time Complexity:** O(n) where n is the length of the string
- **Space Complexity:** O(1)

## Files
- `solution.py` - Contains the implementation with test cases
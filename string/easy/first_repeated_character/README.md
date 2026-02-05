# First Repeated Character

Find the earliest repeated character in a string.

## Problem Description
Given a string, find the earliest repeated character. The earliest repeated character means the character that occurs more than once and whose second occurrence has the smallest index.

## Time and Space Complexity
- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(1) using fixed-size array for lowercase letters

## Examples
- Input: "geeksforgeeks", Output: "e"
- Input: "hello geeks", Output: "l"
- Input: "abc", Output: "-1"

## Solution
The solution uses frequency counting to track character occurrences, then finds the first character with frequency greater than 1.

## Usage
```python
from solution import first_repeated_char

result = first_repeated_char("geeksforgeeks")  # Returns "e"
result = first_repeated_char("hello geeks")     # Returns "l"
result = first_repeated_char("abc")             # Returns "-1"
```
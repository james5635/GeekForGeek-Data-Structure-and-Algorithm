# Remove All Adjacent Duplicates

Remove all adjacent duplicate characters from a string repeatedly until no more duplicates can be removed.

## Problem Description
Given a string, remove all adjacent duplicate characters. Keep removing until no more adjacent duplicates can be removed.

## Time and Space Complexity
- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(n) for the stack

## Examples
- Input: "abbaca", Output: "ca"
- Input: "azxxzy", Output: "ay"
- Input: "geeksforgeek", Output: "gfsor"

## Solution
The solution uses a stack-like approach where we iterate through characters and remove adjacent pairs by popping from the stack when we encounter a duplicate.

## Usage
```python
from solution import remove_adjacent_duplicates

result = remove_adjacent_duplicates("abbaca")  # Returns "ca"
result = remove_adjacent_duplicates("azxxzy")  # Returns "ay"
```
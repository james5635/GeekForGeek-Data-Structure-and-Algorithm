# K-th Non-Repeating Character

Find the k-th non-repeating character in a string.

## Problem Description
Given a string `str` of length `n` and a number `k`, find the kth non-repeating character in the string.

## Time and Space Complexity
- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(n) for the hash map (or O(1) for fixed-size array if only lowercase letters)

## Examples
- Input: str = "geeksforgeeks", k = 3, Output: "r"
- Input: str = "geeksforgeeks", k = 2, Output: "o"

## Solution
The solution uses a hash map to count character frequencies, then iterates through the string to find the kth character with frequency 1.

## Usage
```python
from solution import kth_non_repeating_char

result = kth_non_repeating_char("geeksforgeeks", 3)  # Returns "r"
result = kth_non_repeating_char("geeksforgeeks", 2)  # Returns "o"
```
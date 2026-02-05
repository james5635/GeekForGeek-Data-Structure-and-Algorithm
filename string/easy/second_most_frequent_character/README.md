# Second Most Frequent Character

Find the second most frequent character in a string.

## Problem Description
Given a string, find the second most frequent character. If there are multiple characters with the same frequency, return any one of them. Handle edge cases where no second most frequent character exists.

## Time and Space Complexity
- **Time Complexity:** O(n), where n is the length of the string
- **Space Complexity:** O(k), where k is the number of unique characters

## Examples
- Input: "aababbccd", Output: "a" or "c" (most frequent: 'b', second most: 'a' and 'c')
- Input: "test", Output: "No second most frequent character"
- Input: "aaaa", Output: "No second most frequent character"

## Solution
The solution counts character frequencies using a hash map, then identifies the character with the second highest frequency. Multiple implementations handle ties and edge cases differently.

## Usage
```python
from solution import second_most_frequent_char

result = second_most_frequent_char("aababbccd")  # Returns "a" or "c"
result = second_most_frequent_char("test")         # Returns "No second most frequent character"
```
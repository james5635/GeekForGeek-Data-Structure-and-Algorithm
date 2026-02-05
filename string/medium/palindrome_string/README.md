# Palindrome String

Check if a string is a palindrome and related palindrome operations.

## Approach
- Use two-pointer technique to compare characters from both ends
- For robust checking, ignore case and non-alphanumeric characters
- Can also use string reversal for simple cases
- Additional functions for finding longest palindromic substring and counting palindromic substrings

## Complexity
- **Time Complexity**: O(n) for palindrome checking
- **Space Complexity**: O(1) additional space

## Usage
```python
from solution import is_palindrome, longest_palindromic_substring

result = is_palindrome("racecar")
print(result)  # Output: True

longest = longest_palindromic_substring("babad")
print(longest)  # Output: "bab" or "aba"
```
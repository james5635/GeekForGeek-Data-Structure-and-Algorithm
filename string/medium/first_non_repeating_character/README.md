# First Non-Repeating Character

Find the first non-repeating character in a string.

## Approach
- Count the frequency of each character using a hash map
- Iterate through the string again to find the first character with frequency 1
- For ASCII strings, we can optimize using a fixed-size array

## Complexity
- **Time Complexity**: O(n) - where n is the length of the string
- **Space Complexity**: O(1) - constant space for character count (256 for ASCII)

## Usage
```python
from solution import first_non_repeating_character

result = first_non_repeating_character("geeksforgeeks")
print(result)  # Output: 'f'
```
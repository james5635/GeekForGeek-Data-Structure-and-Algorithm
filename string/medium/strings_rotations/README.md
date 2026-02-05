# Strings Rotations of Each Other

Check if two strings are rotations of each other.

## Approach
- Check if the lengths of both strings are equal
- Concatenate the first string with itself
- Check if the second string is a substring of the concatenated string
- For optimal performance, can use KMP algorithm for substring search

## Complexity
- **Time Complexity**: O(n) - using substring search
- **Space Complexity**: O(n) - for the concatenated string

## Usage
```python
from solution import are_rotations

result = are_rotations("ABCD", "CDAB")
print(result)  # Output: True
```
# Reverse a String

This problem reverses a given string completely.

## Approach
- Use Python string slicing with step -1
- Alternative approaches: two-pointer swap, built-in reversed() function

## Complexity
- **Time:** O(n) where n is the length of the string
- **Space:** O(n) for the result string

## Usage
```python
from solution import reverse_string

result = reverse_string("hello")  # Returns "olleh"
result = reverse_string("Python")  # Returns "nohtyP"
```
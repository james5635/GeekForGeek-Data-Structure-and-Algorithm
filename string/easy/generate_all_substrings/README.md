# Generate All Substrings

This problem generates all possible substrings of a given string.

## Approach
- Use nested loops to generate substrings
- Outer loop for starting position, inner loop for ending position
- Alternative implementation using list comprehension

## Complexity
- **Time:** O(n²) for generating all substrings
- **Space:** O(n²) for storing all substrings

## Usage
```python
from solution import generate_all_substrings

substrings = generate_all_substrings("abc")  # Returns ["a", "ab", "abc", "b", "bc", "c"]
count = count_substrings("abc")  # Returns 6
```
# Count Distinct Substrings

Count the number of distinct substrings of a string.

## Approach
- Generate all possible substrings using nested loops
- Store each substring in a set to automatically handle duplicates
- For better performance with large strings, use suffix automaton or suffix array with LCP
- Rolling hash can also be used for optimization

## Complexity
- **Time Complexity**: O(n²) for basic approach, can be optimized to O(n) with suffix automaton
- **Space Complexity**: O(n²) in worst case for storing all substrings

## Usage
```python
from solution import count_distinct_substrings

result = count_distinct_substrings("abab")
print(result)  # Output: 7
```
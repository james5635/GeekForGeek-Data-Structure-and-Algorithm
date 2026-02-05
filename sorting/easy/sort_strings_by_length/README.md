# Sort Strings by Length

## Problem Statement
Given an array of strings, sort the strings based on their lengths in ascending order.

## Approach
### Built-in Sort
Use Python's `sorted()` or `list.sort()` with `key=len`:
```python
sorted(strings, key=len)
```
Python's sort is stable, so strings with equal lengths maintain their relative order.

### Counting Sort
If the maximum string length is known and bounded, use counting sort for O(n + k) time complexity where k is the max length.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Built-in Sort | O(n log n * m) | O(n) |
| Counting Sort | O(n + k) | O(n + k) |

Where:
- n = number of strings
- m = average string length
- k = maximum string length

## Key Points
- Python's sort is stable (maintains relative order)
- Can sort in ascending or descending order
- Secondary sorting criteria (alphabetical) can be added
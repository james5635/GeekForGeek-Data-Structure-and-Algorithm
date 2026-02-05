# Sentinel Linear Search

## Problem Description
Sentinel Linear Search is a variation of linear search where we avoid the comparison `i < n` in the loop by placing the target element at the end of the array as a sentinel.

## Examples
- Input: `arr = [10, 20, 180, 30, 60, 50, 110, 100, 70], key = 180`
  Output: `2` (index of 180)
- Input: `arr = [10, 20, 30], key = 40`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(n) - Linear search
- **Space Complexity:** O(1) - No extra space

## Main Function
```python
def sentinel_linear_search(arr, key):
    """
    Search using sentinel linear search technique.
    
    Args:
        arr: List of integers
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import sentinel_linear_search

arr = [10, 20, 180, 30, 60, 50, 110, 100, 70]
key = 180
result = sentinel_linear_search(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 2
```

## Reference
https://www.geeksforgeeks.org/sentinel-linear-search/

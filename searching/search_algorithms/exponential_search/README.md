# Exponential Search

## Problem Description
Exponential Search (also known as doubling search or galloping search) involves two steps: First, find the range where the element is present. Then, do binary search in the found range. It's particularly useful for unbounded/infinite searches.

## Examples
- Input: `arr = [2, 3, 4, 10, 40, 50, 70], key = 10`
  Output: `3` (index of 10)
- Input: `arr = [2, 3, 4, 10, 40], key = 50`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Finding range + binary search
- **Space Complexity:** O(log n) - Recursion stack for binary search

## Main Function
```python
def exponential_search(arr, key):
    """
    Search using exponential search algorithm.
    
    Args:
        arr: Sorted list of integers
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import exponential_search

arr = [2, 3, 4, 10, 40, 50, 70]
key = 10
result = exponential_search(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 3
```

## Reference
https://www.geeksforgeeks.org/exponential-search/

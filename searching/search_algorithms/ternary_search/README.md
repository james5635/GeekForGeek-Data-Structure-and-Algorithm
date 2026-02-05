# Ternary Search

## Problem Description
Ternary Search is a divide-and-conquer algorithm that divides the array into three parts instead of two. It is used to find the position of a target value within a sorted array.

## Examples
- Input: `arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key = 5`
  Output: `4` (index of 5)
- Input: `arr = [1, 2, 3, 4, 5], key = 10`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(log3 n) - Dividing array into 3 parts
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def ternary_search(arr, key):
    """
    Search using ternary search algorithm.
    
    Args:
        arr: Sorted list of integers
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import ternary_search

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 5
result = ternary_search(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 4
```

## Reference
https://www.geeksforgeeks.org/ternary-search/

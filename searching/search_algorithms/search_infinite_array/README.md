# Search in an Infinite Sorted Array

## Problem Description
Given an infinite sorted array (or an array with unknown size), search for a target value. You don't know the size of the array, so you cannot use array length for binary search bounds.

## Examples
- Input: `arr = [1, 2, 3, 4, 5, 6, 7, ...], key = 5`
  Output: `4` (index of 5)
- Input: `arr = [1, 2, 3, 4, 5, ...], key = 10`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Finding range + binary search
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def search_infinite_array(arr, key):
    """
    Search for a key in an infinite sorted array.
    
    Args:
        arr: Infinite sorted array (implemented as regular list)
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import search_infinite_array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
key = 10
result = search_infinite_array(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 9
```

## Reference
https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

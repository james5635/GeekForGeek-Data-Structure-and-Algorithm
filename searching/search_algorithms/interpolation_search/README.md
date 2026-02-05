# Interpolation Search

## Problem Description
Interpolation Search is an improvement over Binary Search for instances where the values in a sorted array are uniformly distributed. It calculates the probable position of the target value using interpolation formula.

## Examples
- Input: `arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47], key = 18`
  Output: `4` (index of 18)
- Input: `arr = [10, 12, 13, 16, 18], key = 20`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(log log n) average for uniformly distributed data, O(n) worst case
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def interpolation_search(arr, key):
    """
    Search using interpolation search algorithm.
    
    Args:
        arr: Sorted list of uniformly distributed integers
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import interpolation_search

arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
key = 18
result = interpolation_search(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 4
```

## Reference
https://www.geeksforgeeks.org/interpolation-search/

# Jump Search

## Problem Description
Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements by jumping ahead by fixed steps (block size) and then performing linear search within the identified block.

## Examples
- Input: `arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], key = 55`
  Output: `10` (index of 55)
- Input: `arr = [0, 1, 1, 2, 3, 5, 8, 13], key = 21`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(√n) - Optimal block size is √n
- **Space Complexity:** O(1) - Only using a few variables

## Main Function
```python
def jump_search(arr, key):
    """
    Search using jump search algorithm.
    
    Args:
        arr: Sorted list of integers
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import jump_search

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
key = 55
result = jump_search(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 10
```

## Reference
https://www.geeksforgeeks.org/jump-search/

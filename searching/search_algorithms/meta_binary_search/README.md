# Meta Binary Search

## Problem Description
Meta Binary Search (also called One-Sided Binary Search) is a modified binary search where we only use one comparison per iteration by checking bits from most significant to least significant.

## Examples
- Input: `arr = [2, 3, 4, 10, 40], key = 10`
  Output: `3` (index of 10)
- Input: `arr = [2, 3, 4, 10, 40], key = 5`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Similar to binary search
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def meta_binary_search(arr, key):
    """
    Search using meta binary search (one-sided binary search).
    
    Args:
        arr: Sorted list of integers
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import meta_binary_search

arr = [2, 3, 4, 10, 40]
key = 10
result = meta_binary_search(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 3
```

## Reference
https://www.geeksforgeeks.org/meta-binary-search-one-sided-binary-search/

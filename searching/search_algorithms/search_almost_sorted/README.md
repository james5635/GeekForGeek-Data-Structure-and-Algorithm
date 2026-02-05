# Search in an Almost Sorted Array

## Problem Description
Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions (i.e., arr[i] may be present at arr[i+1] or arr[i-1]), write an efficient function to search an element in this array.

## Examples
- Input: `arr = [10, 3, 40, 20, 50, 80, 70], key = 40`
  Output: `2` (index of 40)
- Input: `arr = [10, 3, 40, 20, 50, 80, 70], key = 90`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Modified binary search
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def search_almost_sorted(arr, key):
    """
    Search in an almost sorted array where elements can be at arr[i-1], arr[i], or arr[i+1].
    
    Args:
        arr: Almost sorted array
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import search_almost_sorted

arr = [10, 3, 40, 20, 50, 80, 70]
key = 40
result = search_almost_sorted(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 2
```

## Reference
https://www.geeksforgeeks.org/search-almost-sorted-array/

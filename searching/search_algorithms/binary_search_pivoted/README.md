# Binary Search on Pivoted (Rotated) Array

## Problem Description
Given a sorted and rotated array arr[] of n distinct elements, find if there is an element x in the array. A sorted array is rotated at some pivot point. For example, `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`.

## Examples
- Input: `arr = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3`
  Output: `8` (index of 3)
- Input: `arr = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 30`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Binary search approach
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def search_pivoted_array(arr, key):
    """
    Search for a key in a sorted and pivoted array.
    
    Args:
        arr: Sorted and rotated array of distinct elements
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """

def search_pivoted_single_pass(arr, key):
    """
    Search in rotated sorted array using single binary search pass.
    
    Args:
        arr: Sorted and rotated array
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import search_pivoted_single_pass

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3
result = search_pivoted_single_pass(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 8
```

## Reference
https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

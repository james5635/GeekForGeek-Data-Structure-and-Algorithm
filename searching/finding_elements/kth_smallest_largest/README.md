# Kth Smallest and Largest Element in Array

## Problem Description
Given an array arr[] and an integer K, find the Kth smallest and Kth largest element in the array.

## Examples
- Input: `arr = [7, 10, 4, 3, 20, 15], k = 3`
  Output: `Kth smallest: 7, Kth largest: 10`
- Input: `arr = [7, 10, 4, 3, 20, 15], k = 4`
  Output: `Kth smallest: 10, Kth largest: 7`

## Time and Space Complexity
- **Time Complexity:** O(n) average - Using QuickSelect algorithm
- **Space Complexity:** O(log n) - Recursion stack

## Main Function
```python
def kth_smallest(arr, k):
    """
    Find the kth smallest element in the array.
    
    Args:
        arr: List of integers
        k: The kth position (1-indexed)
    
    Returns:
        The kth smallest element
    """

def kth_largest(arr, k):
    """
    Find the kth largest element in the array.
    
    Args:
        arr: List of integers
        k: The kth position (1-indexed)
    
    Returns:
        The kth largest element
    """
```

## Usage Example
```python
from solution import kth_smallest, kth_largest

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"Kth smallest: {kth_smallest(arr, k)}")  # Output: 7
print(f"Kth largest: {kth_largest(arr, k)}")    # Output: 10
```

## Reference
https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

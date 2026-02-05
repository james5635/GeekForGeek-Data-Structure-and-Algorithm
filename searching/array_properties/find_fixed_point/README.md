# Find Fixed Point

## Problem Description
Given a sorted array of distinct integers, find a fixed point (value equal to index) in the array. If there are multiple fixed points, return any one.

## Examples
- Input: `arr = [-10, -5, 0, 3, 7]`
  Output: `3` (arr[3] == 3)
- Input: `arr = [-10, -5, 3, 4, 7, 9]`
  Output: `-1` (no fixed point)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Binary search approach
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def find_fixed_point(arr):
    """
    Find a fixed point where arr[i] == i.
    
    Args:
        arr: Sorted array of distinct integers
    
    Returns:
        Index of fixed point, or -1 if none exists
    """
```

## Usage Example
```python
from solution import find_fixed_point

arr = [-10, -5, 0, 3, 7]
result = find_fixed_point(arr)
print(f"Fixed point index: {result}")  # Output: 3
```

## Reference
https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/

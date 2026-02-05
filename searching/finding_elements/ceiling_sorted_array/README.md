# Ceiling in a Sorted Array

## Problem Description
Given a sorted array and a value x, find the ceiling of x in the array. The ceiling of x is the smallest element in the array greater than or equal to x.

## Examples
- Input: `arr = [1, 2, 8, 10, 10, 12, 19], x = 5`
  Output: `8`
- Input: `arr = [1, 2, 8, 10, 10, 12, 19], x = 20`
  Output: `-1` (ceiling doesn't exist)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Binary search approach
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def find_ceiling(arr, x):
    """
    Find the ceiling of x in a sorted array.
    
    Args:
        arr: Sorted list of integers
        x: Target value
    
    Returns:
        Ceiling of x, or -1 if doesn't exist
    """
```

## Usage Example
```python
from solution import find_ceiling

arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
result = find_ceiling(arr, x)
print(f"Ceiling of {x}: {result}")  # Output: 8
```

## Reference
https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/

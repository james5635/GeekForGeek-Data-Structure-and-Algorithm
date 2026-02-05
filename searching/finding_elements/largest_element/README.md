# Largest Element in Array

## Problem Description
Given an array arr[], find the largest element in the array.

## Examples
- Input: `[10, 20, 4]`
  Output: `20`
- Input: `[20, 10, 20, 4, 100]`
  Output: `100`

## Time and Space Complexity
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only using a single variable

## Main Function
```python
def find_largest_element(arr):
    """
    Find the largest element in an array.
    
    Args:
        arr: List of integers
    
    Returns:
        The largest element in the array
    """
```

## Usage Example
```python
from solution import find_largest_element

arr = [10, 20, 4, 45, 99]
result = find_largest_element(arr)
print(f"Largest element: {result}")  # Output: 99
```

## Reference
https://www.geeksforgeeks.org/largest-element-in-array/

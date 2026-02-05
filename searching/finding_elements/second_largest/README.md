# Second Largest Element in Array

## Problem Description
Given an array arr[], find the second largest element in the array.

## Examples
- Input: `[12, 35, 1, 10, 34, 1]`
  Output: `34`
- Input: `[10, 5, 10]`
  Output: `5`

## Time and Space Complexity
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Using only two variables

## Main Function
```python
def find_second_largest(arr):
    """
    Find the second largest element in an array.
    
    Args:
        arr: List of integers
    
    Returns:
        The second largest element, or -1 if doesn't exist
    """
```

## Usage Example
```python
from solution import find_second_largest

arr = [12, 35, 1, 10, 34, 1]
result = find_second_largest(arr)
print(f"Second largest: {result}")  # Output: 34
```

## Reference
https://www.geeksforgeeks.org/second-largest-element-in-an-array/

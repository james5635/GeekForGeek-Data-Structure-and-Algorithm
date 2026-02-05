# Largest Three Elements in Array

## Problem Description
Given an array arr[], find the three largest elements in the array.

## Examples
- Input: `[10, 4, 3, 50, 23, 90]`
  Output: `90, 50, 23`
- Input: `[12, 13, 1, 10, 34, 1]`
  Output: `34, 13, 12`

## Time and Space Complexity
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Using only three variables

## Main Function
```python
def find_largest_three(arr):
    """
    Find the three largest elements in an array.
    
    Args:
        arr: List of integers
    
    Returns:
        List of three largest elements in descending order
    """
```

## Usage Example
```python
from solution import find_largest_three

arr = [10, 4, 3, 50, 23, 90]
result = find_largest_three(arr)
print(f"Three largest: {result}")  # Output: [90, 50, 23]
```

## Reference
https://www.geeksforgeeks.org/find-the-largest-three-elements-in-an-array/

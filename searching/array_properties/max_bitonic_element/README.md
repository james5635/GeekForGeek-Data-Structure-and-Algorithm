# Maximum Element in Bitonic Array

## Problem Description
Given a bitonic array arr[] (first increasing then decreasing), find the maximum element in the array. A bitonic array is an array that is first monotonically increasing and then monotonically decreasing.

## Examples
- Input: `arr = [1, 3, 50, 10, 9, 7, 6]`
  Output: `50`
- Input: `arr = [10, 20, 30, 40, 50]`
  Output: `50` (only increasing)
- Input: `arr = [120, 100, 80, 20, 0]`
  Output: `120` (only decreasing)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Modified binary search
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def find_max_bitonic(arr):
    """
    Find maximum element in bitonic array.
    
    Args:
        arr: Bitonic array (first increasing, then decreasing)
    
    Returns:
        Maximum element in the array
    """
```

## Usage Example
```python
from solution import find_max_bitonic

arr = [1, 3, 50, 10, 9, 7, 6]
result = find_max_bitonic(arr)
print(f"Maximum element: {result}")  # Output: 50
```

## Reference
https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/

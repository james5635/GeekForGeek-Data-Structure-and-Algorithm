# Count 1s in Binary Sorted Array

## Problem Description
Given a binary sorted array (containing only 0s and 1s), find the count of 1s in the array.

## Examples
- Input: `arr = [0, 0, 0, 1, 1, 1, 1]`
  Output: `4`
- Input: `arr = [0, 0, 0, 0]`
  Output: `0`
- Input: `arr = [1, 1, 1, 1, 1]`
  Output: `5`

## Time and Space Complexity
- **Time Complexity:** O(log n) - Binary search for first 1
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def count_ones_binary_array(arr):
    """
    Count the number of 1s in a binary sorted array.
    
    Args:
        arr: Binary sorted array (0s followed by 1s)
    
    Returns:
        Count of 1s in the array
    """
```

## Usage Example
```python
from solution import count_ones_binary_array

arr = [0, 0, 0, 1, 1, 1, 1]
result = count_ones_binary_array(arr)
print(f"Count of 1s: {result}")  # Output: 4
```

## Reference
https://www.geeksforgeeks.org/count-1s-sorted-binary-array/

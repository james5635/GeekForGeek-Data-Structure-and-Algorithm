# Find Partition Point

## Problem Description
Given an array arr[], find a partition point such that all elements to the left are smaller than all elements to the right.

## Examples
- Input: `arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]`
  Output: `4` (partition at index 4, element 6)
  Explanation: All elements before 6 are smaller, all elements after are greater.

## Time and Space Complexity
- **Time Complexity:** O(n) - Two passes or optimized single pass
- **Space Complexity:** O(n) or O(1) - Depending on approach

## Main Function
```python
def find_partition_point(arr):
    """
    Find partition point where all left elements < all right elements.
    
    Args:
        arr: List of integers
    
    Returns:
        Index of partition point, or -1 if none exists
    """
```

## Usage Example
```python
from solution import find_partition_point

arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
result = find_partition_point(arr)
print(f"Partition point index: {result}")  # Output: 4
```

## Reference
https://www.geeksforgeeks.org/find-a-partition-point-in-array/

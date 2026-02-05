# Find Peak Element

## Problem Description
A peak element is an element that is strictly greater than its neighbors. Given an array arr[], find a peak element and return its index. If the array contains multiple peaks, return the index to any of the peaks.

## Examples
- Input: `arr = [1, 2, 3, 1]`
  Output: `2` (element 3 is a peak)
- Input: `arr = [1, 2, 1, 3, 5, 6, 4]`
  Output: `5` (element 6 is a peak) or `1` (element 2 is also a peak)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Binary search approach
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def find_peak_element(arr):
    """
    Find a peak element in the array.
    
    Args:
        arr: List of integers
    
    Returns:
        Index of a peak element
    """
```

## Usage Example
```python
from solution import find_peak_element

arr = [1, 2, 3, 1]
result = find_peak_element(arr)
print(f"Peak element index: {result}")  # Output: 2
print(f"Peak element: {arr[result]}")   # Output: 3
```

## Reference
https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

# First Repeating Element

## Problem Description
Given an array arr[], find the first repeating element in the array. The element should occur more than once and the index of its first occurrence should be smallest.

## Examples
- Input: `arr = [10, 5, 3, 4, 3, 5, 6]`
  Output: `5` (5 appears first at index 1, before 3 appears at index 2)
- Input: `arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]`
  Output: `6`

## Time and Space Complexity
- **Time Complexity:** O(n) - Using hash set
- **Space Complexity:** O(n) - Storing seen elements

## Main Function
```python
def first_repeating_element(arr):
    """
    Find the first repeating element in the array.
    
    Args:
        arr: List of integers
    
    Returns:
        The first repeating element, or -1 if none exists
    """
```

## Usage Example
```python
from solution import first_repeating_element

arr = [10, 5, 3, 4, 3, 5, 6]
result = first_repeating_element(arr)
print(f"First repeating element: {result}")  # Output: 5
```

## Reference
https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/

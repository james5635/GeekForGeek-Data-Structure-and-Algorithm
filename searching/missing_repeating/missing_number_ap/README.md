# Missing Number in Arithmetic Progression

## Problem Description
Given an array that represents elements of arithmetic progression in order, but one element is missing, find the missing number.

## Examples
- Input: `arr = [2, 4, 8, 10, 12, 14]`
  Output: `6`
- Input: `arr = [1, 6, 11, 16, 21, 31]`
  Output: `26`

## Time and Space Complexity
- **Time Complexity:** O(log n) - Modified binary search
- **Space Complexity:** O(1) - Iterative approach

## Main Function
```python
def find_missing_number_ap(arr):
    """
    Find missing number in an arithmetic progression.
    
    Args:
        arr: Array forming AP with one missing element
    
    Returns:
        The missing number in the AP
    """
```

## Usage Example
```python
from solution import find_missing_number_ap

arr = [2, 4, 8, 10, 12, 14]
result = find_missing_number_ap(arr)
print(f"Missing number in AP: {result}")  # Output: 6
```

## Reference
https://www.geeksforgeeks.org/find-missing-number-arithmetic-progression/

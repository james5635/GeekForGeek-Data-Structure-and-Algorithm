# Find the Missing Number

## Problem Description
Given an array of size n-1 containing distinct numbers from 1 to n, find the missing number in the range.

## Examples
- Input: `arr = [1, 2, 4, 6, 3, 7, 8], n = 8`
  Output: `5`
- Input: `arr = [1, 2, 3, 5], n = 5`
  Output: `4`

## Time and Space Complexity
- **Time Complexity:** O(n) - Single pass to calculate sum
- **Space Complexity:** O(1) - Only using sum variables

## Main Function
```python
def find_missing_number(arr, n):
    """
    Find missing number using sum formula.
    
    Args:
        arr: List of integers from 1 to n with one missing
        n: The maximum number in the range
    
    Returns:
        The missing number
    """

def find_missing_number_xor(arr, n):
    """
    Find missing number using XOR approach.
    
    Args:
        arr: List of integers from 1 to n with one missing
        n: The maximum number in the range
    
    Returns:
        The missing number
    """
```

## Usage Example
```python
from solution import find_missing_number

arr = [1, 2, 4, 6, 3, 7, 8]
n = 8
result = find_missing_number(arr, n)
print(f"Missing number: {result}")  # Output: 5
```

## Reference
https://www.geeksforgeeks.org/find-the-missing-number/

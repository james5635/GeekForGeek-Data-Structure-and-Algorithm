# Find Repeating and Missing Number

## Problem Description
Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

## Examples
- Input: `arr = [3, 1, 2, 5, 3]`
  Output: `Missing: 4, Repeating: 3`
- Input: `arr = [4, 3, 6, 2, 1, 1]`
  Output: `Missing: 5, Repeating: 1`

## Time and Space Complexity
- **Time Complexity:** O(n) - Single pass
- **Space Complexity:** O(1) - Mathematical approach

## Main Function
```python
def find_repeating_and_missing(arr):
    """
    Find the repeating and missing numbers.
    
    Args:
        arr: List of integers from 1 to n with one missing and one repeating
    
    Returns:
        Tuple of (repeating_number, missing_number)
    """
```

## Usage Example
```python
from solution import find_repeating_and_missing

arr = [3, 1, 2, 5, 3]
repeating, missing = find_repeating_and_missing(arr)
print(f"Repeating: {repeating}, Missing: {missing}")  # Output: Repeating: 3, Missing: 4
```

## Reference
https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

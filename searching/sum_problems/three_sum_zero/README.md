# Three Sum Zero

## Problem Description
Given an array arr[], find all unique triplets in the array which gives the sum of zero.

## Examples
- Input: `arr = [0, -1, 2, -3, 1]`
  Output: `[[-3, 1, 2], [-1, 0, 1]]`
- Input: `arr = [1, -2, 1, 0, 5]`
  Output: `[[-2, 1, 1]]`

## Time and Space Complexity
- **Time Complexity:** O(n²) - Sorting + two pointer
- **Space Complexity:** O(1) or O(n) - Depending on output storage

## Main Function
```python
def three_sum_zero(arr):
    """
    Find all unique triplets that sum to zero.
    
    Args:
        arr: List of integers
    
    Returns:
        List of triplets that sum to zero
    """
```

## Usage Example
```python
from solution import three_sum_zero

arr = [0, -1, 2, -3, 1]
result = three_sum_zero(arr)
print(f"Triplets summing to zero: {result}")  # Output: [[-3, 1, 2], [-1, 0, 1]]
```

## Reference
https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/

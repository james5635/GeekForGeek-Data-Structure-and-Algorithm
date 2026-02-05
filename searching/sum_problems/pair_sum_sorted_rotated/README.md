# Pair Sum in Sorted Rotated Array

## Problem Description
Given a sorted and rotated array arr[] and a sum X, find if there is a pair with sum equal to X.

## Examples
- Input: `arr = [11, 15, 6, 8, 9, 10], X = 16`
  Output: `True` (6 + 10 = 16)
- Input: `arr = [11, 15, 26, 38, 9, 10], X = 35`
  Output: `True` (26 + 9 = 35)
- Input: `arr = [11, 15, 26, 38, 9, 10], X = 45`
  Output: `False`

## Time and Space Complexity
- **Time Complexity:** O(n) - Two pointer approach
- **Space Complexity:** O(1) - No extra space

## Main Function
```python
def pair_sum_sorted_rotated(arr, X):
    """
    Find if there exists a pair with given sum in sorted rotated array.
    
    Args:
        arr: Sorted and rotated array
        X: Target sum
    
    Returns:
        True if pair exists, False otherwise
    """
```

## Usage Example
```python
from solution import pair_sum_sorted_rotated

arr = [11, 15, 6, 8, 9, 10]
X = 16
result = pair_sum_sorted_rotated(arr, X)
print(f"Pair with sum {X} exists: {result}")  # Output: True
```

## Reference
https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

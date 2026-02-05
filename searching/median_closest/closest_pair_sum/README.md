# Closest Pair Sum

## Problem Description
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has one element from each array.

## Examples
- Input: `arr1 = [1, 4, 5, 7], arr2 = [10, 20, 30, 40], x = 32`
  Output: `(1, 30)` (1 + 30 = 31 is closest to 32)
- Input: `arr1 = [1, 4, 5, 7], arr2 = [10, 20, 30, 40], x = 50`
  Output: `(7, 40)` (7 + 40 = 47 is closest to 50)

## Time and Space Complexity
- **Time Complexity:** O(n) - Two pointer approach
- **Space Complexity:** O(1) - No extra space

## Main Function
```python
def closest_pair_sum(arr1, arr2, x):
    """
    Find pair (one from each array) with sum closest to x.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
        x: Target sum
    
    Returns:
        Tuple of the closest pair
    """
```

## Usage Example
```python
from solution import closest_pair_sum

arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 32
result = closest_pair_sum(arr1, arr2, x)
print(f"Closest pair: {result}")  # Output: (1, 30)
```

## Reference
https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/

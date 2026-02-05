# Two Sum Closest to Zero

## Problem Description
Given an integer array arr[], find the sum of any two elements whose sum is closest to zero. If there are two ways to form sum closest to zero, return the maximum sum among them.

## Examples
- Input: `arr = [-8, 5, 2, -6]`
  Output: `-1` (5 + (-6) = -1)
- Input: `arr = [0, -8, -6, 3]`
  Output: `3` (tie between 0+3=3 and -6+3=-3, return 3)

## Time and Space Complexity
- **Time Complexity:** O(n log n) - Sorting required
- **Space Complexity:** O(1) - In-place sorting

## Main Function
```python
def two_sum_closest_to_zero(arr):
    """
    Find two elements whose sum is closest to zero.
    
    Args:
        arr: List of integers
    
    Returns:
        Sum of the pair closest to zero
    """
```

## Usage Example
```python
from solution import two_sum_closest_to_zero

arr = [-8, 5, 2, -6]
result = two_sum_closest_to_zero(arr)
print(f"Sum closest to zero: {result}")  # Output: -1
```

## Reference
https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/

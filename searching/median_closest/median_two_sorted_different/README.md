# Median of Two Sorted Arrays (Different Sizes)

## Problem Description
Given two sorted arrays of different sizes, find the median of the combined sorted array. This is an extension of the standard median problem with optimized handling for different array sizes.

## Examples
- Input: `arr1 = [1, 3, 5], arr2 = [2, 4]`
  Output: `3` (merged: [1, 2, 3, 4, 5])
- Input: `arr1 = [1, 2, 3], arr2 = [4, 5, 6, 7, 8]`
  Output: `4.5` (merged: [1, 2, 3, 4, 5, 6, 7, 8])

## Time and Space Complexity
- **Time Complexity:** O(log(min(m,n))) - Binary search approach
- **Space Complexity:** O(1) - Constant extra space

## Main Function
```python
def find_median_different_sizes(arr1, arr2):
    """
    Find median of two sorted arrays of different sizes.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
    
    Returns:
        Median value
    """
```

## Usage Example
```python
from solution import find_median_different_sizes

arr1 = [1, 3, 5]
arr2 = [2, 4]
result = find_median_different_sizes(arr1, arr2)
print(f"Median: {result}")  # Output: 3
```

## Reference
https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/

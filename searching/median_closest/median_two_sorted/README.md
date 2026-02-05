# Median of Two Sorted Arrays

## Problem Description
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

## Examples
- Input: `nums1 = [1, 3], nums2 = [2]`
  Output: `2.0`
- Input: `nums1 = [1, 2], nums2 = [3, 4]`
  Output: `2.5` ((2 + 3) / 2 = 2.5)

## Time and Space Complexity
- **Time Complexity:** O(log(min(m,n))) - Binary search on smaller array
- **Space Complexity:** O(1) - Constant extra space

## Main Function
```python
def find_median_sorted_arrays(nums1, nums2):
    """
    Find median of two sorted arrays.
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
    
    Returns:
        Median value as float
    """
```

## Usage Example
```python
from solution import find_median_sorted_arrays

nums1 = [1, 3]
nums2 = [2]
result = find_median_sorted_arrays(nums1, nums2)
print(f"Median: {result}")  # Output: 2.0
```

## Reference
https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/

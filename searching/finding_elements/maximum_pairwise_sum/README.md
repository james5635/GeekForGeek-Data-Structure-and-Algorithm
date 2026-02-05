# Maximum Pairwise Sum

## Problem Description
Given an array of integers, find the maximum sum that can be obtained by pairing elements. This typically refers to finding the maximum sum of pairs in an array.

## Examples
- Input: `[1, 2, 3, 4]`
  Output: `10` (1+2+3+4 as individual elements or max pair sum)
- Input: `[5, 3, 2, 1]`
  Output: `8` (5+3)

## Time and Space Complexity
- **Time Complexity:** O(n log n) - Sorting required
- **Space Complexity:** O(1) - In-place sorting

## Main Function
```python
def maximum_pairwise_sum(arr):
    """
    Find maximum pairwise sum in the array.
    
    Args:
        arr: List of integers
    
    Returns:
        Maximum pairwise sum
    """
```

## Usage Example
```python
from solution import maximum_pairwise_sum

arr = [5, 3, 2, 1]
result = maximum_pairwise_sum(arr)
print(f"Maximum pairwise sum: {result}")
```

## Reference
https://www.geeksforgeeks.org/maximum-sum-of-pairs-in-an-array/

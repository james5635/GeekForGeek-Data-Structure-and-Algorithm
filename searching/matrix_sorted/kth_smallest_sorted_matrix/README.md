# Kth Smallest Element in Sorted Matrix

## Problem Description
Given a n x n matrix where each row and column is sorted in ascending order, find the kth smallest element in the matrix.

## Examples
- Input: 
  ```
  matrix = [[1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]]
  k = 8
  ```
  Output: `13`

## Time and Space Complexity
- **Time Complexity:** O(n log(max-min)) - Binary search on value range
- **Space Complexity:** O(1) - No extra space

## Main Function
```python
def kth_smallest_sorted_matrix(matrix, k):
    """
    Find kth smallest element in a sorted matrix.
    
    Args:
        matrix: n x n sorted matrix
        k: Position of element to find
    
    Returns:
        The kth smallest element
    """
```

## Usage Example
```python
from solution import kth_smallest_sorted_matrix

matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
result = kth_smallest_sorted_matrix(matrix, k)
print(f"Kth smallest element: {result}")  # Output: 13
```

## Reference
https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/

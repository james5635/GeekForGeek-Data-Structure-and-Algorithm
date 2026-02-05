# K Largest Elements in Array

## Problem Description
Given an array of N positive integers, print k largest elements from the array in decreasing order.

## Examples
- Input: `arr = [1, 23, 12, 9, 30, 2, 50], k = 3`
  Output: `50, 30, 23`
- Input: `arr = [11, 5, 12, 9, 44, 17, 2], k = 2`
  Output: `44, 17`

## Time and Space Complexity
- **Time Complexity:** O(n log k) - Using min heap approach
- **Space Complexity:** O(k) - Storing k elements

## Main Function
```python
def k_largest_elements(arr, k):
    """
    Find k largest elements from the array.
    
    Args:
        arr: List of integers
        k: Number of largest elements to find
    
    Returns:
        List of k largest elements in descending order
    """
```

## Usage Example
```python
from solution import k_largest_elements

arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
result = k_largest_elements(arr, k)
print(f"{k} largest elements: {result}")  # Output: [50, 30, 23]
```

## Reference
https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/

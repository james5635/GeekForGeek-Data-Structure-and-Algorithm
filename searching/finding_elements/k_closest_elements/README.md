# K Closest Elements

## Problem Description
Given a sorted array arr[], two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order.

## Examples
- Input: `arr = [1, 2, 3, 4, 5], k = 4, x = 3`
  Output: `[1, 2, 3, 4]`
- Input: `arr = [1, 2, 3, 4, 5], k = 4, x = -1`
  Output: `[1, 2, 3, 4]`

## Time and Space Complexity
- **Time Complexity:** O(log n + k) - Binary search to find position, then expand
- **Space Complexity:** O(k) - Result array

## Main Function
```python
def find_k_closest_elements(arr, k, x):
    """
    Find k closest elements to x in a sorted array.
    
    Args:
        arr: Sorted list of integers
        k: Number of closest elements to find
        x: Target value
    
    Returns:
        List of k closest elements in ascending order
    """
```

## Usage Example
```python
from solution import find_k_closest_elements

arr = [1, 2, 3, 4, 5]
k = 4
x = 3
result = find_k_closest_elements(arr, k, x)
print(f"K closest elements: {result}")  # Output: [1, 2, 3, 4]
```

## Reference
https://www.geeksforgeeks.org/find-k-closest-elements-given-value/

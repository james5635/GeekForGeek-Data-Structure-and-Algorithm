# Common Elements in Three Sorted Arrays

## Problem Description
Given three arrays sorted in non-decreasing order, find all common elements in these arrays.

## Examples
- Input: 
  ```
  arr1 = [1, 5, 10, 20, 40, 80]
  arr2 = [6, 7, 20, 80, 100]
  arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
  ```
  Output: `[20, 80]`

## Time and Space Complexity
- **Time Complexity:** O(n1 + n2 + n3) - Three pointer approach
- **Space Complexity:** O(1) - Not counting output space

## Main Function
```python
def find_common_elements_three_arrays(arr1, arr2, arr3):
    """
    Find common elements in three sorted arrays.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
        arr3: Third sorted array
    
    Returns:
        List of common elements
    """
```

## Usage Example
```python
from solution import find_common_elements_three_arrays

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
result = find_common_elements_three_arrays(arr1, arr2, arr3)
print(f"Common elements: {result}")  # Output: [20, 80]
```

## Reference
https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/

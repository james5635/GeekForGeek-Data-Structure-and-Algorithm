# Majority Element

## Problem Description
Given an array arr[] of size n, find the majority element. The majority element is the element that appears more than n/2 times in the array.

## Examples
- Input: `arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]`
  Output: `4` (appears 5 times, which is > 9/2)
- Input: `arr = [3, 3, 4, 2, 4, 4, 2, 4]`
  Output: `-1` (no majority element)

## Time and Space Complexity
- **Time Complexity:** O(n) - Boyer-Moore Voting Algorithm
- **Space Complexity:** O(1) - Constant extra space

## Main Function
```python
def find_majority_element(arr):
    """
    Find majority element (appears more than n/2 times).
    
    Args:
        arr: List of integers
    
    Returns:
        Majority element, or -1 if none exists
    """
```

## Usage Example
```python
from solution import find_majority_element

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
result = find_majority_element(arr)
print(f"Majority element: {result}")  # Output: 4
```

## Reference
https://www.geeksforgeeks.org/majority-element/

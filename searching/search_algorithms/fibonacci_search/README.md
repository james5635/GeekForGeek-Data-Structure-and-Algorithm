# Fibonacci Search

## Problem Description
Fibonacci Search is a comparison-based technique that uses Fibonacci numbers to search an element in a sorted array. It divides the array into two parts with sizes that are consecutive Fibonacci numbers.

## Examples
- Input: `arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100], key = 85`
  Output: `8` (index of 85)
- Input: `arr = [10, 22, 35, 40, 45], key = 50`
  Output: `-1` (not found)

## Time and Space Complexity
- **Time Complexity:** O(log n) - Similar to binary search
- **Space Complexity:** O(1) - Only using Fibonacci numbers

## Main Function
```python
def fibonacci_search(arr, key):
    """
    Search using fibonacci search algorithm.
    
    Args:
        arr: Sorted list of integers
        key: Element to search for
    
    Returns:
        Index of the key if found, -1 otherwise
    """
```

## Usage Example
```python
from solution import fibonacci_search

arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
key = 85
result = fibonacci_search(arr, key)
print(f"Element {key} found at index: {result}")  # Output: 8
```

## Reference
https://www.geeksforgeeks.org/fibonacci-search/

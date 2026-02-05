# Kth Largest Element in a Stream

## Problem Description
Given an infinite stream of integers, find the kth largest element at any point in the stream.

## Examples
- Input: `stream = [10, 20, 11, 70, 50, 40, 100, 5], k = 3`
  Output: `[10, 10, 10, 11, 20, 40, 50, 50]` (3rd largest after each insertion)

## Time and Space Complexity
- **Time Complexity:** O(log k) per element - Using min heap
- **Space Complexity:** O(k) - Storing k elements in heap

## Main Function
```python
class KthLargest:
    """
    Class to find kth largest element in a stream.
    """
    
    def __init__(self, k, nums):
        """
        Initialize with k and initial stream.
        
        Args:
            k: The kth position
            nums: Initial list of numbers
        """
    
    def add(self, val):
        """
        Add new element and return kth largest.
        
        Args:
            val: New value to add
        
        Returns:
            The kth largest element
        """
```

## Usage Example
```python
from solution import KthLargest

k = 3
nums = [4, 5, 8, 2]
kth_largest = KthLargest(k, nums)
print(kth_largest.add(3))   # Output: 4
print(kth_largest.add(5))   # Output: 5
print(kth_largest.add(10))  # Output: 5
print(kth_largest.add(9))   # Output: 8
print(kth_largest.add(4))   # Output: 8
```

## Reference
https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/

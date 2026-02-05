# Sort by Set Bits Count

## Problem Statement
Given an integer array, sort the array according to the count of set bits (1s) in the binary representation of each number.

## Approach
### Brian Kernighan's Algorithm
Count set bits efficiently by repeatedly clearing the rightmost set bit:
```python
count = 0
while n:
    n &= (n - 1)
    count += 1
```

### Sorting
- Use Python's built-in `sorted()` with custom key (stable sort)
- Or use counting sort with 33 buckets (0-32 bits for 32-bit integers)

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Built-in Sort | O(n log n * log(max)) | O(n) |
| Counting Sort | O(n * log(max)) | O(n) |

Where:
- n = number of elements
- log(max) = number of bits in the largest number

## Key Points
- Brian Kernighan's algorithm counts bits in O(log n) time
- Python's sort is stable (maintains relative order for equal keys)
- Can sort in ascending or descending order
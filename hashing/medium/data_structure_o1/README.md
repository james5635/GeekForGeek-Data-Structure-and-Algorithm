# Data Structure with O(1) Operations

## Problem Statement

Design a data structure that supports insert, delete, search, and getRandom operations in O(1) time complexity.

## Examples

- **Insert:** Add element to set
- **Delete:** Remove element from set  
- **Search:** Check if element exists
- **GetRandom:** Return random element with equal probability

## Approach

1. **Hash Map + Array:** Use hash map to store value-to-index mapping and array to store values
2. **O(1) Delete:** Swap element with last element in array, then pop
3. **O(1) Random:** Use array index for random access

## Complexity Analysis

- **Time Complexity:** O(1) for all operations
- **Space Complexity:** O(n) for n elements

## Files

- `solution.py` - Contains RandomizedSet and RandomizedDict implementations

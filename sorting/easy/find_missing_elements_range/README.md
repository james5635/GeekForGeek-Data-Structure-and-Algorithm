# Find Missing Elements of Range

## Problem Statement
Given an array of distinct elements and a range [low, high], find all numbers in the range that are not present in the array.

## Approach
### Hash Set Approach
1. Insert all array elements into a hash set
2. Iterate through the range [low, high]
3. Check if each number exists in the set
4. Collect numbers not in the set

### Boolean Array Approach
1. Create a boolean array of size (high - low + 1)
2. Mark indices corresponding to array elements
3. Find indices that remain unmarked

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Hash Set | O(n + m) | O(n) |
| Boolean Array | O(n + m) | O(m) |

Where:
- n = number of elements in array
- m = (high - low + 1) = size of the range

## Key Points
- Array elements may be outside the given range
- Works with negative numbers
- Multiple approaches based on space/time trade-offs
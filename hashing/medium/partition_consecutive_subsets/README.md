# Partition Array into Consecutive Subsets

## Problem Statement

Given an array of integers, check if it can be partitioned into consecutive subsequences of length >= 3. A consecutive subsequence is a sequence where each element is one more than the previous element.

## Examples

- **Input:** [1, 2, 3, 3, 4, 5]  
  **Output:** true  
  **Explanation:** Can be partitioned into [1, 2, 3] and [3, 4, 5]

- **Input:** [1, 2, 3, 4, 4, 5]  
  **Output:** false  
  **Explanation:** Cannot partition into valid consecutive subsequences

## Approach

1. **Frequency Count:** Count occurrences of each number
2. **Greedy Formation:** For each number, either:
   - Append to an existing subsequence ending at num-1
   - Start a new subsequence with num, num+1, num+2
3. **Validation:** Check if all subsequences have length >= 3

## Complexity Analysis

- **Time Complexity:** O(n log n) due to sorting
- **Space Complexity:** O(n) for hash maps

## Files

- `solution.py` - Contains implementation with test cases

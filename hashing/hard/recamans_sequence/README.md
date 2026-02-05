# Recaman's Sequence

## Problem Description

Print the first n elements of Recaman's sequence. The sequence is defined as:
- a(0) = 0
- a(n) = a(n-1) - n if positive and not already in sequence
- a(n) = a(n-1) + n otherwise

## Examples

- **Input**: n = 6  
  **Output**: [0, 1, 3, 6, 2, 7]  
  **Explanation**:
  - 0 (first term)
  - 0 - 1 = -1 (negative, so use 0 + 1 = 1)
  - 1 - 2 = -1 (negative, so use 1 + 2 = 3)
  - 3 - 3 = 0 (already in sequence, so use 3 + 3 = 6)
  - 6 - 4 = 2 (valid, use it)
  - 2 - 5 = -3 (negative, so use 2 + 5 = 7)

## Approach

### Hash Set Method

1. **Initialize**: Start with 0
2. **Iterate**: For each index i from 1 to n-1
3. **Calculate**: Try a[i-1] - i
4. **Validate**: If positive and not in set, use it; else use a[i-1] + i
5. **Store**: Add to sequence and hash set

## Complexity Analysis

- **Time Complexity**: O(n) - single pass
- **Space Complexity**: O(n) - for hash set

## Why Hashing?

We need to check if a number is already in the sequence. Hash set provides O(1) lookup time, making the algorithm linear.

## Interesting Properties

1. **Not Monotonic**: The sequence oscillates
2. **Not Injective**: Some numbers may never appear
3. **Conjecture**: Every positive integer eventually appears in the sequence (unproven)

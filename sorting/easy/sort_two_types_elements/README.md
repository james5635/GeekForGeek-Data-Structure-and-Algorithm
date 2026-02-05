# Sort Array with Two Types of Elements

## Problem Statement
Given an array containing only two types of elements (e.g., 0s and 1s, or positive and negative numbers), sort the array such that all elements of one type come before elements of the other type.

## Approach
### Two-Pointer Technique
1. Initialize two pointers: `left` at start and `right` at end
2. Move `left` forward until finding the "wrong" type
3. Move `right` backward until finding the "wrong" type
4. Swap elements at `left` and `right`
5. Repeat until pointers meet

### Dutch National Flag (for three types)
For arrays with 0s, 1s, and 2s, use three pointers (low, mid, high) to partition the array in a single pass.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Two-pointer | O(n) | O(1) |
| Dutch National Flag | O(n) | O(1) |

## Variations
- Sort 0s and 1s
- Sort 0s, 1s, and 2s
- Segregate positive and negative numbers
- Segregate even and odd numbers
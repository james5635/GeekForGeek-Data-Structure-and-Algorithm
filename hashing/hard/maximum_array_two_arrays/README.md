# Maximum Array from Two Arrays

## Problem Description

Given two arrays A[] and B[], create an array C[] of size |A| + |B| such that:
1. C contains all elements from A and B
2. C is in non-increasing order (maximized lexicographically)
3. Relative order of elements from the same array is preserved

## Examples

- **Input**: A = [3, 4, 6, 5], B = [9, 1, 2, 5, 8, 3]  
  **Output**: [9, 8, 6, 5, 3]  
  **Explanation**: Merge to get maximum lexicographical order

## Approach

### Greedy Merge

1. **Compare**: At each step, compare remaining elements of both arrays
2. **Choose**: Pick the larger element (or better future sequence if equal)
3. **Continue**: Until all elements are used

When elements are equal, we need to look ahead to determine which sequence will produce a better result.

## Complexity Analysis

- **Time Complexity**: O(n + m) where n, m are lengths of arrays
- **Space Complexity**: O(n + m) for the result

## Key Insight

The greedy choice works because at each step, choosing the maximum available element (considering future elements) always leads to the globally optimal solution.

## Variations

### With Length Constraint
If we need exactly k elements, we can:
1. Generate maximum subsequences of different lengths from each array
2. Merge all valid combinations
3. Select the best result

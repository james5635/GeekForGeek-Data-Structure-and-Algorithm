# Longest Span with Same Sum in Two Binary Arrays

## Problem Description

Given two binary arrays `arr1[]` and `arr2[]` of the same size n, find the longest span (i, j) where j >= i such that:
```
sum(arr1[i..j]) == sum(arr2[i..j])
```

## Examples

- **Input**:  
  arr1 = [0, 1, 0, 0, 0, 0]  
  arr2 = [1, 0, 1, 0, 0, 1]  
  **Output**: 4  
  **Explanation**: The longest span with same sum is from index 1 to 4

## Approach

### Difference Array Method

1. **Compute Difference**: Calculate the difference between prefix sums at each index
2. **Hash Map**: Store first occurrence of each difference value
3. **Detect Match**: When the same difference occurs again, the span between them has equal sums

## Mathematical Proof

If `prefixSum1[i] - prefixSum2[i] = prefixSum1[j] - prefixSum2[j]`, then:
```
prefixSum1[j] - prefixSum1[i] = prefixSum2[j] - prefixSum2[i]
```

This means the sum of elements from i+1 to j is the same in both arrays.

## Complexity Analysis

- **Time Complexity**: O(n) - single pass
- **Space Complexity**: O(n) - for hash map

## Key Points

- Difference of 0 at index i means subarray [0..i] has equal sums
- Same difference at indices i and j means subarray [i+1..j] has equal sums
- Works for any integer arrays, not just binary

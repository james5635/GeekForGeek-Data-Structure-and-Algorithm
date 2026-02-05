# Sum of All Unique Subarray Sums

## Problem Description

Given an array `arr[]`, calculate the sum of all **unique** subarray sums. A subarray sum is the sum of elements in a contiguous subarray.

## Examples

- **Input**: arr = [1, 2, 1]  
  **Output**: Sum of unique subarray sums  
  **Explanation**: 
  - Subarrays and their sums: [1]=1, [2]=2, [1]=1, [1,2]=3, [2,1]=3, [1,2,1]=4
  - Unique sums: {1, 2, 3, 4}
  - Result: 1 + 2 + 3 + 4 = 10

## Approach

### Hash Set Approach

1. **Generate**: Use nested loops to generate all subarray sums
2. **Store**: Add each sum to a hash set (automatically handles duplicates)
3. **Sum**: Add all unique sums in the set

## Complexity Analysis

- **Time Complexity**: O(n²) - generate all n(n+1)/2 subarray sums
- **Space Complexity**: O(n²) - store unique sums (worst case when all sums are distinct)

## Optimizations

### Prefix Sum
Precompute prefix sums to calculate subarray sums in O(1):
```
sum(i, j) = prefix[j+1] - prefix[i]
```

## Related Problems

1. **Count Subarrays with Given Sum**: Use prefix sum with hash map
2. **Maximum Subarray Sum**: Kadane's algorithm
3. **Number of Subarrays with Sum K**: Prefix sum frequency map

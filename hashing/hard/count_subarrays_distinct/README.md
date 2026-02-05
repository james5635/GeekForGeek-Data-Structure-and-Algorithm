# Count Subarrays Having Distinct Elements

## Problem Description

Given an array `arr[]`, count the total number of subarrays having all distinct elements (no duplicates).

## Examples

- **Input**: arr = [1, 2, 3]  
  **Output**: 6  
  **Explanation**: All subarrays [1], [2], [3], [1,2], [2,3], [1,2,3] have distinct elements

- **Input**: arr = [1, 2, 1]  
  **Output**: 5  
  **Explanation**: Valid subarrays: [1], [2], [1], [1,2], [2,1]

## Approach

### Sliding Window with Hash Set

1. **Expand**: Add elements from right until duplicate found
2. **Contract**: Remove elements from left until duplicate removed
3. **Count**: For each valid window, add (right - left + 1) to count

## Key Insight

For a window `[left..right]` with all distinct elements:
- Number of valid subarrays ending at `right` = `right - left + 1`
- Each subarray starting from `left` to `right` is valid

## Complexity Analysis

- **Time Complexity**: O(n) - each element added and removed at most once
- **Space Complexity**: O(n) - for the hash set

## Variations

### Exactly K Distinct Elements
Use the formula: `exactly(k) = at_most(k) - at_most(k-1)`

### Longest Subarray with Distinct Elements
Track maximum window size during sliding window process

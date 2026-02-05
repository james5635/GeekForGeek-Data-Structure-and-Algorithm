# Minimum Subsets with Distinct Elements

## Problem

Given an array, find the minimum number of subsets that can be formed such that each subset contains only distinct elements.

## Approach

Find the maximum frequency of any element. This determines the minimum number of subsets needed since each occurrence of the most frequent element must go to a different subset.

## Complexity

- **Time Complexity:** O(n) - count frequencies
- **Space Complexity:** O(n) - frequency map

## Example

```
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 3
Explanation: Need 3 subsets: [1,2,3], [2,3], [3]
```

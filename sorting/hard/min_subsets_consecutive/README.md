# Count Minimum Number of Subsets with Consecutive Numbers

## Problem Statement
Given an array arr[] of n integers, find the minimum number of subsets (or subsequences) such that each subset contains consecutive integers. In other words, partition the array into minimum number of groups where each group contains consecutive numbers.

## Examples
- Input: arr[] = [1, 2, 3, 4]
  - Output: 1
  - Explanation: All elements can be in one subset: {1, 2, 3, 4}

- Input: arr[] = [1, 2, 4, 5, 7]
  - Output: 3
  - Explanation: Three subsets: {1, 2}, {4, 5}, {7}

- Input: arr[] = [1, 3, 5, 7]
  - Output: 4
  - Explanation: Each element forms its own subset

## Approaches

### 1. Greedy Sorting (Optimal)
1. Sort the array - O(n log n)
2. Count consecutive groups by checking arr[i] == arr[i-1] + 1
3. Each break in consecutive sequence means new subset
4. **Time Complexity**: O(n log n)
5. **Space Complexity**: O(1) auxiliary

### 2. Hash Map
1. Count frequency of each element - O(n)
2. Sort unique elements and count gaps
3. **Time Complexity**: O(n log n)
4. **Space Complexity**: O(n)

## Algorithm Steps
```
Sort array
subsets = 1
For i from 1 to n-1:
    If arr[i] != arr[i-1] + 1:
        subsets += 1
Return subsets
```

## Handling Duplicates
When the array contains duplicates:
- Duplicates of the same number don't create new subsets
- Remove duplicates first, then apply the algorithm
- Example: [1, 1, 2, 2, 4, 4] → unique [1, 2, 4] → 2 subsets

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Sorting | O(n log n) | O(1) aux | Simple and efficient |
| Hash Map | O(n log n) | O(n) | When frequency info needed |

## Key Insights
- Problem reduces to counting "gaps" in the sorted sequence
- If max - min + 1 == n and all unique, answer is 1
- Answer = number of consecutive sequences in sorted array

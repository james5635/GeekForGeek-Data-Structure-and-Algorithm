# Pair with Given Sum in Sorted Array (Two Sum II)

## Problem Description

Given a 1-based indexed integer array `arr[]` that is sorted in non-decreasing order, along with an integer target. Find two elements in the array such that their sum is equal to target. Return the 1-based indices of the two elements in increasing order. If no such pair exists, return `[-1, -1]`.

## Algorithm

1. Initialize two pointers: `left` at start (0) and `right` at end (n-1)
2. Calculate sum of elements at both pointers
3. If sum equals target, return the 1-based indices
4. If sum < target, increment left pointer to increase sum
5. If sum > target, decrement right pointer to decrease sum
6. Repeat until left >= right

## Complexity Analysis

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(1) | O(1) |
| Average | O(n) | O(1) |
| Worst | O(n) | O(1) |

## Example

```
Input:  arr = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: arr[1] + arr[2] = 2 + 7 = 9
```

## Key Points

- Two-pointer technique leverages the sorted property
- Much more efficient than brute force O(n²) approach
- Returns 1-based indices as per problem requirement
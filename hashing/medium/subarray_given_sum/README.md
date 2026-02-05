# Subarray with Given Sum

## Problem Statement
Given an array of non-negative integers and a target sum, find a subarray that adds to the given sum. Return 1-based indices [left, right] or [-1] if not found.

## Approach
**For non-negative numbers**: Sliding Window
- Use two pointers to maintain a window
- Expand by moving right pointer
- Shrink from left when sum exceeds target

**For arrays with negatives**: Prefix Sum + Hash Map
- Store prefix sums in hash map
- If (current_prefix_sum - target) exists in map, subarray found

## Complexity
- **Time**: O(N) - Single pass
- **Space**: O(1) for sliding window, O(N) for hash map

## Example
```
Input: arr[] = [15, 2, 4, 8, 9, 5, 10, 23], target = 23
Output: [2, 5]
Explanation: Subarray arr[2..5] = 2 + 4 + 8 + 9 = 23
```

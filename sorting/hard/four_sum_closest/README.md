# 4-Sum: Find a Quadruplet with Closest Sum

## Problem Statement
Given an array arr[] of n integers and a target value, find four elements in the array whose sum is closest to the target. Return the closest sum.

## Examples
- Input: arr[] = [1, 0, -1, 0, -2, 2], target = 0
  - Output: 0
  - Explanation: Closest quadruplet is [-2, -1, 1, 2] with sum 0

- Input: arr[] = [2, 2, 2, 2, 2], target = 8
  - Output: 8
  - Explanation: Quadruplet [2, 2, 2, 2] has exact sum

- Input: arr[] = [1, 2, 3, 4, 5], target = 100
  - Output: 14
  - Explanation: Maximum possible sum is 2+3+4+5=14

## Approaches

### 1. Sorting + Two Pointers (Optimal)
1. Sort the array - O(n log n)
2. Use two nested loops for first two elements
3. Use two pointers for remaining two elements
4. Track closest sum found
5. **Time Complexity**: O(n³)
6. **Space Complexity**: O(1) auxiliary

### 2. Brute Force
1. Check all combinations of 4 elements
2. Calculate sum and track minimum difference
3. **Time Complexity**: O(n⁴)
4. **Space Complexity**: O(1)

## Algorithm Steps (Two Pointer)
```
Sort array
closest_sum = sum of first 4 elements
For i from 0 to n-4:
    For j from i+1 to n-3:
        left = j + 1, right = n - 1
        While left < right:
            current_sum = arr[i] + arr[j] + arr[left] + arr[right]
            If |current_sum - target| < |closest_sum - target|:
                closest_sum = current_sum
            If current_sum < target: left++
            Else if current_sum > target: right--
            Else: return target (exact match)
Return closest_sum
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Two Pointer | O(n³) | O(1) aux | Optimal for general case |
| Brute Force | O(n⁴) | O(1) | Only for very small n |

## Key Insights
- Early termination when exact match found
- Early termination when min/max possible sums exceed target
- Track absolute difference to find closest
- Prefer smaller sum when differences are equal

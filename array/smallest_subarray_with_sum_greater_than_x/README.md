# Smallest Subarray with Sum Greater Than X

Given an array of integers (all positive) and a number `x`, find the minimum length subarray with sum greater than `x`.

## Problem Statement

Find the smallest contiguous subarray whose sum is strictly greater than a given number `x`.

### Examples

**Input:** `arr[] = [1, 4, 45, 6, 0, 19], x = 51`  
**Output:** `3`  
**Explanation:** Minimum length subarray is `[45, 6, 0]` or `[6, 0, 19]` with sum = 51 or 25 respectively. Actually `[45, 6, 0]` sum = 51 which is not > 51. `[45, 6, 0, 19]` sum = 70 > 51, length = 4. Or `[4, 45, 6]` sum = 55 > 51, length = 3.

**Input:** `arr[] = [1, 10, 5, 2, 7], x = 9`  
**Output:** `1`  
**Explanation:** Single element `10` has sum = 10 > 9.

**Input:** `arr[] = [1, 2, 4], x = 8`  
**Output:** `-1`  
**Explanation:** No subarray has sum > 8.

## Algorithm Approaches

### 1. Naive Approach - Try All Subarrays
- **File:** `smallest_subarray_with_sum_greater_than_x.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Use two nested loops to generate all subarrays
  - For each starting index, extend until sum > x
  - Track minimum length among all valid subarrays

### 2. Optimal Approach - Sliding Window
- **File:** `smallest_subarray_with_sum_greater_than_x.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Use two pointers (start and end) to maintain a window
  - Expand window by moving end pointer, add to sum
  - When sum > x, shrink from start to find smaller valid window
  - Works because all numbers are positive

## Usage

```bash
python smallest_subarray_with_sum_greater_than_x.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple but slow for large n |
| Sliding Window | O(n) | O(1) | **Preferred** - optimal |

## Sliding Window Algorithm Explained

```
Initialize:
  min_len = infinity
  current_sum = 0
  start = 0

For end from 0 to n-1:
  current_sum += arr[end]
  
  While current_sum > x:
    min_len = min(min_len, end - start + 1)
    current_sum -= arr[start]
    start += 1

Return min_len (or -1 if still infinity)
```

### Example Walkthrough

```
Array: [1, 4, 45, 6, 0, 19], x = 51

Step by step:
  end=0: sum=1, not > 51
  end=1: sum=5, not > 51
  end=2: sum=50, not > 51
  end=3: sum=56 > 51
         window [1,4,45,6], len=4
         shrink: sum-=1, start=1, sum=55 > 51
         window [4,45,6], len=3 ✓
         shrink: sum-=4, start=2, sum=51 not > 51
  end=4: sum=51, not > 51
  end=5: sum=70 > 51
         window [45,6,0,19], len=4
         shrink won't improve min_len

Result: 3 (subarray [4, 45, 6])
```

## Key Insights

- **Positive Numbers Only:** Sliding window works because adding more elements always increases sum
- **Greedy Shrinking:** Once sum > x, we try to remove elements from left to minimize length
- **Single Pass:** Each element is added and removed at most once

## Edge Cases

- **No valid subarray:** Return -1 when sum of entire array ≤ x
- **Single element sufficient:** Return 1 when some element > x
- **All elements needed:** Return n when only entire array works

## Important Constraint

⚠️ **All array elements must be positive** for the sliding window approach to work correctly.

## Variations

- **With Negative Numbers:** Use prefix sum with binary search or deque
- **Return Indices:** Track start and end of minimum subarray
- **Count of such subarrays:** Count all subarrays with sum > x

## Applications

- Data stream processing
- Financial analysis (finding minimum transactions)
- Network packet scheduling
- Resource allocation problems

## References

- [GeeksforGeeks - Smallest subarray with sum greater than a given value](https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/)

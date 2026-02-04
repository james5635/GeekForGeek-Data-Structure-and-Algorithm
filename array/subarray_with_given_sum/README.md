# Subarray with Given Sum (Positive Numbers)

Given an unsorted array of **positive integers** and a target sum, find a contiguous subarray that adds up to the target sum.

## Problem Statement

Find a continuous subarray which has sum equal to given target. Return the starting and ending indices of the subarray.

### Examples

**Input:** `arr[] = [1, 4, 20, 3, 10, 5], target = 33`  
**Output:** `(2, 4)` or subarray `[20, 3, 10]`  
**Explanation:** 20 + 3 + 10 = 33

**Input:** `arr[] = [1, 4, 0, 0, 3, 10, 5], target = 7`  
**Output:** `(1, 4)` or subarray `[4, 0, 0, 3]`  
**Explanation:** 4 + 0 + 0 + 3 = 7

**Input:** `arr[] = [1, 4], target = 0`  
**Output:** `(-1, -1)`  
**Explanation:** No subarray has sum 0 (all positive numbers)

## Algorithm Approaches

### 1. Naive Approach - Try All Subarrays
- **File:** `subarray_with_given_sum.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Check all possible subarrays using two nested loops
  - Return when sum equals target
  - Early termination when sum exceeds target

### 2. Optimal Approach - Sliding Window
- **File:** `subarray_with_given_sum.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Maintain a sliding window with variable size
  - Expand by adding elements from the right
  - Shrink by removing elements from the left when sum > target
  - Works because all numbers are positive

## Usage

```bash
python subarray_with_given_sum.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple but slow |
| Sliding Window | O(n) | O(1) | **Preferred** - optimal |
| Prefix Sum + Hash | O(n) | O(n) | Works with negatives too |

## Sliding Window Algorithm Explained

```
Initialize:
  start = 0
  current_sum = 0

For end from 0 to n-1:
  current_sum += arr[end]
  
  While current_sum > target:
    current_sum -= arr[start]
    start += 1
  
  If current_sum == target:
    Return (start, end)

Return (-1, -1)  # Not found
```

### Example Walkthrough

```
Array: [1, 4, 20, 3, 10, 5], target = 33

Step by step:
  end=0: sum=1, not 33
  end=1: sum=5, not 33
  end=2: sum=25, not 33
  end=3: sum=28, not 33
  end=4: sum=38 > 33
         shrink: sum-=1, start=1, sum=37 > 33
         shrink: sum-=4, start=2, sum=33 == 33 ✓
  
  Result: indices (2, 4), subarray [20, 3, 10]
```

## Key Insights

- **Monotonic Property:** With positive numbers, adding increases sum, removing decreases it
- **Greedy Adjustment:** Dynamically adjust window size based on current sum
- **Single Pass:** Each element enters and leaves window at most once

## Important Constraint

⚠️ **All array elements must be positive** for the sliding window approach.

## Handling Negative Numbers

If the array contains negative numbers, use **Prefix Sum + Hash Map**:
- Store prefix sums and their indices
- If `prefix_sum[j] - prefix_sum[i] = target`, subarray (i+1, j) has sum = target
- Time: O(n), Space: O(n)

## Edge Cases

- **Empty array:** Return (-1, -1)
- **Single element equals target:** Return (0, 0)
- **Entire array equals target:** Return (0, n-1)
- **No valid subarray:** Return (-1, -1)
- **Multiple valid subarrays:** Returns the first one found

## Variations

- **Find all subarrays:** Modify to continue after finding one
- **Count subarrays:** Count all subarrays with given sum
- **Smallest/Largest subarray:** Among all valid, find min/max length
- **Non-contiguous subsequence:** Use dynamic programming

## Applications

- **Financial analysis:** Finding periods with specific profit/loss
- **Time series analysis:** Pattern matching in data streams
- **Resource allocation:** Finding contiguous segments meeting criteria
- **Data compression:** Finding repeating patterns

## References

- [GeeksforGeeks - Find subarray with given sum](https://www.geeksforgeeks.org/find-subarray-with-given-sum/)

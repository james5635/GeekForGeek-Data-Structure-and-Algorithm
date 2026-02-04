# Maximum Circular Subarray Sum

Given an array arr[] of N integers arranged in a circular fashion, find the maximum subarray sum.

## Problem Statement

In a circular array, the last element is connected to the first element. Find the maximum sum of any contiguous subarray (allowing wrap-around).

### Examples

**Input:** `arr[] = [8, -8, 9, -9, 10, -11, 12]`  
**Output:** `22`  
**Explanation:** Subarray `[12, 8, -8, 9, -9, 10]` gives maximum sum = 22 (wrapping from end to start)

**Input:** `arr[] = [10, -3, -4, 7, 6, 5, -4, -1]`  
**Output:** `23`  
**Explanation:** Subarray `[7, 6, 5, -4, -1, 10]` gives maximum sum = 23

**Input:** `arr[] = [-1, -2, -3, -4]`  
**Output:** `-1`  
**Explanation:** All negative, return max element = -1

## Algorithm Approaches

### 1. Naive Approach - Check All Circular Subarrays
- **File:** `maximum_circular_subarray_sum.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:**
  - For each starting position, extend subarray considering circular wrapping
  - Track maximum sum across all possible subarrays

### 2. Optimal Approach - Kadane's + Total - Min
- **File:** `maximum_circular_subarray_sum.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:**
  - Case 1: Maximum is non-circular → Normal Kadane's
  - Case 2: Maximum wraps around → Total - Minimum Subarray
  - Result: Maximum of Case 1 and Case 2
  - Handle all-negative case separately

## Usage

```bash
python maximum_circular_subarray_sum.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple but slow |
| Optimal | O(n) | O(1) | Fast, uses Kadane's twice |

## Algorithm Details

### Optimal Approach Logic

```
Case 1: Maximum subarray does NOT wrap around
  → max_kadane = Kadane's algorithm on array

Case 2: Maximum subarray DOES wrap around
  → max_circular = Total Sum - Minimum Subarray Sum
  (The minimum subarray is what we exclude)

Special Case: All elements negative
  → max_kadane < 0, so return max_kadane (max element)

Result: max(max_kadane, max_circular)
```

### Mathematical Proof

```
Total array sum = S
If we want a wrapping subarray:
  Sum = arr[i..n-1] + arr[0..j] where i > j
  
This is equivalent to:
  Sum = Total Sum - Sum of middle non-selected portion
  
To maximize wrapping sum, we need to MINIMIZE
the non-selected portion, which is a normal subarray!

So: Max Circular = Total - Min Normal Subarray
```

### Example Walkthrough

```
Input: [8, -8, 9, -9, 10, -11, 12]

Normal Kadane's:
  Subarray: [12] = 12
  Max = 12

Total Sum = 8 + (-8) + 9 + (-9) + 10 + (-11) + 12 = 11

Minimum Subarray:
  Using inverted Kadane's: [-11]
  Min = -11

Max Circular = Total - Min = 11 - (-11) = 22

Result: max(12, 22) = 22 ✓
```

## Key Insights

- **Two Cases:** Either the subarray wraps or it doesn't
- **Complementary:** Max circular = Total - Min normal subarray
- **All Negative:** Must be handled separately (max_circular would be 0 which is wrong)
- **Single Pass:** Both Kadane's runs are O(n), so total is O(n)

## Edge Cases

- All positive: Returns total sum of array
- All negative: Returns maximum element
- Single element: Returns that element
- Mix of positive and negative: Finds optimal subarray

## Variations

- **Minimum Circular Subarray:** Use max instead of min
- **Count of subarrays:** Count how many achieve max sum
- **Multiple wraps:** Not applicable (circular means single wrap)

## References

- [GeeksforGeeks - Maximum Circular Subarray Sum](https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/)
- [LeetCode - Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

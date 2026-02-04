# Maximum Subarray Sum (Kadane's Algorithm)

Given an array `arr[]` of size `n`, find the maximum sum of any contiguous subarray (subarray with consecutive elements).

## Problem Statement

Find the subarray with the largest sum. The subarray must contain at least one element.

### Examples

**Input:** `arr[] = [-2, -3, 4, -1, -2, 1, 5, -3]`  
**Output:** `7`  
**Explanation:** Subarray `[4, -1, -2, 1, 5]` has maximum sum = 7.

**Input:** `arr[] = [1, 2, 3, 4, 5]`  
**Output:** `15`  
**Explanation:** Entire array has maximum sum = 15.

**Input:** `arr[] = [-1, -2, -3, -4]`  
**Output:** `-1`  
**Explanation:** Maximum subarray is `[-1]` (single largest element).

## Algorithm Approaches

### 1. Naive Approach - Check All Subarrays
- **File:** `max_subarray_sum.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Generate all possible subarrays using two nested loops
  - Calculate sum for each and track maximum
  - Simple but inefficient for large arrays

### 2. Optimal Approach - Kadane's Algorithm
- **File:** `max_subarray_sum.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - At each position, decide whether to extend existing subarray or start new
  - Track maximum sum ending at each position (`max_ending_here`)
  - Track global maximum (`max_so_far`)
  - **Key Insight:** If sum becomes negative, start fresh from next element

### 3. Divide and Conquer Approach
- **File:** `max_subarray_sum.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(log n) for recursion
- **Description:** 
  - Divide array into two halves
  - Maximum subarray can be in left half, right half, or crossing the middle
  - Recursively solve for each case

## Usage

```bash
python max_subarray_sum.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple, too slow for large n |
| Kadane's | O(n) | O(1) | **Preferred** - optimal |
| Divide & Conquer | O(n log n) | O(log n) | Good for understanding recursion |

## Kadane's Algorithm Explained

```
Initialize:
  max_so_far = arr[0]
  max_ending_here = arr[0]

For each element from index 1 to n-1:
  # Decision: extend or start fresh
  max_ending_here = max(arr[i], max_ending_here + arr[i])
  
  # Update global maximum
  max_so_far = max(max_so_far, max_ending_here)

Return max_so_far
```

### Example Walkthrough

```
Array: [-2, -3, 4, -1, -2, 1, 5, -3]

Step by step:
  i=0: max_ending = -2, max_so_far = -2
  i=1: max(-3, -2-3=-5) = -3, max_so_far = -2
  i=2: max(4, -3+4=1) = 4, max_so_far = 4
  i=3: max(-1, 4-1=3) = 3, max_so_far = 4
  i=4: max(-2, 3-2=1) = 1, max_so_far = 4
  i=5: max(1, 1+1=2) = 2, max_so_far = 4
  i=6: max(5, 2+5=7) = 7, max_so_far = 7  ← Maximum found!
  i=7: max(-3, 7-3=4) = 4, max_so_far = 7

Result: 7 (subarray [4, -1, -2, 1, 5])
```

## Key Insights

- **Greedy Decision:** At each step, choose the better option
- **Reset Strategy:** When sum becomes negative, starting fresh is better
- **All Negative:** Returns the least negative (maximum) element
- **Linear Time:** Single pass through array is sufficient

## Edge Cases

- **All positive:** Entire array is the answer
- **All negative:** Single largest element is the answer
- **Single element:** That element is the answer
- **Mixed positive/negative:** Kadane's finds optimal subarray

## Variations

- **Maximum Subarray with Indices:** Track start and end indices
- **Maximum Circular Subarray:** Array is circular (wraps around)
- **Maximum Product Subarray:** Find subarray with maximum product
- **K-Concatenation Maximum Sum:** Array concatenated k times

## Applications

- Finance: Finding best time to buy/sell stocks
- Signal processing: Detecting signal in noise
- Genomics: Finding similar DNA segments
- Image processing: Maximum sum rectangle in 2D

## References

- [GeeksforGeeks - Largest Sum Contiguous Subarray](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
- Original paper by Jay Kadane (1984)

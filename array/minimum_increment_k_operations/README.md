# Minimum Increment by K Operations to Make All Elements Equal

This directory contains the implementation to find the minimum number of increment-by-k operations required to make all array elements equal.

## Problem Statement

You are given an array of n-elements, you have to find the number of operations needed to make all elements of the array equal. Where a single operation can increment an element by k. If it is not possible to make all elements equal, print -1.

### Examples

**Input:** `arr[] = [4, 7, 19, 16]`, `k = 3`  
**Output:** `10`  
**Explanation:** Maximum element is 19. Operations needed: (19-4)/3 + (19-7)/3 + (19-19)/3 + (19-16)/3 = 5 + 4 + 0 + 1 = 10

**Input:** `arr[] = [4, 4, 4, 4]`, `k = 3`  
**Output:** `0`  
**Explanation:** All elements are already equal.

**Input:** `arr[] = [4, 2, 6, 8]`, `k = 3`  
**Output:** `-1`  
**Explanation:** It's not possible to make all elements equal by incrementing by 3. For example, 8 - 2 = 6 which is not divisible by 3.

## Algorithm Approach

### Optimal Approach - Single Pass
- **File:** `min_increment_k_operations.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Find the maximum element in the array
  - For each element, check if `(max - arr[i]) % k == 0`
  - If any element fails this check, return -1 (impossible to make equal)
  - Otherwise, sum up all `(max - arr[i]) / k` operations

### Key Insight
For all elements to be made equal by only incrementing by k, the difference between any two elements must be divisible by k. If this condition is not met for any element, it's impossible to make all elements equal.

## Usage

The implementation file can be run independently:

```bash
python min_increment_k_operations.py
```

The file includes comprehensive test cases to demonstrate functionality.

## Algorithm Steps

1. Find the maximum element in the array
2. Initialize result counter to 0
3. Iterate through each element:
   - Calculate the difference between max and current element
   - If difference is not divisible by k, return -1
   - Otherwise, add (difference / k) to result
4. Return the total result

## Mathematical Proof

For all elements to become equal by incrementing by k:
- Let max be the target value (we can only increment, not decrement)
- Each element arr[i] needs `(max - arr[i]) / k` operations
- This is only possible if `(max - arr[i])` is perfectly divisible by k
- If any element cannot reach max through k-increments, the task is impossible

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Single Pass | O(n) | O(1) |

The single pass approach is optimal with O(n) time and O(1) space complexity.

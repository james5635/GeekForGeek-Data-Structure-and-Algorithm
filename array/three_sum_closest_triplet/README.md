# Find Triplet with Sum Closest to Target

## Problem Statement

Given an array of integers and a target value, find **three integers** in the array such that their sum is **closest** to the target. Return the sum of the three integers.

**Assumption:** Each input would have exactly one solution.

## Examples

**Example 1:**
- Input: `arr = [-1, 2, 1, -4], target = 1`
- Output: `2`
- Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2), difference = |2-1| = 1

**Example 2:**
- Input: `arr = [1, 1, 1, 0], target = 100`
- Output: `3`
- Explanation: The closest possible sum is 1 + 1 + 1 = 3, difference = 97

**Example 3:**
- Input: `arr = [0, 0, 0], target = 1`
- Output: `0`

## Approaches

### 1. Brute Force (O(n³))

Check all possible triplets and track the one with minimum difference from target.

**Algorithm:**
```python
closest_sum = arr[0] + arr[1] + arr[2]
min_diff = abs(closest_sum - target)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            current_sum = arr[i] + arr[j] + arr[k]
            current_diff = abs(current_sum - target)
            
            if current_diff < min_diff:
                min_diff = current_diff
                closest_sum = current_sum
                
            if min_diff == 0:  # Exact match found
                return closest_sum
```

**Time:** O(n³)  
**Space:** O(1)

### 2. Sort + Two Pointers (O(n²)) ⭐ Optimal

This is the most efficient approach and the standard solution for this problem.

**Algorithm:**
1. Sort the array
2. Initialize `closest_sum` with the sum of first three elements
3. For each index `i` from 0 to n-3:
   - Use two pointers: `left = i+1`, `right = n-1`
   - While `left < right`:
     - Calculate `current_sum = arr[i] + arr[left] + arr[right]`
     - If `|current_sum - target| < |closest_sum - target|`: update `closest_sum`
     - If `current_sum == target`: return immediately (can't get better)
     - If `current_sum < target`: `left++` (need larger sum)
     - If `current_sum > target`: `right--` (need smaller sum)
4. Return `closest_sum`

**Why this works:**
- Sorting allows us to use the two-pointer technique
- By fixing one element and using two pointers on the remaining sorted subarray, we efficiently explore all possible combinations
- The sorted property guarantees we can adjust pointers to move towards a better sum

**Time:** O(n log n) for sorting + O(n²) for search = **O(n²)**  
**Space:** O(1) auxiliary space (if in-place sort)

## Detailed Walkthrough

Let's trace through Example 1: `arr = [-1, 2, 1, -4], target = 1`

**Step 1: Sort**
`sorted_arr = [-4, -1, 1, 2]`

**Step 2: Initialize**
`closest_sum = -4 + (-1) + 1 = -4`

**Step 3: Iterate**

**i = 0 (arr[0] = -4):**
- left = 1, right = 3
- sum = -4 + (-1) + 2 = -3
- |-3 - 1| = 4 < |-4 - 1| = 5 ✓ Update closest_sum = -3
- sum < target, so left++
- sum = -4 + 1 + 2 = -1
- |-1 - 1| = 2 < 4 ✓ Update closest_sum = -1
- sum < target, left++ → left = right, done

**i = 1 (arr[1] = -1):**
- left = 2, right = 3
- sum = -1 + 1 + 2 = 2
- |2 - 1| = 1 < 2 ✓ Update closest_sum = 2
- sum > target, right--
- left >= right, done

**i = 2:** Not enough elements left

**Result:** `closest_sum = 2` ✓

## Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n³) | O(1) | Never use in practice |
| Sort + Two Pointers | O(n²) | O(1) | **Standard solution** |

## Edge Cases

1. **Array with less than 3 elements:** Handle gracefully (return error or None)
2. **Exact match exists:** Return immediately for efficiency
3. **Multiple equally close sums:** Any valid answer is acceptable
4. **All same elements:** e.g., [2, 2, 2], target = 7 → return 6
5. **Large numbers:** Be careful of overflow in some languages

## Variations

### Return the Triplet instead of Sum

```python
def three_sum_closest_with_triplet(arr, target):
    # Same logic but track the actual elements
    closest_triplet = (arr[0], arr[1], arr[2])
    # ... rest of implementation
    return closest_sum, closest_triplet
```

### Find All Triplets with Closest Sum

If there are multiple triplets with the same closest difference, return all of them.

## Applications

- **Financial modeling:** Finding three investments whose combined risk/return is closest to target
- **Recommendation systems:** Finding three products whose combined price matches budget
- **Data analysis:** Finding three data points that best represent a target metric
- **Physics simulations:** Finding three forces that sum to desired resultant

## Related Problems

- **3Sum:** Find all unique triplets that sum to zero
- **4Sum:** Find four elements that sum to target
- **Two Sum:** Find two elements that sum to target
- **KSum:** Generalization to k elements

## References

- [GeeksforGeeks: Find a triplet with sum closest to given value](https://www.geeksforgeeks.org/find-a-triplet-with-sum-closest-to-given-value/)
- [LeetCode: 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
- [LeetCode: 3Sum](https://leetcode.com/problems/3sum/)
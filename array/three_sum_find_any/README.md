# Find Any Triplet with Given Sum (3Sum)

## Problem Statement

Given an array of integers and a target sum, find **any three elements** that sum to the target. Return the triplet if found, otherwise return None/null.

This is a variation of the classic **3Sum problem**.

## Examples

**Example 1:**
- Input: `arr = [1, 4, 45, 6, 10, 8], target = 22`
- Output: `(4, 10, 8)` or `(1, 6, ...)` wait
- Actually: `4 + 10 + 8 = 22` ✓

**Example 2:**
- Input: `arr = [1, 2, 3, 4, 5], target = 9`
- Output: `(2, 3, 4)` since `2 + 3 + 4 = 9`

**Example 3:**
- Input: `arr = [1, 2], target = 3`
- Output: `None` (need at least 3 elements)

## Approaches

### 1. Brute Force (O(n³))

Check all possible triplets using three nested loops.

```python
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] == target:
                return (arr[i], arr[j], arr[k])
```

**Time:** O(n³)  
**Space:** O(1)

### 2. Sort + Binary Search (O(n² log n))

Sort the array first, then for each element, use binary search to find if a valid pair exists in the remaining array.

**Algorithm:**
1. Sort the array
2. For each index i from 0 to n-3:
   - Skip duplicates
   - For the subarray arr[i+1:], check if there exists a pair summing to target - arr[i]
   - Use binary search or two pointers for the pair search

**Time:** O(n log n) for sort + O(n² log n) for search = O(n² log n)  
**Space:** O(1) or O(n) for sorting

### 3. Sort + Two Pointers (O(n²)) ⭐ Optimal

**This is the most efficient and commonly used approach.**

**Algorithm:**
1. Sort the array
2. For each index i from 0 to n-3:
   - Skip duplicates (if arr[i] == arr[i-1])
   - Set left = i+1, right = n-1
   - While left < right:
     - Calculate current sum = arr[i] + arr[left] + arr[right]
     - If sum == target: return triplet
     - If sum < target: left++
     - If sum > target: right--
3. Return None if no triplet found

**Why this works:**
- By fixing one element and using two pointers on the sorted remaining array, we can efficiently find the required pair
- The two pointers approach reduces the pair search from O(n²) to O(n)

**Time:** O(n log n) for sort + O(n²) for search = **O(n²)**  
**Space:** O(1) or O(n) for sorting

## Key Differences Between Approaches

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| Brute Force | O(n³) | O(1) | Never in practice |
| Sort + Binary Search | O(n² log n) | O(1) | Educational |
| Sort + Two Pointers | O(n²) | O(1) | **Production code** |

## Extension: Find ALL Triplets

The same approaches can be modified to return **all unique triplets** instead of just any one:

```python
def three_sum_all_triplets(arr, target):
    result = []
    arr.sort()
    n = len(arr)
    
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        left, right = i + 1, n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == target:
                result.append([arr[i], arr[left], arr[right]])
                # Skip duplicates
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return result
```

## Edge Cases

1. **Array with less than 3 elements:** Return None
2. **No valid triplet:** Return None
3. **All elements same:** Check if 3 * element == target
4. **Negative numbers:** Handle correctly in all approaches
5. **Large numbers:** Watch for integer overflow in some languages

## Applications

- Financial analysis (finding three transactions that sum to specific amount)
- Recommendation systems (finding three items that satisfy criteria)
- Geometric problems (three points satisfying conditions)
- Subset sum variations

## References

- [GeeksforGeeks: Find a triplet that sum to a given value](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
- [LeetCode: 3Sum](https://leetcode.com/problems/3sum/)
- [LeetCode: Two Sum](https://leetcode.com/problems/two-sum/)
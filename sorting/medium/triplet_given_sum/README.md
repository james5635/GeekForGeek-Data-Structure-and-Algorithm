# Find a Triplet that Sum to a Given Value

## Problem Statement

Given an array of integers and a target sum, determine if there exists a triplet (three elements) in the array whose sum equals the given target.

## Examples

**Example 1:**
```
Input: arr = [1, 4, 45, 6, 10, 8], target = 22
Output: True
Explanation: Triplet [4, 10, 8] sums to 22 (4 + 10 + 8 = 22)
```

**Example 2:**
```
Input: arr = [1, 2, 3, 4, 5], target = 100
Output: False
Explanation: No three elements sum to 100
```

## Approach

### Two-Pointer Technique (Optimal)

1. **Sort the array** - O(n log n)
2. **Fix one element** and use two pointers for the remaining sum
3. **Two-pointer search:**
   - For each index `i` from `0` to `n-3`
   - Set `left = i + 1`, `right = n - 1`
   - While `left < right`:
     - If `arr[i] + arr[left] + arr[right] == target`: **Found!**
     - If sum `< target`: `left++` (need larger sum)
     - If sum `> target`: `right--` (need smaller sum)

### Why It Works
Sorting allows us to use the two-pointer technique. By fixing one element and searching the remaining array with two pointers, we reduce the O(n³) brute force to O(n²).

## Complexity Analysis

- **Time Complexity:** O(n²)
  - Sorting: O(n log n)
  - Outer loop: O(n)
  - Inner two-pointer scan: O(n)
  - Total: O(n²)
- **Space Complexity:** O(1) auxiliary
  - In-place sorting
  - Only using indices

## Implementation

```python
def find_triplet_sum(arr, target):
    if not arr or len(arr) < 3:
        return False
    
    arr.sort()
    n = len(arr)
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return False
```

## Alternative Approaches

### Brute Force: O(n³)
```python
def find_triplet_brute_force(arr, target):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    return False
```

### Hashing: O(n²) time, O(n) space
- Use hash set to store pairs

## Variations

- **Return the actual triplet:** Return the three values
- **Find all triplets:** Return all unique triplets (like 3Sum problem)
- **Count all triplets:** Count how many triplets sum to target

## Edge Cases

- **Array size < 3:** Return False
- **Empty array:** Return False
- **Duplicates:** Skip duplicates to avoid duplicate triplets
- **Negative numbers:** Handled correctly
- **Multiple valid triplets:** Can return any one or all

## Applications

- 3Sum problem variations
- Financial analysis (finding three transactions that sum to target)
- Geometric problems

## Related Problems

- 3Sum (LeetCode)
- 3Sum Closest
- 4Sum
- Two Sum

## Reference

- [GeeksforGeeks - Find a Triplet that Sum to a Given Value](https://www.geeksforgeeks.org/dsa/find-a-triplet-that-sum-to-a-given-value/)
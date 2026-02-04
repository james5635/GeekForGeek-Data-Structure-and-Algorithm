# Find Any Quadruplet with Given Sum (4Sum)

## Problem Statement

Given an array of integers and a target sum, find **any four elements** that sum to the target. Return the quadruplet if found, otherwise return None/null.

This extends the 3Sum problem to four elements.

## Examples

**Example 1:**
- Input: `arr = [1, 0, -1, 0, -2, 2], target = 0`
- Output: `[-1, 0, 0, 1]` or `[-2, -1, 1, 2]` or `[-2, 0, 0, 2]`
- Explanation: All are valid quadruplets that sum to 0

**Example 2:**
- Input: `arr = [2, 2, 2, 2, 2], target = 8`
- Output: `[2, 2, 2, 2]`

**Example 3:**
- Input: `arr = [1, 2, 3, 4], target = 100`
- Output: `None` (no valid quadruplet)

## Approaches

### 1. Brute Force (O(n⁴))

Check all possible quadruplets using four nested loops.

```python
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if arr[i] + arr[j] + arr[k] + arr[l] == target:
                    return (arr[i], arr[j], arr[k], arr[l])
```

**Time:** O(n⁴)  
**Space:** O(1)

**Note:** Only for educational purposes or very small arrays.

### 2. Hash Map of Pair Sums (O(n²)) ⭐ Optimal

This is the most efficient approach for large inputs.

**Key Insight:**
If `a + b + c + d = target`, then `(a + b) + (c + d) = target`

So we can:
1. Store all pair sums in a hash map
2. For each pair sum, check if `target - pair_sum` exists in the map
3. Ensure the four indices are all distinct

**Algorithm:**
```python
# Step 1: Build pair sums map
pair_sums = defaultdict(list)
for i in range(n):
    for j in range(i+1, n):
        current_sum = arr[i] + arr[j]
        pair_sums[current_sum].append((i, j))

# Step 2: Find two pairs that sum to target
for sum1, pairs1 in pair_sums.items():
    sum2 = target - sum1
    if sum2 not in pair_sums:
        continue
    
    pairs2 = pair_sums[sum2]
    
    for i1, j1 in pairs1:
        for i2, j2 in pairs2:
            indices = {i1, j1, i2, j2}
            if len(indices) == 4:  # All distinct
                return (arr[i1], arr[j1], arr[i2], arr[j2])
```

**Time:** O(n²) for building map + O(n²) for finding = **O(n²)**  
**Space:** O(n²) for storing pair sums

**Pros:**
- Optimal time complexity
- Good for very large arrays

**Cons:**
- High space complexity
- More complex implementation
- Doesn't naturally return sorted/ordered results

### 3. Sort + Two Pointers Extension (O(n³))

Extend the 3Sum two-pointer approach to 4Sum.

**Algorithm:**
1. Sort the array
2. For each pair of indices (i, j) where i < j:
   - Use two pointers on the remaining subarray to find if a pair exists that sums to `target - arr[i] - arr[j]`
   - Similar to the 3Sum two-pointer approach

**Time:** O(n log n) for sort + O(n³) for search = **O(n³)**  
**Space:** O(1) auxiliary

**Pros:**
- Better space complexity than hash map approach
- Returns sorted results naturally
- Simpler to understand than hash map

**Cons:**
- Slower than hash map for large inputs (O(n³) vs O(n²))

## Comparison Summary

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| Brute Force | O(n⁴) | O(1) | Never in practice |
| Hash Map (Pair Sums) | O(n²) | O(n²) | Large inputs, space available |
| Sort + Two Pointers | O(n³) | O(1) | Medium inputs, limited space |

## Time vs Space Trade-off

```
Input Size    |  Best Approach
--------------|------------------
n <= 50       |  Any approach
50 < n <= 500 |  Sort + Two Pointers (O(n³))
n > 500       |  Hash Map (O(n²))
```

## Extension: Find All Quadruplets

The same approaches can be modified to return **all unique quadruplets** instead of just any one:

```python
def four_sum_all_quadruplets(arr, target):
    result = []
    arr.sort()
    n = len(arr)
    
    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            
            left, right = j + 1, n - 1
            remaining = target - arr[i] - arr[j]
            
            while left < right:
                current_sum = arr[left] + arr[right]
                
                if current_sum == remaining:
                    result.append([arr[i], arr[j], arr[left], arr[right]])
                    
                    # Skip duplicates
                    while left < right and arr[left] == arr[left+1]:
                        left += 1
                    while left < right and arr[right] == arr[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < remaining:
                    left += 1
                else:
                    right -= 1
    
    return result
```

## Related Problems

- **2Sum:** Find two elements that sum to target
- **3Sum:** Find three elements that sum to target
- **4Sum II:** Four arrays instead of one array
- **KSum:** Generalization to k elements

## References

- [GeeksforGeeks: Find four elements that sum to given value](https://www.geeksforgeeks.org/find-four-elements-that-sum-to-given-value/)
- [LeetCode: 4Sum](https://leetcode.com/problems/4sum/)
- [LeetCode: Two Sum](https://leetcode.com/problems/two-sum/)
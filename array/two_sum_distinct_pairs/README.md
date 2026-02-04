# Find Distinct Pairs with Given Sum

## Problem Statement

Given an array of integers and a target sum, find all **distinct pairs** of elements that sum to the target.

**Key difference from "all pairs":** If the array contains duplicates that form the same pair, return that pair only once.

## Examples

**Example 1:**
- Input: `arr = [1, 5, 7, -1, 5], target = 6`
- Output: `[(-1, 7), (1, 5)]`
- Explanation: (1, 5) appears twice in all pairs, but only once as distinct pair

**Example 2:**
- Input: `arr = [1, 1, 1, 1], target = 2`
- Output: `[(1, 1)]`
- Explanation: Only one distinct pair (1, 1) even though there are C(4,2) = 6 pairs

**Example 3:**
- Input: `arr = [1, 2, 3, 4, 5], target = 5`
- Output: `[(1, 4), (2, 3)]`

## Approaches

### 1. Brute Force with Set (O(n²))

Use nested loops to check all pairs, but store results in a set to ensure uniqueness.

**Algorithm:**
1. Initialize empty set for distinct pairs
2. For each pair (i, j) where i < j:
   - If arr[i] + arr[j] == target:
     - Add sorted tuple (min, max) to set
3. Return sorted list from set

**Time:** O(n²)  
**Space:** O(k) where k = number of distinct pairs

### 2. Sort + Two Pointers (O(n log n))

Sort the array first, then use two pointers to find pairs while naturally handling duplicates.

**Algorithm:**
1. Sort the array
2. Initialize left = 0, right = n-1
3. While left < right:
   - Calculate current sum
   - If sum == target: add pair, skip duplicates on both sides
   - If sum < target: left++
   - If sum > target: right--

**Time:** O(n log n)  
**Space:** O(1) excluding result

**Pros:**
- No extra space for hash map
- Automatically handles duplicates by skipping

**Cons:**
- Modifies/sorts the array
- Cannot easily return all pair instances

### 3. Hash Set (O(n))

Use a hash set to track seen elements and identify distinct pairs efficiently.

**Algorithm:**
1. Initialize empty set for seen elements
2. Initialize empty set for distinct pairs
3. For each element in array:
   - complement = target - element
   - If complement in seen:
     - Add sorted pair to distinct pairs set
   - Add element to seen
4. Return sorted list

**Time:** O(n)  
**Space:** O(n)

**Note:** This approach only works correctly when we want at most one pair per element combination. For handling duplicates with counts, use Hash Map approach.

### 4. Hash Map / Counter (O(n)) - Optimal

Use a frequency map to properly handle duplicates by counting occurrences.

**Algorithm:**
1. Build frequency map of all elements
2. Initialize empty set for distinct pairs
3. For each unique element:
   - Calculate complement
   - If complement not in map, continue
   - If element == complement:
     - Need at least 2 occurrences
     - Add pair if frequency >= 2
   - Else:
     - Add sorted pair to set
4. Return sorted list

**Time:** O(n)  
**Space:** O(n)

**Pros:**
- Optimal time complexity
- Correctly handles all edge cases
- Properly counts for duplicate pairs

## Complexity Summary

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force + Set | O(n²) | O(k) | Simple, handles all cases |
| Sort + Two Pointers | O(n log n) | O(1) | Best space, modifies array |
| Hash Set | O(n) | O(n) | Fast, simple duplicates handling |
| Hash Map (Optimal) | O(n) | O(n) | Best overall, handles all cases |

## Key Differences from "All Pairs"

| Aspect | All Pairs | Distinct Pairs |
|--------|-----------|----------------|
| `[1, 5, 5], target=6` | `[(1,5), (1,5)]` | `[(1,5)]` |
| `[1, 1, 1], target=2` | 3 pairs | 1 pair |
| Use case | Counting all valid combinations | Finding unique value combinations |

## Applications

- Finding unique relationships in data
- Database query optimization (DISTINCT pairs)
- Recommendation systems (unique user-item pairs)
- Network analysis (unique connections)

## References

- [GeeksforGeeks: Find all pairs with given sum](https://www.geeksforgeeks.org/find-all-pairs-with-given-sum/)
- [GeeksforGeeks: Count distinct pairs with given sum](https://www.geeksforgeeks.org/count-distinct-pairs-with-given-sum/)
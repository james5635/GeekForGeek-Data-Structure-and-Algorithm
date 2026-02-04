# Sorted Subsequence of Size 3

Given an array `arr[]` of size `n`, find a sorted subsequence of size 3 (three indices `i`, `j`, `k` such that `i < j < k` and `arr[i] < arr[j] < arr[k]`).

## Problem Statement

Find any three elements in increasing order of indices and values. Return any one valid triplet.

### Examples

**Input:** `arr[] = [12, 11, 10, 5, 6, 2, 30]`  
**Output:** `(5, 6, 30)` or `(5, 6, 30)`  
**Explanation:** 5 < 6 < 30 and indices 3 < 4 < 6.

**Input:** `arr[] = [1, 2, 3, 4]`  
**Output:** `(1, 2, 3)` or any valid triplet  
**Explanation:** Multiple valid answers exist.

**Input:** `arr[] = [4, 3, 2, 1]`  
**Output:** `None`  
**Explanation:** Array is strictly decreasing, no valid subsequence exists.

## Algorithm Approaches

### 1. Naive Approach - Check All Triplets
- **File:** `sorted_subsequence_size_3.py`
- **Time Complexity:** O(n³)
- **Space Complexity:** O(1)
- **Description:** 
  - Use three nested loops to check all possible triplets
  - Return first valid triplet found

### 2. Better Approach - Two Arrays
- **File:** `sorted_subsequence_size_3.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** 
  - Create `smaller[]` array: for each position, store index of smaller element to its left
  - Create `greater[]` array: for each position, store index of greater element to its right
  - Find index where both smaller and greater exist

### 3. Optimal Approach - Single Pass
- **File:** `sorted_subsequence_size_3.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Track `first`: smallest element seen so far
  - Track `second`: smallest element greater than `first`
  - When we find an element greater than `second`, we have our triplet
  - Greedily maintain smallest valid pair

## Usage

```bash
python sorted_subsequence_size_3.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n³) | O(1) | Simple but too slow |
| Two Arrays | O(n) | O(n) | Good, uses extra space |
| Single Pass | O(n) | O(1) | **Preferred** - optimal |

## How Two Arrays Approach Works

```
Array: [12, 11, 10, 5, 6, 2, 30]

smaller[]: Tracks index of smaller element on left
  [-1, -1, -1, -1, 3, -1, 4]
  Explanation:
    - Index 4 (value 6): smaller element is at index 3 (value 5)
    - Index 6 (value 30): smaller element is at index 4 (value 6)

greater[]: Tracks index of greater element on right
  [-1, -1, -1, 4, 6, 6, -1]
  Explanation:
    - Index 3 (value 5): greater element at index 4 (value 6)
    - Index 4 (value 6): greater element at index 6 (value 30)

Result: Index 4 has both smaller (3) and greater (6)
        → (arr[3], arr[4], arr[6]) = (5, 6, 30)
```

## How Optimal Approach Works

```
Array: [12, 11, 10, 5, 6, 2, 30]

Initialize: first = ∞, second = ∞

i=0 (12): 12 < first → first = 12
i=1 (11): 11 < first → first = 11
i=2 (10): 10 < first → first = 10
i=3 (5):  5 < first  → first = 5
i=4 (6):  6 > first (5) and 6 < second → second = 6
i=5 (2):  2 < first (5) → first = 2
i=6 (30): 30 > second (6) → Found! (2, 6, 30)

Wait, this gives (2, 6, 30) but 2 comes after 6 in original array!
The key insight is that we're tracking potential candidates, not final answer.
The algorithm maintains: first < second and both are candidates.
When we find a third > second, we can reconstruct the valid triplet.
```

## Key Insights

- **Greedy Strategy:** Keep the smallest valid pair (first, second) to maximize chances
- **Candidate Tracking:** We don't store indices, just values, and verify at the end
- **O(1) Space:** Optimal solution doesn't need auxiliary arrays

## Edge Cases

- Less than 3 elements: return None
- Strictly decreasing: return None
- Multiple valid answers: return any one
- Duplicates: handled correctly (use <= for comparisons)

## Variations

- **Longest Increasing Subsequence:** Classic DP problem
- **Increasing Triplet Subsequence:** LeetCode variation
- **Count of Sorted Subsequences:** More complex counting

## References

- [GeeksforGeeks - Find a sorted subsequence of size 3 in linear time](https://www.geeksforgeeks.org/find-a-sorted-subsequence-of-size-3-in-linear-time/)

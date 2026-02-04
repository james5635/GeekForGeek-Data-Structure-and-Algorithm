# Two Sum Closest to Zero

Given an array `arr[]` of size `n`, find two elements whose sum is closest to zero. Return any one pair with the minimum absolute sum.

## Problem Statement

Find a pair of elements (i, j) where `i ≠ j` such that `|arr[i] + arr[j]|` is minimized.

### Examples

**Input:** `arr[] = [1, 60, -10, 70, -80, 85]`  
**Output:** `(-80, 85)` or `(85, -80)`  
**Explanation:** -80 + 85 = 5, which is closest to 0. Other pairs: 1 + (-10) = -9, 60 + (-80) = -20, etc.

**Input:** `arr[] = [1, 2, 3, 4, 5]`  
**Output:** `(1, 2)`  
**Explanation:** 1 + 2 = 3, closest to 0 (all sums are positive).

**Input:** `arr[] = [-5, -4, -3, -2, -1]`  
**Output:** `(-2, -1)` or `(-1, -2)`  
**Explanation:** -2 + (-1) = -3, closest to 0 (all sums are negative).

**Input:** `arr[] = [5, -5]`  
**Output:** `(5, -5)` or `(-5, 5)`  
**Explanation:** 5 + (-5) = 0, exact zero sum.

## Algorithm Approaches

### 1. Naive Approach - Check All Pairs
- **File:** `two_sum_closest_zero.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Check all possible pairs using nested loops
  - Track pair with minimum absolute sum

### 2. Better Approach - Sort + Binary Search
- **File:** `two_sum_closest_zero.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) or O(n)
- **Description:** 
  - Sort the array
  - For each element, binary search for its negative (closest to zero)
  - Track minimum absolute sum

### 3. Optimal Approach - Sort + Two Pointer
- **File:** `two_sum_closest_zero.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) or O(n)
- **Description:** 
  - Sort the array
  - Use two pointers from both ends
  - If sum < 0, need larger sum → move left pointer right
  - If sum > 0, need smaller sum → move right pointer left
  - Track minimum absolute sum

## Usage

```bash
python two_sum_closest_zero.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple, too slow |
| Sort + Binary Search | O(n log n) | O(1) or O(n) | Good but two-pointer is simpler |
| Sort + Two Pointer | O(n log n) | O(1) or O(n) | **Preferred** - elegant |

## How Two Pointer Approach Works

```
Array: [1, 60, -10, 70, -80, 85]

Step 1: Sort → [-80, -10, 1, 60, 70, 85]

Step 2: Two pointers
  left=0 (-80), right=5 (85), sum=5, |sum|=5
    min_sum = 5, result = (-80, 85)
    sum > 0 → right--
  
  left=0 (-80), right=4 (70), sum=-10, |sum|=10
    10 > 5, don't update
    sum < 0 → left++
  
  left=1 (-10), right=4 (70), sum=60, |sum|=60
    60 > 5, don't update
    sum > 0 → right--
  
  Continue...

Result: (-80, 85) with sum = 5
```

## Why Two Pointer Works

```
Sorted array: [-80, -10, 1, 60, 70, 85]

If sum < 0:
  - We need to increase the sum
  - Moving left right increases sum (less negative or more positive)
  
If sum > 0:
  - We need to decrease the sum
  - Moving right left decreases sum (less positive or more negative)
  
If sum = 0:
  - Perfect! Can't get better than this
  - Return immediately
```

## Key Insights

- **Sorting Enables Two Pointers:** After sorting, we can make intelligent decisions
- **Greedy Movement:** At each step, we move the pointer that can improve the sum
- **Absolute Value:** We care about |sum|, not just sum
- **Single Pass:** After sorting, we find answer in one pass

## Edge Cases

- Less than 2 elements: return None
- Exact zero sum: optimal solution found early
- All positive: pair with smallest two elements
- All negative: pair with largest two elements (closest to 0)
- Duplicates: handled correctly

## Variations

- **Return Indices:** Return original indices instead of values
- **Closest to Target:** Find pair with sum closest to any target
- **Three Sum Closest:** Find triplet closest to target
- **K Sum Closest:** Generalization to k elements

## Related Problems

- Two Sum - Check if Pair Exists
- Two Sum - All Pairs
- 3 Sum Closest
- 4 Sum Closest

## References

- [GeeksforGeeks - Two elements whose sum is closest to zero](https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/)

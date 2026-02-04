# Two Sum - Check if Pair Exists

Given an array `arr[]` of size `n` and a target sum `target`, check if there exists a pair of elements in the array whose sum equals the target.

## Problem Statement

Determine if any two distinct elements in the array sum to the target value.

### Examples

**Input:** `arr[] = [1, 4, 45, 6, 10, -8]`, `target = 16`  
**Output:** `True`  
**Explanation:** 6 + 10 = 16, so pair exists.

**Input:** `arr[] = [1, 2, 4, 3]`, `target = 6`  
**Output:** `True`  
**Explanation:** 2 + 4 = 6, pair exists.

**Input:** `arr[] = [1, 2, 3, 4, 5]`, `target = 10`  
**Output:** `False`  
**Explanation:** No two elements sum to 10.

**Input:** `arr[] = [5, 5]`, `target = 10`  
**Output:** `True`  
**Explanation:** 5 + 5 = 10 (using same value at different indices).

## Algorithm Approaches

### 1. Naive Approach - Check All Pairs
- **File:** `two_sum_pair_exists.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Use two nested loops to check all pairs
  - Return True if any pair sums to target

### 2. Better Approach - Sort + Binary Search
- **File:** `two_sum_pair_exists.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) or O(n)
- **Description:** 
  - Sort the array
  - For each element, binary search for (target - element)
  - More efficient than naive for sorted data

### 3. Better Approach - Sort + Two Pointer
- **File:** `two_sum_pair_exists.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) or O(n)
- **Description:** 
  - Sort the array
  - Use two pointers from both ends
  - Move pointers based on sum comparison
  - More efficient than binary search approach

### 4. Optimal Approach - HashSet
- **File:** `two_sum_pair_exists.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** 
  - Use set to store seen elements
  - For each element, check if (target - element) exists in set
  - Add current element to set

## Usage

```bash
python two_sum_pair_exists.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple, no extra space |
| Sort + Binary Search | O(n log n) | O(1) or O(n) | Good if already sorted |
| Sort + Two Pointer | O(n log n) | O(1) or O(n) | Efficient for sorted |
| HashSet | O(n) | O(n) | **Preferred** - fastest |

## How HashSet Approach Works

```
Array: [1, 4, 45, 6, 10, -8], Target: 16

Initialize: seen = {}

i=0, num=1:
  complement = 16 - 1 = 15
  15 not in seen → seen = {1}

i=1, num=4:
  complement = 16 - 4 = 12
  12 not in seen → seen = {1, 4}

i=2, num=45:
  complement = 16 - 45 = -29
  -29 not in seen → seen = {1, 4, 45}

i=3, num=6:
  complement = 16 - 6 = 10
  10 not in seen → seen = {1, 4, 45, 6}

i=4, num=10:
  complement = 16 - 10 = 6
  6 IS in seen! → Return True

Pair found: 6 (index 3) + 10 (index 4) = 16
```

## How Two Pointer Approach Works

```
Array: [1, 4, 45, 6, 10, -8], Target: 16

Step 1: Sort → [-8, 1, 4, 6, 10, 45]

Step 2: Two pointers
  left=0 (-8), right=5 (45), sum=37 > 16 → right--
  left=0 (-8), right=4 (10), sum=2 < 16 → left++
  left=1 (1), right=4 (10), sum=11 < 16 → left++
  left=2 (4), right=4 (10), sum=14 < 16 → left++
  left=3 (6), right=4 (10), sum=16 == 16 → Found!

Return True
```

## Key Insights

- **Complement Strategy:** Looking for `target - current` is key
- **Time-Space Tradeoff:** HashSet uses space for O(n) time
- **Sorting Benefit:** Two-pointer works well with sorted data
- **Single Pass:** HashSet finds answer in one traversal

## Edge Cases

- Empty array: return False
- Single element: return False (need pair)
- Duplicate values: handled correctly (different indices)
- Negative numbers: all approaches work
- Zero target: pair can be (0,0) or (x, -x)

## Variations

- **Return Pair Values:** Return the actual values, not just boolean
- **Return Pair Indices:** Return indices of the pair
- **Count Pairs:** Count all pairs with given sum
- **Three Sum:** Find triplet with given sum
- **Closest Pair:** Find pair with sum closest to target

## Related Problems

- Two Sum - Closest to Zero
- Two Sum - All Pairs
- Two Sum - Distinct Pairs
- 3 Sum, 4 Sum variations

## References

- [GeeksforGeeks - Check if there is a pair with given sum](https://www.geeksforgeeks.org/given-an-array-and-a-number-x-check-for-pair-in-array-with-sum-as-x/)
- [LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)

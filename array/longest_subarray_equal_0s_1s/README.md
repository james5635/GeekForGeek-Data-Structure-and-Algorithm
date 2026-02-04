# Longest Subarray with Equal 0s and 1s

Given a binary array containing only 0s and 1s, find the length of the longest contiguous subarray having an equal number of 0s and 1s.

## Problem Statement

Find the longest subarray where the count of 0s equals the count of 1s.

### Examples

**Input:** `arr[] = [1, 0, 1, 1, 1, 0, 0]`  
**Output:** `6`  
**Explanation:** Subarray `[1, 0, 1, 1, 0, 0]` from index 1 to 6 has three 0s and three 1s.

**Input:** `arr[] = [1, 0, 1, 1, 0, 0, 0]`  
**Output:** `4`  
**Explanation:** Subarray `[0, 1, 1, 0]` or `[1, 0, 0, 1]` has two 0s and two 1s.

**Input:** `arr[] = [0, 0, 0, 0]`  
**Output:** `0`  
**Explanation:** No subarray with equal 0s and 1s exists.

## Algorithm Approaches

### 1. Naive Approach - Try All Subarrays
- **File:** `longest_subarray_equal_0s_1s.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Check all possible subarrays
  - Count 0s and 1s in each
  - Track maximum length where counts are equal

### 2. Optimal Approach - Prefix Sum with Hash Map
- **File:** `longest_subarray_equal_0s_1s.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** 
  - Treat 0 as -1 and 1 as +1
  - Use prefix sum technique
  - If same prefix sum appears twice, elements between have sum = 0
  - Sum = 0 means equal number of 0s and 1s

## Usage

```bash
python longest_subarray_equal_0s_1s.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Too slow for large n |
| Prefix Sum + Hash | O(n) | O(n) | **Preferred** - optimal |

## Prefix Sum Algorithm Explained

### Key Transformation
- Replace all 0s with -1s
- Now, equal 0s and 1s means sum = 0
- Find longest subarray with sum = 0

### Algorithm

```
Transform: 0 → -1, 1 → +1

Initialize:
  prefix_sum = 0
  max_len = 0
  prefix_map = {0: -1}  # sum 0 at index -1

For i from 0 to n-1:
  prefix_sum += (1 if arr[i] == 1 else -1)
  
  If prefix_sum in prefix_map:
    # Found subarray with sum 0
    length = i - prefix_map[prefix_sum]
    max_len = max(max_len, length)
  Else:
    prefix_map[prefix_sum] = i  # Store first occurrence

Return max_len
```

### Example Walkthrough

```
Array: [1, 0, 1, 1, 1, 0, 0]
Transformed: [1, -1, 1, 1, 1, -1, -1]

Step by step:
  i=0: sum=1, map={0:-1, 1:0}
  i=1: sum=0, found in map at -1
       length = 1 - (-1) = 2, max_len = 2
  i=2: sum=1, found in map at 0
       length = 2 - 0 = 2, max_len = 2
  i=3: sum=2, map={0:-1, 1:0, 2:3}
  i=4: sum=3, map={0:-1, 1:0, 2:3, 3:4}
  i=5: sum=2, found in map at 3
       length = 5 - 3 = 2, max_len = 2
  i=6: sum=1, found in map at 0
       length = 6 - 0 = 6, max_len = 6 ✓

Result: 6 (subarray from index 1 to 6: [0, 1, 1, 1, 0, 0])
Wait, let's verify: [0, 1, 1, 1, 0, 0] has three 0s and three 1s ✓
```

## Key Insights

- **Problem Transformation:** Equal 0s and 1s ↔ Sum = 0
- **Prefix Sum Property:** Same prefix sum at i and j means subarray (i+1, j) sums to 0
- **First Occurrence:** Store only first occurrence to maximize length
- **Initial Value:** prefix_sum = 0 at index -1 handles subarrays starting from index 0

## Why Store First Occurrence?

Storing the first occurrence of each prefix sum ensures we get the maximum length:
- If prefix_sum appears at indices 2, 5, 8
- Using first occurrence (2): lengths are 3, 6
- Using last occurrence: lengths would be smaller

## Edge Cases

- **All 0s or all 1s:** Return 0 (no valid subarray)
- **Single element:** Return 0 (can't have equal counts)
- **Two elements [0, 1] or [1, 0]:** Return 2
- **Empty array:** Return 0

## Variations

- **Longest subarray with given difference:** k more 1s than 0s
- **Count subarrays with equal 0s and 1s:** Modify to count all
- **Largest subarray with sum divisible by k:** Generalization

## Applications

- **Data balancing:** Finding balanced segments in binary data
- **Load balancing:** Equal distribution problems
- **Stock analysis:** Periods with equal gains/losses
- **DNA sequencing:** Finding balanced GC content regions

## Related Problems

- **Longest Common Span:** Two binary arrays with same 0/1 balance
- **Subarray with 0 sum:** General case with any integers

## References

- [GeeksforGeeks - Largest subarray with equal number of 0s and 1s](https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/)

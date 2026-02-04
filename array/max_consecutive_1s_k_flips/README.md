# Maximum Consecutive 1s with K Flips

Given a binary array `arr[]` of size `n` containing only 0s and 1s, and an integer `k`, find the maximum number of consecutive 1s that can be obtained by flipping at most `k` 0s.

## Problem Statement

Find the longest contiguous subarray that contains at most `k` zeros. By flipping these `k` zeros to 1s, we get `k` consecutive 1s.

### Examples

**Input:** `arr[] = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]`, `k = 2`  
**Output:** `6`  
**Explanation:** Flip 0s at indices 3 and 4 (or 9 and any other) to get 6 consecutive 1s: `[1, 1, 1, 0, 0, 1, 1, 1, 1, 1]` after flipping first two 0s.

**Input:** `arr[] = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1]`, `k = 1`  
**Output:** `5`  
**Explanation:** Flip 0 at index 3 to get `[1, 1, 0, 1, 1, 1, 1, 0, 1, 1]`, longest consecutive 1s = 5 (indices 3-7).

**Input:** `arr[] = [1, 1, 1, 1]`, `k = 0`  
**Output:** `4`  
**Explanation:** Already all 1s, no flips needed.

**Input:** `arr[] = [0, 0, 0, 0]`, `k = 2`  
**Output:** `2`  
**Explanation:** Can flip at most 2 zeros to get 2 consecutive 1s.

## Algorithm Approaches

### 1. Naive Approach - Try All Windows
- **File:** `max_consecutive_1s_k_flips.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Try all possible subarrays
  - Count zeros in each subarray
  - Track maximum length with at most k zeros

### 2. Optimal Approach - Sliding Window
- **File:** `max_consecutive_1s_k_flips.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Use two pointers (left and right) to maintain a window
  - Expand window by moving right pointer
  - Count zeros in current window
  - If zeros exceed k, shrink window from left
  - Track maximum window size

### 3. Alternative - Using Queue
- **File:** `max_consecutive_1s_k_flips.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(k)
- **Description:** 
  - Use queue to store positions of zeros
  - When queue size exceeds k, move left to after first zero in queue

## Usage

```bash
python max_consecutive_1s_k_flips.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple, too slow |
| Sliding Window | O(n) | O(1) | **Preferred** - optimal |
| Queue | O(n) | O(k) | Good for tracking positions |

## How Sliding Window Works

```
Array: [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

Initialize: left = 0, zeros = 0, max_len = 0

right=0 (1): zeros=0, window=[1], len=1, max_len=1
right=1 (1): zeros=0, window=[1,1], len=2, max_len=2
right=2 (1): zeros=0, window=[1,1,1], len=3, max_len=3
right=3 (0): zeros=1, window=[1,1,1,0], len=4, max_len=4
right=4 (0): zeros=2, window=[1,1,1,0,0], len=5, max_len=5
right=5 (0): zeros=3 > k=2, shrink!
  left=0 (1): zeros=3, left=1
  left=1 (1): zeros=3, left=2
  left=2 (1): zeros=3, left=3
  left=3 (0): zeros=2, left=4
  window=[0,0,1,1,1,1] (from index 4)
right=5: window=[0,0,0], len=3, max_len=5
right=6 (1): zeros=2, window=[0,0,0,1], len=4, max_len=5
right=7 (1): zeros=2, window=[0,0,0,1,1], len=5, max_len=5
right=8 (1): zeros=2, window=[0,0,0,1,1,1], len=6, max_len=6
right=9 (1): zeros=2, window=[0,0,0,1,1,1,1], len=7, max_len=7
  Wait, this exceeds our k limit! Let me recalculate...
  
Actually at right=5, after shrinking, window starts at index 4 (value 0)
So zeros in [0,0,1,1,1,1] = 2, which equals k. ✓

Final answer: 6 (window with 2 zeros and 4 ones = 6 consecutive after flipping)
```

## Key Insights

- **Window Property:** We want longest window with at most k zeros
- **Greedy Expansion:** Always try to expand window
- **Shrinking Condition:** Only shrink when zeros exceed k
- **Two Pointer Technique:** Classic sliding window pattern

## Mathematical Formulation

```
Find max(j - i + 1) such that:
  count of 0s in arr[i..j] <= k

Sliding window maintains:
  window = arr[left..right]
  zeros = count of 0s in window
  
Invariant: zeros <= k

When zeros > k:
  Move left forward until zeros <= k
```

## Edge Cases

- Empty array: return 0
- k = 0: find longest consecutive 1s without flips
- k >= count of zeros: can flip all zeros, return n
- All zeros: return min(k, n)
- All ones: return n

## Variations

- **Return Indices:** Return start and end of best window
- **Which Zeros to Flip:** Return positions of zeros to flip
- **Max Consecutive 1s III:** LeetCode variation
- **Max Consecutive 1s with K Flips (Circular):** Array is circular
- **Min Flips for K Consecutive 1s:** Reverse problem

## Related Problems

- Max Consecutive Ones (without flips)
- Max Consecutive Ones II (at most one flip)
- Max Consecutive Ones III (general k)
- Longest Subarray with at most K zeros

## Applications

- **DNA Sequencing:** Find longest valid sequence with mutations
- **Signal Processing:** Find longest clean signal with noise tolerance
- **Data Analysis:** Find longest valid data segment with errors
- **Image Processing:** Find largest valid region with artifacts

## References

- [GeeksforGeeks - Maximize number of 0s by flipping a subarray](https://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/)
- [LeetCode - Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

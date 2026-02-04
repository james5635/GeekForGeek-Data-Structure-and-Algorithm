# K-th Largest Sum Contiguous Subarray

Given an array of integers, find the k-th largest sum among all possible contiguous subarrays.

## Problem Statement

A contiguous subarray is a subarray formed by consecutive elements of the array. Find the k-th largest sum among all such subarrays.

### Examples

**Input:** `arr[] = [20, -5, -1]`, `k = 3`  
**Output:** `14`  
**Explanation:**  
All subarray sums:
- `[20]` = 20
- `[20, -5]` = 15
- `[20, -5, -1]` = 14
- `[-5]` = -5
- `[-5, -1]` = -6
- `[-1]` = -1

Sorted descending: 20, 15, 14, -1, -5, -6  
3rd largest = 14

**Input:** `arr[] = [10, -10, 20, -40]`, `k = 6`  
**Output:** `-10`

## Algorithm Approaches

### 1. Naive Approach - Generate All and Sort
- **File:** `kth_largest_sum_contiguous_subarray.py`
- **Time Complexity:** O(n² log n)
- **Space Complexity:** O(n²)
- **Description:**
  - Generate all n*(n+1)/2 subarray sums
  - Sort in descending order
  - Return k-th element

### 2. Better Approach - Min Heap of Size k
- **File:** `kth_largest_sum_contiguous_subarray.py`
- **Time Complexity:** O(n² log k)
- **Space Complexity:** O(k)
- **Description:**
  - Generate all subarray sums
  - Maintain min heap of size k
  - Keep only k largest seen so far
  - Top of heap is k-th largest

### 3. Optimal Approach - Prefix Sum with Heap
- **File:** `kth_largest_sum_contiguous_subarray.py`
- **Time Complexity:** O(n² log k)
- **Space Complexity:** O(n)
- **Description:**
  - Compute prefix sums
  - For each pair (i, j), calculate sum = prefix[j] - prefix[i]
  - Use min heap to track k largest

## Usage

```bash
python kth_largest_sum_contiguous_subarray.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n² log n) | O(n²) | Simple, uses too much space |
| Min Heap | O(n² log k) | O(k) | Better space, same time |
| Prefix + Heap | O(n² log k) | O(n) | Uses prefix for efficiency |
| Optimized | O(n log n) avg | O(k) | Best for large k |

## Algorithm Details

### Min Heap Approach Logic

```python
min_heap = []

for each subarray sum s:
    if len(min_heap) < k:
        push s to heap
    elif s > min_heap[0]:
        replace top with s

return min_heap[0]  # k-th largest
```

### Prefix Sum Logic

```
Prefix sum: prefix[i] = sum of arr[0..i-1]
Subarray sum arr[i..j] = prefix[j+1] - prefix[i]

Example: arr = [20, -5, -1]
prefix = [0, 20, 15, 14]

Sum of [20, -5] (indices 0..1):
  = prefix[2] - prefix[0] = 15 - 0 = 15 ✓
```

### Example Walkthrough

```
Input: arr = [20, -5, -1], k = 3

Step 1: Generate all subarray sums
  i=0: [20]=20, [20,-5]=15, [20,-5,-1]=14
  i=1: [-5]=-5, [-5,-1]=-6
  i=2: [-1]=-1
  
  All sums: [20, 15, 14, -5, -6, -1]

Step 2: Min Heap of size 3
  Push 20: heap = [20]
  Push 15: heap = [15, 20]
  Push 14: heap = [14, 20, 15]
  Push -5: -5 < 14, ignore
  Push -6: -6 < 14, ignore
  Push -1: -1 < 14, ignore
  
  Final heap: [14, 20, 15] (min heap)

Step 3: Return heap[0] = 14 ✓
```

## Key Insights

- **Only Need Top k:** Don't need to sort all n² sums
- **Min Heap Property:** Top element is always k-th largest seen
- **Early Termination:** Can stop if current sum is too small
- **Prefix Optimization:** Faster sum calculation with prefix array

## Edge Cases

- k = 1: Maximum subarray sum (Kadane's algorithm can be used)
- k = n*(n+1)/2: Minimum subarray sum
- All negative: Works correctly
- All positive: Total sum is 1st largest
- Single element: Only one subarray

## Variations

- **K-th smallest sum:** Use max heap instead
- **K-th largest distinct sum:** Handle duplicates
- **Count subarrays with sum >= X:** Different problem
- **Online queries:** Preprocess for multiple k queries

## References

- [GeeksforGeeks - K-th Largest Sum Contiguous Subarray](https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/)

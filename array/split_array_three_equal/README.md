# Split Array into Three Equal Sum Subarrays

Given an array `arr[]` of size `n`, determine whether the array can be split into three contiguous parts with equal sum. If possible, return the indices where the splits should occur.

## Problem Statement

Check if there exist indices `i` and `j` (where `i < j`) such that:
- Sum of elements from index 0 to i = Sum of elements from index i+1 to j = Sum of elements from index j+1 to n-1

### Examples

**Input:** `arr[] = [1, 3, 4, 0, 4]`  
**Output:** `True` (indices 1 and 2)  
**Explanation:** 
- First part: [1, 3] = 4
- Second part: [4] = 4  
- Third part: [0, 4] = 4

**Input:** `arr[] = [0, 0, 0, 0]`  
**Output:** `True` (multiple valid splits)  
**Explanation:** Can split as [0], [0, 0], [0] or [0, 0], [0], [0], etc.

**Input:** `arr[] = [1, 2, 3, 4, 5]`  
**Output:** `False`  
**Explanation:** Total sum = 15, not divisible by 3.

**Input:** `arr[] = [1, 2]`  
**Output:** `False`  
**Explanation:** Array too small to split into three parts.

## Algorithm Approaches

### 1. Naive Approach - Check All Split Points
- **File:** `split_array_three_equal.py`
- **Time Complexity:** O(n³)
- **Space Complexity:** O(1)
- **Description:** 
  - Try all possible pairs of split points (i, j)
  - Calculate sum of three parts for each pair
  - Return True if any pair gives equal sums

### 2. Better Approach - Prefix Sum Array
- **File:** `split_array_three_equal.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(n)
- **Description:** 
  - Precompute prefix sum array for O(1) range sum queries
  - Try all split points using prefix sums
  - Early termination if total sum not divisible by 3

### 3. Optimal Approach - Single Pass
- **File:** `split_array_three_equal.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Calculate total sum first
  - If not divisible by 3, return False immediately
  - Traverse array, accumulating running sum
  - When running sum equals target, we found a partition
  - Need exactly 2 partitions (third is automatic)

## Usage

```bash
python split_array_three_equal.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n³) | O(1) | Simple, too slow |
| Prefix Sum | O(n²) | O(n) | Better, precomputation helps |
| Single Pass | O(n) | O(1) | **Preferred** - optimal |

## How Optimal Approach Works

```
Array: [1, 3, 4, 0, 4]

Step 1: Calculate total sum
  total = 1 + 3 + 4 + 0 + 4 = 12
  12 % 3 = 0 ✓ (divisible)
  target = 12 / 3 = 4

Step 2: Traverse and find partitions
  running_sum = 0, count = 0
  
  i=0: running_sum = 1, not equal to 4
  i=1: running_sum = 1 + 3 = 4 ✓
       Found first partition!
       count = 1, running_sum = 0
  
  i=2: running_sum = 4 ✓
       Found second partition!
       count = 2, running_sum = 0
       Return True (third partition is automatic)

Result: True, split at indices 1 and 2
```

## Key Insights

- **Divisibility Check:** If total sum not divisible by 3, impossible to split
- **Target Calculation:** Each partition must sum to total/3
- **Partition Counting:** Need exactly 2 partitions found, third is implied
- **Running Sum Reset:** Reset sum when partition found to find next

## Mathematical Formula

```
Total sum = S
Each partition sum = S/3

Condition: S % 3 == 0

Running sum accumulates:
  When running_sum == S/3:
    - Partition found
    - Increment count
    - Reset running_sum = 0
    
Success if count >= 2 (2 partitions found)
```

## Edge Cases

- Less than 3 elements: impossible to split
- Total sum not divisible by 3: impossible
- All zeros: multiple valid splits
- Negative numbers: works correctly
- Exact splits required: no overlap, no gaps

## Variations

- **Return Indices:** Find and return the actual split points
- **Count Ways:** Count number of ways to split
- **K Equal Parts:** Generalize to k parts instead of 3
- **Non-contiguous:** Split without contiguity constraint (different problem)

## Applications

- Load balancing: Divide workload equally
- Resource allocation: Split resources fairly
- Array partitioning: Data processing pipelines
- Game theory: Fair division problems

## References

- [GeeksforGeeks - Split an array into two equal Sum subarrays](https://www.geeksforgeeks.org/split-an-array-into-two-equal-sum-subarrays/)

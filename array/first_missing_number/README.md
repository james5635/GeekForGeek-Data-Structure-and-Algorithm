# First Missing Positive Number

Given an unsorted integer array `nums`, return the smallest missing positive integer.

## Problem Statement

Find the smallest positive integer (greater than 0) that is not present in the array.

### Examples

**Input:** `nums = [1, 2, 0]`  
**Output:** `3`  
**Explanation:** Numbers 1 and 2 are present, 3 is missing.

**Input:** `nums = [3, 4, -1, 1]`  
**Output:** `2`  
**Explanation:** 1 is present, but 2 is missing (smallest missing positive).

**Input:** `nums = [7, 8, 9, 11, 12]`  
**Output:** `1`  
**Explanation:** No positive integers 1-6 are present, so 1 is missing.

## Algorithm Approaches

### 1. Naive Approach - Sort and Scan
- **File:** `first_missing_number.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) or O(n) depending on sort
- **Description:**
  - Sort the array
  - Traverse from beginning, find first missing positive
  - Track expected next positive integer

### 2. Better Approach - Hash Set
- **File:** `first_missing_number.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:**
  - Store all elements in a hash set
  - Check integers 1, 2, 3, ... until not found
  - Return first missing

### 3. Optimal Approach - Cyclic Sort
- **File:** `first_missing_number.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) - in-place
- **Description:**
  - Place each element at its correct index (element x goes to index x-1)
  - After placement, find first index where value ≠ index+1
  - That index+1 is the answer

### 4. Alternative Optimal - Partition and Mark
- **File:** `first_missing_number.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:**
  - Partition array: move positive numbers to front
  - Use sign of numbers to mark presence
  - Find first unmarked position

## Usage

```bash
python first_missing_number.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive (Sort) | O(n log n) | O(1) or O(n) | Simple, not optimal |
| Hash Set | O(n) | O(n) | Fast, uses extra space |
| Cyclic Sort | O(n) | O(1) | Optimal, in-place |
| Partition+Mark | O(n) | O(1) | Optimal, alternative |

## Algorithm Details

### Cyclic Sort Logic

```python
for i in range(n):
    # While element is in valid range AND not at correct position
    while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
        # Swap to place element at correct index
        correct_idx = arr[i] - 1
        swap(arr[i], arr[correct_idx])

# Find first position where value != index + 1
for i in range(n):
    if arr[i] != i + 1:
        return i + 1

# All 1..n present, return n+1
return n + 1
```

### Example Walkthrough

```
Input: [3, 4, -1, 1]

Step 1: i=0, arr[0]=3
        3 is valid (1 <= 3 <= 4) and not at position 2 (3-1)
        Swap arr[0] and arr[2]: [-1, 4, 3, 1]
        
        i=0, arr[0]=-1
        -1 is not valid, skip

Step 2: i=1, arr[1]=4
        4 is valid and not at position 3 (4-1)
        Swap arr[1] and arr[3]: [-1, 1, 3, 4]
        
        i=1, arr[1]=1
        1 is valid and not at position 0 (1-1)
        Swap arr[1] and arr[0]: [1, -1, 3, 4]
        
        i=1, arr[1]=-1
        -1 is not valid, skip

Step 3: i=2, arr[2]=3
        3 is valid and at correct position (3-1=2) ✓

Step 4: i=3, arr[3]=4
        4 is valid and at correct position (4-1=3) ✓

Final array: [1, -1, 3, 4]
             0   1   2   3

Check: i=0, arr[0]=1 == 0+1 ✓
       i=1, arr[1]=-1 != 1+1=2 ✗

Return: i+1 = 2 ✓
```

## Key Insights

- **Range Constraint:** Answer must be in range [1, n+1] where n is array size
- **Index Mapping:** Element x belongs at index x-1
- **In-place:** Can reorder array to mark presence
- **Linear Time:** Despite nested while loop, each element swapped at most once

## Edge Cases

- All negative: Return 1
- All positive consecutive from 1: Return n+1
- Duplicates: Handled correctly
- Large numbers: Ignored (outside valid range)
- Single element: Handle [0], [1], [2] correctly

## Variations

- **Find first missing non-negative:** Include 0 in search
- **Find k-th missing positive:** Track count of missing
- **Missing in sorted array:** Can use binary search O(log n)
- **First duplicate:** Similar approach, different condition

## References

- [GeeksforGeeks - Find the smallest positive number missing from an array](https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/)
- [LeetCode - First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

# Three Way Partitioning of an Array Around a Given Range

## Problem Statement

Given an array and a range `[low, high]`, partition the array such that:
1. All elements **smaller than `low`** come first
2. All elements in range **`[low, high]`** come next  
3. All elements **greater than `high`** appear in the end

The elements in each region don't need to be sorted, just correctly partitioned.

## Examples

**Example 1:**
```
Input: arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 9, 10], low = 14, high = 20
Output: [1, 5, 4, 2, 9, 10, 14, 20, 20, 54, 87]

Explanation:
- Elements < 14: [1, 5, 4, 2, 9, 10]
- Elements in [14, 20]: [14, 20, 20]  
- Elements > 20: [54, 87]
```

## Approach

### Dutch National Flag Algorithm
Similar to the classic Dutch National Flag problem with three colors, we use three pointers:

1. **`low` pointer**: Boundary of elements < `low_val` (grows from left)
2. **`mid` pointer**: Current element being examined (moves left to right)
3. **`high` pointer**: Boundary of elements > `high_val` (grows from right)

### Algorithm Steps
1. Initialize: `low = 0`, `mid = 0`, `high = n - 1`
2. While `mid <= high`:
   - If `arr[mid] < low_val`: Swap with `arr[low]`, increment both `low` and `mid`
   - If `arr[mid] > high_val`: Swap with `arr[high]`, decrement `high` (don't increment `mid` yet)
   - If `low_val <= arr[mid] <= high_val`: Just increment `mid`

## Complexity Analysis

- **Time Complexity:** O(n)
  - Single pass through array: O(n)
- **Space Complexity:** O(1)
  - In-place partitioning
  - Only using three pointers

## Implementation

```python
def three_way_partition(arr, low_val, high_val):
    if not arr or low_val > high_val:
        return arr
    
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1
    
    while mid <= high:
        if arr[mid] < low_val:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > high_val:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
    
    return arr
```

## Edge Cases

- **Empty array:** Returns empty
- **Single element:** Correctly placed based on value
- **All in one region:** Works correctly
- **All equal:** Stays in middle region
- **Invalid range (low > high):** Returns original

## Applications

- Quicksort with three-way partitioning
- Sorting arrays with many duplicates
- Color sorting (Dutch National Flag)
- Range-based data organization

## Related Problems

- Dutch National Flag Problem
- Sort 0s, 1s, and 2s
- Partition around pivot

## Reference

- [GeeksforGeeks - Three Way Partitioning of an Array Around a Given Range](https://www.geeksforgeeks.org/dsa/three-way-partitioning-of-an-array-around-a-given-range/)
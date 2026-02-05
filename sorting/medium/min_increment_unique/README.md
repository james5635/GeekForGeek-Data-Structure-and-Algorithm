# Minimum Increment to Make Array Unique

## Problem Statement

Given an array of integers, find the minimum number of increment operations required to make all elements in the array unique. Each increment operation increases an element by 1.

## Examples

**Example 1:**
```
Input: arr = [1, 2, 2]
Output: 1
Explanation: Increment one of the 2s to make it 3.
             Array becomes [1, 2, 3]
             Total increments = 1
```

**Example 2:**
```
Input: arr = [3, 2, 1, 2, 1, 7]
Output: 6
Explanation: [3, 2, 1, 2, 1, 7] -> [3, 4, 1, 2, 5, 7]
             Increments: 2->4 (2), 1->5 (4), Total = 6
```

## Approach

### Greedy Approach
1. **Sort the array** - This brings duplicates together
2. **Traverse through sorted array** starting from second element
3. **Ensure uniqueness** - Each element must be at least 1 greater than the previous element
4. **Count increments** - Add the difference needed to make current element valid

### Why Greedy Works
By sorting the array first, we process elements in increasing order. When we encounter a duplicate or smaller element, we increment it to be just 1 more than the previous element. This is optimal because:
- We make the minimum necessary increment
- We preserve the sorted order for subsequent elements

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Sorting the array: O(n log n)
  - Single traversal: O(n)
- **Space Complexity:** O(1) auxiliary
  - In-place sorting
  - Only using counter variables

## Implementation

```python
def min_increment_for_unique(arr):
    if not arr or len(arr) <= 1:
        return 0
    
    arr.sort()
    increments = 0
    
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            needed = arr[i - 1] + 1
            increments += needed - arr[i]
            arr[i] = needed
    
    return increments
```

## Edge Cases

- **Empty array:** Returns 0
- **Single element:** Returns 0 (already unique)
- **All unique:** Returns 0 (no increments needed)
- **All same:** Requires maximum increments (0+1+2+...+(n-1))
- **Negative numbers:** Handled correctly

## Variations

- **Using Counting Sort:** O(n + max_val) when range of values is small
- **Using Set:** O(n) time but O(n) space for tracking used values

## Reference

- [GeeksforGeeks - Minimum Increment Operations to Make Array Unique](https://www.geeksforgeeks.org/dsa/minimum-increment-operations-to-make-array-unique/)
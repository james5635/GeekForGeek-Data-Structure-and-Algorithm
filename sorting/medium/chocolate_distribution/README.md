# Chocolate Distribution Problem

## Problem Statement

Given an array of integers where each value represents the number of chocolates in a packet. There are `m` students, and the task is to distribute chocolate packets such that:
1. Each student gets exactly one packet
2. The difference between the maximum and minimum number of chocolates given to students is minimized

## Examples

**Example 1:**
```
Input: arr = [7, 3, 2, 4, 9, 12, 56], m = 3
Output: 2
Explanation: If we distribute packets with chocolates [2, 3, 4],
             the difference = 4 - 2 = 2 (minimum possible)
```

**Example 2:**
```
Input: arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5
Output: 6
Explanation: Distribute packets [3, 4, 7, 9, 9], 
             difference = 9 - 3 = 6
```

## Approach

### Sorting + Sliding Window
1. **Sort the array** - Brings similar values together
2. **Use sliding window of size m** - Each window represents one distribution option
3. **Calculate difference** for each window: `arr[i+m-1] - arr[i]`
4. **Return minimum difference**

### Why This Works
After sorting, any m consecutive elements in the array represent a valid distribution where the difference is minimized for that particular selection. By checking all possible windows, we find the global minimum.

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Sorting: O(n log n)
  - Sliding window scan: O(n)
- **Space Complexity:** O(1) auxiliary
  - In-place sorting
  - Only using difference variable

## Implementation

```python
def find_min_diff(arr, m):
    if m > len(arr) or m <= 0:
        raise ValueError("Invalid input")
    
    arr.sort()
    min_diff = float('inf')
    
    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    return min_diff
```

## Edge Cases

- **Not enough packets:** Raise error if m > len(arr)
- **Single student:** Returns 0 (one packet, no difference)
- **All same values:** Returns 0
- **m = 0 or negative:** Invalid input
- **Empty array:** Invalid input

## Variations

- **Return actual packets:** Also return which m packets to distribute
- **Return min/max:** Return the actual min and max values
- **Multiple valid distributions:** Return all optimal solutions

## Applications

- Fair resource distribution
- Load balancing
- Data partitioning
- Range minimization problems

## Reference

- [GeeksforGeeks - Chocolate Distribution Problem](https://www.geeksforgeeks.org/dsa/chocolate-distribution-problem/)
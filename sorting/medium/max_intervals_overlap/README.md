# Maximum Intervals Overlap Point

## Problem Statement

Given a set of time intervals, find the point (or time) where the maximum number of intervals overlap.

## Examples

**Example 1:**
```
Input: intervals = [[1, 5], [2, 6], [3, 7], [4, 8]]
Output: 4
Explanation: At time 4, all 4 intervals are active/overlapping
```

**Example 2:**
```
Input: intervals = [[1, 4], [2, 5], [9, 12], [5, 9], [5, 12]]
Output: 5
Explanation: At time 5, 4 intervals are active [1,4], [2,5], [5,9], [5,12]
```

## Approach

### Sorting + Two Pointers
1. **Separate start and end times** into two arrays
2. **Sort both arrays** independently
3. **Use two pointers** to traverse both arrays
4. **Track active intervals:**
   - When we see a start time → increment count
   - When we see an end time → decrement count
5. **Track maximum** count and corresponding time

### Why This Works
By processing all start and end times in sorted order, we can efficiently track how many intervals are active at any point in time without checking all pairs.

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Sorting start times: O(n log n)
  - Sorting end times: O(n log n)
  - Linear scan: O(n)
- **Space Complexity:** O(n)
  - Arrays for start and end times: O(n)

## Implementation

```python
def find_max_overlap(intervals):
    if not intervals:
        return None
    
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    
    max_overlap = 0
    current_overlap = 0
    max_time = starts[0]
    
    i = j = 0
    n = len(intervals)
    
    while i < n and j < n:
        if starts[i] <= ends[j]:
            current_overlap += 1
            if current_overlap > max_overlap:
                max_overlap = current_overlap
                max_time = starts[i]
            i += 1
        else:
            current_overlap -= 1
            j += 1
    
    return max_time
```

## Edge Cases

- **Empty array:** Returns None
- **Single interval:** Returns start time
- **No overlaps:** Returns first start time
- **All intervals overlap:** Returns last start time
- **Multiple points with same max:** Returns first occurrence

## Variations

- **Find all max overlap points:** Track all times with maximum count
- **Return count as well:** Return tuple of (time, count)
- **Continuous time:** Find interval with max overlap

## Applications

- Resource scheduling
- Hotel room booking
- Traffic analysis
- CPU scheduling
- Meeting room requirements

## Related Problems

- Minimum Number of Platforms Required
- Meeting Rooms II
- Car Pooling

## Reference

- [GeeksforGeeks - Find the Point Where Maximum Intervals Overlap](https://www.geeksforgeeks.org/dsa/find-the-point-where-maximum-intervals-overlap/)
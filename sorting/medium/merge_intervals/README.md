# Merge Intervals

## Problem Statement

Given an array of intervals where each interval is represented as `[start, end]`, merge all overlapping intervals and return an array of non-overlapping intervals.

## Examples

**Example 1:**
```
Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation: [1, 3] and [2, 6] overlap, so they are merged into [1, 6]
```

**Example 2:**
```
Input: intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
Explanation: [1, 4] and [4, 5] overlap (touch at 4), so they are merged into [1, 5]
```

## Approach

### Sorting + Linear Scan
1. **Sort intervals by start time** - This ensures we process intervals in order
2. **Initialize result** with the first interval
3. **For each subsequent interval:**
   - If it overlaps with the last merged interval (current.start <= last.end), merge them by extending the end
   - Otherwise, add it as a new interval

### Overlap Detection
Two intervals `[a, b]` and `[c, d]` overlap if:
- `c <= b` (second starts before or at first ends)

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Sorting: O(n log n)
  - Merging scan: O(n)
- **Space Complexity:** O(n)
  - Result array: O(n)
  - Sorting auxiliary: O(log n) to O(n)

## Implementation

```python
def merge_intervals(intervals):
    if not intervals or len(intervals) <= 1:
        return intervals
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:
            # Overlap detected, merge
            last[1] = max(last[1], current[1])
        else:
            # No overlap
            merged.append(current)
    
    return merged
```

## Edge Cases

- **Empty array:** Returns empty array
- **Single interval:** Returns same interval
- **No overlaps:** Returns sorted intervals
- **All overlap:** Returns single merged interval
- **Touching intervals:** Merged if `start <= end` (inclusive)

## Applications

- Calendar scheduling
- Resource allocation
- Time range consolidation
- Meeting room availability

## Related Problems

- Insert Interval
- Non-overlapping Intervals
- Meeting Rooms
- Find Minimum Number of Arrows to Burst Balloons

## Reference

- [GeeksforGeeks - Merging Intervals](https://www.geeksforgeeks.org/dsa/merging-intervals/)
# Check Interval Overlap

## Problem Statement
Given a collection of intervals, merge all overlapping intervals and check if any overlap exists.

## Approach
### Merge Intervals Algorithm
1. Sort all intervals by their start time
2. Initialize result with the first interval
3. For each subsequent interval:
   - If it overlaps with the last interval in result (current.start <= last.end), merge by extending the end time
   - Otherwise, add it to the result

### Check Overlap
Simply check if any interval starts before or at the end of the previous interval.

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Sort | O(n log n) | O(1) or O(n) |
| Merge | O(n) | O(n) |
| Check Overlap | O(n log n) | O(1) |

## Key Points
- Two intervals [a, b] and [c, d] overlap if c <= b
- Sorting by start time is crucial
- Touching intervals (b == c) are considered overlapping
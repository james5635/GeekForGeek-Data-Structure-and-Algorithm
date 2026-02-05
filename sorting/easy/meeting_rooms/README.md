# Meeting Rooms - Check if a person can attend all meetings

## Problem Description

Given a 2D array `arr[][]` where `arr[i][0]` represents the starting time and `arr[i][1]` represents the ending time of the ith meeting, determine whether it is possible for a person to attend all meetings without any overlaps.

Note: A person can attend a meeting if its starting time is the same as the previous meeting's ending time.

## Algorithm

1. Sort the meetings by their start times
2. Iterate through sorted meetings
3. For each meeting, check if it overlaps with the next meeting
4. Overlap occurs if current meeting's end time > next meeting's start time
5. Return False if any overlap found, True otherwise

## Complexity Analysis

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(n log n) | O(1) |
| Average | O(n log n) | O(1) |
| Worst | O(n log n) | O(1) |

## Example

```
Input:  [[2, 4], [1, 2], [7, 8], [5, 6], [6, 8]]
Output: False
Explanation: Meetings [5, 6] and [6, 8] don't overlap, but [6, 8] and [6, 8] would
```

## Key Points

- Sorting is the key to solving this efficiently
- After sorting, only need to check adjacent meetings
- Time complexity dominated by sorting step
- O(n²) brute force approach exists but is inefficient
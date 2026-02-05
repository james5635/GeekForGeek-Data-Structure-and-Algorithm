# Minimum Platforms Required (Railway/Bus Station)

## Problem Statement

Given arrival and departure times of all trains/buses that reach a station, find the minimum number of platforms required so that no train/bus waits (we are given arrival and departure times of all trains/buses).

## Examples

**Example 1:**
```
Input: 
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

Output: 3

Explanation: Maximum 3 trains are present at the station at the same time:
- At 940: trains that arrived at 900 (departs 910), 940 (departs 1200), and 950 (departs 1120)
- The train that arrived at 900 departs at 910, but the train at 950 arrives at 950
```

## Approach

### Sorting + Two Pointers
1. **Sort both arrival and departure arrays**
2. **Use two pointers** to traverse both arrays
3. **Track platform count:**
   - If next arrival ≤ next departure: new train arrives → increment platforms
   - If next departure < next arrival: train departs → decrement platforms
4. **Track maximum** platforms needed

### Key Insight
We only care about how many trains are present at any given time, not the specific trains. Sorting helps us process events chronologically.

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Sorting arrival: O(n log n)
  - Sorting departure: O(n log n)
  - Linear scan: O(n)
- **Space Complexity:** O(n)
  - Arrays for sorted times: O(n)

## Implementation

```python
def find_min_platforms(arrival, departure):
    if not arrival:
        return 0
    
    n = len(arrival)
    arrival.sort()
    departure.sort()
    
    platforms_needed = 0
    max_platforms = 0
    i = j = 0
    
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1
    
    return max_platforms
```

## Edge Cases

- **Empty arrays:** Returns 0
- **Single train:** Returns 1
- **All trains at same time:** Returns n (number of trains)
- **No overlap:** Returns 1
- **Complete overlap:** Returns n

## Variations

- **Event-based approach:** Create events and sort by time
- **Count array approach:** If time range is small, use counting
- **Return peak time:** Find when maximum platforms are needed

## Applications

- Railway station platform planning
- Airport gate allocation
- Meeting room scheduling
- Resource allocation
- CPU process scheduling

## Related Problems

- Meeting Rooms II
- Car Pooling
- Maximum Intervals Overlap

## Reference

- [GeeksforGeeks - Minimum Number of Platforms Required](https://www.geeksforgeeks.org/dsa/minimum-number-platforms-required-railwaybus-station/)
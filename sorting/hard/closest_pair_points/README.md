# Closest Pair of Points using Divide and Conquer

## Problem Statement
Given an array of n points in the 2D plane, find the pair of points that are closest to each other (minimum Euclidean distance).

## Examples
- Input: points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
  - Output: 1.41421 (distance between (2, 3) and (3, 4))

## Approaches

### 1. Brute Force
1. Calculate distance between all pairs of points
2. Track minimum distance
3. **Time Complexity**: O(n²)
4. **Space Complexity**: O(1)

### 2. Divide and Conquer (Optimal)
1. Sort points by x-coordinate
2. Recursively find closest pair in left and right halves
3. Check strip around middle line for closer pairs
4. **Time Complexity**: O(n log n)
5. **Space Complexity**: O(n)

### 3. Plane Sweep
1. Sort points by x-coordinate
2. Maintain active set of candidate points
3. Only check points within min_dist in x direction
4. **Time Complexity**: O(n log n)
5. **Space Complexity**: O(n)

## Algorithm Steps (Divide and Conquer)
```
ClosestPair(points):
    If n <= 3: return brute force result
    
    Sort points by x: Px
    Sort points by y: Py
    
    Divide: Split into left and right halves
    Conquer: d_left = ClosestPair(left)
             d_right = ClosestPair(right)
    d = min(d_left, d_right)
    
    Combine: Check strip of width 2d around middle line
    Return minimum of d and strip minimum
```

## Strip Optimization
- Only points within distance d of middle line need checking
- For each point in strip, only check next 7 points
- This guarantees O(n) strip processing

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Brute Force | O(n²) | O(1) | Only for small n |
| Divide & Conquer | O(n log n) | O(n) | Classic algorithm |
| Plane Sweep | O(n log n) | O(n) | Practical for large n |

## Key Insights
- Divide and conquer exploits geometric properties
- Strip optimization is crucial for O(n log n) complexity
- At most 6 points can fit in a d x 2d rectangle
- Sorting by both x and y coordinates enables efficient merging

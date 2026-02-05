# Maximum Points on Same Line

## Problem

Given N points on a 2D plane, find the maximum number of points that lie on the same straight line.

## Approach

For each point, calculate the slope of the line formed with every other point. Use a hash map to count points with the same slope. Slope is represented as a reduced fraction (dy, dx) to avoid floating point precision issues.

## Complexity

- **Time Complexity:** O(n^2) - for each point, check all other points
- **Space Complexity:** O(n) - hash map for slopes

## Example

```
Input: points = [[1,1], [2,2], [3,3]]
Output: 3
Explanation: All three points lie on the line y = x
```

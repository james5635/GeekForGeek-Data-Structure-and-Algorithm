# Employees Under Every Employee

## Problem Statement
Given employee-manager relationships, find the count of employees under each manager (both direct and indirect reports).

## Approach
Use DFS with memoization:
1. Build adjacency list: manager -> list of direct reports
2. For each employee, use DFS to count all subordinates recursively
3. Use memoization to store computed counts and avoid recomputation
4. Return results sorted by employee name

## Complexity
- **Time**: O(N) - Visit each employee once with memoization
- **Space**: O(N) - Adjacency list and memoization cache

## Example
```
Input: [[A, C], [B, C], [C, F], [D, E], [E, F], [F, F]]
Output: [[A, 0], [B, 0], [C, 2], [D, 0], [E, 1], [F, 5]]

Explanation:
- C has A, B as direct reports
- E has D as direct report  
- F (CEO) has C, E as direct reports + all their subordinates = 5 total
```

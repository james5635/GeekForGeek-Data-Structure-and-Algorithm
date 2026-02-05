# Largest Fibonacci Subset

## Problem Statement
Given an array arr[], find the largest subset containing elements that are Fibonacci numbers.

## Approach
**Hash Set Approach**:
1. Find maximum element in array
2. Generate all Fibonacci numbers up to max element
3. Store Fibonacci numbers in hash set for O(1) lookup
4. Filter array to keep only Fibonacci numbers

**Alternative Mathematical Approach**:
- A number N is Fibonacci if either (5*N² + 4) or (5*N² - 4) is a perfect square

## Complexity
- **Time**: O(N + M) where N is array size, M is max element
- **Space**: O(N + M) for hash set

## Example
```
Input: arr[] = [1, 4, 3, 9, 10, 13, 7]
Output: [1, 3, 13]
Explanation: Only 1, 3, and 13 are Fibonacci numbers
```

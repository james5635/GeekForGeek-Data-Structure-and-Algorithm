# Find K Numbers with Most Occurrences

## Problem Statement
Given an array of n numbers and a positive integer k, find the k numbers that appear the most frequently in the array. The numbers should be printed in decreasing order of their frequencies. If two numbers have the same frequency, the larger number should be given preference.

## Examples
- Input: arr[] = [3, 1, 4, 4, 5, 2, 6, 1], k = 2
  - Output: [4, 1]
  - Explanation: Frequency of 4 = 2, Frequency of 1 = 2. Since 4 > 1, 4 is printed first

- Input: arr[] = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], k = 4
  - Output: [5, 11, 7, 10]

## Approaches

### 1. Hash Map + Sorting
1. Count frequency of each element using hash map - O(n)
2. Sort elements by frequency (descending), then by value (descending) - O(n log n)
3. Return first k elements - O(k)

**Time Complexity**: O(n log n)
**Space Complexity**: O(n)

### 2. Hash Map + Min Heap (Optimal)
1. Count frequency of each element - O(n)
2. Use min heap of size k to keep track of top k frequent elements
3. Return elements from heap - O(k log k)

**Time Complexity**: O(n log k)
**Space Complexity**: O(n)

### 3. Bucket Sort
1. Count frequency of each element - O(n)
2. Create buckets where index = frequency - O(n)
3. Collect elements from highest frequency bucket - O(n)

**Time Complexity**: O(n)
**Space Complexity**: O(n)

### 4. Quickselect
1. Count frequency of each element - O(n)
2. Use quickselect to find top k elements - O(n) average
3. Sort the top k elements - O(k log k)

**Time Complexity**: O(n) average, O(n²) worst
**Space Complexity**: O(n)

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Best For |
|----------|----------------|------------------|----------|
| Sorting | O(n log n) | O(n) | Small n |
| Min Heap | O(n log k) | O(n) | Large n, small k |
| Bucket Sort | O(n) | O(n) | Limited frequency range |
| Quickselect | O(n) avg | O(n) | One-time query |

## Key Insights
- Min heap approach is most efficient for large arrays with small k
- Bucket sort provides O(n) time when max frequency is bounded
- Tie-breaking rule (larger number first) requires careful comparison

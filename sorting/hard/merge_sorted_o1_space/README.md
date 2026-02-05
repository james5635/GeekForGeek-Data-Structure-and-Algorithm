# Merge Two Sorted Arrays with O(1) Extra Space

## Problem Statement
Given two sorted arrays `arr1[]` and `arr2[]` of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify `arr1[]` to contain the first n elements and `arr2[]` to contain the last m elements.

## Examples
- Input: arr1[] = [1, 3, 5, 7], arr2[] = [0, 2, 6, 8, 9]
  - Output: arr1[] = [0, 1, 2, 3], arr2[] = [5, 6, 7, 8, 9]

- Input: arr1[] = [10, 12], arr2[] = [5, 18, 20]
  - Output: arr1[] = [5, 10], arr2[] = [12, 18, 20]

## Approaches

### 1. Gap Method (Shell Sort Inspired)
- Calculate initial gap = ceil((n + m) / 2)
- While gap > 0:
  - Compare elements at distance gap
  - Swap if they are in wrong order
  - Reduce gap = ceil(gap / 2)
- **Time Complexity**: O((n+m) * log(n+m))
- **Space Complexity**: O(1)

### 2. Insertion Sort Like
- Compare last element of arr1 with first element of arr2
- If arr1[i] > arr2[0], swap and sort arr2 using insertion
- **Time Complexity**: O(n*m) in worst case
- **Space Complexity**: O(1)

### 3. Binary Search Method
- Start from end of arr1 and beginning of arr2
- If arr1[i] > arr2[0], swap and binary search to place in arr2
- **Time Complexity**: O(n*log(m))
- **Space Complexity**: O(1)

## Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Gap Method | O((n+m)log(n+m)) | O(1) |
| Insertion | O(n*m) | O(1) |
| Binary Search | O(n*log(m)) | O(1) |

## Key Insights
- The gap method is inspired by Shell Sort and efficiently handles interleaved arrays
- Binary search method is optimal when one array is much smaller
- All approaches maintain O(1) space constraint

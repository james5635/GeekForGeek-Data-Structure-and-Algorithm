# Find Surpasser Count of Each Element in Array

## Problem Statement
Given an array arr[] of n integers, the surpasser count of an element is the number of elements to its right that are greater than it. Find the surpasser count for each element in the array.

## Examples
- Input: arr[] = [2, 7, 5, 3, 0, 8, 1]
  - Output: [4, 1, 1, 1, 2, 0, 0]
  - Explanation: For 2, elements to right greater than it: 7,5,3,8 = 4

- Input: arr[] = [5, 4, 3, 2, 1]
  - Output: [0, 0, 0, 0, 0]

- Input: arr[] = [1, 2, 3, 4, 5]
  - Output: [4, 3, 2, 1, 0]

## Approaches

### 1. Brute Force
1. For each element, count elements to its right that are greater
2. **Time Complexity**: O(n²)
3. **Space Complexity**: O(1)

### 2. Modified Merge Sort (Optimal)
1. Use merge sort to process elements from right to left
2. While merging, count elements from right subarray that are greater
3. **Time Complexity**: O(n log n)
4. **Space Complexity**: O(n)

### 3. Binary Indexed Tree (Fenwick Tree)
1. Coordinate compression + BIT
2. Query count of greater elements to the right
3. **Time Complexity**: O(n log n)
4. **Space Complexity**: O(n)

### 4. Segment Tree
1. Similar to BIT but with segment tree
2. **Time Complexity**: O(n log n)
3. **Space Complexity**: O(n)

## Algorithm Steps (Merge Sort)
```
Store (value, original_index) pairs
surpasser_count = array of zeros

MergeSort(left, right):
    if left >= right: return
    mid = (left + right) / 2
    MergeSort(left, mid)
    MergeSort(mid+1, right)
    Merge(left, mid, right)

Merge(left, mid, right):
    i = left, j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            surpasser_count[arr[i].index] += (right - j + 1)
            i++
        else:
            j++
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Best For |
|----------|----------------|------------------|----------|
| Brute Force | O(n²) | O(1) | Very small n |
| Merge Sort | O(n log n) | O(n) | General use |
| BIT | O(n log n) | O(n) | Range queries |
| Segment Tree | O(n log n) | O(n) | More operations |

## Key Insights
- Similar to counting inversions but in reverse direction
- Merge sort naturally processes elements in order from right to left
- Coordinate compression essential for BIT/Segment Tree when values are large

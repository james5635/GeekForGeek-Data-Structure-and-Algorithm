# Top K Frequent Elements

## Problem Description

Given an array of integers and a number k, find the k most frequent elements in the array. If multiple elements have the same frequency, return them in any order.

**Example:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1, 2]

Explanation: 1 appears 3 times, 2 appears 2 times. These are the top 2 frequent elements.
```

## Algorithms

### 1. Min Heap
**Time:** O(n log k), **Space:** O(n)

Use a min heap of size k to track top k elements. Process all elements once.

### 2. Bucket Sort
**Time:** O(n), **Space:** O(n)

Create buckets where index represents frequency. Best when k is large.

### 3. QuickSelect
**Time:** O(n) average, **Space:** O(n)

Use QuickSelect to find kth most frequent element, then collect all elements with frequency >= kth.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Min Heap | O(n log k) | O(n) |
| Bucket Sort | O(n) | O(n) |
| QuickSelect | O(n) avg | O(n) |
| Brute Force | O(n log n) | O(n) |

## Functions

### `top_k_frequent_heap(nums, k)`
Find top k frequent elements using Min Heap.

**Parameters:**
- `nums`: List of integers
- `k`: Number of top frequent elements to find

**Returns:**
- List of k most frequent elements

### `top_k_frequent_bucket_sort(nums, k)`
Bucket sort approach for O(n) time.

### `top_k_frequent_quickselect(nums, k)`
QuickSelect approach for average O(n) time.

## Usage

```python
from solution import top_k_frequent_heap

nums = [1, 1, 1, 2, 2, 3]
k = 2
result = top_k_frequent_heap(nums, k)
print(result)  # [1, 2]
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Frequency Counting**: First count frequency of each element using a hash map
2. **Heap Selection**: Min heap keeps track of k largest elements efficiently
3. **Bucket Sort Optimization**: When k is large (close to n), bucket sort is optimal
4. **QuickSelect**: Good for finding exact kth element without full sorting

## References

- [GeeksForGeeks - Find K Numbers with Most Occurrences](https://www.geeksforgeeks.org/dsa/find-k-numbers-occurrences-given-array/)

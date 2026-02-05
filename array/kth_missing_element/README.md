# K-th Missing Element in Sorted Array

## Problem Description

Given a sorted array of distinct positive integers and a positive integer k, find the k-th missing element in the array.

The missing elements are the positive integers that are not present in the array.

**Examples:**
```
Input: arr = [2, 3, 5, 9, 10], k = 1
Output: 1
Explanation: Missing elements are 1, 4, 6, 7, 8. The 1st missing is 1.

Input: arr = [2, 3, 5, 9, 10], k = 3
Output: 6
Explanation: The 3rd missing element is 6.
```

## Algorithms

### 1. Binary Search (Optimal)
**Time:** O(log n), **Space:** O(1)

Calculate missing count before each index: `missing_before_i = arr[i] - (i + 1)`
Use binary search to find position where k missing elements occur.

### 2. Linear Scan
**Time:** O(n), **Space:** O(1)

Scan through array, tracking missing elements between consecutive elements.

### 3. Simple Set Approach
**Time:** O(n + m), **Space:** O(n)

Use a set to track present elements, then iterate to find k-th missing.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Binary Search | O(log n) | O(1) |
| Linear Scan | O(n) | O(1) |
| Set Approach | O(n + m) | O(n) |

## Functions

### `find_kth_missing_element(arr, k)`
Find the k-th missing element using binary search.

**Parameters:**
- `arr`: Sorted list of distinct positive integers
- `k`: Position of missing element to find

**Returns:**
- The k-th missing element, or -1 if not found

### `find_kth_missing_element_linear(arr, k)`
Linear approach for comparison.

### `find_kth_missing_element_simple(arr, k)`
Simple approach using set.

## Usage

```python
from solution import find_kth_missing_element

arr = [2, 3, 5, 9, 10]
k = 3
result = find_kth_missing_element(arr, k)
print(result)  # 6
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Missing Count Formula**: For element at index i, missing elements before it = `arr[i] - (i + 1)`
2. **Binary Search Property**: The array is sorted, so we can use binary search to find where missing count exceeds k
3. **Edge Cases**: Handle cases where all k missing elements are before first element or after last element

## References

- [GeeksForGeeks - K-th Missing Element in Sorted Array](https://www.geeksforgeeks.org/dsa/k-th-missing-element-in-sorted-array/)

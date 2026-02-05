# Surpasser Count

## Problem Description

Given an array arr[], the surpasser count of an element arr[i] is the number of elements that are greater than arr[i] and appear to its right in the array.

**Example:**
```
Input: [2, 7, 5, 3, 0, 8, 1]
Output: [4, 1, 1, 1, 2, 0, 0]

Explanation:
- Surpasser count of 2 is 4 (7, 5, 3, 8)
- Surpasser count of 7 is 1 (8)
- Surpasser count of 5 is 1 (8)
- And so on...
```

## Algorithm

**Approach:** Modified Merge Sort

The key insight is that during the merge step of merge sort, when we take an element from the left half, all remaining elements in the right half are greater than it and appear to its right.

**Steps:**
1. Create pairs of (value, original_index) to track original positions
2. Perform merge sort on the array
3. During merge, when an element from left half is placed, count all remaining elements in right half as surpassers
4. Store the count in result array at original index

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Modified Merge Sort | O(n log n) | O(n) |
| Brute Force | O(n²) | O(1) |

## Functions

### `find_surpasser_count(arr)`
Main function that returns list of surpasser counts for each element.

**Parameters:**
- `arr`: List of integers

**Returns:**
- List of surpasser counts for each element

### `find_surpasser_count_brute_force(arr)`
Brute force implementation for comparison.

## Usage

```python
from solution import find_surpasser_count

arr = [2, 7, 5, 3, 0, 8, 1]
result = find_surpasser_count(arr)
print(result)  # [4, 1, 1, 1, 2, 0, 0]
```

## Running the Code

```bash
python solution.py
```

This will run all test cases including:
- Basic example
- Already sorted array
- Reverse sorted array
- Array with duplicates
- Empty array
- Single element array

## Key Insights

1. **Merge Sort Property**: Merge sort naturally groups elements in a way that helps count inversions and surpassers
2. **Index Tracking**: We need to track original indices because merge sort reorders elements
3. **Counting During Merge**: When we place an element from the left half, all remaining elements in the right half are greater and appear to its right

## References

- [GeeksForGeeks - Find Surpasser Count of Each Element in Array](https://www.geeksforgeeks.org/dsa/find-surpasser-count-of-each-element-in-array/)

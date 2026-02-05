# Sort Given Matrix

## Problem Statement
Given a n x n matrix, sort all elements such that the matrix is sorted in row-major order.

## Approach
### Flatten and Sort
1. Extract all elements from the matrix into a 1D array
2. Sort the 1D array using any efficient sorting algorithm
3. Fill the matrix back row by row

### Snake Pattern (Alternative)
After sorting, fill the matrix in snake pattern (alternating row directions).

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Flatten & Sort | O(n² log(n²)) | O(n²) |
| Snake Pattern | O(n² log(n²)) | O(n²) |

Where n = dimension of the n x n matrix

## Key Points
- n² elements need to be sorted
- Space needed for temporary storage
- Simple and straightforward approach
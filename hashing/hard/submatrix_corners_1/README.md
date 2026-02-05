# Submatrix with Corners as 1

## Problem Description

Given a binary matrix, count the number of square submatrices where all four corners are 1.

## Examples

```
Matrix:
1 0 1
0 1 0
1 0 1
```

**Output**: 1  
**Explanation**: The four corners of the entire matrix form a valid submatrix.

## Approach

### Row Pair Method

For each pair of rows (r1, r2):
1. Find all columns where both rows have 1s
2. If there are k such columns, we can form C(k,2) rectangles

**Why it works**: Any two columns from the common set, combined with the two rows, form a valid rectangle with all four corners as 1.

### Column Pair Hashing

1. For each row, find all pairs of columns with 1s
2. Use hash map to count occurrences of each column pair
3. For k occurrences, we can form C(k,2) rectangles

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Row Pairs | O(rows² × cols) | O(1) or O(cols) |
| Column Hashing | O(rows × cols²) | O(cols²) |

## Related Problems

1. **All 1s Submatrix**: Count all submatrices filled with 1s
2. **Square Submatrices with All 1s**: Count all square submatrices with all 1s
3. **Maximum Submatrix Sum**: Kadane's algorithm extension

# Sort N Numbers in Range 0 to N²-1 in Linear Time

## Problem Description

Given an array of n numbers where elements are in the range from 0 to n²-1, sort the array in linear time O(n).

**Why standard sorts don't work optimally:**
- Counting Sort would take O(n²) time (range is n²)
- Comparison-based sorts (Merge Sort, Heap Sort) take O(n log n) time

## Examples

### Example 1
- **Input:** `[40, 12, 45, 32, 33, 1, 22]` (n=7, range 0-48)
- **Output:** `[1, 12, 22, 32, 33, 40, 45]`

### Example 2
- **Input:** `[0, 23, 14, 12, 9]` (n=5, range 0-24)
- **Output:** `[0, 9, 12, 14, 23]`

## Algorithm

### Radix Sort with Base n

**Key Insight:** Any number in range [0, n²-1] can be represented using 2 digits in base n.

For example, if n=5:
- 23 in base 5 = 43 (4×5¹ + 3×5⁰)
- 7 in base 5 = 12 (1×5¹ + 2×5⁰)

**Steps:**
1. Perform Counting Sort on the least significant digit (units place in base n)
2. Perform Counting Sort on the most significant digit (n's place in base n)

**Why it works:** 
- Radix Sort is stable
- Two passes are sufficient because max value n²-1 has at most 2 digits in base n
- Each counting sort pass takes O(n) time

## Time & Space Complexity

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Counting Sort | O(n²) | O(n²) |
| Merge/Heap Sort | O(n log n) | O(n) or O(1) |
| **Radix Sort (Base n)** | **O(n)** | **O(n)** |

## Generalization

For range [0, n^p - 1], we need p passes of counting sort.

| Range | Passes Needed |
|-------|--------------|
| [0, n-1] | 1 pass |
| [0, n²-1] | 2 passes |
| [0, n³-1] | 3 passes |

## References

- [GeeksforGeeks - Sort n numbers in range 0 to n²-1](https://www.geeksforgeeks.org/dsa/sort-n-numbers-range-0-n2-1-linear-time/)

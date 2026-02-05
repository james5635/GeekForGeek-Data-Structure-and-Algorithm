# Searching Algorithms

This directory contains 37+ implementations of searching algorithms from GeeksForGeeks, covering various techniques and problem types.

## Directory Structure

### finding_elements/
Algorithms for finding specific elements in arrays:
- **largest_element** - Find the largest element (O(n))
- **second_largest** - Find second largest element (O(n))
- **largest_three** - Find three largest elements (O(n))
- **k_largest_elements** - Find k largest elements (O(n log k))
- **kth_smallest_largest** - Find kth smallest/largest (O(n) avg)
- **kth_largest_stream** - Kth largest in a stream (O(n log k))
- **k_closest_elements** - K closest elements to x (O(log n + k))
- **maximum_pairwise_sum** - Maximum pairwise sum (O(n))
- **ceiling_sorted_array** - Ceiling in sorted array (O(log n))
- **find_peak_element** - Find a peak element (O(log n))

### search_algorithms/
Various search techniques:
- **binary_search_pivoted** - Search in pivoted sorted array (O(log n))
- **search_almost_sorted** - Search in almost sorted array (O(log n))
- **search_infinite_array** - Search in infinite sorted array (O(log p))
- **sentinel_linear_search** - Sentinel linear search (O(n))
- **meta_binary_search** - Meta/binary search (O(log n))
- **ternary_search** - Ternary search (O(log₃ n))
- **jump_search** - Jump search (O(√n))
- **interpolation_search** - Interpolation search (O(log log n) avg)
- **exponential_search** - Exponential search (O(log n))
- **fibonacci_search** - Fibonacci search (O(log n))

### missing_repeating/
Find missing or repeating numbers:
- **find_missing_number** - Find missing number 1 to N (O(n))
- **first_repeating_element** - First repeating element (O(n))
- **repeating_and_missing** - Repeating and missing numbers (O(n))
- **count_1s_binary_array** - Count 1s in sorted binary array (O(log n))
- **missing_number_ap** - Missing number in arithmetic progression (O(log n))

### matrix_sorted/
Matrix-related searching:
- **kth_smallest_sorted_matrix** - Kth smallest in sorted matrix (O(n log(max-min)))

### array_properties/
Algorithms exploiting array properties:
- **common_elements_three_arrays** - Common elements in three sorted arrays (O(n))
- **find_fixed_point** - Find fixed point (O(log n))
- **find_partition_point** - Find partition point (O(n))
- **majority_element** - Majority element using Moore's Voting (O(n))
- **max_bitonic_element** - Maximum in bitonic array (O(log n))

### sum_problems/
Sum-related problems:
- **two_sum_closest_zero** - Two elements with sum closest to zero (O(n log n))
- **three_sum_zero** - Triplets with sum zero (O(n²))
- **pair_sum_sorted_rotated** - Pair sum in sorted rotated array (O(n))

### median_closest/
Median and closest element problems:
- **closest_pair_sum** - Closest pair sum from two arrays (O(m + n))
- **median_two_sorted** - Median of two sorted arrays (O(log n))
- **median_two_sorted_different** - Median of different size arrays (O(log(min(m,n))))

## Quick Reference by Complexity

### O(1) Space, O(n) Time
- Largest Element
- Second Largest
- Largest Three
- Maximum Pairwise Sum
- Majority Element

### O(log n) Time
- Binary Search (Pivoted)
- Search Almost Sorted
- Find Peak Element
- Ceiling in Sorted Array
- Find Fixed Point
- Maximum in Bitonic Array
- Count 1s in Binary Array

### O(n) Time (Linear)
- First Repeating Element
- Find Missing Number
- Common Elements Three Arrays
- Find Partition Point
- Pair Sum in Sorted Rotated

### Heap/Order Statistics (O(n log k))
- K Largest Elements
- Kth Largest in Stream
- K Closest Elements

### Matrix/Advanced
- Kth Smallest in Sorted Matrix
- Median of Two Sorted Arrays

## How to Use

Each algorithm directory contains:
- `solution.py` - Implementation with test cases
- `README.md` - Problem description and complexity analysis

Example:
```bash
cd searching/finding_elements/largest_element
python solution.py
```

Or import in your code:
```python
from searching.finding_elements.largest_element.solution import find_largest_element

arr = [10, 20, 4, 45, 99]
result = find_largest_element(arr)
print(result)  # 99
```

## Running All Tests

```bash
cd /home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/searching
find . -name "solution.py" -exec python {} \;
```

## Topics Covered

1. **Basic Searching** - Linear and binary search variations
2. **Sorted Array Searching** - Binary search on rotated, infinite arrays
3. **Element Finding** - Kth largest, closest elements, peaks
4. **Missing/Repeating** - Mathematical and XOR approaches
5. **Matrix Search** - Searching in 2D sorted matrices
6. **Sum Problems** - Two sum, three sum variations
7. **Median Problems** - Finding median in complex scenarios
8. **Specialized Search** - Ternary, jump, interpolation, Fibonacci

## References

All implementations are based on GeeksForGeeks DSA Tutorial:
https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/

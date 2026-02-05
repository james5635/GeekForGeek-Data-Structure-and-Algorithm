# Sorting Algorithms

This directory contains 52+ implementations of sorting-based algorithms from GeeksForGeeks, organized by difficulty level.

## Directory Structure

### easy/ (19 algorithms)
Basic sorting problems and array manipulation:

**Array Validation & Basic Operations:**
- **check_array_sorted** - Check if array is sorted (O(n))
- **sort_two_types_elements** - Sort array with two types of elements (O(n))
- **sort_string_characters** - Sort characters in a string (O(n))
- **sort_given_matrix** - Sort matrix elements (O(mn log(mn)))
- **sort_wave_form** - Sort array in wave form (O(n))

**Set Bits & String Operations:**
- **sort_by_set_bits** - Sort by count of set bits (O(n log n))
- **sort_strings_by_length** - Sort strings by length (O(n log n))
- **sort_even_odd_places** - Even indices increasing, odd decreasing (O(n log n))

**Range & Interval Problems:**
- **check_interval_overlap** - Check if intervals overlap (O(n log n))
- **find_missing_elements_range** - Find missing elements in range (O(n))
- **merge_two_sorted_arrays** - Merge two sorted arrays (O(n+m))
- **sort_two_halves_sorted** - Sort array with two sorted halves (O(n))

**Searching in Sorted Arrays:**
- **pair_sum_sorted_array** - Pair with given sum (O(n))
- **intersection_sorted_arrays** - Intersection of two sorted arrays (O(n+m))
- **union_sorted_arrays** - Union of two sorted arrays (O(n+m))
- **meeting_rooms** - Check if person can attend all meetings (O(n log n))

**Specialized Sorting:**
- **sort_different_machines** - Sort numbers from different machines (O(N log k))
- **sort_linked_list** - Sort a singly linked list (O(n log n))
- **kth_smallest_removing** - K-th smallest after removing integers (O(n log n))

### medium/ (23 algorithms)
Intermediate sorting problems with various techniques:

**Frequency & Distribution:**
- **sort_by_frequency** - Sort elements by frequency (O(n log n))
- **min_increment_unique** - Min increments to make array unique (O(n log n))
- **chocolate_distribution** - Minimize max-min difference (O(n log n))
- **min_max_buy_candies** - Min/max amount to buy N candies (O(n log n))

**Interval Problems:**
- **merge_intervals** - Merge overlapping intervals (O(n log n))
- **max_intervals_overlap** - Find point with maximum overlap (O(n log n))
- **min_platforms_required** - Min platforms for trains/buses (O(n log n))

**Partitioning & Flag Algorithms:**
- **three_way_partitioning** - Partition around a range (O(n))
- **sort_0s_1s_2s** - Dutch National Flag problem (O(n))
- **sort_linked_list_012** - Sort linked list with 0s, 1s, 2s (O(n))

**Counting & Inversions:**
- **inversion_count** - Count inversions using merge sort (O(n log n))
- **k_largest_smallest** - Find k largest/smallest (O(n) avg)

**Sum Problems:**
- **triplet_given_sum** - Find triplet with given sum (O(n²))
- **triplet_sum_closest** - Triplet with sum closest to target (O(n²))
- **smallest_diff_triplet** - Smallest difference triplet from 3 arrays (O(n log n))
- **four_sum_quadruplet** - Find quadruplet with given sum (O(n³))

**Advanced Sorting:**
- **merge_k_sorted_arrays** - Merge k sorted arrays (O(n log k))
- **min_unsorted_subarray** - Min length subarray to sort (O(n))
- **nearly_sorted** - Sort nearly sorted array (O(n log k))
- **sort_range_0_to_n2** - Sort range [0, n²-1] (O(n))
- **sort_1_to_n** - Sort array containing 1 to n (O(n))
- **sort_by_another_array** - Sort by order of another array (O(m log m + n))
- **permute_two_arrays** - Check if permutations satisfy condition (O(n log n))

### hard/ (10 algorithms)
Advanced sorting problems requiring sophisticated techniques:

**Space-Optimized & Merge Problems:**
- **merge_sorted_o1_space** - Merge sorted arrays O(1) space (O(n log n))
- **k_most_frequent** - K most frequent elements (O(n log k))

**N-Sum Problems:**
- **unique_triplets_sum** - Unique triplets with given sum (O(n²))
- **four_elements_sum** - Four elements sum to value (O(n³))
- **four_sum_closest** - Quadruplet with closest sum (O(n³))

**Advanced Counting:**
- **surpasser_count** - Surpasser count of each element (O(n log n))
- **min_subsets_consecutive** - Min subsets of consecutive numbers (O(n log n))
- **min_swaps_permuted** - Min swaps for permuted array (O(n))

**Geometric & Special Sorting:**
- **sort_by_equation** - Sort by applying given equation (O(n log n))
- **closest_pair_points** - Closest pair of points (O(n log n))

## Quick Reference by Technique

### Two Pointer Technique
- pair_sum_sorted_array
- intersection_sorted_arrays
- union_sorted_arrays
- triplet_given_sum
- triplet_sum_closest

### Merge Sort Variants
- inversion_count
- merge_k_sorted_arrays
- merge_two_sorted_arrays
- merge_sorted_o1_space

### Dutch National Flag
- sort_two_types_elements
- sort_0s_1s_2s
- three_way_partitioning
- sort_linked_list_012

### Heap-Based
- k_largest_smallest
- k_most_frequent
- merge_k_sorted_arrays
- nearly_sorted

### Binary Search on Answer
- sort_range_0_to_n2
- kth_smallest_removing
- find_missing_elements_range

### Greedy with Sorting
- min_increment_unique
- chocolate_distribution
- min_max_buy_candies
- meeting_rooms
- permute_two_arrays

### Divide and Conquer
- closest_pair_points
- merge_sorted_o1_space
- surpasser_count

## How to Use

Each algorithm directory contains:
- `solution.py` - Implementation with test cases
- `README.md` - Problem description and complexity analysis

Example:
```bash
cd sorting/medium/merge_intervals
python solution.py
```

Or import in your code:
```python
from sorting.medium.merge_intervals.solution import merge_intervals

intervals = [[1,3], [2,6], [8,10], [15,18]]
result = merge_intervals(intervals)
print(result)  # [[1,6], [8,10], [15,18]]
```

## Complexity Summary

| Category | Count | Typical Time Complexity |
|----------|-------|------------------------|
| Easy | 19 | O(n) to O(n log n) |
| Medium | 23 | O(n log n) to O(n²) |
| Hard | 10 | O(n log n) to O(n³) |

## Topics Covered

1. **Basic Sorting** - Array validation, simple sorts
2. **Two Pointer** - Pair sum, intersection, union
3. **Merge Operations** - Merge k arrays, intervals
4. **Partitioning** - Dutch National Flag, 3-way partition
5. **Frequency Based** - Sort by frequency, counting
6. **Interval Problems** - Merge, overlap, platforms
7. **Sum Problems** - 2-sum, 3-sum, 4-sum variations
8. **Space Optimization** - O(1) space merges
9. **Geometric** - Closest pair of points
10. **Distribution** - Chocolate, candies problems

## References

All implementations are based on GeeksForGeeks DSA Tutorial:
https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/

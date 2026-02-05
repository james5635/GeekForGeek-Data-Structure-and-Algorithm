# Hashing Algorithms

This directory contains 50+ implementations of hashing-based algorithms from GeeksForGeeks, organized by difficulty level. Hashing is a fundamental technique for efficient data retrieval and pattern matching.

## Directory Structure

### easy/ (18 algorithms)
Basic hashing problems for set operations and frequency counting:

**Set Operations:**
- **array_is_subset** - Check if array is subset of another (O(n))
- **check_sets_disjoint** - Check if two sets are disjoint (O(n))
- **union_intersection_sorted** - Union and intersection of sorted arrays (O(n+m))
- **union_intersection_unsorted** - Union and intersection of unsorted arrays (O(n+m))
- **min_subsets_distinct** - Minimum subsets with distinct elements (O(n))
- **min_removals_no_common** - Min removals for no common elements (O(n))

**Pair Problems:**
- **pair_with_given_sum** - Check if pair with given sum exists (O(n))
- **count_pairs_given_sum** - Count pairs with given sum (O(n))
- **count_pairs_diff_k** - Count pairs with difference k (O(n))

**Element Properties:**
- **check_numbers_equal** - Check equality without arithmetic operators (O(1))
- **fizz_buzz** - Classic FizzBuzz implementation (O(n))
- **max_distance_same_element** - Max distance between same elements (O(n))
- **duplicate_within_k** - Check duplicates within k distance (O(n))
- **frequent_element** - Find most frequent element (O(n))
- **find_repetitive_element** - Find repetitive element in 1..n-1 (O(n))

**Missing Elements:**
- **missing_elements_range** - Find missing elements in range (O(n))
- **missing_elements_1_to_n** - Find missing elements from 1 to n (O(n))

**Geometry:**
- **max_points_same_line** - Max points on same line (O(n²))

### medium/ (18 algorithms)
Intermediate hashing with subarrays, windows, and complex patterns:

**Divisibility & Sums:**
- **count_pairs_sum_divisible_k** - Count pairs with sum divisible by k (O(n))
- **subarray_sum_divisible_k** - Count subarrays with sum divisible by k (O(n))
- **count_triplets_given_sum** - Count triplets with given sum (O(n²))
- **triplets_zero_sum** - Find all triplets with zero sum (O(n²))
- **count_pairs_a_plus_b_k** - Count pairs where a + b = k (O(n))

**Subarray Problems:**
- **subarray_zero_sum** - Check if subarray with 0 sum exists (O(n))
- **subarray_given_sum** - Find subarray with given sum (O(n))
- **smallest_subarray_k_distinct** - Smallest subarray with k distinct (O(n))
- **count_distinct_window** - Count distinct elements in every window (O(n))

**Sequences & Subsets:**
- **longest_consecutive_subsequence** - Longest consecutive subsequence (O(n))
- **largest_fibonacci_subset** - Largest Fibonacci subset (O(n))
- **partition_consecutive_subsets** - Partition into consecutive subsets (O(n log n))

**String & Word Problems:**
- **group_words_same_chars** - Group words with same characters (O(n * k log k))
- **min_insertions_palindrome** - Min insertions for palindrome (O(n²))

**Data Structures:**
- **data_structure_o1** - O(1) insert, delete, search, getRandom
- **reconstruct_itinerary** - Reconstruct itinerary from tickets (O(E log E))
- **employees_under_every_employee** - Count employees under each manager (O(n))
- **kth_distinct_element** - Find kth distinct element (O(n))

### hard/ (14 algorithms)
Advanced hashing with complex patterns and optimizations:

**N-Sum Problems:**
- **count_quadruplets_given_sum** - Count quadruplets with given sum (O(n²))
- **four_elements_sum** - Four elements sum to given value (O(n²))
- **four_sum_four_arrays** - 4Sum from four sorted arrays (O(n²))

**Subarray & Span Problems:**
- **largest_subarray_equal_0s_1s** - Largest subarray with equal 0s and 1s (O(n))
- **longest_span_two_arrays** - Longest span with same sum (O(n))
- **count_subarrays_distinct** - Count subarrays with distinct elements (O(n))
- **sum_unique_subarray_sums** - Sum of all unique subarray sums (O(n²))

**Mathematical & Special Sequences:**
- **fraction_to_string** - Fraction to recurring decimal string (O(n))
- **recamans_sequence** - Recaman's sequence (O(n))
- **longest_bitonic_subsequence** - Longest strictly bitonic subsequence (O(n²))

**String Algorithms:**
- **palindrome_substring_queries** - Palindrome substring queries (O(n) or O(n²))

**Tree & Matrix:**
- **identical_duplicate_subtrees** - Find duplicate subtrees in binary tree (O(n))
- **submatrix_corners_1** - Submatrix with corners as 1 (O(m² * n))

**Array Construction:**
- **maximum_array_two_arrays** - Maximum array from two arrays (O(n))

## Quick Reference by Technique

### Hash Set Applications
- union_intersection_sorted/unsorted
- check_sets_disjoint
- longest_consecutive_subsequence
- count_subarrays_distinct
- largest_fibonacci_subset

### Hash Map / Dictionary Applications
- pair_with_given_sum
- count_pairs_given_sum
- subarray_given_sum
- subarray_zero_sum
- max_distance_same_element
- frequent_element

### Prefix Sum + Hashing
- subarray_sum_divisible_k
- largest_subarray_equal_0s_1s
- longest_span_two_arrays
- subarray_given_sum

### Sliding Window + Hashing
- count_distinct_window
- smallest_subarray_k_distinct
- duplicate_within_k

### Two Pointer + Hashing
- triplets_zero_sum
- count_triplets_given_sum
- partition_consecutive_subsets

### Rolling Hash / String Hashing
- palindrome_substring_queries
- group_words_same_chars

## How to Use

Each algorithm directory contains:
- `solution.py` - Implementation with test cases
- `README.md` - Problem description and complexity analysis

Example:
```bash
cd hashing/medium/subarray_given_sum
python solution.py
```

Or import in your code:
```python
from hashing.medium.subarray_given_sum.solution import find_subarray_with_sum

arr = [1, 4, 20, 3, 10, 5]
target = 33
result = find_subarray_with_sum(arr, target)
print(result)  # [2, 4] (subarray [20, 3, 10])
```

## Complexity Summary

| Category | Count | Typical Time Complexity |
|----------|-------|------------------------|
| Easy | 18 | O(n) to O(n²) |
| Medium | 18 | O(n) to O(n²) |
| Hard | 14 | O(n) to O(n²) |

## Topics Covered

1. **Set Operations** - Union, intersection, subset, disjoint
2. **Pair Problems** - Two sum, difference, divisibility
3. **Subarray Problems** - Zero sum, given sum, distinct elements
4. **Frequency Counting** - Most frequent, distinct elements
5. **Missing Elements** - Finding gaps in sequences
6. **Window Problems** - Sliding window with hash sets
7. **N-Sum Problems** - 2-sum, 3-sum, 4-sum variations
8. **Sequence Problems** - Consecutive, Fibonacci, bitonic
9. **String Hashing** - Palindrome queries, word grouping
10. **Special Patterns** - Recaman's sequence, duplicate subtrees

## Key Hashing Concepts

### When to Use Hashing
- **O(1) Lookup:** When you need fast element existence check
- **Frequency Counting:** Counting occurrences of elements
- **Pair Matching:** Finding complementary elements
- **Duplicate Detection:** Checking for duplicates efficiently
- **Prefix Patterns:** Tracking prefix sums or states

### Common Patterns
1. **Hash Set** - For existence checks and uniqueness
2. **Hash Map** - For frequency counting and mapping
3. **Prefix Sum + Hash Map** - For subarray problems
4. **Rolling Hash** - For string pattern matching

### Time vs Space Trade-off
Hashing typically trades space for time:
- **Without hashing:** O(n²) time, O(1) space
- **With hashing:** O(n) time, O(n) space

## References

All implementations are based on GeeksForGeeks DSA Tutorial:
https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/

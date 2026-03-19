# Deque Data Structure - GeeksforGeeks Implementations

This folder contains Python implementations of Deque-based algorithms and data structures from GeeksforGeeks DSA tutorials.

## Table of Contents

| # | File | Topic | Time Complexity |
|---|------|-------|-----------------|
| 1 | [01_min_max_difference.py](01_min_max_difference.py) | Minimize Max Adjacent Difference | O(n) |
| 2 | [02_max_freq_substring.py](02_max_freq_substring.py) | Max Frequency Substring | O(n log n) |
| 3 | [03_prefix_suffix_length.py](03_prefix_suffix_length.py) | Prefix-Suffix Lengths | O(n²) |
| 4 | [04_spiral_level_order.py](04_spiral_level_order.py) | Spiral Level Order Traversal | O(n) |
| 5 | [05_backspace_string.py](05_backspace_string.py) | Backspace String Processing | O(n) |
| 6 | [06_sequence_from_string.py](06_sequence_from_string.py) | Sequence from String Positions | O(n) |
| 7 | [07_largest_permutation.py](07_largest_permutation.py) | Largest Permutation at Ends | O(n) |
| 8 | [08_strings_equal_insert.py](08_strings_equal_insert.py) | Strings Equal by Insertion | O(n) |
| 9 | [09_rearrange_linked_list.py](09_rearrange_linked_list.py) | Rearrange Linked List | O(n) |
| 10 | [10_stack_queue_deque.py](10_stack_queue_deque.py) | Stack & Queue using Deque | O(1) ops |
| 11 | [11_bitonic_sequence.py](11_bitonic_sequence.py) | Generate Bitonic Sequence | O(n) |
| 12 | [12_rearrange_queries.py](12_rearrange_queries.py) | Array Rearrange Queries | O(q) |
| 13 | [13_longest_subarray_diff.py](13_longest_subarray_diff.py) | Longest Subarray with Diff ≤ X | O(n) |
| 14 | [14_reverse_linked_groups.py](14_reverse_linked_groups.py) | Reverse Linked List Groups | O(n) |
| 15 | [15_max_sum_subsequence.py](15_max_sum_subsequence.py) | Max Sum Subsequence K-Distant | O(n) |
| 16 | [16_nth_term_recurrence.py](16_nth_term_recurrence.py) | Nth Term of Recurrence | O(n) |
| 17 | [17_max_equal_subarray.py](17_max_equal_subarray.py) | Max Equal Elements Subarray | O(n) |
| 18 | [18_lexicographically_largest_string.py](18_lexicographically_largest_string.py) | Largest String K Removals | O(n) |
| 19 | [19_segregate_even_odd_linked.py](19_segregate_even_odd_linked.py) | Segregate Even/Odd Linked List | O(n) |
| 20 | [20_permutation_k_differences.py](20_permutation_k_differences.py) | Permutation with K Differences | O(n) |
| 21 | [21_01_bfs.py](21_01_bfs.py) | 0-1 BFS Shortest Path | O(V+E) |
| 22 | [22_min_deques_sorted.py](22_min_deques_sorted.py) | Min Deques for Sorted Array | O(n³) |
| 23 | [23_min_number_ops.py](23_min_number_ops.py) | Min Number by + and * Ops | O(2^n) |
| 24 | [24_deque_circular_array.py](24_deque_circular_array.py) | Deque using Circular Array | O(1) |
| 25 | [25_deque_linked_list.py](25_deque_linked_list.py) | Deque using Doubly Linked List | O(1) |

---

## Algorithm Details

### Deque Implementations

| File | Approach | Operations |
|------|----------|------------|
| 24_deque_circular_array.py | Circular Array | O(1) insert/delete front/rear |
| 25_deque_linked_list.py | Doubly Linked List | O(1) insert/delete front/rear |

### Sliding Window Problems

| File | Problem | Approach |
|------|---------|----------|
| 01_min_max_difference.py | Minimize max adjacent diff | Sliding window + deque |
| 02_max_freq_substring.py | Max frequency substring K | HashMap + sliding window |
| 13_longest_subarray_diff.py | Longest subarray with diff ≤ X | Dual deques (min/max) |
| 17_max_equal_subarray.py | Max equal elements with K increments | Sliding window |

### Linked List Problems

| File | Problem | Approach |
|------|---------|----------|
| 09_rearrange_linked_list.py | Alternate first-last | Deque-based |
| 14_reverse_linked_groups.py | Reverse K groups | Deque swap |
| 19_segregate_even_odd_linked.py | Even/odd segregation | Deque |

### String Problems

| File | Problem | Approach |
|------|---------|----------|
| 05_backspace_string.py | Process backspace chars | Deque |
| 08_strings_equal_insert.py | Check equality by 1 insert | Two-pointer |
| 18_lexicographically_largest_string.py | Largest string K removals | Greedy stack |

### BFS & Graph

| File | Problem | Approach |
|------|---------|----------|
| 21_01_bfs.py | 0-1 BFS shortest path | Deque (appendleft for 0, append for 1) |

### Miscellaneous

| File | Problem | Approach |
|------|---------|----------|
| 03_prefix_suffix_length.py | Prefix-suffix matching | String comparison |
| 04_spiral_level_order.py | Spiral level order | Deque alternating |
| 06_sequence_from_string.py | Sequence from F/B | Deque |
| 07_largest_permutation.py | Largest permutation | Deque compare |
| 10_stack_queue_deque.py | Stack/Queue using Deque | Custom implementation |
| 11_bitonic_sequence.py | Generate bitonic | Deque |
| 12_rearrange_queries.py | Array queries | Deque rotation |
| 15_max_sum_subsequence.py | Max sum with K distance | DP + deque |
| 16_nth_term_recurrence.py | Nth term product K | Rolling product deque |
| 20_permutation_k_differences.py | K unique differences | Deque |
| 22_min_deques_sorted.py | Min deques sorted | Greedy |
| 23_min_number_ops.py | Min by +/* ops | Bitmask enumeration |

---

## Topics Covered

- Deque implementations (Circular Array, Doubly Linked List)
- Sliding window maximum/minimum patterns
- 0-1 BFS shortest path algorithm
- Linked list manipulation with deque
- String processing with backspace
- Monotonic deque patterns
- Dynamic programming with deque optimization
- Spiral tree traversal
- Array queries and rearrangements

---

## Usage

```bash
# Run individual test
python Deque/01_min_max_difference.py
python Deque/21_01_bfs.py

# Run all tests
for file in Deque/*.py; do python "$file"; done
```

---

## References

- [GeeksforGeeks Deque Data Structure](https://www.geeksforgeeks.org/deque-data-structure/)
- [GeeksforGeeks 0-1 BFS](https://www.geeksforgeeks.org/dsa/0-1-bfs-shortest-path-binary-graph/)
- [GeeksforGeeks DSA Tutorial](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)

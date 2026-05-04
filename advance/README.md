# Advance Data Structures & Algorithms

Collection of advanced algorithm implementations from [GeeksforGeeks](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/).

## Algorithms

### Trie

| File | Algorithm | Description | Source |
|------|-----------|-------------|--------|
| `trie_insert_search.py` | Trie Insert and Search | Insert words and search in a Trie | [Link](https://www.geeksforgeeks.org/dsa/trie-insert-and-search/) |
| `trie_delete.py` | Trie Delete | Delete a word from Trie with all conditions | [Link](https://www.geeksforgeeks.org/dsa/trie-delete/) |
| `boggle_using_trie.py` | Boggle Using Trie | Find all words in Boggle board using Trie | [Link](https://www.geeksforgeeks.org/dsa/boggle-using-trie/) |
| `prefix_match_count.py` | Prefix Match Count | Count strings with given prefix of length k | [Link](https://www.geeksforgeeks.org/dsa/count-of-strings-whose-prefix-match-with-the-given-string-to-a-given-length-k/) |
| `palindrome_pair.py` | Palindrome Pair | Find palindrome pairs in array of words | [Link](https://www.geeksforgeeks.org/dsa/palindrome-pair-in-an-array-of-words-or-strings/) |
| `camelcase_pattern_matching.py` | CamelCase Pattern Matching | Match CamelCase patterns against dictionary | [Link](https://www.geeksforgeeks.org/dsa/camelcase-pattern-matching/) |
| `common_prefix_suffix_count.py` | Common Prefix-Suffix Count | Count common prefix/suffix strings in two lists | [Link](https://www.geeksforgeeks.org/dsa/counting-common-prefix-suffix-strings-in-two-lists/) |
| `longest_common_prefix.py` | Longest Common Prefix | Find LCP using word-by-word matching | [Link](https://www.geeksforgeeks.org/dsa/longest-common-prefix-using-word-by-word-matching/) |
| `assign_usernames_trie.py` | Assign Usernames Using Trie | Assign unique usernames with Trie | [Link](https://www.geeksforgeeks.org/dsa/program-for-assigning-usernames-using-trie/) |

### Matrix & Directory

| File | Algorithm | Description | Source |
|------|-----------|-------------|--------|
| `print_unique_rows.py` | Print Unique Rows | Print unique rows in a binary matrix | [Link](https://www.geeksforgeeks.org/dsa/print-unique-rows/) |
| `duplicate_rows_binary_matrix.py` | Duplicate Rows in Binary Matrix | Find duplicate rows using HashSet/Trie | [Link](https://www.geeksforgeeks.org/dsa/find-duplicate-rows-binary-matrix/) |
| `phone_directory.py` | Phone Directory | Implement a phone directory using Trie | [Link](https://www.geeksforgeeks.org/dsa/implement-a-phone-directory/) |

### Segment Tree & Sparse Table

| File | Algorithm | Description | Source |
|------|-----------|-------------|--------|
| `segment_tree_rmq.py` | Segment Tree RMQ | Range Minimum Query using Segment Tree | [Link](https://www.geeksforgeeks.org/dsa/segment-tree-range-minimum-query/) |
| `sparse_table.py` | Sparse Table | RMQ and GCD queries using Sparse Table | [Link](https://www.geeksforgeeks.org/dsa/sparse-table/) |
| `sparse_table_range_sum.py` | Sparse Table Range Sum | Range sum queries using Sparse Table | [Link](https://www.geeksforgeeks.org/dsa/range-sum-query-using-sparse-table/) |
| `range_minimum_query.py` | Range Minimum Query | Static array RMQ using Sparse Table | [Link](https://www.geeksforgeeks.org/dsa/range-minimum-query-for-static-array/) |
| `range_lcm_queries.py` | Range LCM Queries | Range LCM queries using Segment Tree | [Link](https://www.geeksforgeeks.org/dsa/range-lcm-queries/) |
| `merge_sort_tree.py` | Merge Sort Tree | Range order statistics using Merge Sort Tree | [Link](https://www.geeksforgeeks.org/dsa/merge-sort-tree-for-range-order-statistics/) |

### SQRT Decomposition & Mo's Algorithm

| File | Algorithm | Description | Source |
|------|-----------|-------------|--------|
| `sqrt_decomposition.py` | SQRT Decomposition | Range sum with updates using block decomposition | [Link](https://www.geeksforgeeks.org/dsa/square-root-sqrt-decomposition-algorithm/) |
| `mos_algorithm.py` | Mo's Algorithm | Range query using SQRT decomposition | [Link](https://www.geeksforgeeks.org/dsa/mos-algorithm-query-square-root-decomposition-set-1-introduction/) |

### Array Problems

| File | Algorithm | Description | Source |
|------|-----------|-------------|--------|
| `smallest_subarray_gcd.py` | Smallest Subarray with Given GCD | Find smallest subarray with given GCD | [Link](https://www.geeksforgeeks.org/dsa/smallest-subarray-with-given-gcd/) |
| `minimum_xor_pair.py` | Minimum XOR Value Pair | Find pair with minimum XOR value | [Link](https://www.geeksforgeeks.org/dsa/minimum-xor-value-pair/) |
| `count_based_abs_diff.py` | Count Based Absolute Difference | Count elements with absolute difference condition | [Link](https://www.geeksforgeeks.org/dsa/count-based-absolute-difference-for-array-element/) |
| `min_jumps_to_end.py` | Minimum Jumps to End | Min number of jumps to reach end of array | [Link](https://www.geeksforgeeks.org/dsa/minimum-number-of-jumps-to-reach-end-of-a-given-array/) |
| `max_value_array_rotation.py` | Max Value with Array Rotation | Max sum of i*arr[i] with rotations | [Link](https://www.geeksforgeeks.org/dsa/find-maximum-value-of-sum-iarri-with-only-rotations-on-given-array-allowed/) |

### Bit Manipulation

| File | Algorithm | Description | Source |
|------|-----------|-------------|--------|
| `space_optimization_bit.py` | Space Optimization Using Bits | Optimize space using bit manipulations | [Link](https://www.geeksforgeeks.org/competitive-programming/space-optimization-using-bit-manipulations/) |

## Running Tests

Each file includes example usage and test cases in the `__main__` block. Run any file directly:

```bash
python advance/trie_insert_search.py
python advance/segment_tree_rmq.py
```

## Categories

- **Trie**: Insert, search, delete, and advanced Trie applications
- **Segment Tree**: Range queries (min, sum, LCM) and Merge Sort Tree
- **Sparse Table**: O(1) range queries for static arrays
- **SQRT Decomposition**: Block-based range queries and updates
- **Mo's Algorithm**: Offline range query algorithm
- **Array Problems**: Various array manipulation algorithms
- **Bit Manipulation**: Space optimization techniques

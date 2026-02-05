# String Algorithms

This folder contains Python implementations of string algorithms from [GeeksforGeeks DSA Tutorial](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/).

## Table of Contents

- [Basic Operations](#basic-operations)
- [Easy Problems](#easy-problems)
- [Medium Problems](#medium-problems)
- [Hard Problems](#hard-problems)

---

## Basic Operations

| # | Problem | File | Description |
|---|---------|------|-------------|
| 1 | String Length | `string_length.py` | Calculate the length of a string manually and using built-in methods |
| 2 | Check Strings Equal | `check_strings_equal.py` | Check if two strings are the same |
| 3 | Search Character | `search_character.py` | Find the first occurrence of a character in a string |
| 4 | Insert Character | `insert_character.py` | Insert a character at a given position in a string |
| 5 | Remove Character at Position | `remove_character_position.py` | Remove a character from a specific position |
| 6 | Remove All Occurrences | `remove_all_occurrences.py` | Remove all occurrences of a character from a string |
| 7 | Concatenate Strings | `concatenate_strings.py` | Join two strings together |
| 8 | Reverse String | `reverse_string.py` | Reverse a string using multiple approaches |
| 9 | Generate All Substrings | `generate_all_substrings.py` | Generate all possible substrings of a string |

---

## Easy Problems

| # | Problem | File | Description |
|---|---------|------|-------------|
| 1 | Check Binary String | `check_binary_string.py` | Check if a string contains only '0' and '1' |
| 2 | Camel Case | `camel_case.py` | Convert a sentence to camelCase format |
| 3 | Count Binary Substrings | `count_binary_substrings.py` | Count substrings that start and end with '1' |
| 4 | Pangram Check | `pangram_check.py` | Check if a string contains all 26 alphabets |
| 5 | Palindrome String | `palindrome_string.py` | Check if a string reads the same forwards and backwards |
| 6 | Check Substring | `check_substring.py` | Check if one string is a substring of another |
| 7 | Check Subsequence | `check_subsequence.py` | Check if one string is a subsequence of another |
| 8 | Check Anagram | `check_anagram.py` | Check if two strings are anagrams of each other |
| 9 | Check K-Anagrams | `check_k_anagrams.py` | Check if two strings are k-anagrams |
| 10 | URLify String | `urlify_string.py` | Replace spaces with '%20' |

---

## Medium Problems

| # | Problem | File | Description |
|---|---------|------|-------------|
| 1 | First Repeated Character | `first_repeated_char.py` | Find the first repeated character in a string |
| 2 | First Non-Repeating Character | `first_non_repeating_char.py` | Find the first non-repeating character |
| 3 | Check String Rotations | `check_string_rotations.py` | Check if two strings are rotations of each other |
| 4 | Kth Non-Repeating Character | `kth_non_repeating_char.py` | Find the kth non-repeating character |
| 5 | ATOI Implementation | `atoi_implementation.py` | Implement the atoi function (string to integer) |
| 6 | Validate IP Address | `validate_ip_address.py` | Check if a string is a valid IPv4/IPv6 address |
| 7 | Add Binary Strings | `add_binary_strings.py` | Add two binary strings |
| 8 | Multiply Two Strings | `multiply_strings.py` | Multiply two numbers represented as strings |
| 9 | Check Isomorphic | `check_isomorphic.py` | Check if two strings are isomorphic |
| 10 | Remove Adjacent Duplicates | `remove_adjacent_duplicates.py` | Remove all adjacent duplicate characters |
| 11 | Roman to Integer | `roman_to_integer.py` | Convert Roman numerals to integers |
| 12 | Check Interleaving | `check_interleaving.py` | Check if a string is an interleaving of two others |
| 13 | String Permutations | `string_permutations.py` | Generate all permutations of a string |
| 14 | Longest Palindromic Substring | `longest_palindromic_substring.py` | Find the longest palindromic substring |
| 15 | Anagram Substring Search | `anagram_substring_search.py` | Search for all anagram substrings |
| 16 | Binary Strings No Consecutive 1s | `binary_strings_no_consecutive_ones.py` | Generate binary strings without consecutive 1s |
| 17 | Lexicographically Next String | `lexicographically_next_string.py` | Find the next lexicographic string |
| 18 | Split Into Four Strings | `split_into_four_strings.py` | Split string into four distinct strings |
| 19 | Word Break | `word_break.py` | Check if a string can be segmented into dictionary words |
| 20 | Minimum Swaps Bracket Balancing | `min_swaps_bracket_balancing.py` | Minimum swaps to balance brackets |
| 21 | Mobile Numeric Keypad | `mobile_numeric_keypad.py` | Convert sentence to mobile keypad sequence |
| 22 | Shortest Path Print String | `shortest_path_print_string.py` | Shortest path to type a string on screen |

---

## Hard Problems

| # | Problem | File | Description |
|---|---------|------|-------------|
| 1 | Lexicographic Rank | `lexicographic_rank.py` | Find the lexicographic rank of a string |
| 2 | Multiply Large Numbers | `multiply_large_numbers.py` | Multiply very large numbers as strings |
| 3 | Increase LCS Length | `increase_lcs_length.py` | Ways to increase LCS length of two strings by one |
| 4 | Alien Dictionary Order | `alien_dictionary_order.py` | Find character precedence from alien dictionary |
| 5 | Check Anagrams No Extra Space | `check_anagrams_no_extra_space.py` | Check anagrams without using extra space |
| 6 | Make Anagrams No Deletion | `make_anagrams_no_deletion.py` | Make two strings anagrams without deletion |
| 7 | Palindrome Substring Queries | `palindrome_substring_queries.py` | Answer multiple palindrome substring queries |
| 8 | Word Search | `word_search.py` | Search for a word in a 2D grid |
| 9 | Word Search Zigzag | `word_search_zigzag.py` | Word search with zigzag movement allowed |
| 10 | Minimum Bracket Reversals | `min_bracket_reversals.py` | Minimum reversals to balance an expression |
| 11 | Word Wrap | `word_wrap.py` | Optimal word wrapping with minimum cost |
| 12 | Decode String Recursive | `decode_string_recursive.py` | Decode a string with recursive substring counts |

---

## How to Run

Each Python file can be run independently:

```bash
python3 string/<filename>.py
```

For example:

```bash
python3 string/reverse_string.py
python3 string/check_anagram.py
python3 string/word_break.py
```

Each file includes:
- Algorithm implementation with multiple approaches
- Time and space complexity analysis
- Test cases demonstrating the algorithm

---

## Topics Covered

- String manipulation and traversal
- Pattern matching algorithms
- Anagram and palindrome problems
- Substring and subsequence problems
- Dynamic programming on strings
- Backtracking and recursion
- Graph-based string problems
- Mathematical string operations

---

**Total Algorithms Implemented: 54**

*Source: GeeksforGeeks DSA Tutorial - String Section*
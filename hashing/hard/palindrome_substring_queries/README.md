# Palindrome Substring Queries

## Problem Description

Given a string `s` and multiple queries, where each query specifies a substring range `[left, right]`. For each query, determine if the substring `s[left..right]` is a palindrome.

## Examples

- **Input**:  
  s = "abaaabaaaba"  
  queries = [[0, 10], [5, 8], [2, 5], [5, 9]]  
  **Output**: [1, 0, 0, 1]  
  **Explanation**: 
  - [0, 10]: "abaaabaaaba" is palindrome
  - [5, 8]: "baaa" is not palindrome
  - [2, 5]: "aaab" is not palindrome
  - [5, 9]: "baaab" is palindrome

## Approaches

### 1. Naive Approach (O(q × n))
For each query, check if substring is palindrome using two pointers.

### 2. Rolling Hash / Rabin-Karp (O(n + q))
- Precompute prefix hashes for original and reversed string
- Compare hashes to check palindrome in O(1) per query

### 3. Manacher's Algorithm (O(n + q))
- Preprocess to find longest palindrome centered at each position
- Answer each query in O(1) by checking radius

## Complexity Analysis

| Approach | Preprocessing | Query Time | Space |
|----------|---------------|------------|-------|
| Naive | O(1) | O(n) | O(1) |
| Rolling Hash | O(n) | O(1) | O(n) |
| Manacher | O(n) | O(1) | O(n) |

## Key Insight

A substring `s[l..r]` is a palindrome if and only if it equals its reverse. With preprocessing, we can check this equality in constant time.

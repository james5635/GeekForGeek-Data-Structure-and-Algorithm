# Sort String Characters

## Problem Statement
Given a string, sort its characters in alphabetical order (lexicographical order).

## Approach
### Counting Sort (Optimal)
Since we're dealing with a limited set of characters (26 lowercase English letters), counting sort is most efficient:
1. Count frequency of each character
2. Reconstruct string in alphabetical order using counts

### Built-in Sort
Convert string to list, sort, and join back. Simple but O(n log n).

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Counting Sort | O(n + k) | O(n + k) |
| Built-in Sort | O(n log n) | O(n) |

Where:
- n = length of string
- k = size of alphabet (26 for lowercase English)

## Key Points
- Strings are immutable in Python, so we work with lists
- Counting sort is optimal for limited character sets
- Can be extended to sort by frequency
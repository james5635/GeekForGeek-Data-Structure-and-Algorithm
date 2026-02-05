# Group Words with Same Set of Characters

## Problem Statement

Given a list of words, group words that have the same set of characters. Two words have the same set if they contain exactly the same characters.

## Examples

- **Input:** ["eat", "tea", "tan", "ate", "nat", "bat"]  
  **Output:** [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]  
  **Explanation:** Words grouped by same sorted characters

- **Input:** ["aaa", "aa", "a"]  
  **Output:** [["aaa", "aa", "a"]]  
  **Explanation:** Same character set {'a'}

## Approach

1. **Sort Characters:** Use sorted characters as key for grouping
2. **Hash Map:** Map sorted key to list of words
3. **Variants:** Can also group by character set only (ignoring frequency)

## Complexity Analysis

- **Time Complexity:** O(n * m log m) where n = words, m = max word length
- **Space Complexity:** O(n * m) for storing groups

## Files

- `solution.py` - Contains implementation with test cases

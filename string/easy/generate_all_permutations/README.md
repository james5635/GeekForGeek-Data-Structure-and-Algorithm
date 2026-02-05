# Generate All Permutations

Generate all possible permutations of characters in a given string.

## Problem Description
Given a string, generate all possible permutations of its characters. Handle duplicate characters appropriately to avoid duplicate permutations.

## Time and Space Complexity
- **Time Complexity:** O(n!), where n is the length of the string
- **Space Complexity:** O(n!) for storing all permutations

## Examples
- Input: "abc", Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
- Input: "aab", Output: ["aab", "aba", "baa"] (unique permutations)

## Solution
The solution uses backtracking to generate permutations recursively. For strings with duplicate characters, additional logic is added to avoid duplicate permutations.

## Usage
```python
from solution import generate_permutations, generate_permutations_with_duplicates

# For strings without duplicates
perms = generate_permutations("abc")

# For strings with potential duplicates  
perms = generate_permutations_with_duplicates("aab")
```
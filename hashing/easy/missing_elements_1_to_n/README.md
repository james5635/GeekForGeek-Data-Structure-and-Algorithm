# Find Missing Elements from 1 to N

## Problem

Given an array of size n containing numbers from 1 to n with some numbers missing, find all missing numbers.

## Approach

**Hash Set Approach:** Store all elements in a set, then check 1 to n for missing elements.

**Marking Approach:** Mark indices by making elements negative. Unmarked indices indicate missing elements (O(1) space).

**Sum Approach:** For single missing element, use n*(n+1)/2 formula.

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** 
  - Hash Set: O(n)
  - Marking: O(1) extra space

## Example

```
Input: arr = [1, 3, 5, 6], n = 6
Output: [2, 4]
```

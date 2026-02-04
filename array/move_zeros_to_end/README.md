# Move All Zeros to End of Array

This directory contains implementations of different approaches to move all zeros to the end of an array while maintaining the relative order of non-zero elements.

## Problem Statement

Given an array of integers `arr[]`, move all the `zeros` to the `end` of the array while maintaining the relative order of all `non-zero` elements.

### Examples

**Input:** `arr[] = [1, 2, 0, 4, 3, 0, 5, 0]`  
**Output:** `[1, 2, 4, 3, 5, 0, 0, 0]`  
**Explanation:** There are three 0s that are moved to the end.

**Input:** `arr[] = [10, 20, 30]`  
**Output:** `[10, 20, 30]`  
**Explanation:** No change in array as there are no 0s.

**Input:** `arr[] = [0, 0]`  
**Output:** `[0, 0]`  
**Explanation:** No change in array as there are all 0s.

## Algorithm Approaches

### 1. Naive Approach - Using Temporary Array
- **File:** `naive_approach.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** Creates a temporary array to store non-zero elements first, then fills zeros, and copies back.

### 2. Better Approach - Two Traversals
- **File:** `two_traversals.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - First traversal: Move all non-zero elements to the front
  - Second traversal: Fill remaining positions with zeros

### 3. Optimal Approach - One Traversal
- **File:** `one_traversal.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** Uses two-pointer technique with swapping to move zeros to end in a single pass.

### 4. Library Methods Approach
- **File:** `library_methods.py`
- **Time Complexity:** O(n) to O(n log n) depending on method
- **Space Complexity:** O(n)
- **Description:** Uses Python built-in functions and methods:
  - List comprehension
  - Sort with custom key
  - Filter function

## Usage

Each implementation file can be run independently:

```bash
python naive_approach.py
python two_traversals.py
python one_traversal.py
python library_methods.py
```

All files include comprehensive test cases to demonstrate functionality.

## Key Insights

- **Maintaining Order:** The relative order of non-zero elements must be preserved
- **In-place vs Extra Space:** Some approaches use extra space while others modify in-place
- **Trade-offs:** Choose approach based on space constraints and performance requirements

## Comparison of Approaches

| Approach | Time Complexity | Space Complexity | Traversals | In-place |
|----------|----------------|------------------|------------|----------|
| Naive (Temp Array) | O(n) | O(n) | 3 | No |
| Two Traversals | O(n) | O(1) | 2 | Yes |
| One Traversal | O(n) | O(1) | 1 | Yes |
| Library Methods | O(n) to O(n log n) | O(n) | Varies | No |

The one traversal approach is generally preferred for optimal performance with O(1) space complexity.
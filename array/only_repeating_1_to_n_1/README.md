# Only Repeating Element in Range [1, n-1]

Given an array `arr[]` of size `n` containing elements from `1` to `n-1` (inclusive) with exactly one element appearing twice, find that repeating element.

## Problem Statement

The array has n elements with values from 1 to n-1, meaning exactly one value repeats and all others appear exactly once. Find the repeating element.

### Examples

**Input:** `arr[] = [1, 2, 3, 3, 4]`, n = 5  
**Output:** `3`  
**Explanation:** Range is [1, 4], element 3 appears twice.

**Input:** `arr[] = [1, 1]`, n = 2  
**Output:** `1`  
**Explanation:** Range is [1, 1], element 1 appears twice.

**Input:** `arr[] = [1, 2, 3, 4, 4]`, n = 5  
**Output:** `4`  
**Explanation:** Element 4 appears twice.

## Algorithm Approaches

### 1. Sorting Approach
- **File:** `only_repeating_1_to_n_1.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(1) or O(n)
- **Description:** 
  - Sort the array
  - Scan for adjacent duplicates
  - First duplicate found is the repeating element

### 2. HashSet Approach
- **File:** `only_repeating_1_to_n_1.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** 
  - Use a set to track seen elements
  - Return the element already in the set

### 3. Sum Formula Approach
- **File:** `only_repeating_1_to_n_1.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Calculate expected sum of 1 to n-1
  - Subtract from actual sum
  - Difference is the repeating element

### 4. XOR Approach
- **File:** `only_repeating_1_to_n_1.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - XOR all array elements
  - XOR with all numbers from 1 to n-1
  - Result is the repeating element (others cancel out)

### 5. Floyd's Cycle Detection Approach
- **File:** `only_repeating_1_to_n_1.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Treat array as linked list (value at index i points to index arr[i])
  - Duplicate creates a cycle
  - Use slow and fast pointers to find cycle entry (repeating element)

## Usage

```bash
python only_repeating_1_to_n_1.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Sorting | O(n log n) | O(1) or O(n) | Simple, modifies array |
| HashSet | O(n) | O(n) | Fast, extra space |
| Sum Formula | O(n) | O(1) | Fast, overflow risk |
| XOR | O(n) | O(1) | Fast, no overflow |
| Floyd's Cycle | O(n) | O(1) | Most elegant, no overflow |

## How Floyd's Cycle Detection Works

```
Array: [1, 2, 3, 3, 4]

Treat as linked list where arr[i] points to index arr[i]:
  Index 0 (value 1) → Index 1
  Index 1 (value 2) → Index 2
  Index 2 (value 3) → Index 3
  Index 3 (value 3) → Index 3 (points to itself!)
  Index 4 (value 4) → Index 4

Because value 3 appears twice, there's a cycle at index 3.

Phase 1: Find meeting point using slow and fast pointers
Phase 2: Find entry point of cycle
```

## Mathematical Formulas

### Sum Formula
```
Expected Sum = (n-1) × n / 2
Actual Sum = sum(arr)
Repeating = Actual Sum - Expected Sum
```

### XOR Formula
```
result = 0
for num in arr:
    result ^= num
for i in range(1, n):
    result ^= i
# result = repeating element
```

## Key Insights

- **Pigeonhole Principle:** With n elements and n-1 distinct values, one must repeat
- **Linked List Abstraction:** Floyd's approach creatively treats array as linked list
- **Cycle Detection:** The duplicate creates a cycle in the implicit graph
- **Multiple Optimal Solutions:** XOR and Floyd's both achieve O(n) time, O(1) space

## Edge Cases

- n = 2: Two elements with same value
- Repeating at boundaries (1 or n-1)
- Large arrays: XOR or Floyd's preferred

## References

- [GeeksforGeeks - Find the only repetitive element](https://www.geeksforgeeks.org/find-the-only-repetitive-element-between-1-to-n-1/)

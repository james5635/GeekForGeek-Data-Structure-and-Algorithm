# Sum of All Subarrays

Given an array `arr[]` of size `n`, find the sum of all subarrays of the given array.

## Problem Statement

A subarray is a contiguous part of an array. Calculate the sum of all possible subarrays.

### Examples

**Input:** `arr[] = [1, 2, 3]`  
**Output:** `20`  
**Explanation:** All subarrays are: [1], [1,2], [1,2,3], [2], [2,3], [3]  
Sum = 1 + 3 + 6 + 2 + 5 + 3 = 20

**Input:** `arr[] = [1, 2, 3, 4]`  
**Output:** `50`  
**Explanation:** Sum of all subarrays = 50

**Input:** `arr[] = [5]`  
**Output:** `5`  
**Explanation:** Only one subarray: [5]

## Algorithm Approaches

### 1. Naive Approach - Generate All Subarrays
- **File:** `sum_of_all_subarrays.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - Use nested loops to generate all subarrays
  - Outer loop picks starting point
  - Inner loop extends the subarray and adds to running sum
  - Add each subarray sum to total

### 2. Optimal Approach - Element Contribution Formula
- **File:** `sum_of_all_subarrays.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Key insight: Each element `arr[i]` appears in `(i+1) × (n-i)` subarrays
  - `(i+1)`: Number of ways to choose start index (0 to i)
  - `(n-i)`: Number of ways to choose end index (i to n-1)
  - Sum = Σ(arr[i] × (i+1) × (n-i)) for all i from 0 to n-1

## Usage

```bash
python sum_of_all_subarrays.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple but slow for large n |
| Optimal | O(n) | O(1) | Uses mathematical insight |

## Mathematical Derivation

For an element at index `i` in an array of size `n`:

```
Number of subarrays containing arr[i]:
  = (Choices for start index) × (Choices for end index)
  = (i + 1) × (n - i)

Example for arr = [1, 2, 3], element 2 at index 1:
  - Start can be: index 0 or 1 (2 choices)
  - End can be: index 1 or 2 (2 choices)
  - Total subarrays containing 2: 2 × 2 = 4
  - These are: [2], [1,2], [2,3], [1,2,3]
```

## Key Insights

- **Contribution Counting:** Instead of enumerating subarrays, count how many times each element contributes
- **Range Counting:** For each position, count valid start and end indices
- **Formula Application:** The formula (i+1) × (n-i) can be derived using combinatorics

## Edge Cases

- Empty array: returns 0
- Single element: returns that element
- Negative numbers: formula works correctly
- Large arrays: O(n) approach handles efficiently

## References

- [GeeksforGeeks - Sum of all subarrays](https://www.geeksforgeeks.org/sum-of-all-subarrays/)

# Missing Number

Given an array `arr[]` of size `n-1` containing distinct integers in the range `[1, n]`, find the missing number from the range.

## Problem Statement

An array contains n-1 distinct integers from 1 to n, with exactly one number missing. Find that missing number.

### Examples

**Input:** `arr[] = [1, 2, 4, 5]`, n = 5  
**Output:** `3`  
**Explanation:** The array should contain [1, 2, 3, 4, 5], missing 3.

**Input:** `arr[] = [1, 3]`, n = 3  
**Output:** `2`  
**Explanation:** Missing number is 2.

**Input:** `arr[] = [2, 3, 4, 5]`, n = 5  
**Output:** `1`  
**Explanation:** Missing first number 1.

## Algorithm Approaches

### 1. Naive Approach - Linear Search
- **File:** `missing_number.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Description:** 
  - For each number from 1 to n, search it in the array
  - The number not found is the missing one

### 2. Better Approach - Hashing
- **File:** `missing_number.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:** 
  - Store all array elements in a HashSet
  - Check which number from 1 to n is not in the set

### 3. Optimal Approach 1 - Sum Formula
- **File:** `missing_number.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Use formula: Sum of 1 to n = n × (n + 1) / 2
  - Missing number = Expected sum - Actual sum
  - **Caution:** May cause integer overflow for very large n

### 4. Optimal Approach 2 - XOR
- **File:** `missing_number.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - XOR all numbers from 1 to n
  - XOR all array elements
  - Result is the missing number
  - No overflow risk

## Usage

```bash
python missing_number.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) | Simple but slow |
| Hashing | O(n) | O(n) | Fast but uses extra space |
| Sum Formula | O(n) | O(1) | Fast, risk of overflow |
| XOR | O(n) | O(1) | Fast, no overflow risk |

## Mathematical Formulas

### Sum Formula
```
Expected Sum = n × (n + 1) / 2
Actual Sum = sum(arr)
Missing Number = Expected Sum - Actual Sum
```

### XOR Formula
```
XOR_all = 1 ^ 2 ^ 3 ^ ... ^ n
XOR_arr = arr[0] ^ arr[1] ^ ... ^ arr[n-2]
Missing = XOR_all ^ XOR_arr
```

## How XOR Works

```
Example: arr = [1, 2, 4, 5], n = 5

XOR_all = 1 ^ 2 ^ 3 ^ 4 ^ 5
XOR_arr = 1 ^ 2 ^ 4 ^ 5

Missing = XOR_all ^ XOR_arr
        = (1 ^ 2 ^ 3 ^ 4 ^ 5) ^ (1 ^ 2 ^ 4 ^ 5)
        = (1 ^ 1) ^ (2 ^ 2) ^ 3 ^ (4 ^ 4) ^ (5 ^ 5)
        = 0 ^ 0 ^ 3 ^ 0 ^ 0
        = 3
```

## Key Insights

- **Overflow Consideration:** Sum formula may overflow for large n, XOR doesn't
- **XOR Advantage:** XOR handles negative numbers and prevents overflow
- **Mathematical Elegance:** Both optimal solutions use elegant mathematics
- **Single Pass:** XOR can be done in single pass with optimization

## Edge Cases

- Single element: returns 1 or 2 depending on value
- Missing first element (1): handled correctly
- Missing last element (n): handled correctly
- Large arrays: XOR preferred to avoid overflow

## Variations

- **Missing Two Numbers:** Requires different approach
- **Missing Number in Sorted Array:** Can use binary search O(log n)
- **Missing Number in Unsorted with Duplicates:** More complex

## References

- [GeeksforGeeks - Find the Missing Number](https://www.geeksforgeeks.org/find-the-missing-number/)

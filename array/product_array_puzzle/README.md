# Product Array Puzzle

Given an array `arr[]` of n integers, construct a Product Array `prod[]` (of same size) such that `prod[i]` is equal to the product of all the elements of `arr[]` except `arr[i]`.

## Problem Statement

For each position `i` in the array, calculate the product of all elements except the one at position `i`.

### Examples

**Input:** `arr[] = [10, 3, 5, 6, 2]`  
**Output:** `[180, 600, 360, 300, 900]`  
**Explanation:**
- prod[0] = 3 × 5 × 6 × 2 = 180
- prod[1] = 10 × 5 × 6 × 2 = 600
- prod[2] = 10 × 3 × 6 × 2 = 360
- And so on...

**Input:** `arr[] = [1, 2, 3, 4]`  
**Output:** `[24, 12, 8, 6]`

## Algorithm Approaches

### 1. Naive Approach - Nested Loop
- **File:** `product_array_puzzle.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) extra (O(n) for output)
- **Description:**
  - For each position i, iterate through all elements
  - Multiply all elements except arr[i]
  - Store in result[i]

### 2. Better Approach - Prefix and Suffix Arrays
- **File:** `product_array_puzzle.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) - for prefix and suffix arrays
- **Description:**
  - prefix[i] = product of elements from 0 to i-1
  - suffix[i] = product of elements from i+1 to n-1
  - result[i] = prefix[i] × suffix[i]

### 3. Optimal Approach - Two Passes with O(1) Space
- **File:** `product_array_puzzle.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) extra (output array doesn't count)
- **Description:**
  - First pass: Store prefix products in result array
  - Second pass: Multiply by suffix products (right to left)
  - Use running variable for suffix product

## Usage

```bash
python product_array_puzzle.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) extra | Simple but slow |
| Prefix-Suffix | O(n) | O(n) | Fast, uses extra space |
| Optimal | O(n) | O(1) extra | Best approach |

## Algorithm Details

### Optimal Approach Logic

```python
# First pass: result[i] contains product of elements before i
result[0] = 1
for i from 1 to n-1:
    result[i] = result[i-1] × arr[i-1]

# Second pass: multiply by product of elements after i
suffix_product = 1
for i from n-1 down to 0:
    result[i] = result[i] × suffix_product
    suffix_product = suffix_product × arr[i]
```

### Example Walkthrough

```
Input: arr = [10, 3, 5, 6, 2]

First Pass (Left to Right):
  i=0: result[0] = 1 (no elements before)
  i=1: result[1] = result[0] × arr[0] = 1 × 10 = 10
  i=2: result[2] = result[1] × arr[1] = 10 × 3 = 30
  i=3: result[3] = result[2] × arr[2] = 30 × 5 = 150
  i=4: result[4] = result[3] × arr[3] = 150 × 6 = 900
  
  result after first pass: [1, 10, 30, 150, 900]

Second Pass (Right to Left):
  i=4: result[4] = 900 × 1 = 900, suffix = 1 × 2 = 2
  i=3: result[3] = 150 × 2 = 300, suffix = 2 × 6 = 12
  i=2: result[2] = 30 × 12 = 360, suffix = 12 × 5 = 60
  i=1: result[1] = 10 × 60 = 600, suffix = 60 × 3 = 180
  i=0: result[0] = 1 × 180 = 180, suffix = 180 × 10 = 1800
  
  Final result: [180, 600, 360, 300, 900] ✓
```

## Key Insights

- **Decomposition:** prod[i] = (product of left side) × (product of right side)
- **In-place:** Can reuse output array to store intermediate results
- **Two Passes:** Left pass for prefix, right pass for suffix
- **Division Alternative:** Could use total_product / arr[i], but fails with zeros

## Edge Cases

- Single element: Return [1]
- Array with zero(s): Handled correctly (product becomes 0 for some elements)
- All zeros: All products are 0 except for zero positions
- Negative numbers: Handled correctly

## Variations

- **Without division constraint:** Could use total product
- **With modulo:** Calculate product modulo some number
- **Logarithm approach:** Use log to convert product to sum
- **Handling overflow:** Use modulo or big integers

## References

- [GeeksforGeeks - Product of Array Except Self](https://www.geeksforgeeks.org/a-product-array-puzzle/)
- [LeetCode - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

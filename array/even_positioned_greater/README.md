# Even Positioned Greater Than Odd

Given an array `arr[]` of size `n`, rearrange it such that every even positioned element is greater than or equal to its adjacent odd positioned elements.

## Problem Statement

Rearrange the array so that for all even indices `i`:  
`arr[i] >= arr[i-1]` (if i > 0) and `arr[i] >= arr[i+1]` (if i < n-1)

In simpler terms: `arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4]...`

### Examples

**Input:** `arr[] = [1, 2, 3, 4, 5, 6]`  
**Output:** `[6, 1, 5, 2, 4, 3]` or `[6, 2, 5, 1, 4, 3]` etc.  
**Explanation:** All even positioned elements (6, 5, 4) are greater than their adjacent odd positioned elements.

**Input:** `arr[] = [6, 5, 4, 3, 2, 1]`  
**Output:** `[6, 4, 5, 2, 3, 1]`  
**Explanation:** Array rearranged to satisfy the condition.

**Input:** `arr[] = [1, 3, 2]`  
**Output:** `[3, 1, 2]`  
**Explanation:** 3 (index 0) >= 1 (index 1) and 2 (index 2) >= 1 (index 1)

## Algorithm Approaches

### 1. Sort and Assign Approach
- **File:** `even_positioned_greater.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Description:** 
  1. Sort the array in ascending order
  2. Fill odd positions (1, 3, 5...) from the start of sorted array (smaller elements)
  3. Fill even positions (0, 2, 4...) from the end of sorted array (larger elements)
  4. This ensures all even positions have larger values

### 2. Single Pass Swap Approach (Optimal)
- **File:** `even_positioned_greater.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:** 
  - Traverse the array once
  - For even index i: ensure arr[i] >= arr[i+1] (swap if not)
  - For odd index i: ensure arr[i] <= arr[i+1] (swap if not)
  - This local adjustment ensures global property

## Usage

```bash
python even_positioned_greater.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | When to Use |
|----------|----------------|------------------|-------------|
| Sort & Assign | O(n log n) | O(n) | When exact optimal arrangement needed |
| Single Pass Swap | O(n) | O(1) | When performance is critical |

## Key Insights

- **Local Property:** The single pass approach works because local swaps propagate the ordering
- **Wiggle Sort:** This is similar to the "wiggle sort" problem
- **Multiple Valid Outputs:** There can be multiple valid rearrangements for the same input
- **In-place Modification:** The O(n) approach modifies the array in-place

## Edge Cases

- Empty array: returns empty
- Single element: returns as-is
- Two elements: larger one at index 0
- All equal elements: already valid

## References

- [GeeksforGeeks - Rearrange array such that even positioned are greater than odd](https://www.geeksforgeeks.org/rearrange-array-such-that-even-positioned-are-greater-than-odd/)

# Find All Pairs with Given Sum

## Problem Statement

Given an array of integers and a target sum, find all pairs of elements that sum to the target. The solution should handle duplicates appropriately.

## Examples

**Input:** `arr = [1, 5, 7, -1, 5], target = 6`
**Output:** `[(1, 5), (1, 5), (7, -1)]`

**Input:** `arr = [1, 1, 1, 1], target = 2`
**Output:** `[(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]` (6 pairs)

## Approaches

### 1. Brute Force (O(n²))

Check all possible pairs using two nested loops.

```python
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            add_pair_to_result()
```

**Time:** O(n²)  
**Space:** O(1) excluding result

### 2. Sort + Two Pointers (O(n log n))

1. Sort the array
2. Use two pointers (left at start, right at end)
3. Move pointers based on sum comparison
4. Handle duplicates carefully

**Time:** O(n log n) for sorting + O(n) for search = O(n log n)  
**Space:** O(1) excluding result (if in-place sort)

**Pros:**
- Returns unique pairs (no duplicates)
- No extra space for hash map

**Cons:**
- Destroys original array order
- Doesn't return all duplicate pairs

### 3. Hash Map (O(n)) - Optimal

1. Build frequency map of all elements
2. For each element, check if `target - element` exists
3. Calculate number of valid pairs based on frequencies

**Time:** O(n) for building map + O(n) for finding pairs = O(n)  
**Space:** O(n) for frequency map

**Pros:**
- Optimal time complexity
- Handles duplicates correctly
- Returns all valid pairs

**Cons:**
- Extra space for hash map
- Order of pairs not deterministic

## Complexity Summary

| Approach | Time | Space | Handles Duplicates |
|----------|------|-------|-------------------|
| Brute Force | O(n²) | O(1) | Yes |
| Sort + Two Pointers | O(n log n) | O(1) | Returns unique pairs only |
| Hash Map | O(n) | O(n) | Yes |

## When to Use Which

- **Brute Force:** Only for very small arrays or educational purposes
- **Sort + Two Pointers:** When you need unique pairs and can modify/sort the array
- **Hash Map:** When you need optimal performance and must return all pairs including duplicates

## Edge Cases

1. **Empty array:** Return empty list
2. **Single element:** Return empty list (no pairs possible)
3. **All duplicates:** Calculate pairs correctly using combination formula
4. **Negative numbers:** Handle correctly in all approaches
5. **Large numbers:** Avoid overflow in sum calculation

## References

- [GeeksforGeeks: Count pairs with given sum](https://www.geeksforgeeks.org/count-pairs-with-given-sum/)
- [LeetCode: Two Sum](https://leetcode.com/problems/two-sum/)
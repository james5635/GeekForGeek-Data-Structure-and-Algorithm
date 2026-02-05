# Sort Array According to Order Defined by Another Array

## Problem Description

Given two arrays `a1[]` and `a2[]`, sort `a1[]` such that elements appear in the order of `a2[]`. Elements in `a1[]` that are not in `a2[]` should be placed at the end in ascending order.

## Examples

### Example 1
- **Input:** 
  - a1 = `[2, 1, 2, 3, 4]`
  - a2 = `[2, 1, 2]`
- **Output:** `[2, 2, 1, 3, 4]`
- **Explanation:** Elements 2 and 1 follow the order in a2. Remaining 3 and 4 are sorted at the end.

### Example 2
- **Input:**
  - a1 = `[4, 1, 3, 3, 2]`
  - a2 = `[3, 1]`
- **Output:** `[3, 3, 1, 2, 4]`
- **Explanation:** Elements 3 and 1 come first as per a2. Others (2, 4) are sorted and placed after.

## Approaches

### Approach 1: Hashing (Recommended)

1. Count frequency of each element in `a1[]` using a hash map
2. Iterate through `a2[]` and append matching elements to result based on frequency
3. Remove processed elements from the map
4. Sort remaining elements and append to result

**Time Complexity:** O(m log m + n) where m = len(a1), n = len(a2)
**Space Complexity:** O(m) for the frequency map

### Approach 2: Custom Comparator

1. Create a map from `a2[]` storing index of each element
2. Sort `a1[]` using custom key:
   - If element exists in `a2[]`, use its index as priority
   - If not, use infinity and sort by value

**Time Complexity:** O(m log m + n)
**Space Complexity:** O(n) for the order map

## Comparison

| Approach | Time | Space | Advantages |
|----------|------|-------|------------|
| Hashing | O(m log m + n) | O(m) | Stable, preserves original frequencies |
| Custom Comparator | O(m log m + n) | O(n) | Simple implementation |

## Applications

- Database query ordering
- Priority-based sorting
- Custom ranking systems
- Sorting by categorical preference

## References

- [GeeksforGeeks - Sort by Another Array](https://www.geeksforgeeks.org/dsa/sort-array-according-order-defined-another-array/)

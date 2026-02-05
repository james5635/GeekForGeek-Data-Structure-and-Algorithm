# 4 Sum - Find Any Quadruplet Having Given Sum

## Problem Description

Given an array `arr[]` of integers and an integer `target`, find any quadruplet in `arr[]` such that its sum is equal to the target.

**Note:** If there are multiple quadruplets with sum = target, return any one of them.

## Examples

### Example 1
- **Input:** `arr = [2, 4, 6, 8, 1, 3], target = 15`
- **Output:** `[2, 4, 6, 3]` (or any valid quadruplet)
- **Explanation:** The quadruplet {2, 4, 6, 3} has sum = 15

### Example 2
- **Input:** `arr = [1, 2, 3, 4, 10], target = 20`
- **Output:** `[]`
- **Explanation:** No quadruplet adds up to a sum of 20

## Approaches

### Approach 1: Brute Force (O(n⁴))
Generate all possible quadruplets using four nested loops and check if any sum equals target.

### Approach 2: Sorting + Two Pointers (O(n³)) ⭐ Recommended

1. Sort the array
2. Use two nested loops to fix the first two elements
3. Use two pointers (left and right) to find the remaining two elements
4. Adjust pointers based on current sum compared to target

**Why it works:**
- Sorting enables two-pointer technique
- For fixed i and j, we need to find if any pair in the remaining array sums to `target - arr[i] - arr[j]`
- Two-pointer technique finds such pairs in O(n) time

### Approach 3: Hashing (O(n²) time, O(n²) space)
Store all pair sums in a hash map, then check if the complement sum exists.

## Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n⁴) | O(1) |
| Sorting + Two Pointers | O(n³) | O(1) |
| Hashing | O(n²) | O(n²) |

## Key Insights

- **Sorting is key:** Enables efficient two-pointer search
- **Early termination:** Can stop as soon as one valid quadruplet is found
- **No need for all solutions:** Problem asks for "any" quadruplet, not all

## Related Problems

- 2 Sum (Two Sum)
- 3 Sum
- 4 Sum II (Four Sum II)
- K Sum

## References

- [GeeksforGeeks - 4 Sum Find Quadruplet](https://www.geeksforgeeks.org/dsa/4-sum-find-any-quadruplet-having-given-sum/)

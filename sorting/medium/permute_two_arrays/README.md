# Permute Two Arrays such that Sum of Every Pair is Greater than or Equal to K

## Problem Description

Given two arrays `a[]` and `b[]` of equal size and an integer `k`, determine whether there exists any permutation of the arrays such that for every index `i`, the condition `a[i] + b[i] >= k` holds.

## Examples

### Example 1
- **Input:** 
  - a = `[2, 1, 3]`
  - b = `[7, 8, 9]`
  - k = `10`
- **Output:** `True`
- **Explanation:** Rearranging gives a = `[1, 2, 3]` and b = `[9, 8, 7]`. Each pair sum (10, 10, 10) >= k = 10

### Example 2
- **Input:**
  - a = `[1, 2, 2, 1]`
  - b = `[3, 3, 3, 4]`
  - k = `5`
- **Output:** `False`
- **Explanation:** Even after rearranging, at least one pair sum is less than 5

## Algorithm

### Greedy Approach

**Key Insight:** To maximize the sum of pairs, pair the smallest element of one array with the largest element of the other.

**Steps:**
1. Sort array `a[]` in ascending order
2. Sort array `b[]` in descending order
3. Check if `a[i] + b[i] >= k` for all `i`

**Why it works:** This greedy pairing ensures each sum is as large as possible. If this pairing fails, no other pairing can succeed.

## Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Greedy (Sort) | O(n log n) | O(1) or O(n) |
| Brute Force | O(n! × n) | O(n) |

## Proof of Correctness

**Claim:** If there exists any valid permutation, the greedy approach will find it.

**Proof:**
- Suppose greedy pairing fails at some index `i`
- This means `a[i] + b[i] < k` where `a[i]` is the i-th smallest in a and `b[i]` is the i-th largest in b
- For any other pairing, either we pair `a[i]` with a smaller element from b (worse), or we pair `b[i]` with a larger element from a (impossible since a[i] is already larger than all previous)
- Therefore, no valid pairing exists

## References

- [GeeksforGeeks - Permute Two Arrays](https://www.geeksforgeeks.org/dsa/permute-two-arrays-sum-every-pair-greater-equal-k/)

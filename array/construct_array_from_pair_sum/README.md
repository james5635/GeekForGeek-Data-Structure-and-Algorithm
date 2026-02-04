# Construct Array from Pair Sum

## Problem Statement

Given a pair-sum array, construct the original array.

The pair-sum array of an array `arr` with `n` elements contains `n*(n-1)/2` elements, where each element is the sum of two distinct elements from `arr`.

For example, if `arr = [a, b, c, d]`, the pair-sum array is: `[a+b, a+c, a+d, b+c, b+d, c+d]`

## Examples

**Input:** `pair_sum = [5, 6, 7, 8, 9, 10]`
**Output:** `[2, 3, 4, 5]`

**Explanation:**
- 2+3=5, 2+4=6, 2+5=7, 3+4=8, 3+5=9, 4+5=10

## Approaches

### 1. Mathematical Approach

**Intuition:**
The first three pair sums give us:
- `pair[0] = a + b`
- `pair[1] = a + c`
- `pair[2] = b + c`

Adding these three: `(a+b) + (a+c) + (b+c) = 2(a+b+c)`

So: `a + b + c = (pair[0] + pair[1] + pair[2]) / 2`

Then:
- `a = (a+b+c) - (b+c) = (a+b+c) - pair[2]`
- `b = (a+b+c) - (a+c) = (a+b+c) - pair[1]`
- `c = (a+b+c) - (a+b) = (a+b+c) - pair[0]`

**Algorithm:**
1. Calculate n from the pair sum size: `n*(n-1)/2 = len(pair_sum)`
2. If n < 3, handle base cases
3. Find a, b, c using the formula above
4. Find remaining elements: `arr[i] = pair[i-1] - arr[0]` for i >= 3

**Time Complexity:** O(n²) - finding n and reconstructing array
**Space Complexity:** O(n) - for result array

### 2. Optimal Approach

Same as mathematical approach but with cleaner implementation and better edge case handling.

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

## Key Insights

1. **Unique Reconstruction:** The first three elements can uniquely determine the first three array elements
2. **Remaining Elements:** Once the first element is known, all other elements can be derived
3. **Validation:** The input must have exactly `n*(n-1)/2` elements for some n

## Applications

- Data recovery from compressed pair-sum representations
- Cryptographic applications
- Array reconstruction problems

## References

- [GeeksforGeeks: Construct an array from its pair-sum array](https://www.geeksforgeeks.org/construct-an-array-from-its-pair-sum-array/)
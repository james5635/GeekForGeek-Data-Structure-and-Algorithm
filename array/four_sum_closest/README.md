# 4Sum Closest - Find Quadruplet with Closest Sum to Target

## Problem Description

Given an array and a target value, find four elements such that their sum is closest to the target. Return the closest sum value.

**Example:**
```
Input: arr = [1, 0, -1, 0, -2, 2], target = 1
Output: 1

Explanation: The quadruplet (-1, 0, 0, 2) sums to 1, which equals the target.
```

## Algorithm

**Approach:** Sorting + Two Nested Loops + Two Pointers

**Steps:**
1. Sort the array
2. Initialize closest_sum with sum of first four elements
3. Use two nested loops to fix first two elements
4. Use two pointers for remaining two elements
5. Update closest_sum when current_sum is closer to target
6. Return closest_sum

**Early Termination:** If exact match found, return immediately.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Sorting + Two Loops + Two Pointers | O(n³) | O(1) |
| Brute Force | O(n⁴) | O(1) |

## Functions

### `four_sum_closest(arr, target)`
Find the sum of four elements closest to target.

**Parameters:**
- `arr`: Input array of integers
- `target`: Target sum value

**Returns:**
- Integer representing the closest sum to target, or None if array has fewer than 4 elements

### `four_sum_closest_quadruplet(arr, target)`
Find the quadruplet with sum closest to target.

**Returns:**
- Tuple of (closest_sum, quadruplet)

## Usage

```python
from solution import four_sum_closest

arr = [1, 0, -1, 0, -2, 2]
target = 1
result = four_sum_closest(arr, target)
print(result)  # 1

# Get quadruplet too
closest_sum, quadruplet = four_sum_closest_quadruplet(arr, target)
print(f"Sum: {closest_sum}, Quadruplet: {quadruplet}")
# Sum: 1, Quadruplet: (-1, 0, 0, 2)
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Tracking Closest**: Keep track of minimum absolute difference from target
2. **Early Exit**: Return immediately if exact match found
3. **Pointer Movement**: Adjust left/right based on whether current sum is less than or greater than target
4. **Closest vs Exact**: Problem asks for closest, not exact match

## References

- [GeeksForGeeks - 4Sum Closest](https://www.geeksforgeeks.org/dsa/4-sum-find-a-quadruplet-with-closest-sum/)

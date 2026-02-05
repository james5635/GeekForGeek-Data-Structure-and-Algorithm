# Trapping Rain Water

## Problem Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example:**
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map is represented by array. 
In this case, 6 units of rain water are being trapped.
```

## Algorithms

### 1. Two Pointers (Optimal)
**Time:** O(n), **Space:** O(1)

Use two pointers from both ends, tracking left and right maximums. Water trapped at any position depends on the minimum of left_max and right_max.

### 2. Dynamic Programming
**Time:** O(n), **Space:** O(n)

Precompute left_max and right_max arrays for each position, then calculate trapped water.

### 3. Stack-based
**Time:** O(n), **Space:** O(n)

Use a stack to track bars. When current bar is higher than stack top, calculate trapped water.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Two Pointers | O(n) | O(1) |
| Dynamic Programming | O(n) | O(n) |
| Stack-based | O(n) | O(n) |
| Brute Force | O(n²) | O(1) |

## Functions

### `trap_two_pointers(height)`
Optimal solution using two pointers.

**Parameters:**
- `height`: List of non-negative integers representing elevation map

**Returns:**
- Total units of water trapped

### `trap_dp(height)`
Dynamic programming approach with precomputed max arrays.

### `trap_stack(height)`
Stack-based approach.

## Usage

```python
from solution import trap_two_pointers

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
water = trap_two_pointers(height)
print(water)  # 6
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Water Trapping Condition**: Water can only be trapped between two bars that are higher than the bars between them
2. **Boundary Effect**: Water level at any position is determined by the minimum of the highest bar on left and right
3. **Two Pointer Insight**: We can process from both ends simultaneously, always handling the side with smaller boundary

## References

- [GeeksForGeeks - Trapping Rain Water](https://www.geeksforgeeks.org/dsa/trapping-rain-water/)

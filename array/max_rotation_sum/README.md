# Maximize Sum of i*arr[i] with Rotations

## Problem Description

Given an array, find the maximum value of sum(i * arr[i]) with only rotations allowed on the given array. After each rotation, the element at index 0 moves to index n-1, and all other elements shift left by one.

**Example:**
```
Array: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Rotation 0: sum = 0*10 + 1*1 + 2*2 + ... + 9*9 = 285
Rotation 1: sum = 0*1 + 1*2 + 2*3 + ... + 9*10 = 330
Output: 330
```

## Algorithms

### 1. Optimized O(N) Approach
**Key Insight:** R(j) = R(j-1) + arrSum - n * arr[n-j]

Where:
- R(j) = sum for rotation j
- arrSum = sum of all elements
- n = array length

### 2. Naive O(N²) Approach
Calculate sum for each rotation independently.

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Optimized | O(N) | O(1) |
| Naive | O(N²) | O(1) |

## Functions

### `max_sum_rotation_optimized(arr)`
Find maximum sum using O(N) optimized approach.

**Parameters:**
- `arr`: Input array

**Returns:**
- Tuple of (max_sum, best_rotation)

### `max_sum_rotation_naive(arr)`
Naive O(N²) approach for comparison.

### Helper Functions
- `calculate_rotation_sum(arr, rotation)`: Calculate sum for specific rotation
- `rotate_array(arr)`: Rotate array by one position

## Usage

```python
from solution import max_sum_rotation_optimized

arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_sum, rotation = max_sum_rotation_optimized(arr)
print(f"Max sum: {max_sum}")  # 330
print(f"Best rotation: {rotation}")  # 1
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Recurrence Relation:** R(j) = R(j-1) + arrSum - n * arr[n-j]
2. **Constant Space:** Only need to track current sum and maximum
3. **Single Pass:** After computing initial sum, each rotation computed in O(1)
4. **Mathematical Insight:** When we rotate, each element's index changes predictably

## Mathematical Derivation

For rotation j:
```
R(j) = sum(i * arr[(i+j) % n]) for i in 0..n-1
R(j) = R(j-1) + sum(arr) - n * arr[n-j]
```

Explanation:
- Each element's index decreases by 1 (except first which goes to end)
- Net change = sum of all elements - n * element_moving_to_end

## References

- [GeeksForGeeks - Maximize Value of Sum i*arr[i] with Rotations](https://www.geeksforgeeks.org/dsa/maximize-value-of-expression-sum-i-arr-i-with-only-rotations-on-given-array-allowed/)

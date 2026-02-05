# Smallest Difference Triplet from Three Arrays

## Problem Description

Given three sorted arrays, find a triplet (one element from each array) such that the difference between the maximum and minimum element in the triplet is minimum.

**Example:**
```
Input: 
arr1 = [1, 4, 10]
arr2 = [2, 15, 20]
arr3 = [10, 12]

Output: (10, 15, 10) or similar with difference = 5

Explanation: The triplet (10, 15, 10) has max=15, min=10, diff=5 which is minimum.
```

## Algorithm

**Approach:** Three Pointers

**Key Insight:** Start with first elements of all three arrays. Calculate difference. To minimize difference, move the pointer pointing to the smallest element (this might bring a larger value closer to others).

**Steps:**
1. Initialize three pointers at start of each array
2. Calculate current difference
3. Update minimum difference if current is smaller
4. Move pointer of array with smallest element
5. Repeat until any pointer reaches end

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Three Pointers | O(n1 + n2 + n3) | O(1) |
| Brute Force | O(n1 × n2 × n3) | O(1) |

*Note: Assumes arrays are already sorted. If not, add O(n log n) for sorting.*

## Functions

### `smallest_difference_triplet(arr1, arr2, arr3)`
Find triplet with smallest difference from three sorted arrays.

**Parameters:**
- `arr1`: First sorted array
- `arr2`: Second sorted array
- `arr3`: Third sorted array

**Returns:**
- Tuple of three elements forming the triplet with minimum difference, or None if any array is empty

### `smallest_difference_triplet_value(arr1, arr2, arr3)`
Return only the minimum difference value.

## Usage

```python
from solution import smallest_difference_triplet

arr1 = [1, 4, 10]
arr2 = [2, 15, 20]
arr3 = [10, 12]
result = smallest_difference_triplet(arr1, arr2, arr3)
print(result)  # (10, 15, 10)
diff = max(result) - min(result)  # 5
```

## Running the Code

```bash
python solution.py
```

## Key Insights

1. **Greedy Choice**: Moving the smallest pointer is optimal because it potentially reduces the gap
2. **Early Termination**: If difference becomes 0, we can stop (optimal solution found)
3. **Sorted Input Required**: Algorithm assumes sorted arrays for correctness
4. **Linear Time**: Each pointer moves at most n times

## References

- [GeeksForGeeks - Smallest Difference Triplet from Three Arrays](https://www.geeksforgeeks.org/dsa/smallest-difference-triplet-from-three-arrays/)

# Sort Array by Applying Given Equation

## Problem Statement
Given an array arr[] of n integers and coefficients a, b, c of a quadratic function f(x) = ax² + bx + c, sort the array based on the value of f(x) for each element x in the array.

## Examples
- Input: arr[] = [-3, -1, 2, 4], f(x) = x²
  - Output: [-1, 2, -3, 4] (sorted by f(x): 1, 4, 9, 16)

- Input: arr[] = [1, 2, 3, 4], f(x) = -x²
  - Output: [4, 3, 2, 1] (decreasing order)

## Properties of Quadratic Functions
- **If a > 0**: Parabola opens upward, minimum at vertex
- **If a < 0**: Parabola opens downward, maximum at vertex
- **Vertex**: Located at x = -b/(2a)

## Approaches

### 1. Calculate and Sort (General)
1. Calculate f(x) for all elements
2. Sort by calculated values
3. **Time Complexity**: O(n log n)
4. **Space Complexity**: O(n)

### 2. Two-Pointer Merge (Optimal for sorted input)
1. Find vertex of parabola
2. Use two pointers from vertex outward
3. Merge based on f(x) values
4. **Time Complexity**: O(n) for sorted input
5. **Space Complexity**: O(n)

## Algorithm Steps (Two Pointer)
```
Find vertex = -b/(2a)
If a > 0:
    Elements closer to vertex have smaller f(x)
    Merge from center outward
Else:
    Elements farther from vertex have smaller f(x) 
    Merge from outside inward
```

## Special Cases

### Linear Function (a = 0)
- If b > 0: Return array in ascending order
- If b < 0: Return array in descending order

### Symmetric Arrays
- For f(x) = x² on symmetric array [-k, ..., 0, ..., k]
- Start from center (0) and move outward

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | When to Use |
|----------|----------------|------------------|-------------|
| Calculate + Sort | O(n log n) | O(n) | Unsorted input |
| Two Pointer | O(n) | O(n) | Already sorted input |
| Merge Split | O(n log n) | O(n) | General case |

## Key Insights
- Quadratic functions are symmetric around the vertex
- Distance from vertex determines f(x) value
- Can exploit sorted property for O(n) solution
- Linear case (a=0) is much simpler

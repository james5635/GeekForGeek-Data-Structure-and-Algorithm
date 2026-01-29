# Generating All Subarrays

Given an array, the task is to generate all possible non-empty subarrays.

## Approaches

### 1. Iterative Approach
- **Idea**: Use three nested loops. The outer loop selects the starting index, the middle loop selects the ending index, and the innermost loop prints the elements of the subarray.
- **Time Complexity**: $O(n^3)$
- **Space Complexity**: $O(1)$
- **File**: [iterative_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/generating_all_subarrays/iterative_approach.py)

### 2. Recursive Approach
- **Idea**: Use recursion with two pointers `start` and `end`.
    1. Stop if `end` reaches the array size.
    2. If `start` > `end`, increment `end` and reset `start` to 0.
    3. Otherwise, print the subarray `[start...end]` and increment `start`.
- **Time Complexity**: $O(n^2)$ (number of subarrays is $n(n+1)/2$, and printing each takes proportional time, but the recursion depth is also a factor. Actually, it's more about how many times the function is called.)
- **Space Complexity**: $O(n^2)$ (due to recursion stack in the worst case, or $O(n)$ if optimized, but here it's $O(n^2)$ recursive calls total.)
- **File**: [recursive_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/generating_all_subarrays/recursive_approach.py)

## Example
**Input**: `arr = [1, 2, 3]`
**Output**:
```
[1]
[1, 2]
[2]
[1, 2, 3]
[2, 3]
[3]
```

## Source
[GeeksforGeeks - Generating All Subarrays](https://www.geeksforgeeks.org/dsa/generating-subarrays-using-recursion/)

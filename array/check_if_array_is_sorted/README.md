# Check if an Array is Sorted

Given an array, check if it is sorted in non-decreasing order.

## Approaches

### 1. Iterative Approach
- **Idea**: Traverse from the second element (index 1) and compare it with the previous element. If any element is smaller than the previous one, the array is not sorted.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$
- **File**: [iterative_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/check_if_array_is_sorted/iterative_approach.py)

### 2. Recursive Approach
- **Idea**: Check if the last two elements are in order, then recursively check the rest of the array (size $n-1$).
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$ (due to recursion stack)
- **File**: [recursive_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/check_if_array_is_sorted/recursive_approach.py)

### 3. Built-in Approach
- **Idea**: Compare the array with its sorted version using Python's `sorted()` method.
- **Time Complexity**: $O(n \log n)$ (Python uses Timsort)
- **Space Complexity**: $O(n)$ (temp array for sorted)
- **File**: [builtin_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/check_if_array_is_sorted/builtin_approach.py)

## Example
**Input**: `arr = [10, 20, 30, 40, 50]`
**Output**: `true`

**Input**: `arr = [10, 20, 30, 5, 6]`
**Output**: `false`

## Source
[GeeksforGeeks - Check if an Array is Sorted](https://www.geeksforgeeks.org/dsa/program-check-array-sorted-not-iterative-recursive/)

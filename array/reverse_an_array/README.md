# Array Reverse

Given an array, the task is to reverse the array.

## Approaches

### 1. Naive Approach (Using Temporary Array)
- **Idea**: Create a temporary array of the same size, copy elements in reverse order, and then copy them back to the original array.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
- **File**: [naive_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/reverse_an_array/naive_approach.py)

### 2. Expected Approach 1 (Two Pointers)
- **Idea**: Use two pointers, one at the beginning and one at the end, and swap elements while the left pointer is less than the right pointer.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$
- **File**: [two_pointers_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/reverse_an_array/two_pointers_approach.py)

### 3. Recursive Approach
- **Idea**: Swap the first and last elements and then recursively call the function for the rest of the array.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$ (due to recursion stack)
- **File**: [recursive_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/reverse_an_array/recursive_approach.py)

### 4. Built-in Methods
- **Idea**: Use Python's built-in `reverse()` method or list slicing `[::-1]`.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$ (for `reverse()`) or $O(n)$ (for slicing if result is not assigned back in-place).
- **File**: [builtin_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/reverse_an_array/builtin_approach.py)

## Example
**Input**: `arr = [1, 4, 3, 2, 6, 5]`
**Output**: `[5, 6, 2, 3, 4, 1]`

## Source
[GeeksforGeeks - Array Reverse](https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/)

# Leaders in an Array

Given an array, find all the "leaders." An element is a leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.

## Approaches

### 1. Naive Approach (Nested Loops)
- **Idea**: Use two nested loops. The outer loop picks an element, and the inner loop checks if there's any element to its right that is greater.
- **Time Complexity**: $O(n^2)$
- **Space Complexity**: $O(1)$ (ignoring the space for the result)
- **File**: [naive_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/leaders_in_an_array/naive_approach.py)

### 2. Optimized Approach (Suffix Maximum)
- **Idea**: Scan the array from right to left while keeping track of the maximum element seen so far. If the current element is greater than or equal to the current maximum, it is a leader.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$ (ignoring the space for the result)
- **File**: [optimized_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/leaders_in_an_array/optimized_approach.py)

## Example
**Input**: `arr = [16, 17, 4, 3, 5, 2]`
**Output**: `17 5 2`

## Source
[GeeksforGeeks - Leaders in an Array](https://www.geeksforgeeks.org/dsa/leaders-in-an-array/)

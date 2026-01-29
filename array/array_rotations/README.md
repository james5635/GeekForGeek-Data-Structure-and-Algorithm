# Array Rotations (Clockwise or Right)

Given an array of size $n$, rotate it by $d$ elements to the right.

## Approaches

### 1. Rotate one by one
- **Idea**: Shift the elements by one position to the right $d$ times. In each shift, the last element becomes the first.
- **Time Complexity**: $O(n \times d)$
- **Space Complexity**: $O(1)$
- **File**: [rotate_one_by_one.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/array_rotations/rotate_one_by_one.py)

### 2. Using Temporary Array
- **Idea**: Create a temporary array of size $n$. Copy the last $d$ elements to the front and the first $n-d$ elements to the back.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
- **File**: [using_temp_array.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/array_rotations/using_temp_array.py)

### 3. Juggling Algorithm
- **Idea**: Shift elements in cycles. The number of cycles is equal to $GCD(n, d)$.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$
- **File**: [juggling_algorithm.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/array_rotations/juggling_algorithm.py)

### 4. Reversal Algorithm
- **Idea**: 
    1. Reverse the entire array.
    2. Reverse the first $d$ elements.
    3. Reverse the last $n-d$ elements.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$
- **File**: [reversal_algorithm.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/array_rotations/reversal_algorithm.py)

## Example
**Input**: `arr = [1, 2, 3, 4, 5, 6]`, `d = 2`
**Output**: `[5, 6, 1, 2, 3, 4]`

## Source
[GeeksforGeeks - Rotate an Array - Clockwise or Right](https://www.geeksforgeeks.org/dsa/complete-guide-on-array-rotations/)

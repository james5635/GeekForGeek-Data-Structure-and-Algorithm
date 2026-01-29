# Remove Duplicates from Sorted Array

Given a sorted array, the task is to remove the duplicate elements in-place such that each element appears only once.

## Approaches

### 1. Using Hash Set
- **Idea**: Use a hash set to keep track of elements already seen. This approach works even if the array is not sorted.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(n)$
- **File**: [using_set.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/remove_duplicates_from_sorted_array/using_set.py)

### 2. Efficient Approach (Two Pointers)
- **Idea**: Since the array is sorted, duplicate elements are adjacent. We can maintain an index `idx` for unique elements and traverse the array, updating `arr[idx]` whenever a new unique element is found.
- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$
- **File**: [efficient_approach.py](file:///home/jame/Desktop/coding/GeekForGeek-Data-Structure-and-Algorithm/array/remove_duplicates_from_sorted_array/efficient_approach.py)

## Example
**Input**: `arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]`
**Output**: `[1, 2, 3, 4, 5]`
**New Size**: `5`

## Source
[GeeksforGeeks - Remove duplicates from Sorted Array](https://www.geeksforgeeks.org/dsa/remove-duplicates-sorted-array/)

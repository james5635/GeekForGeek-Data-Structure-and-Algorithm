# Sort an Array of 0s, 1s, and 2s (Dutch National Flag Problem)

## Problem Statement

Given an array containing only 0s, 1s, and 2s, sort the array in-place such that all 0s come first, then all 1s, and then all 2s. This is also known as the **Dutch National Flag Problem**.

## Examples

**Example 1:**
```
Input: arr = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
```

**Example 2:**
```
Input: arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
```

## Approach

### Dutch National Flag Algorithm (Optimal)

We use three pointers to partition the array into three regions:

1. **`low`**: Boundary of 0s region (elements before `low` are 0)
2. **`mid`**: Current element being examined
3. **`high`**: Boundary of 2s region (elements after `high` are 2)

**Algorithm:**
```
Initialize: low = 0, mid = 0, high = n - 1

While mid <= high:
    If arr[mid] == 0:
        Swap arr[low] and arr[mid]
        low++, mid++
    If arr[mid] == 1:
        mid++
    If arr[mid] == 2:
        Swap arr[mid] and arr[high]
        high--
        (Don't increment mid, need to check swapped element)
```

### Why Three Pointers?
- `low` expands the 0s region from the left
- `high` expands the 2s region from the right  
- `mid` scans through the unknown middle region

## Complexity Analysis

- **Time Complexity:** O(n)
  - Single pass through array: O(n)
- **Space Complexity:** O(1)
  - In-place sorting
  - Only using three pointers

## Implementation

```python
def sort_012(arr):
    if not arr:
        return arr
    
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr
```

## Alternative: Counting Method

```python
def sort_012_counting(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)
    return [0] * count_0 + [1] * count_1 + [2] * count_2
```

- **Time:** O(n) - requires two passes
- **Space:** O(n) - creates new array

## Edge Cases

- **Empty array:** Returns empty
- **All same values:** Already sorted
- **Already sorted:** No swaps needed
- **Reverse sorted:** Maximum swaps needed
- **Invalid values:** Raise error

## Applications

- Color sorting (Dutch flag has three colors)
- Data partitioning with three categories
- Quicksort with three-way partitioning
- Median finding

## Related Problems

- Three Way Partitioning Around a Range
- Sort Colors (LeetCode)
- Partition Array into Three Parts

## Reference

- [GeeksforGeeks - Sort an Array of 0s, 1s, and 2s](https://www.geeksforgeeks.org/dsa/sort-an-array-of-0s-1s-and-2s/)
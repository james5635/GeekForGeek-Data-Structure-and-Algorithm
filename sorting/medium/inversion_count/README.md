# Inversion Count in Array Using Merge Sort

## Problem Statement

Given an array, count the number of inversions. An **inversion** is a pair of indices `(i, j)` such that `i < j` and `arr[i] > arr[j]`.

## Examples

**Example 1:**
```
Input: arr = [2, 4, 1, 3, 5]
Output: 3
Explanation: The inversions are:
- (0, 2): 2 > 1
- (1, 2): 4 > 1  
- (1, 3): 4 > 3
```

**Example 2:**
```
Input: arr = [5, 4, 3, 2, 1]
Output: 10
Explanation: Reverse sorted array has C(5,2) = 10 inversions
```

## Approach

### Modified Merge Sort (Optimal)

We can count inversions efficiently using a modified merge sort:

1. **Divide:** Split array into two halves
2. **Conquer:** Recursively count inversions in each half
3. **Combine:** Count **split inversions** (one element in left, one in right) during merge

### Key Insight

During the merge step, when we take an element from the **right half** before elements remaining in the **left half**, we have found inversions. Specifically, if `arr[i] > arr[j]` where `i` is in left and `j` is in right, then all elements from index `i` to `mid` are greater than `arr[j]` (since left half is sorted).

**Split inversions added:** `(mid - i + 1)`

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Same as merge sort
- **Space Complexity:** O(n)
  - Temporary array for merging: O(n)
  - Recursion stack: O(log n)

## Implementation

```python
def count_inversions(arr):
    if not arr or len(arr) <= 1:
        return 0
    
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    
    if left < right:
        mid = (left + right) // 2
        
        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        inv_count += merge_and_count(arr, temp, left, mid, right)
    
    return inv_count

def merge_and_count(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)  # Key step!
            j += 1
        k += 1
    
    # Copy remaining elements
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    # Copy back to original
    for i in range(left, right + 1):
        arr[i] = temp[i]
    
    return inv_count
```

## Alternative Approaches

### Brute Force: O(n²)
```python
def count_inversions_brute_force(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count
```

### Using BST/Order Statistic Tree: O(n log n)
- Insert elements from right to left
- Use tree to count how many already inserted elements are smaller

## Edge Cases

- **Empty array:** 0 inversions
- **Single element:** 0 inversions
- **Already sorted:** 0 inversions
- **Reverse sorted:** n(n-1)/2 inversions (maximum)
- **All same:** 0 inversions

## Applications

- Measuring sortedness of array
- Collaborative filtering (similarity between rankings)
- Genetics (measuring evolutionary distance)
- Voting theory

## Related Problems

- Count of Smaller Numbers After Self
- Global and Local Inversions
- Reverse Pairs

## Reference

- [GeeksforGeeks - Inversion Count in Array Using Merge Sort](https://www.geeksforgeeks.org/dsa/inversion-count-in-array-using-merge-sort/)
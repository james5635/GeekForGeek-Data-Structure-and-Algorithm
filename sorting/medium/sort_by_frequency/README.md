# Sort by Frequency

## Problem Statement

Given an array of integers, sort the array according to the frequency of elements. Elements with higher frequency come first. If frequencies of two elements are the same, the smaller number comes first.

## Example

**Input:**
```
arr = [2, 5, 2, 8, 5, 6, 8, 8]
```

**Output:**
```
[8, 8, 8, 2, 2, 5, 5, 6]
```

**Explanation:**
- 8 occurs 3 times
- 2 occurs 2 times
- 5 occurs 2 times
- 6 occurs 1 time

8 comes first (highest frequency), then 2 (smaller than 5 for same frequency), then 5, then 6.

## Approach

1. **Count Frequencies:** Use a dictionary or Counter to count the frequency of each element
2. **Sort:** Use Python's sorted function with a custom key that:
   - Sorts by frequency in descending order (negative frequency)
   - Sorts by value in ascending order (for ties)

## Complexity Analysis

- **Time Complexity:** O(n log n)
  - Counting frequencies: O(n)
  - Sorting: O(n log n)
- **Space Complexity:** O(n)
  - Dictionary storage: O(n)
  - Result array: O(n)

## Implementation

Two approaches are provided:

### Approach 1: Using sorted() with custom key
```python
def sort_by_frequency(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))
```

### Approach 2: Using most_common
```python
def sort_by_frequency_alternative(arr):
    freq = Counter(arr)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    result = []
    for num, count in sorted_items:
        result.extend([num] * count)
    return result
```

## Edge Cases

- Empty array: Returns empty array
- All elements same: Returns same array
- All elements unique: Returns sorted array (ascending order)
- Same frequencies: Smaller element comes first
- Negative numbers: Handled correctly

## Reference

- [GeeksforGeeks - Sort Elements by Frequency](https://www.geeksforgeeks.org/dsa/sort-elements-by-frequency/)
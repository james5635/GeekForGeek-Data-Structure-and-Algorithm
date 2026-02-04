# Rearrange Array such that arr[i] = i

Given an array of size N where elements are in range from 0 to N-1. All elements may not be present in the array. If element is not present, we put -1 at that position.

## Problem Statement

Rearrange the array such that:
- `arr[i] = i` if value `i` is present in the array
- `arr[i] = -1` if value `i` is not present in the array

### Examples

**Input:** `arr[] = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]`  
**Output:** `[0, 1, 2, 3, 4, -1, 6, -1, -1, 9]`  
**Explanation:** 
- 0 is not present → -1 at index 0
- 1 is at index 3 → 1 at index 1
- 2 is at index 6 → 2 at index 2
- And so on...

**Input:** `arr[] = [19, 7, 0, 3, 18]`  
**Output:** `[-1, -1, -1, 3, -1]`  
**Explanation:** Only 0 and 3 are valid (within range [0, 4]), others are out of range.

## Algorithm Approaches

### 1. Naive Approach - Linear Search
- **File:** `rearrange_array_arri.py`
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1) (modifies in-place or uses O(n) for result)
- **Description:**
  - For each position i from 0 to n-1:
    - Search entire array for value i
    - If found, place i at position i
    - Otherwise, place -1

### 2. Optimal Approach - In-place Swapping
- **File:** `rearrange_array_arri.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:**
  - Traverse the array
  - For each element arr[i], if it's valid (0 <= arr[i] < n) and not at correct position:
    - Swap arr[i] with arr[arr[i]] (place it at correct position)
  - Repeat until all elements are in place or cannot be moved
  - Invalid positions become -1

## Usage

```bash
python rearrange_array_arri.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive | O(n²) | O(1) or O(n) | Simple but slow |
| Optimal | O(n) | O(1) | Fast, in-place |

## Algorithm Details

### Optimal Approach Logic

```
For each position i:
  While arr[i] is valid AND arr[i] ≠ i:
    target = arr[i]
    Swap arr[i] with arr[target]
    
After processing:
  All arr[i] = i (if i was present)
  Or arr[i] = -1 (if i was not present)
```

### Example Walkthrough

```
Input:  [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
         0   1   2  3  4  5  6   7  8   9

Step 1: i=2, arr[2]=6 → swap with arr[6]=2 → [-1, -1, 2, 1, 9, 3, 6, -1, 4, -1]
Step 2: i=3, arr[3]=1 → swap with arr[1]=-1 → [-1, 1, 2, -1, 9, 3, 6, -1, 4, -1]
        i=3, arr[3]=-1 → stop
Step 3: i=4, arr[4]=9 → swap with arr[9]=-1 → [-1, 1, 2, -1, -1, 3, 6, -1, 4, 9]
        i=4, arr[4]=-1 → stop
Step 4: i=5, arr[5]=3 → swap with arr[3]=-1 → [-1, 1, 2, 3, -1, -1, 6, -1, 4, 9]
        i=5, arr[5]=-1 → stop
Step 5: i=8, arr[8]=4 → swap with arr[4]=-1 → [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
        i=8, arr[8]=-1 → stop

Result: Place 0 at position 0 (if present, else -1)
        Final: [0, 1, 2, 3, 4, -1, 6, -1, -1, 9]
```

## Key Insights

- **Cyclic Swapping:** Each element is swapped at most once to its correct position
- **In-place Modification:** No extra space needed except for swapping
- **Linear Time:** Despite nested while loop, each element is swapped at most once

## Edge Cases

- All elements -1: Returns array of all -1
- Array already sorted: Returns same array
- Reverse sorted array: Sorts in ascending order
- Out of range elements: Becomes -1

## Variations

- **Rearrange array such that arr[i] = i without -1:** All elements guaranteed to be in range
- **Given multiple occurrences:** Decide which one to keep
- **Find missing numbers:** Return list of missing indices

## References

- [GeeksforGeeks - Rearrange an array such that arr[i] = i](https://www.geeksforgeeks.org/rearrange-array-arri/)

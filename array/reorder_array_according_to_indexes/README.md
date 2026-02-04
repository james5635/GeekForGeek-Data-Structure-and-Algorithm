# Reorder Array According to Given Indexes

Given two arrays: `arr[]` and `index[]` of same size N. The task is to reorder array `arr[]` according to the array `index[]` such that `arr[index[i]]` becomes `arr[i]` after reordering.

## Problem Statement

Rearrange the array `arr[]` so that each element `arr[i]` is placed at position `index[i]`.

### Examples

**Input:** `arr[] = [50, 40, 70, 60, 90]`, `index[] = [3, 0, 4, 1, 2]`  
**Output:** `arr[] = [40, 60, 90, 50, 70]`, `index[] = [0, 1, 2, 3, 4]`  
**Explanation:**
- Element 50 (at index 0) goes to index 3
- Element 40 (at index 1) goes to index 0
- Element 70 (at index 2) goes to index 4
- And so on...

**Input:** `arr[] = [10, 11, 12]`, `index[] = [1, 0, 2]`  
**Output:** `arr[] = [11, 10, 12]`, `index[] = [0, 1, 2]`  
**Explanation:** Elements at indices 0 and 1 are swapped.

## Algorithm Approaches

### 1. Naive Approach - Create New Array
- **File:** `reorder_array_according_to_indexes.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Description:**
  - Create a new result array of size N
  - Place each `arr[i]` at position `index[i]` in result
  - Copy result back to original array

### 2. Better Naive - Sort Pairs
- **File:** `reorder_array_according_to_indexes.py`
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Description:**
  - Create pairs of `(index[i], arr[i])`
  - Sort pairs by index
  - Extract arr values in sorted order

### 3. Optimal Approach - In-place Swapping
- **File:** `reorder_array_according_to_indexes.py`
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Description:**
  - For each position i, follow the index chain
  - Swap elements until each is at its correct position
  - Simultaneously update the index array

## Usage

```bash
python reorder_array_according_to_indexes.py
```

## Complexity Comparison

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Naive (New Array) | O(n) | O(n) | Simple, needs extra space |
| Sort Pairs | O(n log n) | O(n) | Sorting overhead |
| In-place Swap | O(n) | O(1) | Optimal, no extra space |

## Algorithm Details

### In-place Swapping Logic

```python
for i from 0 to n-1:
    while index[i] != i:
        target = index[i]
        # Swap arr[i] with arr[target]
        swap(arr[i], arr[target])
        # Swap index[i] with index[target]
        swap(index[i], index[target])
```

### Example Walkthrough

```
Input: arr = [50, 40, 70, 60, 90], index = [3, 0, 4, 1, 2]

i=0: index[0]=3 ≠ 0
     Swap arr[0]↔arr[3]: [60, 40, 70, 50, 90]
     Swap index[0]↔index[3]: [1, 0, 4, 3, 2]
     
     index[0]=1 ≠ 0
     Swap arr[0]↔arr[1]: [40, 60, 70, 50, 90]
     Swap index[0]↔index[1]: [0, 1, 4, 3, 2]
     
     index[0]=0 ✓

i=1: index[1]=1 ✓

i=2: index[2]=4 ≠ 2
     Swap arr[2]↔arr[4]: [40, 60, 90, 50, 70]
     Swap index[2]↔index[4]: [0, 1, 2, 3, 4]
     
     index[2]=2 ✓

i=3: index[3]=3 ✓
i=4: index[4]=4 ✓

Result: arr = [40, 60, 90, 50, 70], index = [0, 1, 2, 3, 4]
```

## Key Insights

- **Cyclic Permutation:** The reordering is essentially applying a permutation
- **Cycle Detection:** Each element is part of a cycle that eventually returns to correct position
- **Simultaneous Update:** Both arr and index are modified together
- **Linear Time:** Each element is swapped at most once

## Edge Cases

- Already sorted: No swaps needed
- Reverse order: Maximum swaps needed
- Single element: Trivial case
- Duplicate indices: Not valid (permutation required)

## Variations

- **Reverse operation:** Given reordered array, find original index
- **Multiple arrays:** Reorder multiple arrays by same index
- **Partial reorder:** Only reorder a subrange

## References

- [GeeksforGeeks - Reorder an array according to given indexes](https://www.geeksforgeeks.org/reorder-array-according-given-indexes/)

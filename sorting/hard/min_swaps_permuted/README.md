# Minimum Swaps to Reach Permuted Array

## Problem Statement
Given an array arr[] of n integers where each element is between 1 to n (inclusive), find the minimum number of swaps required to sort the array. In one swap, you can swap any element with any other element.

## Examples
- Input: arr[] = [4, 3, 2, 1]
  - Output: 2
  - Explanation: 
    - Swap 4 with 1: [1, 3, 2, 4]
    - Swap 3 with 2: [1, 2, 3, 4]

- Input: arr[] = [2, 3, 4, 1, 5]
  - Output: 3

- Input: arr[] = [1, 2, 3, 4]
  - Output: 0 (already sorted)

## Approaches

### 1. Cycle Detection (Optimal)
1. Create a mapping of value to index
2. Identify cycles in the permutation
3. For a cycle of length k, we need k-1 swaps
4. **Time Complexity**: O(n log n) for sorting
5. **Space Complexity**: O(n)

### 2. Graph-based
1. Build a graph where edges represent correct positions
2. Count cycles in the graph
3. **Time Complexity**: O(n)
4. **Space Complexity**: O(n)

## Algorithm Steps (Cycle Detection)
```
Create pairs (value, original_index)
Sort pairs by value
Initialize visited array
swaps = 0

For i from 0 to n-1:
    If not visited[i] and not in correct position:
        cycle_size = 0
        j = i
        While not visited[j]:
            visited[j] = true
            j = position where arr[j] should be
            cycle_size += 1
        swaps += (cycle_size - 1)

Return swaps
```

## Cycle Detection Logic
- Each element should be at a specific position in sorted array
- This creates a permutation graph with cycles
- Elements in a cycle can be sorted with (cycle_length - 1) swaps
- Total swaps = sum of (cycle_length - 1) for all cycles

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Cycle Detection | O(n log n) | O(n) | Simple and efficient |
| Graph-based | O(n) | O(n) | Linear but more complex |

## Example Walkthrough
Array: [4, 3, 2, 1]
Sorted: [1, 2, 3, 4]

Positions:
- 4 should be at index 3, currently at 0
- 3 should be at index 2, currently at 1
- 2 should be at index 1, currently at 2
- 1 should be at index 0, currently at 3

Cycle: 0 → 3 → 0 (length 2)
Cycle: 1 → 2 → 1 (length 2)

Swaps needed: (2-1) + (2-1) = 2

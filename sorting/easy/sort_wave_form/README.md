# Sort Array in Wave Form

## Problem Statement
Given an unsorted array, arrange elements in wave form such that:
- arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= ...

## Approach
### Optimal Single Pass (O(n))
1. Traverse all even indexed elements
2. Ensure each even element is greater than or equal to its neighbors
3. Swap with left or right neighbor if needed

### Alternative: Sort First (O(n log n))
1. Sort the array
2. Swap adjacent elements (0-1, 2-3, 4-5, ...)

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Single Pass | O(n) | O(1) |
| Sort First | O(n log n) | O(1) or O(n) |

## Key Points
- Even indices contain "peak" elements
- Odd indices contain "valley" elements
- Single pass approach is optimal and doesn't require full sorting
# Sort Numbers Stored on Different Machines

## Problem Description

Given n machines in the form of linked lists. Each machine contains some numbers in sorted form. The amount of numbers each machine has is not fixed. Output the numbers from all machines in sorted non-decreasing form.

## Algorithm

1. Create a min-heap to track the smallest element from each machine
2. Push the first element from each machine (linked list) into the heap
3. While heap is not empty:
   - Pop the smallest element and add to result
   - Push the next element from the same machine into heap
4. Return the merged sorted list

## Complexity Analysis

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(N log k) | O(k) |
| Average | O(N log k) | O(k) |
| Worst | O(N log k) | O(k) |

Where N = total number of elements, k = number of machines

## Example

```
Input:  Machine 1: [30, 40, 50]
        Machine 2: [35, 45]
        Machine 3: [10, 60, 70, 80, 100]
Output: [10, 30, 35, 40, 45, 50, 60, 70, 80, 100]
```

## Key Points

- Uses min-heap (priority queue) for efficient merging
- Similar to k-way merge algorithm
- Time complexity depends on number of machines
- Space efficient - only stores k elements in heap
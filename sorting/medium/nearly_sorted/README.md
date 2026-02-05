# Nearly Sorted Algorithm (K-Sorted Array)

## Problem Description

Given an array `arr[]` and an integer `k`, where every element is at most `k` positions away from its correct sorted position. Sort the array efficiently.

This means if the array were completely sorted, the element at index `i` in the given array can be at any index from `i-k` to `i+k`.

## Examples

### Example 1
- **Input:** `arr = [2, 3, 1, 4], k = 2`
- **Output:** `[1, 2, 3, 4]`
- **Explanation:** 
  - Element 1 moves from index 2 to 0
  - Element 2 moves from index 0 to 1
  - Element 3 moves from index 1 to 2
  - Element 4 stays at index 3

### Example 2
- **Input:** `arr = [1, 4, 5, 2, 3, 6, 7, 8, 9, 10], k = 2`
- **Output:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

## Algorithm

### Optimal Approach - Using Min-Heap

**Key Insight:** For the current position `i` in the sorted array, the correct element must be within the next `k+1` elements (from the current position in the original array).

1. Create a min-heap and insert the first `k+1` elements
2. For each position `i` in the result:
   - Pop the minimum from heap (this is the next element in sorted order)
   - If there are more elements, push the next element from the original array
3. After processing all elements, pop remaining elements from heap

**Why it works:** The heap always contains the `k+1` smallest elements that haven't been placed yet. The minimum of these is guaranteed to be the next element in sorted order.

## Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Naive (Sort) | O(n log n) | O(1) |
| **Min-Heap** | **O(n log k)** | **O(k)** |
| Insertion Sort | O(nk) | O(1) |

## Advantages of Heap Approach

- **Efficient for small k:** When k << n, O(n log k) is much better than O(n log n)
- **Online algorithm:** Can process elements as they arrive
- **Space efficient:** Only needs O(k) extra space

## Use Cases

- Merging k sorted lists
- Finding median in a stream
- Real-time data processing where elements arrive out of order

## References

- [GeeksforGeeks - Nearly Sorted Algorithm](https://www.geeksforgeeks.org/dsa/nearly-sorted-algorithm/)

# K Largest/Smallest Elements in an Array

## Problem Description

Given an array `arr[]` and an integer `k`, find `k` largest (or smallest) elements in the array. Elements in the output should be in decreasing order (for largest) or increasing order (for smallest).

## Examples

### Example 1 - K Largest
- **Input:** `arr = [1, 23, 12, 9, 30, 2, 50], k = 3`
- **Output:** `[50, 30, 23]`

### Example 2 - K Smallest
- **Input:** `arr = [11, 5, 12, 9, 44, 17, 2], k = 2`
- **Output:** `[2, 5]`

## Approaches

### Approach 1: Sorting (O(n log n))
Sort the entire array and take first/last k elements.

### Approach 2: Min/Max Heap (O(n log k)) ⭐ Recommended

**For K Largest:**
1. Create a min-heap with first k elements
2. For remaining elements, if element > heap top, replace top with element
3. Heap contains k largest elements

**For K Smallest:**
1. Create a max-heap with first k elements
2. For remaining elements, if element < heap top, replace top with element
3. Heap contains k smallest elements

**Why O(n log k)?**
- Building heap: O(k)
- n-k insertions, each O(log k)
- Total: O(k + (n-k) log k) = O(n log k)

### Approach 3: Quick Select (O(n) average)
Use partitioning (like QuickSort) to find k largest without fully sorting.

**Steps:**
1. Partition array around a pivot
2. If left part has exactly k elements, we're done
3. If more than k, search left; if less, search right with reduced k

## Time & Space Complexity

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Sorting | O(n log n) | O(1) or O(n) |
| **Min/Max Heap** | **O(n log k)** | **O(k)** |
| Quick Select | O(n) avg, O(n²) worst | O(1) or O(log n) |

## When to Use Which

| Scenario | Recommended Approach |
|----------|---------------------|
| k << n | Heap (much faster) |
| k ≈ n | Sorting |
| Cannot modify array | Heap |
| Need guaranteed O(n) | Quick Select with median-of-medians |

## Applications

- Finding top k products by rating
- Leaderboards in games
- Top k frequent elements
- Recommendation systems

## References

- [GeeksforGeeks - K Largest/Smallest Elements](https://www.geeksforgeeks.org/dsa/k-largestor-smallest-elements-in-an-array/)

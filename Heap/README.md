# Heap Data Structure - GeeksforGeeks Implementations

This folder contains Python implementations of Heap data structure algorithms from GeeksforGeeks.

## Topics

### Basics & Implementation (`basics/`)
| File | Description |
|------|-------------|
| `binary_heap.py` | Min/Max Heap implementation with insert, delete, extract, heapify |
| `heap_applications.py` | Real-world heap applications |
| `heap_using_stl.py` | C++ STL heap equivalents in Python |
| `priority_queue_cpp.py` | C++ std::priority_queue equivalent |
| `priority_queue_java.py` | Java PriorityQueue equivalent |
| `heapq_python.py` | Python heapq module guide |

### Easy Problems (`easy/`)
| File | Problem |
|------|---------|
| `check_binary_heap.py` | Check if array represents a binary heap |
| `kth_smallest_largest.py` | K-th smallest/largest element in unsorted array |
| `heap_sort.py` | Heap sort algorithm |
| `heap_height.py` | Height of heap with N nodes |

### Medium Problems (`medium/`)
| File | Problem |
|------|---------|
| `nearly_sorted.py` | Sort nearly sorted array (each element at most k positions away) |
| `k_closest_elements.py` | Find K closest elements to given value |
| `check_binary_tree_is_heap.py` | Check if binary tree is a valid heap |
| `huffman_coding.py` | Huffman coding for lossless compression |
| `connect_ropes.py` | Minimum cost to connect n ropes |
| `k_max_sum_combinations.py` | K maximum sum combinations from two arrays |
| `kth_largest_stream.py` | K-th largest element in a stream |
| `k_most_frequent_words.py` | Find K most frequent words from a file |
| `convert_min_to_max_heap.py` | Convert min heap to max heap |
| `bst_to_min_heap.py` | In-place convert BST to min heap |
| `k_closest_points_origin.py` | K closest points to origin |

### Hard Problems (`hard/`)
| File | Problem |
|------|---------|
| `skyline_problem.py` | The Skyline Problem |
| `median_stream.py` | Median of stream of integers |
| `kth_largest_sum_subarray.py` | K-th largest sum contiguous subarray |
| `merge_k_sorted_arrays.py` | Merge K sorted arrays |
| `merge_k_sorted_lists.py` | Merge K sorted linked lists |
| `smallest_range_k_lists.py` | Smallest range containing elements from K lists |
| `prims_mst.py` | Prim's Minimum Spanning Tree |
| `dijkstra.py` | Dijkstra's shortest path algorithm |
| `merge_max_heaps.py` | Merge two binary max heaps |

### Other Heap Types (`other_types/`)
| File | Type | Key Complexity |
|------|------|----------------|
| `binomial_heap.py` | Binomial Heap | O(log n) operations |
| `fibonacci_heap.py` | Fibonacci Heap | O(1) amortized insert, O(log n) extract |
| `leftist_heap.py` | Leftist Heap | O(log n) merge |
| `k_ary_heap.py` | K-ary Heap | O(k log_k n) extract |

## Heap Types Comparison

| Operation | Binary | Binomial | Fibonacci | Leftist |
|-----------|--------|----------|-----------|---------|
| Insert | O(log n) | O(log n) | O(1)* | O(log n) |
| Extract Min | O(log n) | O(log n) | O(log n)* | O(log n) |
| Union | O(n) | O(log n) | O(1)* | O(log n) |
| Decrease Key | O(log n) | O(log n) | O(1)* | O(log n) |

*Amortized time complexity

## Usage Example

```python
from heapq import heappush, heappop, heapify

# Create a min heap
heap = [3, 1, 4, 1, 5, 9]
heapify(heap)  # Convert list to heap in-place

# Add elements
heappush(heap, 2)

# Remove smallest
smallest = heappop(heap)

# For max heap, negate values
max_heap = [3, 1, 4, 1, 5, 9]
heapify([-x for x in max_heap])
```

## Run Examples

```bash
python Heap/easy/heap_sort.py
python Heap/medium/connect_ropes.py
python Heap/hard/median_stream.py
```

## References

- [GeeksforGeeks Heap Data Structure](https://www.geeksforgeeks.org/dsa/heap-data-structure/)
- [GeeksforGeeks Binary Heap](https://www.geeksforgeeks.org/binary-heap/)
- [GeeksforGeeks Applications of Heap](https://www.geeksforgeeks.org/applications-of-heap-data-structure/)
- [GeeksforGeeks Heap Sort](https://www.geeksforgeeks.org/heap-sort/)
- [GeeksforGeeks Huffman Coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)
- [GeeksforGeeks Merge K Sorted Arrays](https://www.geeksforgeeks.org/merge-k-sorted-arrays/)
- [GeeksforGeeks Median of Stream](https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/)

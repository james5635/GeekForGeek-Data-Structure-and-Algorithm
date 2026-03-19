"""
Theoretical explanations of heap data structure and related concepts.
This file provides explanations and Python equivalents of heap concepts from other languages.
"""

import heapq
import queue
from typing import List, Any, Optional


# 1. Heap using STL/C++ (show equivalent Python concepts)
def heap_stl_equivalent():
    """
    In C++ STL, heap operations are available through:
    - make_heap: converts a range into a heap
    - push_heap: adds an element to the heap
    - pop_heap: removes the largest element from the heap
    - sort_heap: sorts a heap

    Python's heapq module provides similar functionality but for min-heaps:
    - heapq.heapify: converts a list into a heap (in-place, O(n))
    - heapq.heappush: pushes an item onto the heap
    - heapq.heappop: pops the smallest item off the heap
    - heapq.heapreplace: pops and returns the smallest item, and adds a new item
    - heapq.nlargest/nsmallest: get the n largest/smallest elements
    """
    print("=== Heap STL/C++ Equivalent in Python ===")

    # Example showing heapq operations
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original data: {data}")

    # Convert to heap (equivalent to make_heap)
    heapq.heapify(data)
    print(f"After heapify (min-heap): {data}")

    # Push an element (equivalent to push_heap)
    heapq.heappush(data, 0)
    print(f"After heappush(0): {data}")

    # Pop an element (equivalent to pop_heap)
    smallest = heapq.heappop(data)
    print(f"After heappop() -> popped {smallest}: {data}")

    # Replace (pop then push)
    heapq.heapreplace(data, 7)
    print(f"After heapreplace(7): {data}")

    # Get n largest elements
    three_largest = heapq.nlargest(3, data)
    print(f"Three largest elements: {three_largest}")

    # Get n smallest elements
    three_smallest = heapq.nsmallest(3, data)
    print(f"Three smallest elements: {three_smallest}")

    print()


# 2. Priority queue in Java/C++ (show equivalent Python using queue.PriorityQueue or heapq)
def priority_queue_equivalents():
    """
    In Java: PriorityQueue class (min-heap by default)
    In C++: priority_queue (max-heap by default, but can be customized)

    Python equivalents:
    - heapq module: manual min-heap implementation
    - queue.PriorityQueue: thread-safe priority queue implementation
    """
    print("=== Priority Queue Equivalents in Python ===")

    # Method 1: Using heapq (manual, not thread-safe)
    print("1. Using heapq module (manual min-heap):")
    heap = []
    heapq.heappush(heap, (5, "Task E"))  # (priority, item)
    heapq.heappush(heap, (1, "Task A"))
    heapq.heappush(heap, (3, "Task C"))
    heapq.heappush(heap, (2, "Task B"))

    print("   Popping elements in priority order:")
    while heap:
        priority, task = heapq.heappop(heap)
        print(f"   Priority {priority}: {task}")
    print()

    # Method 2: Using queue.PriorityQueue (thread-safe)
    print("2. Using queue.PriorityQueue (thread-safe):")
    pq = queue.PriorityQueue()
    pq.put((5, "Task E"))
    pq.put((1, "Task A"))
    pq.put((3, "Task C"))
    pq.put((2, "Task B"))

    print("   Popping elements in priority order:")
    while not pq.empty():
        priority, task = pq.get()
        print(f"   Priority {priority}: {task}")
    print()

    # Note: For max-heap behavior with heapq, we can negate priorities
    print("3. Max-heap equivalent using heapq (negating priorities):")
    max_heap = []
    heapq.heappush(max_heap, (-5, "Task E"))  # Negative for max-heap
    heapq.heappush(max_heap, (-1, "Task A"))
    heapq.heappush(max_heap, (-3, "Task C"))
    heapq.heappush(max_heap, (-2, "Task B"))

    print("   Popping elements in max-priority order:")
    while max_heap:
        neg_priority, task = heapq.heappop(max_heap)
        print(f"   Priority {-neg_priority}: {task}")
    print()


# 3. Applications of heap data structure (list and brief explain)
def heap_applications_explanation():
    """
    Brief explanation of heap applications:
    1. Priority Queues: Heaps are the underlying data structure for priority queues
    2. Graph Algorithms: Dijkstra's shortest path, Prim's MST
    3. Heap Sort: Comparison-based sorting algorithm
    4. K-way Merge: Merging k sorted lists efficiently
    5. Finding Kth Largest/Smallest Element: Using min-heap or max-heap
    6. Median Maintenance: Using two heaps (max-heap for lower half, min-heap for upper half)
    7. Huffman Coding: Data compression algorithm
    8. Load Balancing: Distributing tasks across servers
    9. Event Simulation: Managing events in discrete event simulation
    10. K Most Frequent Elements: Finding top k frequent items in a stream
    """
    print("=== Applications of Heap Data Structure ===")
    applications = [
        "1. Priority Queues: Heaps efficiently support insert and extract-min/max operations",
        "2. Graph Algorithms: Dijkstra's algorithm (shortest path) and Prim's algorithm (MST)",
        "3. Heap Sort: O(n log n) comparison-based sorting algorithm",
        "4. K-way Merge: Efficiently merge k sorted arrays/lists using a min-heap",
        "5. Kth Largest/Smallest: Find kth order statistic in O(n log k) time",
        "6. Median Maintenance: Track median of a stream using two heaps",
        "7. Huffman Coding: Build optimal prefix codes for data compression",
        "8. Load Balancing: Assign tasks to least loaded servers",
        "9. Event Simulation: Process events in chronological order",
        "10. K Most Frequent: Find top k frequent elements in O(n log k) time",
    ]

    for app in applications:
        print(f"   {app}")
    print()


# Main function to demonstrate all explanations
def main():
    print("=== Heap Theoretical Concepts ===\n")

    heap_stl_equivalent()
    priority_queue_equivalents()
    heap_applications_explanation()


if __name__ == "__main__":
    main()

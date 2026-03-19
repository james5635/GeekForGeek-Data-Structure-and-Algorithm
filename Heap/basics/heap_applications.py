"""
Applications of Heap Data Structure

Heaps are used in various real-world applications due to their efficient
insert/delete operations and constant-time access to min/max element.

Time Complexity Analysis:
- Insert: O(log n)
- Delete: O(log n)
- Get Min/Max: O(1)
- Heapify: O(n)

Space Complexity: O(n)

Source: https://www.geeksforgeeks.org/applications-of-heap-data-structure/
"""

import heapq
from typing import List, Tuple, Any
from collections import defaultdict


def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """
    Merge k sorted arrays using a min-heap.

    Time: O(n log k) where n is total elements, k is number of arrays
    Space: O(k) for the heap
    """
    result = []
    min_heap = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))

    return result


def k_largest_elements(arr: List[int], k: int) -> List[int]:
    """
    Find k largest elements using a min-heap of size k.

    Time: O(n log k)
    Space: O(k)
    """
    if k >= len(arr):
        return sorted(arr, reverse=True)

    min_heap = arr[:k]
    heapq.heapify(min_heap)

    for num in arr[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)

    return sorted(min_heap, reverse=True)


def k_smallest_elements(arr: List[int], k: int) -> List[int]:
    """
    Find k smallest elements using a max-heap of size k.

    Time: O(n log k)
    Space: O(k)
    """
    if k >= len(arr):
        return sorted(arr)

    max_heap = [-x for x in arr[:k]]
    heapq.heapify(max_heap)

    for num in arr[k:]:
        if num < -max_heap[0]:
            heapq.heapreplace(max_heap, -num)

    return sorted([-x for x in max_heap])


def k_most_frequent(arr: List[Any], k: int) -> List[Tuple[Any, int]]:
    """
    Find k most frequent elements.

    Time: O(n log k)
    Space: O(n)
    """
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1

    return heapq.nlargest(k, freq.items(), key=lambda x: x[1])


def median_from_stream(stream: List[float]) -> List[float]:
    """
    Find running median from a stream of numbers using two heaps.

    Time: O(n log n)
    Space: O(n)
    """
    low = []
    high = []
    result = []

    for num in stream:
        heapq.heappush(low, -heapq.heappushpop(high, num))

        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2
        else:
            median = -low[0]

        result.append(median)

    return result


def sort_nearly_sorted(arr: List[int], k: int) -> List[int]:
    """
    Sort an array where each element is at most k positions from its sorted position.

    Time: O(n log k)
    Space: O(k)
    """
    heap = arr[: k + 1]
    heapq.heapify(heap)

    result = []
    for i in range(k + 1, len(arr)):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    while heap:
        result.append(heapq.heappop(heap))

    return result


def huffman_encoding(frequencies: List[Tuple[str, int]]) -> dict:
    """
    Huffman coding using min-heap to build optimal prefix codes.

    Time: O(n log n)
    Space: O(n)
    """
    heap = [(freq, char) for char, freq in frequencies]
    heapq.heapify(heap)

    if len(heap) == 1:
        return {heap[0][1]: "0"}

    codes = {}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for char, freq in [left, right]:
            code = codes.get(char, "")
            codes[char] = ("1" + code) if char == left[1] else ("0" + code)
            if freq != char:
                codes[char] = code

        heapq.heappush(heap, (left[0] + right[0], left[1] + right[1]))

    return codes


def dijkstra_shortest_path(graph: dict, start: str) -> dict:
    """
    Dijkstra's algorithm using priority queue (min-heap).

    Time: O((V + E) log V)
    Space: O(V)
    """
    dist = {start: 0}
    pq = [(0, start)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph.get(u, []):
            if v not in visited:
                new_dist = d + weight
                if new_dist < dist.get(v, float("inf")):
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

    return dist


def resource_allocation(tasks: List[Tuple[int, int]]) -> List[int]:
    """
    Allocate resources based on priority using min-heap.
    tasks: List of (priority, task_id) tuples
    Higher priority value = higher priority

    Time: O(n log n)
    """
    heapq.heapify(tasks)
    result = []

    while tasks:
        priority, task_id = heapq.heappop(tasks)
        result.append(task_id)

    return result


if __name__ == "__main__":
    print("=== Merge K Sorted Arrays ===")
    arrays = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
    print(f"Merged: {merge_k_sorted_arrays(arrays)}")

    print("\n=== K Largest Elements ===")
    arr = [1, 23, 12, 9, 30, 2, 50]
    print(f"3 largest: {k_largest_elements(arr, 3)}")

    print("\n=== K Smallest Elements ===")
    print(f"3 smallest: {k_smallest_elements(arr, 3)}")

    print("\n=== Running Median ===")
    stream = [5, 15, 1, 3, 8, 7, 9, 2]
    print(f"Medians: {median_from_stream(stream)}")

    print("\n=== Sort Nearly Sorted Array (k=2) ===")
    nearly_sorted = [6, 5, 3, 2, 8, 10, 9]
    print(f"Sorted: {sort_nearly_sorted(nearly_sorted, 2)}")

    print("\n=== Dijkstra's Shortest Path ===")
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 1), ("D", 5)],
        "C": [("D", 8), ("E", 10)],
        "D": [("E", 2)],
        "E": [],
    }
    print(f"From A: {dijkstra_shortest_path(graph, 'A')}")

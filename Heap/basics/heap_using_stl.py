"""
Heap Operations Using Python's heapq Module

This module provides Python equivalents to C++ STL heap functions:
- make_heap() -> heapq.heapify()
- push_heap() -> heapq.heappush()
- pop_heap() -> heapq.heappop() + heappop()
- sort_heap() -> sorted() after heapify
- is_heap() -> custom check
- is_heap_until() -> custom implementation

Time Complexity:
- heapify: O(n)
- heappush: O(log n)
- heappop: O(log n)
- sort_heap: O(n log n)

Space Complexity: O(n)

Source: https://www.geeksforgeeks.org/heap-using-stl-c/
"""

import heapq
from typing import List, Iterator, Callable


class HeapOperations:
    """Python implementation of C++ STL heap operations."""

    @staticmethod
    def make_heap(arr: List[int], reverse: bool = False) -> List[int]:
        """
        Convert a range to a heap (equivalent to std::make_heap).

        By default creates min-heap. Use reverse=True for max-heap behavior.

        Time: O(n)
        Space: O(1) in-place
        """
        if reverse:
            arr = [-x for x in arr]
        heapq.heapify(arr)
        return arr if not reverse else [-x for x in arr]

    @staticmethod
    def push_heap(arr: List[int], val: int, reverse: bool = False) -> None:
        """
        Push element to heap (equivalent to std::push_heap).

        Must be called after appending to list.
        Time: O(log n)
        """
        heapq.heappush(arr, -val if reverse else val)

    @staticmethod
    def pop_heap(arr: List[int], reverse: bool = False) -> int:
        """
        Move max/min element to end and pop (equivalent to std::pop_heap + pop_back).

        Time: O(log n)
        """
        return heapq.heappop(arr) if not reverse else -heapq.heappop(arr)

    @staticmethod
    def sort_heap(arr: List[int], reverse: bool = False) -> List[int]:
        """
        Sort heap in ascending order (equivalent to std::sort_heap).

        Time: O(n log n)
        """
        result = sorted(arr, reverse=reverse)
        arr.clear()
        arr.extend(result)
        return arr

    @staticmethod
    def is_heap(arr: List[int], reverse: bool = False) -> bool:
        """
        Check if range is a valid heap (equivalent to std::is_heap).

        Time: O(n)
        """
        n = len(arr)
        for i in range((n - 2) // 2 + 1):
            if reverse:
                left = 2 * i + 1
                right = 2 * i + 2
                if left < n and arr[i] < arr[left]:
                    return False
                if right < n and arr[i] < arr[right]:
                    return False
            else:
                left = 2 * i + 1
                right = 2 * i + 2
                if left < n and arr[i] > arr[left]:
                    return False
                if right < n and arr[i] > arr[right]:
                    return False
        return True

    @staticmethod
    def is_heap_until(arr: List[int], reverse: bool = False) -> int:
        """
        Find largest subrange that is a heap (equivalent to std::is_heap_until).

        Returns index of first element that breaks heap property.
        Time: O(n)
        """
        n = len(arr)
        for i in range((n - 2) // 2 + 1):
            left = 2 * i + 1
            right = 2 * i + 2
            if reverse:
                if left < n and arr[i] < arr[left]:
                    return left
                if right < n and arr[i] < arr[right]:
                    return right
            else:
                if left < n and arr[i] > arr[left]:
                    return left
                if right < n and arr[i] > arr[right]:
                    return right
        return n


def demo_make_heap():
    """Demonstrate make_heap equivalent."""
    print("=== make_heap equivalent ===")
    v1 = [20, 30, 40, 25, 15]
    heapq.heapify(v1)
    print(f"Max element: {max(v1)}")  # Root is not max in min-heap, use -values for max
    print(f"Heap: {v1}")


def demo_push_heap():
    """Demonstrate push_heap equivalent."""
    print("\n=== push_heap equivalent ===")
    v1 = [20, 30, 40, 10]
    heapq.heapify(v1)
    print(f"Initial heap: {v1}")

    v1.append(50)
    heapq.heappush(v1, 50)
    print(f"After push: {v1}")


def demo_pop_heap():
    """Demonstrate pop_heap equivalent."""
    print("\n=== pop_heap equivalent ===")
    v1 = [40, 10, 20, 50, 30]
    heapq.heapify(v1)
    print(f"Initial heap: {v1}")

    max_val = heapq.heappop(v1)
    print(f"Popped max: {max_val}")
    print(f"After pop: {v1}")


def demo_sort_heap():
    """Demonstrate sort_heap equivalent."""
    print("\n=== sort_heap equivalent ===")
    v1 = [20, 30, 40, 25, 15]
    heapq.heapify(v1)
    print(f"Heap elements: {v1}")

    v1.sort()
    print(f"After sort_heap: {v1}")


def demo_is_heap():
    """Demonstrate is_heap equivalent."""
    print("\n=== is_heap equivalent ===")
    v1 = [40, 30, 25, 35, 15]

    heap_ops = HeapOperations()
    result = heap_ops.is_heap(v1)
    print(f"Is heap: {result}")

    v2 = [40, 30, 25, 35, 15, 50]
    print(f"Is heap (extended): {heap_ops.is_heap(v2)}")


def demo_max_heap():
    """Demonstrate max-heap operations using negative values."""
    print("\n=== Max Heap Operations ===")
    arr = [20, 30, 40, 25, 15]

    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    print(f"Max heap (negated): {max_heap}")
    print(f"Max element: {-max_heap[0]}")


if __name__ == "__main__":
    demo_make_heap()
    demo_push_heap()
    demo_pop_heap()
    demo_sort_heap()
    demo_is_heap()
    demo_max_heap()

    print("\n" + "=" * 50)
    print("Summary of C++ STL to Python heapq mappings:")
    print("=" * 50)
    print("std::make_heap()    -> heapq.heapify()")
    print("std::push_heap()   -> heapq.heappush()")
    print("std::pop_heap()    -> heapq.heappop()")
    print("std::sort_heap()   -> heap.sort()")
    print("std::is_heap()     -> custom is_heap()")
    print("std::is_heap_until -> custom is_heap_until()")

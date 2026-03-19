"""
Heap Queue (heapq) in Python

Python's heapq module provides heap queue algorithm implementation.
A heap is a binary tree where each parent node is less than or equal to
its children (min-heap by default).

Key Operations:
- heapify(): Convert list to heap in-place
- heappush(): Push element onto heap
- heappop(): Pop and return smallest element
- heappushpop(): Push and pop in one operation
- heapreplace(): Replace smallest with new element
- nlargest(): Get n largest elements
- nsmallest(): Get n smallest elements
- merge(): Merge multiple sorted iterables

Time Complexity:
- heapify: O(n)
- heappush/pop: O(log n)
- nlargest/nsmallest: O(n log k)

Space Complexity: O(n)

Source: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
"""

import heapq
from typing import List, Any, Iterator


def create_heap() -> List[int]:
    """
    Create a heap from a list using heapify().

    Time: O(n)
    """
    li = [25, 20, 15, 30, 40]
    heapq.heapify(li)
    return li


def create_max_heap() -> List[int]:
    """
    Create a max-heap by storing negative values.

    Time: O(n)
    """
    nums = [10, 20, 15, 30, 40]
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)
    return [-x for x in max_heap]


def push_and_pop() -> None:
    """
    Demonstrate heappush() and heappop() operations.

    Time: O(log n) each
    """
    h = [10, 20, 15, 30, 40]
    heapq.heapify(h)

    heapq.heappush(h, 5)
    print(f"After push(5): {h}")

    min_val = heapq.heappop(h)
    print(f"Popped: {min_val}")
    print(f"After pop: {h}")


def push_pop_combined() -> int:
    """
    Use heappushpop() for combined operation.

    More efficient than separate push + pop.
    Time: O(log n)
    """
    h = [10, 20, 15, 30, 40]
    heapq.heapify(h)

    return heapq.heappushpop(h, 5)


def replace_operation() -> int:
    """
    Use heapreplace() to replace smallest and push new element.

    Unlike heappushpop, this always replaces before pushing.
    Time: O(log n)
    """
    h = [10, 20, 15, 30, 40]
    heapq.heapify(h)

    return heapq.heapreplace(h, 5)


def find_largest_smallest() -> None:
    """
    Find largest and smallest elements using nlargest/nsmallest.
    """
    h = [10, 20, 15, 30, 40]
    heapq.heapify(h)

    largest = heapq.nlargest(3, h)
    smallest = heapq.nsmallest(3, h)

    print(f"3 largest: {largest}")
    print(f"3 smallest: {smallest}")


def merge_heaps() -> List[int]:
    """
    Merge multiple sorted iterables.

    Time: O(n log k) where k is number of iterables
    """
    h1 = [1, 3, 5, 7]
    h2 = [2, 4, 6, 8]
    h3 = [0, 9, 10]

    merged = list(heapq.merge(h1, h2, h3))
    return merged


class HeapSort:
    """
    Heap Sort implementation using heapq.
    """

    @staticmethod
    def sort(arr: List[int], reverse: bool = False) -> List[int]:
        """
        Sort array using heap sort.

        Time: O(n log n)
        Space: O(n)
        """
        heapq.heapify(arr)

        if reverse:
            return [heapq.heappop(arr) for _ in range(len(arr))]
        else:
            return [heapq.heappop(arr) for _ in range(len(arr))][::-1]


class MinHeap:
    """Min Heap wrapper class around heapq."""

    def __init__(self):
        self._heap: List[Any] = []

    def push(self, item: Any) -> None:
        heapq.heappush(self._heap, item)

    def pop(self) -> Any:
        return heapq.heappop(self._heap)

    def peek(self) -> Any:
        return self._heap[0] if self._heap else None

    def pushpop(self, item: Any) -> Any:
        return heapq.heappushpop(self._heap, item)

    def replace(self, item: Any) -> Any:
        return heapq.heapreplace(self._heap, item)

    def nlargest(self, n: int) -> List[Any]:
        return heapq.nlargest(n, self._heap)

    def nsmallest(self, n: int) -> List[Any]:
        return heapq.nsmallest(n, self._heap)

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)

    def __repr__(self) -> str:
        return f"Heap({self._heap})"


class MaxHeap:
    """Max Heap wrapper class using negative values."""

    def __init__(self):
        self._heap: List[Any] = []

    def push(self, item: Any) -> None:
        if isinstance(item, (int, float)):
            heapq.heappush(self._heap, -item)
        else:
            raise TypeError("MaxHeap only supports numeric values")

    def pop(self) -> Any:
        return -heapq.heappop(self._heap)

    def peek(self) -> Any:
        return -self._heap[0] if self._heap else None

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)

    def __repr__(self) -> str:
        return f"MaxHeap({[-x for x in self._heap]})"


def demo_min_heap_class():
    """Demonstrate MinHeap class."""
    print("=== MinHeap Class ===")
    heap = MinHeap()

    for val in [25, 20, 15, 30, 40, 5]:
        heap.push(val)

    print(f"Heap: {heap}")
    print(f"Peek: {heap.peek()}")
    print(f"Pop: {heap.pop()}")
    print(f"Peek after pop: {heap.peek()}")
    print(f"3 smallest: {heap.nsmallest(3)}")


def demo_max_heap_class():
    """Demonstrate MaxHeap class."""
    print("\n=== MaxHeap Class ===")
    heap = MaxHeap()

    for val in [25, 20, 15, 30, 40, 50]:
        heap.push(val)

    print(f"Heap: {heap}")
    print(f"Peek (max): {heap.peek()}")
    print(f"Pop: {heap.pop()}")
    print(f"Peek after pop: {heap.peek()}")


def demo_priority_queue_with_heapq():
    """Implement priority queue using heapq."""
    print("\n=== Priority Queue using heapq ===")

    heap = []
    items = [
        (3, "Low priority task"),
        (1, "High priority task"),
        (2, "Medium priority task"),
    ]

    for priority, task in items:
        heapq.heappush(heap, (priority, task))

    while heap:
        priority, task = heapq.heappop(heap)
        print(f"Priority {priority}: {task}")


if __name__ == "__main__":
    print("=== Create Heap ===")
    print(f"Heap: {create_heap()}")

    print("\n=== Max Heap ===")
    print(f"Max Heap: {create_max_heap()}")

    print("\n=== Push and Pop ===")
    push_and_pop()

    print("\n=== Push-Pop Combined ===")
    print(f"heappushpop result: {push_pop_combined()}")

    print("\n=== Replace Operation ===")
    print(f"heapreplace result: {replace_operation()}")

    print("\n=== Largest/Smallest ===")
    find_largest_smallest()

    print("\n=== Merge ===")
    print(f"Merged: {merge_heaps()}")

    print("\n=== Heap Sort ===")
    arr = [25, 20, 15, 30, 40, 5]
    sorted_arr = sorted(
        [
            heapq.heappop(arr := arr.copy()) or arr.append(x) or arr
            for x in [25, 20, 15, 30, 40, 5]
        ][1:]
    )
    print(
        f"Sorted: {[x for x in (lambda a: [heapq.heappop(a) for _ in range(len(a))])([25, 20, 15, 30, 40, 5])]}"
    )

    print("\n=== Heap Sort Alternative ===")
    arr = [25, 20, 15, 30, 40, 5]
    result = HeapSort.sort(arr.copy())
    print(f"Sorted: {result}")

    demo_min_heap_class()
    demo_max_heap_class()
    demo_priority_queue_with_heapq()

    print("\n" + "=" * 50)
    print("heapq module functions summary:")
    print("=" * 50)
    print("heapq.heapify()      - Convert list to heap")
    print("heapq.heappush()     - Push element to heap")
    print("heapq.heappop()      - Pop smallest element")
    print("heapq.heappushpop()  - Push then pop")
    print("heapq.heapreplace()  - Pop then push")
    print("heapq.nlargest()     - Get n largest elements")
    print("heapq.nsmallest()    - Get n smallest elements")
    print("heapq.merge()        - Merge sorted iterables")

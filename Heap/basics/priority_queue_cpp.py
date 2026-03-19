"""
Priority Queue Implementation in Python

Python's equivalent to C++ std::priority_queue:
- Uses heapq as underlying data structure
- By default creates max-heap in C++, min-heap in Python (use negation)
- Supports: push, pop, peek, empty, size operations

C++ Priority Queue Features:
- add/remove elements based on priority
- Higher value = higher priority (max-heap by default)
- Custom comparator support

Time Complexity:
- push: O(log n)
- pop: O(log n)
- peek: O(1)
- empty/size: O(1)

Space Complexity: O(n)

Source: https://www.geeksforgeeks.org/priority-queue-in-cpp-stl/
"""

import heapq
from typing import TypeVar, Generic, Callable, List, Optional, Iterator

T = TypeVar("T")


class PriorityQueue(Generic[T]):
    """
    Priority Queue implementation in Python.

    By default, this is a min-priority queue (smallest element has highest priority).
    For max-priority behavior, use PriorityQueue(max_heap=True) or store negative values.
    """

    def __init__(self, max_heap: bool = False):
        self._heap: List[tuple] = []
        self._max_heap = max_heap
        self._counter = 0

    def push(self, item: T, priority: float = 0) -> None:
        """
        Add an element to the priority queue.

        Args:
            item: The element to add
            priority: Priority value (lower = higher priority for min-heap)
        """
        if self._max_heap:
            priority = -priority
        entry = (priority, self._counter, item)
        heapq.heappush(self._heap, entry)
        self._counter += 1

    def pop(self) -> Optional[T]:
        """
        Remove and return the highest priority element.

        Returns:
            The element with highest priority, or None if empty
        """
        if self.is_empty():
            return None
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Optional[T]:
        """
        Return the highest priority element without removing it.

        Returns:
            The element with highest priority, or None if empty
        """
        if self.is_empty():
            return None
        _, _, item = self._heap[0]
        return item

    def empty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self._heap) == 0

    def size(self) -> int:
        """Return the number of elements in the priority queue."""
        return len(self._heap)

    def is_empty(self) -> bool:
        """Alias for empty()."""
        return self.empty()

    def __len__(self) -> int:
        return self.size()

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __iter__(self) -> Iterator[T]:
        """Iterate over elements (note: does not preserve priority order)."""
        return (item for _, _, item in self._heap)

    def __repr__(self) -> str:
        items = sorted(self._heap, key=lambda x: x[0])
        return f"PriorityQueue({[item for _, _, item in items]})"


class MaxPriorityQueue(Generic[T]):
    """
    Max Priority Queue (highest value has highest priority).

    Equivalent to C++ std::priority_queue with default behavior.
    """

    def __init__(self):
        self._heap: List[tuple] = []
        self._counter = 0

    def push(self, item: T) -> None:
        heapq.heappush(self._heap, (-self._counter, item))
        self._counter += 1

    def pop(self) -> Optional[T]:
        if self.is_empty():
            return None
        _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Optional[T]:
        if self.is_empty():
            return None
        _, item = self._heap[0]
        return item

    def empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return self.empty()

    def __len__(self) -> int:
        return self.size()

    def __bool__(self) -> bool:
        return not self.is_empty()


class MinPriorityQueue(Generic[T]):
    """
    Min Priority Queue (smallest value has highest priority).

    Equivalent to C++ std::priority_queue<int, vector<int>, greater<int>>.
    """

    def __init__(self):
        self._heap: List[T] = []
        self._counter = 0

    def push(self, item: T) -> None:
        heapq.heappush(self._heap, (self._counter, item))
        self._counter += 1

    def pop(self) -> Optional[T]:
        if self.is_empty():
            return None
        _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._heap[0][1]

    def empty(self) -> bool:
        return len(self._heap) == 0

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return self.empty()

    def __len__(self) -> int:
        return self.size()

    def __bool__(self) -> bool:
        return not self.is_empty()


def demo_basic_operations():
    """Demonstrate basic priority queue operations."""
    print("=== Basic Priority Queue Operations ===")

    pq = PriorityQueue()

    pq.push("Task 1", 30)
    pq.push("Task 2", 10)
    pq.push("Task 3", 20)
    pq.push("Task 4", 40)

    print(f"Peek: {pq.peek()}")

    while not pq.is_empty():
        print(f"Pop: {pq.pop()}")


def demo_max_heap_default():
    """Demonstrate max-heap priority queue (C++ default behavior)."""
    print("\n=== Max Priority Queue (C++ style) ===")

    pq = MaxPriorityQueue()

    pq.push(30)
    pq.push(10)
    pq.push(20)
    pq.push(40)

    print("Elements removed in order:")
    while not pq.is_empty():
        print(pq.pop(), end=" ")
    print()


def demo_min_heap():
    """Demonstrate min-heap priority queue."""
    print("\n=== Min Priority Queue ===")

    pq = MinPriorityQueue()

    pq.push(30)
    pq.push(10)
    pq.push(20)
    pq.push(40)

    print("Elements removed in order:")
    while not pq.is_empty():
        print(pq.pop(), end=" ")
    print()


def demo_traversal():
    """Demonstrate pseudo traversal (C++ style)."""
    print("\n=== Pseudo Traversal ===")

    pq = MaxPriorityQueue()
    pq.push(9)
    pq.push(8)
    pq.push(6)

    temp = MaxPriorityQueue()
    for _ in range(len(pq)):
        temp.push(pq.peek())

    print("Elements:", end=" ")
    while not temp.is_empty():
        print(temp.pop(), end=" ")
    print()


def demo_empty_check():
    """Demonstrate empty() method."""
    print("\n=== Empty Check ===")

    pq = PriorityQueue()
    print(f"Is empty: {pq.empty()}")

    pq.push("Item", 1)
    print(f"After push, is empty: {pq.empty()}")
    print(f"Size: {pq.size()}")


def demo_with_custom_priority():
    """Demonstrate priority queue with custom priorities."""
    print("\n=== Custom Priority Queue ===")

    pq = PriorityQueue[str]()

    tasks = [
        ("Critical bug fix", 1),
        ("Feature development", 3),
        ("Code review", 2),
        ("Documentation", 4),
    ]

    for task, priority in tasks:
        pq.push(task, priority)

    print("Tasks by priority:")
    while not pq.is_empty():
        task = pq.pop()
        print(f"  - {task}")


if __name__ == "__main__":
    demo_basic_operations()
    demo_max_heap_default()
    demo_min_heap()
    demo_traversal()
    demo_empty_check()
    demo_with_custom_priority()

    print("\n" + "=" * 50)
    print("C++ Priority Queue vs Python equivalents:")
    print("=" * 50)
    print("pq.push(val)    -> pq.push(val)")
    print("pq.top()        -> pq.peek()")
    print("pq.pop()        -> pq.pop()")
    print("pq.empty()      -> pq.is_empty()")
    print("pq.size()       -> pq.size()")
    print("max-heap        -> MaxPriorityQueue()")
    print("min-heap (greater<>) -> MinPriorityQueue()")

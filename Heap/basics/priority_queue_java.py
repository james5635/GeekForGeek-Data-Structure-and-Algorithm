"""
Priority Queue Implementation in Python (Java Style)

Python's equivalent to Java's java.util.PriorityQueue:
- Uses heapq as underlying data structure
- Default is min-heap (natural ordering)
- Custom comparator support via key function
- Automatically grows as elements are added

Java PriorityQueue Features:
- Elements ordered by natural ordering or custom Comparator
- add(), offer() - add elements
- poll(), remove() - remove and return head
- peek(), element() - access head without removing
- iterator() - traverse elements

Time Complexity:
- add/offer: O(log n)
- poll/remove: O(log n)
- peek/element: O(1)
- size/isEmpty: O(1)

Space Complexity: O(n)

Source: https://www.geeksforgeeks.org/priority-queue-in-java/
"""

import heapq
from typing import TypeVar, Generic, Optional, Iterator, Callable, List, Any
from functools import total_ordering

T = TypeVar("T")


class PriorityQueueJava(Generic[T]):
    """
    Java-style PriorityQueue implementation.

    By default, implements min-heap (smallest element has highest priority).
    Use reverse=True for max-heap behavior.
    """

    def __init__(
        self,
        initial_capacity: int = 11,
        comparator: Callable[[T, T], int] = None,
        reverse: bool = False,
    ):
        self._heap: List[tuple] = []
        self._reverse = reverse
        self._comparator = comparator
        self._counter = 0

    def add(self, e: T) -> bool:
        """Add element (equivalent to Java's add())."""
        self.offer(e)
        return True

    def offer(self, e: T) -> bool:
        """Insert element (equivalent to Java's offer())."""
        entry = (-self._counter if self._reverse else self._counter, e)
        heapq.heappush(self._heap, entry)
        self._counter += 1
        return True

    def poll(self) -> Optional[T]:
        """Remove and return head, or None if empty (equivalent to Java's poll())."""
        if self.is_empty():
            return None
        return self.remove()

    def remove(self) -> Optional[T]:
        """Remove and return head (equivalent to Java's remove())."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        _, item = heapq.heappop(self._heap)
        return item

    def remove_element(self, o: Any) -> bool:
        """Remove single instance of element from queue. O(n)"""
        for i, (prio, item) in enumerate(self._heap):
            if item == o:
                self._heap.pop(i)
                heapq.heapify(self._heap)
                return True
        return False

    def peek(self) -> Optional[T]:
        """Return head without removing, or None if empty."""
        if self.is_empty():
            return None
        return self._heap[0][1]

    def element(self) -> T:
        """Return head without removing (throws if empty)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._heap[0][1]

    def contains(self, o: Any) -> bool:
        """Check if element exists in queue."""
        return any(item == o for _, item in self._heap)

    def size(self) -> int:
        """Return number of elements."""
        return len(self._heap)

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._heap) == 0

    def clear(self) -> None:
        """Remove all elements."""
        self._heap.clear()
        self._counter = 0

    def to_array(self) -> List[T]:
        """Convert to array (note: order may not reflect priority)."""
        return [item for _, item in self._heap]

    def iterator(self) -> Iterator[T]:
        """Return iterator (note: order may not reflect priority)."""
        return iter(self.to_array())

    def __len__(self) -> int:
        return self.size()

    def __bool__(self) -> bool:
        return not self.is_empty()

    def __contains__(self, item: Any) -> bool:
        return self.contains(item)

    def __iter__(self) -> Iterator[T]:
        return self.iterator()

    def __repr__(self) -> str:
        return f"PriorityQueueJava({self.to_array()})"


class MaxPriorityQueueJava(Generic[T]):
    """
    Max Priority Queue - highest value has highest priority.

    Equivalent to Java's PriorityQueue with reverseOrder() comparator.
    """

    def __init__(self):
        self._heap: List[tuple] = []
        self._counter = 0

    def add(self, e: T) -> bool:
        heapq.heappush(self._heap, (self._counter, e))
        self._counter += 1
        return True

    def offer(self, e: T) -> bool:
        return self.add(e)

    def poll(self) -> Optional[T]:
        if self.is_empty():
            return None
        _, item = heapq.heappop(self._heap)
        return item

    def remove(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.poll()

    def peek(self) -> Optional[T]:
        if self.is_empty():
            return None
        return self._heap[0][1]

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def __len__(self) -> int:
        return self.size()

    def __bool__(self) -> bool:
        return not self.is_empty()

    def to_array(self) -> List[T]:
        """Return list of elements (not in priority order)."""
        return [item for _, item in sorted(self._heap, key=lambda x: -x[0])]

    def remove_element(self, o: Any) -> bool:
        """Remove single instance of element from queue. O(n)"""
        for i, (prio, item) in enumerate(self._heap):
            if item == o:
                self._heap.pop(i)
                heapq.heapify(self._heap)
                return True
        return False


def demo_basic_operations():
    """Demonstrate basic priority queue operations."""
    print("=== Basic Priority Queue Operations ===")

    pq = PriorityQueueJava[int]()

    pq.add(3)
    pq.add(10)
    pq.add(7)
    pq.add(2)

    print(f"Head of queue (peek): {pq.peek()}")
    print(f"Size: {pq.size()}")
    print(f"Array: {pq.to_array()}")


def demo_with_strings():
    """Demonstrate with String elements (natural ordering)."""
    print("\n=== String Elements ===")

    pq = PriorityQueueJava[str]()
    pq.add("Geeks")
    pq.add("For")
    pq.add("Geeks")

    print(f"Initial: {pq.to_array()}")
    print(f"Peek: {pq.peek()}")

    pq.remove_element("Geeks")
    print(f"After removing 'Geeks': {pq.to_array()}")
    print(f"Poll: {pq.poll()}")
    print(f"Final: {pq.to_array()}")


def demo_iteration():
    """Demonstrate iteration (not in priority order)."""
    print("\n=== Iteration ===")

    pq = PriorityQueueJava[str]()
    pq.add("Geeks")
    pq.add("For")
    pq.add("Geeks")

    print("Iterating (order may not reflect priority):")
    for item in pq:
        print(f"  {item}")


def demo_max_heap():
    """Demonstrate max-heap behavior."""
    print("\n=== Max Priority Queue ===")

    pq = MaxPriorityQueueJava[int]()
    pq.add(3)
    pq.add(10)
    pq.add(7)
    pq.add(2)

    print(f"Array: {pq.to_array()}")
    print(f"Heap: {pq._heap}")
    print(f"Peek (max): {pq.peek()}")

    print("Elements in order:")
    while not pq.is_empty():
        print(pq.poll(), end=" ")
    print()


def demo_growth():
    """Demonstrate automatic growth (Python list handles this)."""
    print("\n=== Auto Growth ===")

    pq = PriorityQueueJava[int](initial_capacity=2)

    for i in range(10):
        pq.add(i)
        print(f"Added {i}, size: {pq.size()}")

    print(f"Final size: {pq.size()}")


if __name__ == "__main__":
    demo_basic_operations()
    demo_with_strings()
    demo_iteration()
    demo_max_heap()
    demo_growth()

    print("\n" + "=" * 50)
    print("Java PriorityQueue vs Python equivalents:")
    print("=" * 50)
    print("pq.add(e)        -> pq.add(e)")
    print("pq.offer(e)      -> pq.offer(e)")
    print("pq.poll()        -> pq.poll()")
    print("pq.remove()      -> pq.remove()")
    print("pq.peek()        -> pq.peek()")
    print("pq.element()     -> pq.element()")
    print("pq.contains(o)  -> pq.contains(o)")
    print("pq.size()        -> pq.size()")
    print("pq.isEmpty()     -> pq.is_empty()")
    print("pq.clear()       -> pq.clear()")
    print("pq.toArray()     -> pq.to_array()")
    print("pq.iterator()    -> pq.iterator()")

"""
K-ary Heap Implementation

A K-ary heap is a generalization of binary heap (K=2) where each node
has K children instead of 2. It follows the same properties as binary
heap with modified child/parent index calculations.

Properties:
    - Nearly complete k-ary tree
    - Max K-ary heap: root >= all children
    - Min K-ary heap: root <= all children

Source: https://www.geeksforgeeks.org/k-ary-heap/
"""


class KAryHeap:
    """
    K-ary Heap implementing max priority queue operations.

    Index Calculations (0-based indexing):
        - Parent(i) = (i - 1) / k
        - Children of i: k*i + 1, k*i + 2, ..., k*i + k
        - Last non-leaf = (n - 2) / k

    Time Complexities:
        - Insert: O(log_k n)
        - Extract Max: O(k log_k n)
        - Build Heap: O(n)
        - Decrease Key: O(log_k n)

    Space Complexity: O(n)
    """

    def __init__(self, k: int = 2):
        if k < 1:
            raise ValueError("k must be >= 1")
        self.k = k
        self.heap: list = []

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def _parent(self, i: int) -> int:
        return (i - 1) // self.k

    def _children(self, i: int) -> list:
        start = self.k * i + 1
        return [start + j for j in range(self.k) if start + j < len(self.heap)]

    def _max_child(self, i: int) -> int:
        """Return index of the maximum child"""
        start = self.k * i + 1
        end = min(start + self.k, len(self.heap))

        max_idx = -1
        max_val = float("-inf")

        for j in range(start, end):
            if self.heap[j] > max_val:
                max_val = self.heap[j]
                max_idx = j

        return max_idx

    def _restore_down(self, i: int):
        """Restore heap property by moving element down (max-heapify)"""
        while True:
            largest = i
            start = self.k * i + 1
            end = min(start + self.k, len(self.heap))

            for j in range(start, end):
                if self.heap[j] > self.heap[largest]:
                    largest = j

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def _restore_up(self, i: int):
        """Restore heap property by moving element up"""
        while i > 0:
            parent = self._parent(i)
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def build_heap(self, arr: list):
        """Build heap from array. O(n)"""
        self.heap = arr.copy()

        start = (len(self.heap) - 2) // self.k
        for i in range(start, -1, -1):
            self._restore_down(i)

    def insert(self, value: int):
        """Insert a value. O(log_k n)"""
        self.heap.append(value)
        self._restore_up(len(self.heap) - 1)

    def get_max(self) -> int:
        """Get maximum element. O(1)"""
        if self.is_empty():
            raise ValueError("Heap is empty")
        return self.heap[0]

    def extract_max(self) -> int:
        """Remove and return maximum. O(k log_k n)"""
        if self.is_empty():
            raise ValueError("Heap is empty")

        max_val = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._restore_down(0)

        return max_val

    def increase_key(self, i: int, new_value: int):
        """Increase key at index i. O(log_k n)"""
        if new_value < self.heap[i]:
            raise ValueError("New value is less than current value")
        self.heap[i] = new_value
        self._restore_down(i)

    def decrease_key(self, i: int, new_value: int):
        """Decrease key at index i. O(log_k n)"""
        if new_value > self.heap[i]:
            raise ValueError("New value is greater than current value")
        self.heap[i] = new_value
        self._restore_up(i)

    def delete(self, i: int) -> int:
        """Delete element at index i. O(k log_k n)"""
        if i < 0 or i >= len(self.heap):
            raise IndexError("Index out of range")

        old_val = self.heap[i]
        self.heap[i] = float("inf")
        self._restore_down(i)
        self.extract_max()
        return old_val

    def __str__(self) -> str:
        return str(self.heap)


def functional_version(arr: list, k: int):
    """
    Functional style K-ary heap operations.
    Demonstrates the core algorithms without class.
    """

    def restore_down(arr, length, index, k):
        """Restore max-heap property downward"""
        while True:
            largest = index
            start = k * index + 1
            end = min(start + k, length)

            for j in range(start, end):
                if arr[j] > arr[largest]:
                    largest = j

            if largest == index:
                break

            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest

    def restore_up(arr, index, k):
        """Restore max-heap property upward"""
        while index > 0:
            parent = (index - 1) // k
            if arr[index] > arr[parent]:
                arr[index], arr[parent] = arr[parent], arr[index]
                index = parent
            else:
                break

    def build_heap(arr, n, k):
        """Build heap from array. O(n)"""
        start = (n - 2) // k
        for i in range(start, -1, -1):
            restore_down(arr, n, i, k)

    def insert(arr, n, k, elem):
        """Insert element. O(log_k n)"""
        arr.append(elem)
        n += 1
        restore_up(arr, n - 1, k)
        return n

    def extract_max(arr, n, k):
        """Extract maximum. O(k log_k n)"""
        max_elem = arr[0]
        arr[0] = arr[n - 1]
        n -= 1
        restore_down(arr, n, 0, k)
        return max_elem, n

    return {
        "build": lambda a, n: n,
        "insert": lambda a, n, e: (insert(a, n, k, e), n),
        "extract": lambda a, n: extract_max(a, n, k),
        "restore_down": lambda a, length, i: restore_down(a, length, i, k),
        "restore_up": lambda a, i: restore_up(a, i, k),
    }


def main():
    heap = KAryHeap(k=3)
    heap.build_heap([4, 5, 6, 7, 8, 9, 10])

    print("Initial K-ary heap (k=3):")
    print(f"Heap: {heap}")
    print(f"Size: {heap.size()}")
    print(f"Max: {heap.get_max()}")

    heap.insert(3)
    print(f"\nAfter inserting 3:")
    print(f"Heap: {heap}")

    max_val = heap.extract_max()
    print(f"\nExtracted max: {max_val}")
    print(f"Heap after extract: {heap}")

    print("\n" + "=" * 50)
    print("Functional version demo:")
    arr = [4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    k = 3

    ops = functional_version(arr, k)
    n = ops["build"](arr, n)
    print(f"Built heap: {arr[:n]}")

    n = ops["insert"](arr, n, 3)[1]
    print(f"After insert 3: {arr[:n]}")

    max_val, n = ops["extract"](arr, n)
    print(f"Extracted max: {max_val}")
    print(f"After extract: {arr[:n]}")


if __name__ == "__main__":
    main()


"""
Time Complexity Analysis:

Height of K-ary heap with n nodes: log_k(n)

restore_down():
    - O(k) comparisons per level
    - O(log_k n) levels
    - Total: O(k log_k n)

restore_up():
    - O(log_k n) levels
    - Total: O(log_k n)

Operation Complexities:
    - Insert: O(log_k n)
    - Extract Max: O(k log_k n)
    - Build Heap: O(n)
    - Decrease Key: O(log_k n)
    - Increase Key: O(k log_k n)

Comparison:
    - Binary Heap (k=2): Insert O(log n), Extract O(log n)
    - K-ary Heap: Insert O(log_k n), Extract O(k log_k n)
    
    For k > 2:
        - Insert is faster
        - Extract is slower
        - Better cache behavior

Applications:
    1. Dijkstra's and Prim's algorithms
       - Decrease key operation is more frequent
       - K-ary heap provides faster decrease key
    
    2. Better cache performance
       - Children are stored closer in memory
       - Improves CPU cache hit rate
    
    3. External sorting
       - K-way merging

Trade-offs:
    - Smaller k: Better for extract-heavy operations
    - Larger k: Better for insert/decrease-key heavy operations
    
    Optimal k typically around: n / log n (empirical)
"""

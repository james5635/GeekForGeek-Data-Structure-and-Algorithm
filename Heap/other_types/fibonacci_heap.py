"""
Fibonacci Heap Implementation

A Fibonacci heap is a data structure for implementing priority queues.
It provides fast amortized running times for operations like insert,
merge, and extract-min.

Key Features:
    - Collection of heap-ordered trees
    - Uses lazy consolidation
    - Faster amortized times for decrease-key operations
    - Used in Dijkstra's and Prim's algorithms for better time complexity

Source: https://www.geeksforgeeks.org/fibonacci-heap-set-1-introduction/
"""

from typing import Optional, List


class FibonacciNode:
    """Node in a Fibonacci Heap"""

    def __init__(self, key: int):
        self.key = key
        self.degree = 0
        self.marked = False
        self.child: Optional["FibonacciNode"] = None
        self.left: "FibonacciNode" = self
        self.right: "FibonacciNode" = self
        self.parent: Optional["FibonacciNode"] = None


class FibonacciHeap:
    """
    Fibonacci Heap implementing priority queue operations.

    Properties:
        - Collection of trees with min-heap property
        - Trees can have any shape (unlike Binomial Heap)
        - Uses lazy consolidation for efficiency
        - Roots connected via circular doubly linked list

    Amortized Time Complexities:
        - Insert: O(1)
        - Find Min: O(1)
        - Extract Min: O(log n)
        - Merge: O(1)
        - Decrease Key: O(1)
        - Delete: O(log n)
    """

    def __init__(self):
        self.min_node: Optional[FibonacciNode] = None
        self.total_nodes: int = 0

    def is_empty(self) -> bool:
        return self.min_node is None

    def insert(self, key: int) -> FibonacciNode:
        """Insert a key into the heap. O(1) amortized"""
        node = FibonacciNode(key)

        if self.min_node is None:
            self.min_node = node
        else:
            self._link_node_to_root_list(node)
            if node.key < self.min_node.key:
                self.min_node = node

        self.total_nodes += 1
        return node

    def _link_node_to_root_list(self, node: FibonacciNode):
        """Add node to root list (circular doubly linked list)"""
        node.right = self.min_node
        node.left = self.min_node.left
        self.min_node.left.right = node
        self.min_node.left = node

    def get_min(self) -> int:
        """Return the minimum key. O(1)"""
        if self.is_empty():
            raise ValueError("Heap is empty")
        return self.min_node.key

    def extract_min(self) -> int:
        """Remove and return the minimum key. O(log n) amortized"""
        if self.is_empty():
            raise ValueError("Heap is empty")

        min_node = self.min_node
        z = min_node

        if z.child is not None:
            children = []
            child = z.child
            while True:
                children.append(child)
                child = child.right
                if child == z.child:
                    break

            for child in children:
                self._link_node_to_root_list(child)
                child.parent = None

        z.left.right = z.right
        z.right.left = z.left

        if z == z.right:
            self.min_node = None
        else:
            self.min_node = z.right
            self._consolidate()

        self.total_nodes -= 1
        return z.key

    def _consolidate(self):
        """Consolidate trees of same degree"""
        max_degree = int(self.total_nodes**0.5) + 1
        degrees: List[Optional[FibonacciNode]] = [None] * max_degree

        roots = []
        current = self.min_node
        if current:
            while True:
                roots.append(current)
                current = current.right
                if current == self.min_node:
                    break

        for root in roots:
            degree = root.degree
            while degrees[degree] is not None:
                other = degrees[degree]
                if root.key > other.key:
                    root, other = other, root
                self._heap_link(other, root)
                degrees[degree] = None
                degree += 1
            degrees[degree] = root

        self.min_node = None
        for node in degrees:
            if node is not None:
                if self.min_node is None:
                    node.left = node
                    node.right = node
                    self.min_node = node
                else:
                    self._link_node_to_root_list(node)
                    if node.key < self.min_node.key:
                        self.min_node = node

    def _heap_link(self, y: FibonacciNode, x: FibonacciNode):
        """Make y a child of x"""
        y.left.right = y.right
        y.right.left = y.left

        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.right = x.child
            y.left = x.child.left
            x.child.left.right = y
            x.child.left = y

        y.parent = x
        x.degree += 1
        y.marked = False

    def decrease_key(self, node: FibonacciNode, new_key: int):
        """Decrease key of a node. O(1) amortized"""
        if new_key > node.key:
            raise ValueError("New key is greater than current key")

        node.key = new_key
        parent = node.parent

        if parent is not None and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min_node.key:
            self.min_node = node

    def _cut(self, x: FibonacciNode, y: FibonacciNode):
        """Cut the link between x and its parent y"""
        if x == x.right:
            y.child = None
        else:
            x.left.right = x.right
            x.right.left = x.left
            if y.child == x:
                y.child = x.right

        y.degree -= 1
        self._link_node_to_root_list(x)
        x.parent = None
        x.marked = False

    def _cascading_cut(self, y: FibonacciNode):
        """Perform cascading cuts"""
        parent = y.parent
        if parent is not None:
            if not y.marked:
                y.marked = True
            else:
                self._cut(y, parent)
                self._cascading_cut(parent)

    def delete(self, node: FibonacciNode):
        """Delete a node. O(log n)"""
        self.decrease_key(node, float("-inf"))
        self.extract_min()

    def merge(self, other: "FibonacciHeap"):
        """Merge two Fibonacci heaps. O(1)"""
        if other.is_empty():
            return

        if self.is_empty():
            self.min_node = other.min_node
        else:
            self_min_right = self.min_node.right
            other_min_left = other.min_node.left

            self.min_node.right = other.min_node
            other.min_node.left = self.min_node
            other_min_left.right = self_min_right
            self_min_right.left = other_min_left

            if other.min_node.key < self.min_node.key:
                self.min_node = other.min_node

        self.total_nodes += other.total_nodes

    def size(self) -> int:
        return self.total_nodes


def main():
    heap = FibonacciHeap()

    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(15)

    print(f"Min: {heap.get_min()}")
    print(f"Extract min: {heap.extract_min()}")
    print(f"Min: {heap.get_min()}")

    heap2 = FibonacciHeap()
    heap2.insert(3)
    heap2.insert(8)

    heap.merge(heap2)
    print(f"After merge, min: {heap.get_min()}")


if __name__ == "__main__":
    main()


"""
Advantages of Fibonacci Heap:
    1. Fast amortized running time for insert, merge, decrease-key
    2. Lazy consolidation improves merge efficiency
    3. Important for Dijkstra's and Prim's algorithms
       - Binary Heap: O(V log V + E log V)
       - Fibonacci Heap: O(V log V + E)

Disadvantages:
    1. More complex structure
    2. Higher constant factors
    3. Less practical for small inputs

Amortized Time Complexities:
    - Insert: O(1)
    - Find Min: O(1)
    - Extract Min: O(log n)
    - Union/Merge: O(1)
    - Decrease Key: O(1)
    - Delete: O(log n)

Important Property:
    Every node in a Fibonacci Heap has degree at most O(log n)
    Size of subtree rooted in node of degree k >= F(k+2)
    where F(k) is k-th Fibonacci number
"""

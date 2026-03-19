"""
Binomial Heap Implementation

A Binomial Heap is a collection of Binomial Trees where each Binomial Tree
follows the Min Heap property. It provides faster union/merge operation
compared to Binary Heap.

A Binomial Tree of order k has exactly 2^k nodes and depth k.

Source: https://www.geeksforgeeks.org/binomial-heap-2/
"""

import math


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
        self.degree = 0
        self.marked = False


class BinomialHeap:
    """
    Binomial Heap implementing priority queue operations.

    Properties:
        - Faster union/merge operation compared to Binary Heap
        - Collection of Binomial Trees with min-heap property
        - At most one Binomial Tree of any degree
    """

    def __init__(self, *args):
        self.trees = list(args) if args else []
        self.min_node = None
        self.count = len(self.trees)
        if self.trees:
            self._find_min()

    def is_empty(self):
        return self.min_node is None

    def insert(self, value):
        """Insert a value into the heap. O(log n)"""
        node = Node(value)
        self.merge(BinomialHeap(node))

    def get_min(self):
        """Return the minimum value. O(1) if min_node tracked"""
        if self.is_empty():
            raise ValueError("Heap is empty")
        return self.min_node.value

    def extract_min(self):
        """Remove and return the minimum value. O(log n)"""
        if self.is_empty():
            raise ValueError("Heap is empty")

        min_node = self.min_node
        self.trees.remove(min_node)
        self.merge(BinomialHeap(*min_node.children))
        self._find_min()
        self.count -= 1
        return min_node.value

    def merge(self, other_heap):
        """Merge two binomial heaps. O(log n)"""
        self.trees.extend(other_heap.trees)
        self.count += other_heap.count
        self._consolidate()

    def _find_min(self):
        """Find the tree with minimum root value"""
        self.min_node = None
        for tree in self.trees:
            if self.min_node is None or tree.value < self.min_node.value:
                self.min_node = tree

    def decrease_key(self, node, new_value):
        """Decrease key of a node. O(log n)"""
        if new_value > node.value:
            raise ValueError("New value is greater than current value")
        node.value = new_value
        self._bubble_up(node)

    def delete(self, node):
        """Delete a specific node. O(log n)"""
        self.decrease_key(node, float("-inf"))
        self.extract_min()

    def _bubble_up(self, node):
        """Bubble up a node to maintain heap property"""
        parent = node.parent
        while parent is not None and node.value < parent.value:
            node.value, parent.value = parent.value, node.value
            node, parent = parent, node.parent

    def _link(self, tree1, tree2):
        """Link two trees - make tree2 a child of tree1"""
        if tree1.value > tree2.value:
            tree1, tree2 = tree2, tree1
        tree2.parent = tree1
        tree1.children.append(tree2)
        tree1.degree += 1

    def _consolidate(self):
        """Consolidate trees of same degree"""
        if not self.trees:
            self.min_node = None
            return

        max_degree = int(math.log(self.count, 2)) + 1 if self.count > 0 else 0
        degree_to_tree = [None] * (max_degree + 1)

        while self.trees:
            current = self.trees.pop(0)
            degree = current.degree

            while degree_to_tree[degree] is not None:
                other = degree_to_tree[degree]
                degree_to_tree[degree] = None
                if current.value < other.value:
                    self._link(current, other)
                else:
                    self._link(other, current)
                    current = other
                degree += 1
            degree_to_tree[degree] = current

        self.min_node = None
        self.trees = [tree for tree in degree_to_tree if tree is not None]
        self._find_min()

    def __len__(self):
        return self.count

    def size(self):
        return self.count


def main():
    heap = BinomialHeap()

    heap.insert(10)
    heap.insert(20)
    heap.insert(5)
    heap.insert(15)
    heap.insert(30)

    print(f"Min element: {heap.get_min()}")
    print(f"Heap size: {len(heap)}")

    print(f"Extracted: {heap.extract_min()}")
    if len(heap) > 0:
        print(f"Min element: {heap.get_min()}")

    print(f"Extracted: {heap.extract_min()}")
    if len(heap) > 0:
        print(f"Min element: {heap.get_min()}")


if __name__ == "__main__":
    main()


"""
Time Complexity:
    - Insert: O(log n)
    - Get Min: O(1)
    - Extract Min: O(log n)
    - Merge: O(log n)
    - Decrease Key: O(log n)
    - Delete: O(log n)

Space Complexity: O(n)

Comparison with Binary and Fibonacci Heap:

Operation          | Binary Heap | Binomial Heap | Fibonacci Heap
-------------------|-------------|---------------|---------------
Make Heap          | O(1)        | O(1)          | O(1)
Insert             | O(log n)    | O(log n)      | O(1)
Find Min           | O(1)        | O(log n)      | O(1)
Extract Min        | O(log n)    | O(log n)      | O(log n)
Union/Merge        | O(n)        | O(log n)      | O(1)
Decrease Key       | O(log n)    | O(log n)      | O(1)
Delete             | O(log n)    | O(log n)      | O(log n)
"""

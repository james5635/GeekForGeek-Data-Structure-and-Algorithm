"""
Leftist Tree / Leftist Heap Implementation

A leftist tree (leftist heap) is a priority queue implemented with a
variant of binary heap. Every node has an s-value (null path length)
which is the distance to the nearest leaf.

Key Properties:
    - Min Heap property: key(i) >= key(parent(i))
    - Leftist property: dist(right(i)) <= dist(left(i))
    - Rightmost path is always the shortest path to a leaf
    - Height is O(log n)

Source: https://www.geeksforgeeks.org/leftist-tree-leftist-heap/
"""


class LeftistNode:
    """Node in a Leftist Heap"""

    def __init__(self, element: int):
        self.element = element
        self.left: "LeftistNode" = None
        self.right: "LeftistNode" = None
        self.dist: int = 0


class LeftistHeap:
    """
    Leftist Heap implementing priority queue operations.

    Properties:
        - Binary tree with heap and leftist properties
        - Efficient merge operation O(log n)
        - Height is O(log n)

    Time Complexities:
        - Get Min: O(1)
        - Insert: O(log n)
        - Delete Min: O(log n)
        - Merge: O(log n)

    Space Complexity: O(n)
    """

    def __init__(self):
        self.root: LeftistNode = None

    def is_empty(self) -> bool:
        return self.root is None

    def merge(self, h1: LeftistNode, h2: LeftistNode) -> LeftistNode:
        """
        Merge two leftist heaps preserving leftist property.
        Returns the root of the merged heap.
        """
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if h1.element < h2.element:
            return self._merge1(h1, h2)
        else:
            return self._merge1(h2, h1)

    def _merge1(self, h1: LeftistNode, h2: LeftistNode) -> LeftistNode:
        """
        Merge h2 into h1.
        Assumes h1's root element is smaller than h2's.
        """
        if h1.left is None:
            h1.left = h2
        else:
            h1.right = self.merge(h1.right, h2)

            if h1.left.dist < h1.right.dist:
                self._swap_children(h1)

            h1.dist = h1.right.dist + 1 if h1.right else 1

        return h1

    def _swap_children(self, t: LeftistNode):
        """Swap left and right children of a node"""
        t.left, t.right = t.right, t.left

    def insert(self, x: int):
        """Insert an element into the heap. O(log n)"""
        new_node = LeftistNode(x)
        self.root = self.merge(new_node, self.root)

    def find_min(self) -> int:
        """Find the minimum element. O(1)"""
        if self.root is None:
            raise ValueError("Heap is empty")
        return self.root.element

    def delete_min(self) -> int:
        """Delete and return the minimum element. O(log n)"""
        if self.root is None:
            raise ValueError("Heap is empty")

        min_elem = self.root.element
        self.root = self.merge(self.root.left, self.root.right)
        return min_elem

    def make_empty(self):
        """Make the heap logically empty"""
        self.root = None

    def merge_heaps(self, other: "LeftistHeap"):
        """Merge another heap into this one"""
        if self is other:
            return
        self.root = self.merge(self.root, other.root)
        other.root = None


def _print_tree(node: LeftistNode, level: int = 0, prefix: str = "Root: "):
    """Helper to visualize the heap structure"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.element) + f" (dist={node.dist})")
        if node.left or node.right:
            if node.left:
                _print_tree(node.left, level + 1, "L: ")
            else:
                print(" " * ((level + 1) * 4) + "L: None")
            if node.right:
                _print_tree(node.right, level + 1, "R: ")
            else:
                print(" " * ((level + 1) * 4) + "R: None")


def main():
    h = LeftistHeap()
    h1 = LeftistHeap()

    arr = [1, 5, 7, 10, 15]
    arr1 = [22, 75]

    for item in arr:
        h.insert(item)

    for item in arr1:
        h1.insert(item)

    print("Heap h after insertions:")
    _print_tree(h.root)
    print()

    print("Heap h1 after insertions:")
    _print_tree(h1.root)
    print()

    print(f"Delete min from h: {h.delete_min()}")
    print(f"Delete min from h1: {h1.delete_min()}")

    h.merge_heaps(h1)
    print("\nHeap after merging h and h1:")
    _print_tree(h.root)
    print()

    print(f"Delete min from merged heap: {h.delete_min()}")


if __name__ == "__main__":
    main()


"""
Merge Operation Details:
    1. Compare roots of two heaps
    2. Make smaller root the new root
    3. Keep left subtree, recursively merge right subtree with other heap
    4. Swap children if leftist property violated
    5. Update distance value

Example:
    Heap 1:      Heap 2:      Merged:
        1            22          1
       / \          / \         / \
      5   7       75   30     5     7
                            / \   /
                           22 75 30

Time Complexity Analysis:
    - The rightmost path is always O(log n)
    - Merge operations primarily work on right path
    - Therefore, merge is O(log n)

Advantages:
    1. Efficient merge operation
    2. Simple implementation
    3. Good for algorithms requiring many merges

Disadvantages:
    1. Insert is O(log n) (slower than binomial heap O(1))
    2. Uses more memory for dist values

Comparison with Binary and Binomial Heaps:

Operation     | Binary Heap | Binomial Heap | Leftist Heap
--------------|-------------|---------------|--------------
Get Min       | O(1)        | O(log n)      | O(1)
Delete Min    | O(log n)    | O(log n)      | O(log n)
Insert        | O(log n)    | O(1)          | O(log n)
Merge         | O(n)        | O(log n)      | O(log n)

Applications:
    - Used in external sorting
    - Priority queue implementations
    - Any scenario requiring efficient merging
"""

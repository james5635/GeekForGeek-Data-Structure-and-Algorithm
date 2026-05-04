"""
Disjoint Set Union-Find Algorithm

This module implements the basic Disjoint Set (Union-Find) data structure
which maintains a collection of disjoint (non-overlapping) sets.

Operations:
    - make_set: Create a new set containing a single element.
    - find: Determine which set an element belongs to (returns the representative/root).
    - union: Merge two sets into a single set.

Time Complexity (naive implementation):
    - find: O(n) worst case (tree can become skewed like a linked list)
    - union: O(n) worst case

Space Complexity: O(n) for storing parent array.

Reference: https://www.geeksforgeeks.org/problems/disjoint-set-union-find/1
"""


class UnionFind:
    """A basic implementation of the Disjoint Set Union-Find data structure.

    Each element is represented as a node in a tree. The root of each tree
    serves as the representative of the set. Initially, every element is in
    its own singleton set (parent[i] == i).

    Attributes:
        parent: List where parent[i] stores the parent of element i.
                If parent[i] == i, then i is the representative of its set.
        size: Total number of elements tracked.
    """

    def __init__(self, size: int) -> None:
        """Initialize Union-Find structure with `size` elements.

        Each element starts in its own set, so parent[i] = i for all i.

        Args:
            size: Number of elements (indexed 0 to size-1).
        """
        self.parent: list[int] = list(range(size))
        self.size = size

    def find(self, i: int) -> int:
        """Find the representative (root) of the set containing element i.

        Recursively traverses the parent pointers until reaching a node
        whose parent is itself (the root/representative).

        Args:
            i: The element to find the representative for.

        Returns:
            The representative (root) of the set containing i.

        Raises:
            IndexError: If i is out of bounds.
        """
        if i < 0 or i >= self.size:
            raise IndexError(f"Element {i} is out of bounds [0, {self.size})")

        # If i is the root, return it
        if self.parent[i] == i:
            return i

        # Recursively find the representative of the parent
        return self.find(self.parent[i])

    def union(self, i: int, j: int) -> None:
        """Merge the sets containing elements i and j.

        Finds the representatives of both sets and makes the representative
        of i's set point to the representative of j's set.

        Args:
            i: First element.
            j: Second element.
        """
        # Find representatives of both sets
        i_rep = self.find(i)
        j_rep = self.find(j)

        # If they are already in the same set, nothing to do
        if i_rep == j_rep:
            return

        # Make i's representative point to j's representative
        self.parent[i_rep] = j_rep

    def is_connected(self, i: int, j: int) -> bool:
        """Check if two elements belong to the same set.

        Args:
            i: First element.
            j: Second element.

        Returns:
            True if i and j are in the same set, False otherwise.
        """
        return self.find(i) == self.find(j)

    def get_sets(self) -> dict[int, list[int]]:
        """Get a dictionary mapping each representative to its members.

        Returns:
            A dict where keys are representatives and values are lists
            of elements belonging to that set.
        """
        sets: dict[int, list[int]] = {}
        for i in range(self.size):
            rep = self.find(i)
            if rep not in sets:
                sets[rep] = []
            sets[rep].append(i)
        return sets


if __name__ == "__main__":
    print("=" * 60)
    print("Disjoint Set Union-Find - Basic Implementation")
    print("=" * 60)

    n = 5
    uf = UnionFind(n)
    print(f"\nCreated UnionFind with {n} elements (0 to {n - 1})")
    print(f"Initial parent array: {uf.parent}")

    print("\n--- Union Operations ---")

    uf.union(0, 2)
    print(f"After union(0, 2): parent = {uf.parent}")
    print(f"  find(0) = {uf.find(0)}, find(2) = {uf.find(2)}")

    uf.union(4, 2)
    print(f"After union(4, 2): parent = {uf.parent}")
    print(f"  find(4) = {uf.find(4)}, find(2) = {uf.find(2)}")

    uf.union(3, 1)
    print(f"After union(3, 1): parent = {uf.parent}")
    print(f"  find(3) = {uf.find(3)}, find(1) = {uf.find(1)}")

    print("\n--- Connectivity Checks ---")

    print(f"Is 4 connected to 0? {uf.is_connected(4, 0)}")
    print(f"Is 1 connected to 0? {uf.is_connected(1, 0)}")
    print(f"Is 3 connected to 1? {uf.is_connected(3, 1)}")

    print("\n--- Current Sets ---")
    sets = uf.get_sets()
    for rep, members in sets.items():
        print(f"  Set with representative {rep}: {members}")

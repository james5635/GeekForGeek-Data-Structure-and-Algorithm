"""
Union by Rank and Path Compression in Union-Find Algorithm

This module implements an optimized Disjoint Set (Union-Find) data structure
using two key optimizations:

1. Path Compression (improves find):
   When find() is called on element x, the root of the tree is returned.
   Path compression makes the found root the direct parent of x, flattening
   the tree. This means subsequent find operations on the same path are faster.

2. Union by Rank (improves union):
   Rank approximates the height of each tree. During union, the shorter tree
   is attached under the root of the taller tree to minimize overall tree height.
   If ranks are equal, one tree is attached to the other and the resulting
   rank is incremented by 1.

Time Complexity (with optimizations):
    - Nearly constant amortized time: O(alpha(n)), where alpha is the
      inverse Ackermann function (alpha(n) <= 4 for all practical values of n).

Space Complexity: O(n) for parent and rank arrays.

Reference: https://www.geeksforgeeks.org/problems/union-by-rank-and-path-compression/1
"""


class DisjointSet:
    """Optimized Disjoint Set with Union by Rank and Path Compression.

    This implementation uses two optimizations to keep tree heights minimal:

    - Path Compression: During find(), every node on the path to the root
      is re-pointed directly to the root, flattening the tree.
    - Union by Rank: During union(), the tree with smaller rank (height)
      is attached under the tree with larger rank to minimize height growth.

    Attributes:
        parent: List where parent[i] stores the parent of element i.
        rank:   List where rank[i] stores the approximate tree height
                rooted at i (only meaningful when i is a representative).
    """

    def __init__(self, n: int) -> None:
        """Initialize DisjointSet with n elements.

        Each element starts as its own set with rank 0.

        Args:
            n: Number of elements (indexed 0 to n-1).
        """
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n

    def find(self, i: int) -> int:
        """Find the representative of the set containing element i with path compression.

        After finding the root, this method makes the root the direct parent
        of i (and all ancestors on the path), compressing the path for future lookups.

        Args:
            i: The element to find the representative for.

        Returns:
            The representative (root) of the set containing i.

        Raises:
            IndexError: If i is out of bounds.
        """
        if i < 0 or i >= len(self.parent):
            raise IndexError(f"Element {i} is out of bounds [0, {len(self.parent)})")

        root = self.parent[i]

        # Path Compression: recursively find root and update parent
        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]

        return root

    def union(self, x: int, y: int) -> None:
        """Merge the sets containing x and y using union by rank.

        The tree with smaller rank is attached under the root of the tree
        with larger rank. If ranks are equal, one is attached to the other
        and the resulting rank is incremented.

        Args:
            x: First element.
            y: Second element.
        """
        x_root = self.find(x)
        y_root = self.find(y)

        # Already in the same set
        if x_root == y_root:
            return

        # Union by Rank: attach shorter tree under taller tree
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[y_root] < self.rank[x_root]:
            self.parent[y_root] = x_root
        else:
            # Ranks are equal: attach y under x and increment x's rank
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def is_connected(self, x: int, y: int) -> bool:
        """Check if x and y belong to the same set.

        Args:
            x: First element.
            y: Second element.

        Returns:
            True if x and y are in the same set, False otherwise.
        """
        return self.find(x) == self.find(y)

    def get_num_sets(self) -> int:
        """Return the number of disjoint sets.

        Returns:
            The count of elements that are their own parent (representatives).
        """
        return sum(1 for i in range(len(self.parent)) if self.parent[i] == i)

    def get_sets(self) -> dict[int, list[int]]:
        """Get a dictionary mapping each representative to its set members.

        Returns:
            A dict where keys are representatives and values are lists
            of elements belonging to that set.
        """
        sets: dict[int, list[int]] = {}
        for i in range(len(self.parent)):
            rep = self.find(i)
            if rep not in sets:
                sets[rep] = []
            sets[rep].append(i)
        return sets


class UnionBySize:
    """Alternative Disjoint Set implementation using Union by Size with Path Compression.

    Instead of tracking rank (approximate height), this version tracks the
    actual size (number of elements) of each tree. The smaller tree is always
    attached under the larger tree.

    Attributes:
        parent: List where parent[i] stores the parent of element i.
        size:   List where size[i] stores the number of elements in the
                tree rooted at i (only meaningful when i is a representative).
    """

    def __init__(self, n: int) -> None:
        """Initialize UnionBySize with n elements.

        Args:
            n: Number of elements (indexed 0 to n-1).
        """
        self.parent: list[int] = list(range(n))
        self.size: list[int] = [1] * n

    def find(self, i: int) -> int:
        """Find the representative of the set containing element i with path compression.

        Args:
            i: The element to find the representative for.

        Returns:
            The representative (root) of the set containing i.

        Raises:
            IndexError: If i is out of bounds.
        """
        if i < 0 or i >= len(self.parent):
            raise IndexError(f"Element {i} is out of bounds [0, {len(self.parent)})")

        root = self.parent[i]

        if self.parent[root] != root:
            self.parent[i] = self.find(root)
            return self.parent[i]

        return root

    def union(self, x: int, y: int) -> None:
        """Merge the sets containing x and y using union by size.

        The tree with fewer elements is attached under the tree with more elements.

        Args:
            x: First element.
            y: Second element.
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]

    def get_set_size(self, i: int) -> int:
        """Get the size of the set containing element i.

        Args:
            i: An element in the set.

        Returns:
            The number of elements in the set containing i.
        """
        return self.size[self.find(i)]

    def is_connected(self, x: int, y: int) -> bool:
        """Check if x and y belong to the same set.

        Args:
            x: First element.
            y: Second element.

        Returns:
            True if x and y are in the same set, False otherwise.
        """
        return self.find(x) == self.find(y)

    def get_sets(self) -> dict[int, list[int]]:
        """Get a dictionary mapping each representative to its set members.

        Returns:
            A dict where keys are representatives and values are lists
            of elements belonging to that set.
        """
        sets: dict[int, list[int]] = {}
        for i in range(len(self.parent)):
            rep = self.find(i)
            if rep not in sets:
                sets[rep] = []
            sets[rep].append(i)
        return sets


if __name__ == "__main__":
    print("=" * 60)
    print("Union by Rank and Path Compression")
    print("=" * 60)

    # --- Example from GFG: Friend relationships ---
    n = 5
    ds = DisjointSet(n)
    print(f"\nCreated DisjointSet with {n} persons (IDs 0 to {n - 1})")
    print(f"Initial parent: {ds.parent}")
    print(f"Initial rank:   {ds.rank}")

    print("\n--- Union Operations ---")

    ds.union(0, 2)
    print(f"union(0, 2) -> parent: {ds.parent}, rank: {ds.rank}")

    ds.union(4, 2)
    print(f"union(4, 2) -> parent: {ds.parent}, rank: {ds.rank}")

    ds.union(3, 1)
    print(f"union(3, 1) -> parent: {ds.parent}, rank: {ds.rank}")

    print("\n--- Connectivity Checks ---")

    print(f"Is 4 a friend of 0? {ds.is_connected(4, 0)}")
    print(f"Is 1 a friend of 0? {ds.is_connected(1, 0)}")

    print(f"\nNumber of disjoint sets: {ds.get_num_sets()}")
    print("Sets:", ds.get_sets())

    # --- Union by Size demonstration ---
    print("\n" + "=" * 60)
    print("Union by Size (Alternative)")
    print("=" * 60)

    ds_size = UnionBySize(n)
    print(f"\nCreated UnionBySize with {n} elements")

    ds_size.union(0, 1)
    print(f"union(0, 1) -> parent: {ds_size.parent}, size: {ds_size.size}")

    ds_size.union(2, 3)
    print(f"union(2, 3) -> parent: {ds_size.parent}, size: {ds_size.size}")

    ds_size.union(0, 4)
    print(f"union(0, 4) -> parent: {ds_size.parent}, size: {ds_size.size}")

    print("\n--- Final Representatives ---")
    for i in range(n):
        print(
            f"  Element {i}: Representative = {ds_size.find(i)}, Set size = {ds_size.get_set_size(i)}"
        )

    print("\nSets:", ds_size.get_sets())

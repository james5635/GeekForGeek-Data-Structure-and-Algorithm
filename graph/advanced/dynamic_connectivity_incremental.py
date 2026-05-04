"""
Dynamic Connectivity - Incremental (Union-Find)

Support two operations on a dynamic set of elements:
1. Union(u, v): Merge the sets containing u and v
2. Find(u): Return the representative of the set containing u
3. Connected(u, v): Check if u and v are in the same set

This is the incremental version: only unions are added (no deletions).

Optimizations:
- Path Compression: Flatten the tree during find operations
- Union by Rank/Size: Attach shorter tree under taller tree

Time Complexity (with both optimizations):
- Find: O(alpha(n)) ~ O(1) amortized
- Union: O(alpha(n)) ~ O(1) amortized
- Connected: O(alpha(n)) ~ O(1) amortized

where alpha is the inverse Ackermann function
"""

from typing import List, Dict, Optional


class UnionFind:
    """Union-Find (Disjoint Set Union) with path compression and union by rank."""

    def __init__(self, n: int):
        """
        Initialize Union-Find with n elements (0 to n-1).

        Args:
            n: Number of elements
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        """
        Find the representative of the set containing x with path compression.

        Args:
            x: Element to find

        Returns:
            Representative (root) of the set
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing x and y by rank.

        Args:
            x: First element
            y: Second element

        Returns:
            True if union was performed (different sets), False if already same set
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        self.size[root_x] += self.size[root_y]
        self.num_components -= 1

        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)

    def get_size(self, x: int) -> int:
        """Get the size of the set containing x."""
        return self.size[self.find(x)]

    def get_components(self) -> Dict[int, List[int]]:
        """
        Get all connected components.

        Returns:
            Dictionary mapping root -> list of elements in that component
        """
        components: Dict[int, List[int]] = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        return components


class UnionFindByName:
    """Union-Find for elements identified by names/labels instead of integers."""

    def __init__(self):
        self.parent: Dict[str, str] = {}
        self.rank: Dict[str, int] = {}
        self.size: Dict[str, int] = {}

    def _make_set(self, x: str) -> None:
        """Create a new set for element x if it doesn't exist."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.size[x] = 1

    def find(self, x: str) -> str:
        """Find representative with path compression."""
        self._make_set(x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str) -> bool:
        """Union by rank."""
        self._make_set(x)
        self._make_set(y)

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        self.size[root_x] += self.size[root_y]

        return True

    def connected(self, x: str, y: str) -> bool:
        """Check connectivity."""
        return self.find(x) == self.find(y)


def count_connected_components(n: int, edges: List[List[int]]) -> int:
    """
    Count the number of connected components in an undirected graph.

    Args:
        n: Number of vertices
        edges: List of edges

    Returns:
        Number of connected components
    """
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.num_components


if __name__ == "__main__":
    # Example 1: Basic Union-Find operations
    print("=== Example 1: Basic Operations ===")
    uf = UnionFind(10)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(6, 7)
    uf.union(8, 9)
    uf.union(1, 3)

    print(f"Components: {uf.num_components}")
    print(f"0 and 2 connected: {uf.connected(0, 2)}")
    print(f"0 and 1 connected: {uf.connected(0, 1)}")
    print(f"Size of component containing 0: {uf.get_size(0)}")

    # Example 2: Get all components
    print("\n=== Example 2: All Components ===")
    uf2 = UnionFind(8)
    uf2.union(0, 1)
    uf2.union(1, 2)
    uf2.union(3, 4)
    uf2.union(5, 6)
    uf2.union(6, 7)

    components = uf2.get_components()
    for root, members in components.items():
        print(f"  Component {root}: {members}")

    # Example 3: Count connected components
    print("\n=== Example 3: Count Components ===")
    edges = [[0, 1], [1, 2], [3, 4], [5, 6]]
    count = count_connected_components(7, edges)
    print(f"Connected components: {count}")  # 7 vertices, 3 edges -> 4 components

    # Example 4: Union-Find by name
    print("\n=== Example 4: Named Elements ===")
    uf3 = UnionFindByName()
    uf3.union("Alice", "Bob")
    uf3.union("Bob", "Charlie")
    uf3.union("Dave", "Eve")

    print(f"Alice connected to Charlie: {uf3.connected('Alice', 'Charlie')}")
    print(f"Alice connected to Dave: {uf3.connected('Alice', 'Dave')}")

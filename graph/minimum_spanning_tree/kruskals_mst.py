"""
Kruskal's Minimum Spanning Tree (MST) Algorithm

Kruskal's algorithm is a greedy algorithm that finds the Minimum Spanning Tree (MST)
of a connected, undirected, weighted graph. It works by sorting all edges by weight
and iteratively adding the smallest edge that doesn't form a cycle.

Algorithm:
1. Sort all edges in non-decreasing order of their weights.
2. Initialize a Disjoint Set Union (DSU) structure for cycle detection.
3. Iterate through sorted edges and add each edge to the MST if it doesn't form
   a cycle (i.e., its endpoints are in different components).
4. Continue until V-1 edges are added (where V is the number of vertices).

Time Complexity: O(E log E) or O(E log V)
Space Complexity: O(V + E)
"""

from typing import List, Tuple


class DisjointSet:
    """Disjoint Set Union (DSU) data structure with path compression and union by rank."""

    def __init__(self, n: int) -> None:
        """
        Initialize DSU with n elements.

        Args:
            n: Number of elements.
        """
        self.parent: List[int] = list(range(n))
        self.rank: List[int] = [0] * n

    def find(self, x: int) -> int:
        """
        Find the root/representative of the set containing x with path compression.

        Args:
            x: Element to find.

        Returns:
            Root of the set containing x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing x and y using union by rank.

        Args:
            x: First element.
            y: Second element.

        Returns:
            True if union was performed, False if x and y were already in the same set.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Graph:
    """Represents an undirected weighted graph using edge list."""

    def __init__(self, vertices: int) -> None:
        """
        Initialize the graph.

        Args:
            vertices: Number of vertices in the graph.
        """
        self.V = vertices
        self.edges: List[Tuple[int, int, int]] = []

    def add_edge(self, u: int, v: int, w: int) -> None:
        """
        Add an undirected edge to the graph.

        Args:
            u: First vertex.
            v: Second vertex.
            w: Weight of the edge.
        """
        self.edges.append((u, v, w))

    def kruskal_mst(self) -> List[Tuple[int, int, int]]:
        """
        Find the Minimum Spanning Tree using Kruskal's algorithm.

        Returns:
            List of tuples (u, v, weight) representing edges in the MST.
        """
        # Sort edges by weight
        sorted_edges = sorted(self.edges, key=lambda e: e[2])

        dsu = DisjointSet(self.V)
        mst_edges: List[Tuple[int, int, int]] = []

        for u, v, w in sorted_edges:
            if dsu.union(u, v):
                mst_edges.append((u, v, w))
                if len(mst_edges) == self.V - 1:
                    break

        return mst_edges

    def mst_weight(self) -> int:
        """
        Calculate the total weight of the MST.

        Returns:
            Total weight of the Minimum Spanning Tree.
        """
        edges = self.kruskal_mst()
        return sum(w for _, _, w in edges)


def kruskals_mst(
    num_vertices: int, edges: List[Tuple[int, int, int]]
) -> List[Tuple[int, int, int]]:
    """
    Find MST using Kruskal's algorithm (convenience function).

    Args:
        num_vertices: Number of vertices in the graph.
        edges: List of tuples (u, v, weight) representing graph edges.

    Returns:
        List of tuples (u, v, weight) representing edges in the MST.
    """
    g = Graph(num_vertices)
    for u, v, w in edges:
        g.add_edge(u, v, w)
    return g.kruskal_mst()


if __name__ == "__main__":
    # Example 1: Standard example
    print("=" * 50)
    print("Kruskal's MST Algorithm - Example 1")
    print("=" * 50)
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    mst_edges = g.kruskal_mst()
    print("Edges in MST:")
    total_weight = 0
    for u, v, w in mst_edges:
        print(f"  {u} -- {v} == {w}")
        total_weight += w
    print(f"Total MST Weight: {total_weight}")

    # Example 2: Larger graph
    print("\n" + "=" * 50)
    print("Kruskal's MST Algorithm - Example 2")
    print("=" * 50)
    edges_list = [
        (0, 1, 2),
        (0, 3, 1),
        (0, 4, 4),
        (1, 2, 3),
        (1, 3, 3),
        (1, 5, 7),
        (2, 3, 5),
        (2, 5, 8),
        (3, 4, 9),
    ]
    mst = kruskals_mst(6, edges_list)
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"  {u} -- {v} == {w}")
    print(f"Total MST Weight: {sum(w for _, _, w in mst)}")

"""
Boruvka's Algorithm for Minimum Spanning Tree

Boruvka's algorithm is one of the oldest MST algorithms (discovered in 1926 by
Otakar Boruvka). It is a greedy algorithm that works by repeatedly finding the
cheapest edge from each component to a different component.

Algorithm:
1. Initialize each vertex as a separate component.
2. Repeat until only one component remains:
   a. For each component, find the cheapest edge connecting it to another component.
   b. Add all these cheapest edges to the MST.
   c. Merge the components connected by these edges.
3. The result is the Minimum Spanning Tree.

Key Properties:
- Each iteration at least halves the number of components.
- The algorithm runs in O(E log V) time.
- Unlike Prim's and Kruskal's, it doesn't require sorting edges or a priority queue.
- Particularly useful for parallel/distributed implementations.

Time Complexity: O(E log V)
Space Complexity: O(V)
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
        Find the root of the set containing x with path compression.

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
            True if union was performed, False if already in the same set.
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

    def boruvka_mst(self) -> Tuple[List[Tuple[int, int, int]], int]:
        """
        Find the Minimum Spanning Tree using Boruvka's algorithm.

        Returns:
            Tuple of (mst_edges, mst_weight) where mst_edges is a list of
            (u, v, weight) tuples and mst_weight is the total weight.
        """
        dsu = DisjointSet(self.V)
        num_components = self.V
        mst_edges: List[Tuple[int, int, int]] = []
        mst_weight = 0

        while num_components > 1:
            # For each component, store the cheapest edge: cheapest[component] = (u, v, w)
            cheapest: List[Tuple[int, int, int] | None] = [None] * self.V

            # Find the cheapest edge for each component
            for u, v, w in self.edges:
                set_u = dsu.find(u)
                set_v = dsu.find(v)

                if set_u != set_v:
                    # Update cheapest edge for component set_u
                    if cheapest[set_u] is None or cheapest[set_u][2] > w:
                        cheapest[set_u] = (u, v, w)

                    # Update cheapest edge for component set_v
                    if cheapest[set_v] is None or cheapest[set_v][2] > w:
                        cheapest[set_v] = (u, v, w)

            # Add all cheapest edges to MST
            for i in range(self.V):
                if cheapest[i] is not None:
                    u, v, w = cheapest[i]
                    set_u = dsu.find(u)
                    set_v = dsu.find(v)

                    if set_u != set_v:
                        dsu.union(set_u, set_v)
                        mst_edges.append((u, v, w))
                        mst_weight += w
                        num_components -= 1

        return mst_edges, mst_weight

    def display_mst(self) -> None:
        """Print the MST found by Boruvka's algorithm."""
        mst_edges, mst_weight = self.boruvka_mst()
        print("Edges in MST:")
        for u, v, w in mst_edges:
            print(f"  {u} -- {v} == {w}")
        print(f"Total weight of MST: {mst_weight}")


def boruvkas_mst(
    num_vertices: int, edges: List[Tuple[int, int, int]]
) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Find MST using Boruvka's algorithm (convenience function).

    Args:
        num_vertices: Number of vertices in the graph.
        edges: List of tuples (u, v, weight) representing graph edges.

    Returns:
        Tuple of (mst_edges, mst_weight).
    """
    g = Graph(num_vertices)
    for u, v, w in edges:
        g.add_edge(u, v, w)
    return g.boruvka_mst()


if __name__ == "__main__":
    # Example 1: Standard example
    print("=" * 50)
    print("Boruvka's MST Algorithm - Example 1")
    print("=" * 50)
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.display_mst()

    # Example 2: Larger graph from TheAlgorithms/Python
    print("\n" + "=" * 50)
    print("Boruvka's MST Algorithm - Example 2")
    print("=" * 50)
    edges_list = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    mst_edges, mst_weight = boruvkas_mst(4, edges_list)
    print("Edges in MST:")
    for u, v, w in mst_edges:
        print(f"  {u} -- {v} == {w}")
    print(f"Total MST Weight: {mst_weight}")

    # Example 3: 8-vertex graph
    print("\n" + "=" * 50)
    print("Boruvka's MST Algorithm - Example 3")
    print("=" * 50)
    V = 8
    g2 = Graph(V)
    g2.add_edge(0, 1, 10)
    g2.add_edge(0, 2, 6)
    g2.add_edge(0, 3, 5)
    g2.add_edge(1, 3, 15)
    g2.add_edge(2, 3, 4)
    g2.add_edge(3, 4, 8)
    g2.add_edge(4, 5, 10)
    g2.add_edge(4, 6, 6)
    g2.add_edge(4, 7, 12)
    g2.add_edge(5, 7, 15)
    g2.add_edge(6, 7, 14)

    g2.display_mst()

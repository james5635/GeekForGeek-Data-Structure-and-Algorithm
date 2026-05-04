"""
Reverse Delete Algorithm for Minimum Spanning Tree

The Reverse Delete algorithm is the reverse of Kruskal's algorithm. While Kruskal's
builds the MST by adding edges, Reverse Delete starts with the full graph and
removes edges.

Algorithm:
1. Sort all edges in decreasing order of their weights.
2. Initialize MST as the original graph.
3. Iterate through sorted edges (highest weight first):
   - Temporarily remove the edge from the graph.
   - Check if the graph becomes disconnected.
   - If disconnected, add the edge back (it's part of the MST).
   - If still connected, the edge is permanently removed.
4. The remaining edges form the MST.

This is a greedy algorithm that removes the heaviest edges first, keeping only
those edges whose removal would disconnect the graph.

Time Complexity: O(E * (V + E) + E log E) - naive implementation
Space Complexity: O(V + E)
"""

from typing import List, Tuple


class Graph:
    """Represents an undirected weighted graph for Reverse Delete MST algorithm."""

    def __init__(self, vertices: int) -> None:
        """
        Initialize the graph.

        Args:
            vertices: Number of vertices in the graph.
        """
        self.V = vertices
        self.adj: List[List[int]] = [[] for _ in range(vertices)]
        self.edges: List[Tuple[int, int, int]] = []  # (weight, u, v)

    def add_edge(self, u: int, v: int, w: int) -> None:
        """
        Add an undirected edge to the graph.

        Args:
            u: First vertex.
            v: Second vertex.
            w: Weight of the edge.
        """
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.edges.append((w, u, v))

    def _dfs(self, v: int, visited: List[bool]) -> None:
        """
        Depth-First Search from vertex v.

        Args:
            v: Starting vertex.
            visited: Array tracking visited vertices.
        """
        visited[v] = True
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited)

    def is_connected(self) -> bool:
        """
        Check if the graph is connected.

        Returns:
            True if all vertices are reachable from vertex 0, False otherwise.
        """
        visited = [False] * self.V
        self._dfs(0, visited)
        return all(visited)

    def _remove_edge(self, u: int, v: int) -> None:
        """Remove edge (u, v) from the adjacency list."""
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def _add_edge(self, u: int, v: int) -> None:
        """Add edge (u, v) back to the adjacency list."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def reverse_delete_mst(self) -> List[Tuple[int, int, int]]:
        """
        Find the Minimum Spanning Tree using the Reverse Delete algorithm.

        Returns:
            List of tuples (u, v, weight) representing edges in the MST.
        """
        # Sort edges by weight (increasing order, we'll iterate backwards)
        self.edges.sort(key=lambda e: e[0])

        mst_edges: List[Tuple[int, int, int]] = []
        mst_weight = 0

        # Iterate through edges in decreasing order of weight
        for i in range(len(self.edges) - 1, -1, -1):
            weight, u, v = self.edges[i]

            # Temporarily remove the edge
            self._remove_edge(u, v)

            # Check if graph becomes disconnected
            if not self.is_connected():
                # Add edge back - it's part of MST
                self._add_edge(u, v)
                mst_edges.append((u, v, weight))
                mst_weight += weight

        return mst_edges, mst_weight

    def display_mst(self) -> None:
        """Print the MST found by Reverse Delete algorithm."""
        mst_edges, mst_weight = self.reverse_delete_mst()
        print("Edges in MST:")
        for u, v, w in mst_edges:
            print(f"  ({u}, {v}) weight={w}")
        print(f"Total weight of MST: {mst_weight}")


def reverse_delete_mst(
    num_vertices: int, edges: List[Tuple[int, int, int]]
) -> Tuple[List[Tuple[int, int, int]], int]:
    """
    Find MST using Reverse Delete algorithm (convenience function).

    Args:
        num_vertices: Number of vertices in the graph.
        edges: List of tuples (u, v, weight) representing graph edges.

    Returns:
        Tuple of (mst_edges, mst_weight).
    """
    g = Graph(num_vertices)
    for u, v, w in edges:
        g.add_edge(u, v, w)
    return g.reverse_delete_mst()


if __name__ == "__main__":
    # Example 1: 9-vertex graph from GeeksforGeeks
    print("=" * 50)
    print("Reverse Delete MST Algorithm - Example 1")
    print("=" * 50)
    V = 9
    g = Graph(V)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)

    g.display_mst()

    # Example 2: Smaller graph
    print("\n" + "=" * 50)
    print("Reverse Delete MST Algorithm - Example 2")
    print("=" * 50)
    edges_list = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    mst_edges, mst_weight = reverse_delete_mst(4, edges_list)
    print("Edges in MST:")
    for u, v, w in mst_edges:
        print(f"  {u} -- {v} == {w}")
    print(f"Total MST Weight: {mst_weight}")

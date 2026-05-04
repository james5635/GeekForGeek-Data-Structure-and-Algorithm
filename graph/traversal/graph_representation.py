"""
Graph Data Structure - Representation using Adjacency List and Adjacency Matrix.

A graph is a collection of nodes (vertices) connected by edges. This module
provides two common representations:
  1. Adjacency List - space-efficient for sparse graphs, O(V + E) space
  2. Adjacency Matrix - fast edge lookup, O(V^2) space

Supports both directed and undirected graphs, weighted and unweighted.
"""

from __future__ import annotations

from collections import deque
from typing import Any


class GraphAdjacencyList:
    """Graph represented using an adjacency list.

    Attributes:
        vertices: Number of vertices in the graph.
        directed: Whether the graph is directed.
        weighted: Whether the graph is weighted.
        adj: Dictionary mapping each vertex to a list of (neighbor, weight) tuples.
    """

    def __init__(
        self, vertices: int, directed: bool = False, weighted: bool = False
    ) -> None:
        """Initialize an empty graph.

        Args:
            vertices: Number of vertices (labeled 0 to vertices-1).
            directed: If True, edges are directed. Default is False (undirected).
            weighted: If True, edges carry weights. Default is False.
        """
        self.vertices = vertices
        self.directed = directed
        self.weighted = weighted
        self.adj: dict[int, list[tuple[int, float]]] = {i: [] for i in range(vertices)}

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        """Add an edge between vertices u and v.

        Args:
            u: Source vertex.
            v: Destination vertex.
            weight: Edge weight (used only if graph is weighted).
        """
        w = weight if self.weighted else 1
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

    def remove_edge(self, u: int, v: int) -> None:
        """Remove the edge from u to v (and v to u if undirected).

        Args:
            u: Source vertex.
            v: Destination vertex.
        """
        self.adj[u] = [(nbr, w) for nbr, w in self.adj[u] if nbr != v]
        if not self.directed:
            self.adj[v] = [(nbr, w) for nbr, w in self.adj[v] if nbr != u]

    def has_edge(self, u: int, v: int) -> bool:
        """Check if an edge exists from u to v.

        Args:
            u: Source vertex.
            v: Destination vertex.

        Returns:
            True if edge exists, False otherwise.
        """
        return any(nbr == v for nbr, _ in self.adj[u])

    def get_neighbors(self, vertex: int) -> list[int]:
        """Return list of neighbors of a vertex.

        Args:
            vertex: The vertex to query.

        Returns:
            List of adjacent vertex labels.
        """
        return [nbr for nbr, _ in self.adj[vertex]]

    def degree(self, vertex: int) -> int:
        """Return the degree of a vertex.

        For directed graphs, returns out-degree.

        Args:
            vertex: The vertex to query.

        Returns:
            Number of edges incident to the vertex.
        """
        return len(self.adj[vertex])

    def display(self) -> None:
        """Print the adjacency list representation."""
        for vertex in range(self.vertices):
            neighbors = self.adj[vertex]
            if neighbors:
                edges = ", ".join(
                    f"{nbr}(w={w})" if self.weighted else str(nbr)
                    for nbr, w in neighbors
                )
                print(f"{vertex} -> {edges}")
            else:
                print(f"{vertex} -> ")


class GraphAdjacencyMatrix:
    """Graph represented using an adjacency matrix.

    Attributes:
        vertices: Number of vertices in the graph.
        directed: Whether the graph is directed.
        weighted: Whether the graph is weighted.
        matrix: 2D list where matrix[i][j] stores edge weight or 1/0.
    """

    def __init__(
        self, vertices: int, directed: bool = False, weighted: bool = False
    ) -> None:
        """Initialize an empty graph with a VxV zero matrix.

        Args:
            vertices: Number of vertices (labeled 0 to vertices-1).
            directed: If True, edges are directed. Default is False.
            weighted: If True, edges carry weights. Default is False.
        """
        self.vertices = vertices
        self.directed = directed
        self.weighted = weighted
        fill_val = 0.0 if weighted else 0
        self.matrix: list[list[float]] = [
            [fill_val] * vertices for _ in range(vertices)
        ]

    def add_edge(self, u: int, v: int, weight: float = 1) -> None:
        """Add an edge between vertices u and v.

        Args:
            u: Source vertex.
            v: Destination vertex.
            weight: Edge weight (used only if graph is weighted).
        """
        w = weight if self.weighted else 1
        self.matrix[u][v] = w
        if not self.directed:
            self.matrix[v][u] = w

    def remove_edge(self, u: int, v: int) -> None:
        """Remove the edge from u to v (and v to u if undirected).

        Args:
            u: Source vertex.
            v: Destination vertex.
        """
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0

    def has_edge(self, u: int, v: int) -> bool:
        """Check if an edge exists from u to v.

        Args:
            u: Source vertex.
            v: Destination vertex.

        Returns:
            True if edge exists, False otherwise.
        """
        return self.matrix[u][v] != 0

    def get_neighbors(self, vertex: int) -> list[int]:
        """Return list of neighbors of a vertex.

        Args:
            vertex: The vertex to query.

        Returns:
            List of adjacent vertex labels.
        """
        return [j for j, val in enumerate(self.matrix[vertex]) if val != 0]

    def degree(self, vertex: int) -> int:
        """Return the degree of a vertex.

        For directed graphs, returns out-degree.

        Args:
            vertex: The vertex to query.

        Returns:
            Number of edges incident to the vertex.
        """
        return sum(1 for val in self.matrix[vertex] if val != 0)

    def display(self) -> None:
        """Print the adjacency matrix representation."""
        header = "   " + " ".join(f"{j:>3}" for j in range(self.vertices))
        print(header)
        for i in range(self.vertices):
            row = " ".join(f"{self.matrix[i][j]:>3.0f}" for j in range(self.vertices))
            print(f"{i}: {row}")


def build_graph_from_edges(
    num_vertices: int,
    edges: list[tuple[Any, ...]],
    directed: bool = False,
    weighted: bool = False,
) -> GraphAdjacencyList:
    """Convenience function to build a graph from an edge list.

    Args:
        num_vertices: Number of vertices.
        edges: List of edges. Each edge is (u, v) or (u, v, weight).
        directed: Whether the graph is directed.
        weighted: Whether the graph is weighted.

    Returns:
        A GraphAdjacencyList instance.
    """
    g = GraphAdjacencyList(num_vertices, directed=directed, weighted=weighted)
    for edge in edges:
        if len(edge) == 3:
            g.add_edge(edge[0], edge[1], edge[2])
        else:
            g.add_edge(edge[0], edge[1])
    return g


if __name__ == "__main__":
    print("=" * 60)
    print("Adjacency List - Undirected Unweighted Graph")
    print("=" * 60)
    g1 = GraphAdjacencyList(5, directed=False, weighted=False)
    g1.add_edge(0, 1)
    g1.add_edge(0, 4)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(1, 4)
    g1.add_edge(2, 3)
    g1.add_edge(3, 4)
    g1.display()

    print(f"\nNeighbors of 1: {g1.get_neighbors(1)}")
    print(f"Degree of 1: {g1.degree(1)}")
    print(f"Edge 0->1 exists: {g1.has_edge(0, 1)}")
    print(f"Edge 0->2 exists: {g1.has_edge(0, 2)}")

    print("\n" + "=" * 60)
    print("Adjacency List - Directed Weighted Graph")
    print("=" * 60)
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
    g2 = build_graph_from_edges(4, edges, directed=True, weighted=True)
    g2.display()

    print("\n" + "=" * 60)
    print("Adjacency Matrix - Undirected Unweighted Graph")
    print("=" * 60)
    m1 = GraphAdjacencyMatrix(5, directed=False, weighted=False)
    m1.add_edge(0, 1)
    m1.add_edge(0, 4)
    m1.add_edge(1, 2)
    m1.add_edge(1, 3)
    m1.add_edge(1, 4)
    m1.add_edge(2, 3)
    m1.add_edge(3, 4)
    m1.display()

    print(f"\nNeighbors of 1: {m1.get_neighbors(1)}")
    print(f"Degree of 1: {m1.degree(1)}")

    print("\n" + "=" * 60)
    print("Adjacency Matrix - Directed Weighted Graph")
    print("=" * 60)
    m2 = GraphAdjacencyMatrix(4, directed=True, weighted=True)
    m2.add_edge(0, 1, 4)
    m2.add_edge(0, 2, 1)
    m2.add_edge(2, 1, 2)
    m2.add_edge(1, 3, 1)
    m2.add_edge(2, 3, 5)
    m2.display()

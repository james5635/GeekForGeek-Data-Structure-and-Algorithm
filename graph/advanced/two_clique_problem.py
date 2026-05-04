"""
Two Clique Problem - Check if Graph Can Be Divided Into Two Cliques

A clique is a subset of vertices where every pair is connected by an edge.
The two-clique problem asks: Can the vertices of a graph be partitioned into
two disjoint cliques?

Key Insight:
A graph can be divided into two cliques if and only if its complement graph
is bipartite.

Why? In the complement graph:
- If two vertices are NOT connected in the original, they ARE connected in complement
- A bipartite complement means we can split vertices into two groups where
  no two vertices within a group are connected in the complement
- This means within each group, all pairs ARE connected in the original = clique

Algorithm:
1. Build the complement graph
2. Check if complement is bipartite using BFS/DFS 2-coloring

Time Complexity: O(V^2) for complement + O(V + E') for bipartite check
Space Complexity: O(V^2)
"""

from typing import List, Tuple, Optional
from collections import deque


def is_bipartite(num_vertices: int, adj: List[List[int]]) -> Tuple[bool, List[int]]:
    """
    Check if a graph is bipartite using BFS 2-coloring.

    Args:
        num_vertices: Number of vertices
        adj: Adjacency list

    Returns:
        Tuple of (is_bipartite, coloring) where coloring[i] = 0 or 1
    """
    color = [-1] * num_vertices

    for start in range(num_vertices):
        if color[start] != -1:
            continue

        # BFS from this start vertex
        queue = deque([start])
        color[start] = 0

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False, []

    return True, color


def build_complement(num_vertices: int, adj: List[List[int]]) -> List[List[int]]:
    """
    Build the complement graph.

    Args:
        num_vertices: Number of vertices
        adj: Adjacency list of original graph

    Returns:
        Adjacency list of complement graph
    """
    # Convert to set for O(1) lookup
    edge_set = set()
    for u in range(num_vertices):
        for v in adj[u]:
            edge_set.add((u, v))

    complement: List[List[int]] = [[] for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if (i, j) not in edge_set and (j, i) not in edge_set:
                complement[i].append(j)
                complement[j].append(i)

    return complement


def can_divide_into_two_cliques(num_vertices: int, edges: List[List[int]]) -> bool:
    """
    Check if graph can be partitioned into two cliques.

    Args:
        num_vertices: Number of vertices
        edges: List of undirected edges

    Returns:
        True if possible, False otherwise
    """
    # Build adjacency list
    adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Build complement
    complement = build_complement(num_vertices, adj)

    # Check if complement is bipartite
    is_bip, _ = is_bipartite(num_vertices, complement)
    return is_bip


def find_two_cliques(
    num_vertices: int, edges: List[List[int]]
) -> Optional[Tuple[List[int], List[int]]]:
    """
    Find the two cliques if they exist.

    Args:
        num_vertices: Number of vertices
        edges: List of undirected edges

    Returns:
        Tuple of two clique vertex lists, or None if not possible
    """
    adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    complement = build_complement(num_vertices, adj)
    is_bip, coloring = is_bipartite(num_vertices, complement)

    if not is_bip:
        return None

    clique1 = [i for i in range(num_vertices) if coloring[i] == 0]
    clique2 = [i for i in range(num_vertices) if coloring[i] == 1]

    return clique1, clique2


def verify_clique(num_vertices: int, edges: List[List[int]], clique: List[int]) -> bool:
    """Verify that a subset of vertices forms a clique."""
    edge_set = set()
    for u, v in edges:
        edge_set.add((min(u, v), max(u, v)))

    for i in range(len(clique)):
        for j in range(i + 1, len(clique)):
            u, v = min(clique[i], clique[j]), max(clique[i], clique[j])
            if (u, v) not in edge_set:
                return False
    return True


if __name__ == "__main__":
    # Example 1: Graph that CAN be divided into two cliques
    print("=== Example 1: Two Cliques Possible ===")
    # Clique 1: {0, 1, 2}, Clique 2: {3, 4}
    edges1 = [
        [0, 1],
        [0, 2],
        [1, 2],  # Clique 1 (triangle)
        [3, 4],  # Clique 2 (edge)
        [0, 3],
        [0, 4],  # Cross edges
        [1, 3],
        [1, 4],  # Cross edges
        [2, 3],
        [2, 4],  # Cross edges
    ]
    result = can_divide_into_two_cliques(5, edges1)
    print(f"Can divide into two cliques: {result}")

    cliques = find_two_cliques(5, edges1)
    if cliques:
        c1, c2 = cliques
        print(f"Clique 1: {c1}")
        print(f"Clique 2: {c2}")
        print(f"Clique 1 verified: {verify_clique(5, edges1, c1)}")
        print(f"Clique 2 verified: {verify_clique(5, edges1, c2)}")

    # Example 2: Graph that CANNOT be divided
    print("\n=== Example 2: Two Cliques Not Possible ===")
    # A simple path 0-1-2-3 cannot be split into two cliques
    edges2 = [[0, 1], [1, 2], [2, 3]]
    result2 = can_divide_into_two_cliques(4, edges2)
    print(f"Can divide into two cliques: {result2}")

    # Example 3: Complete graph (trivially one clique)
    print("\n=== Example 3: Complete Graph ===")
    edges3 = [[0, 1], [0, 2], [1, 2]]
    result3 = can_divide_into_two_cliques(3, edges3)
    print(f"Can divide into two cliques: {result3}")

"""
Peterson Graph Problem

The Petersen graph is a famous graph with 10 vertices and 15 edges.
It is:
- 3-regular (every vertex has degree 3)
- Has diameter 2
- Has chromatic number 3
- Has no Hamiltonian cycle but has a Hamiltonian path
- Is the smallest snark (bridgeless cubic graph with chromatic index 4)
- Is vertex-transitive but not edge-transitive

This module provides utilities to construct the Petersen graph,
verify its properties, and solve common problems on it.

Construction:
- Vertices: 0-9
- Outer cycle: 0-1-2-3-4-0
- Inner star: 5-7-9-6-8-5 (Petersen inner connections)
- Spokes: 0-5, 1-6, 2-7, 3-8, 4-9
"""

from typing import List, Tuple, Dict, Optional
from collections import deque


def create_petersen_graph() -> List[List[int]]:
    """
    Create the Petersen graph as an adjacency list.

    Returns:
        Adjacency list for the Petersen graph
    """
    adj: List[List[int]] = [[] for _ in range(10)]

    # Outer cycle: 0-1-2-3-4-0
    outer = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]

    # Inner star: 5-7-9-6-8-5
    inner = [(5, 7), (7, 9), (9, 6), (6, 8), (8, 5)]

    # Spokes: connect outer to inner
    spokes = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]

    for u, v in outer + inner + spokes:
        adj[u].append(v)
        adj[v].append(u)

    return adj


def get_petersen_edges() -> List[Tuple[int, int]]:
    """
    Get all edges of the Petersen graph.

    Returns:
        List of edges as (u, v) tuples
    """
    outer = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    inner = [(5, 7), (7, 9), (9, 6), (6, 8), (8, 5)]
    spokes = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    return outer + inner + spokes


def is_petersen_graph(adj: List[List[int]]) -> bool:
    """
    Verify if a graph is isomorphic to the Petersen graph.

    Checks:
    - 10 vertices
    - 15 edges
    - 3-regular (all vertices have degree 3)
    - Diameter 2

    Args:
        adj: Adjacency list to check

    Returns:
        True if graph is Petersen graph
    """
    if len(adj) != 10:
        return False

    total_edges = sum(len(neighbors) for neighbors in adj) // 2
    if total_edges != 15:
        return False

    if not all(len(neighbors) == 3 for neighbors in adj):
        return False

    # Check diameter is 2
    return _get_diameter(adj) == 2


def _get_diameter(adj: List[List[int]]) -> int:
    """Calculate the diameter of a graph using BFS from each vertex."""
    n = len(adj)
    max_dist = 0

    for start in range(n):
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        max_dist = max(max_dist, max(dist))

    return max_dist


def find_hamiltonian_path_petersen() -> Optional[List[int]]:
    """
    Find a Hamiltonian path in the Petersen graph.

    Returns:
        List of vertices forming a Hamiltonian path, or None
    """
    adj = create_petersen_graph()

    # Known Hamiltonian path in Petersen graph
    path = [0, 1, 2, 3, 4, 9, 6, 8, 5, 7]

    # Verify it's valid
    for i in range(len(path) - 1):
        if path[i + 1] not in adj[path[i]]:
            return None  # Invalid path

    return path


def find_longest_cycle_petersen() -> List[int]:
    """
    Find the longest cycle in the Petersen graph.

    The Petersen graph has no Hamiltonian cycle (10-cycle).
    The longest cycle is a 9-cycle.

    Returns:
        Vertices of the longest cycle
    """
    # A 9-cycle in the Petersen graph
    return [0, 1, 2, 3, 4, 9, 6, 8, 5]


def is_bipartite_petersen(adj: Optional[List[List[int]]] = None) -> bool:
    """
    Check if the Petersen graph is bipartite.

    The Petersen graph contains odd cycles, so it is NOT bipartite.

    Returns:
        False (always)
    """
    if adj is None:
        adj = create_petersen_graph()

    color = [-1] * 10
    color[0] = 0
    queue = deque([0])

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                return False

    return True


def petersen_graph_properties() -> Dict:
    """
    Get all key properties of the Petersen graph.

    Returns:
        Dictionary with properties
    """
    adj = create_petersen_graph()
    edges = get_petersen_edges()

    return {
        "num_vertices": 10,
        "num_edges": 15,
        "is_3_regular": True,
        "diameter": 2,
        "radius": 2,
        "chromatic_number": 3,
        "chromatic_index": 4,  # It's a snark
        "is_bipartite": False,
        "has_hamiltonian_cycle": False,
        "has_hamiltonian_path": True,
        "is_vertex_transitive": True,
        "is_edge_transitive": False,
        "is_planar": False,
        "girth": 5,  # Length of shortest cycle
        "automorphism_group_size": 120,
    }


if __name__ == "__main__":
    # Example 1: Create and display Petersen graph
    print("=== Petersen Graph Properties ===")
    adj = create_petersen_graph()
    edges = get_petersen_edges()

    print(f"Vertices: 10")
    print(f"Edges: {len(edges)}")
    print(f"\nAdjacency list:")
    for i, neighbors in enumerate(adj):
        print(f"  Vertex {i}: {sorted(neighbors)}")

    # Example 2: Verify properties
    print("\n=== Properties ===")
    props = petersen_graph_properties()
    for key, value in props.items():
        print(f"  {key}: {value}")

    # Example 3: Hamiltonian path
    print("\n=== Hamiltonian Path ===")
    path = find_hamiltonian_path_petersen()
    if path:
        print(f"Path: {' -> '.join(map(str, path))}")
        print(f"Length: {len(path) - 1} edges")

    # Example 4: Longest cycle
    print("\n=== Longest Cycle ===")
    cycle = find_longest_cycle_petersen()
    print(f"Longest cycle: {' -> '.join(map(str, cycle))} -> {cycle[0]}")
    print(f"Cycle length: {len(cycle)} vertices")

    # Example 5: Isomorphism check
    print("\n=== Isomorphism Check ===")
    print(f"Is Petersen graph: {is_petersen_graph(adj)}")

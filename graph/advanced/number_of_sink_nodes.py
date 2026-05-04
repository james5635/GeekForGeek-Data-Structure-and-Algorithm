"""
Number of Sink Nodes in a Graph

A sink node in a directed graph is a vertex with out-degree 0
(no outgoing edges).

This is different from a universal sink (which also requires in-degree = V-1).
A sink node simply has no outgoing edges.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List


def count_sink_nodes(num_vertices: int, edges: List[List[int]]) -> int:
    """
    Count the number of sink nodes (out-degree = 0).

    Args:
        num_vertices: Number of vertices
        edges: List of [u, v] directed edges

    Returns:
        Number of sink nodes
    """
    has_outgoing = [False] * num_vertices

    for u, v in edges:
        has_outgoing[u] = True

    return sum(1 for v in range(num_vertices) if not has_outgoing[v])


def find_sink_nodes(num_vertices: int, edges: List[List[int]]) -> List[int]:
    """
    Find all sink nodes.

    Args:
        num_vertices: Number of vertices
        edges: List of directed edges

    Returns:
        List of sink node indices
    """
    has_outgoing = [False] * num_vertices

    for u, v in edges:
        has_outgoing[u] = True

    return [v for v in range(num_vertices) if not has_outgoing[v]]


def count_sink_nodes_adjlist(adj: List[List[int]]) -> int:
    """
    Count sink nodes using adjacency list.

    Args:
        adj: Adjacency list

    Returns:
        Number of sink nodes
    """
    return sum(1 for neighbors in adj if len(neighbors) == 0)


def is_sink(vertex: int, num_vertices: int, edges: List[List[int]]) -> bool:
    """
    Check if a specific vertex is a sink.

    Args:
        vertex: Vertex to check
        num_vertices: Number of vertices
        edges: List of directed edges

    Returns:
        True if vertex is a sink
    """
    for u, v in edges:
        if u == vertex:
            return False
    return True


def get_sink_analysis(num_vertices: int, edges: List[List[int]]) -> dict:
    """
    Get comprehensive analysis of sink nodes.

    Args:
        num_vertices: Number of vertices
        edges: List of directed edges

    Returns:
        Dictionary with sink analysis
    """
    out_degree = [0] * num_vertices
    in_degree = [0] * num_vertices

    for u, v in edges:
        out_degree[u] += 1
        in_degree[v] += 1

    sinks = [v for v in range(num_vertices) if out_degree[v] == 0]

    return {
        "num_sinks": len(sinks),
        "sink_nodes": sinks,
        "out_degrees": out_degree,
        "in_degrees": in_degree,
        "has_any_sink": len(sinks) > 0,
        "all_sinks": len(sinks) == num_vertices,
    }


if __name__ == "__main__":
    # Example 1: Basic sink count
    print("=== Example 1: Count Sink Nodes ===")
    edges1 = [[0, 1], [0, 2], [1, 2], [2, 3]]
    count = count_sink_nodes(4, edges1)
    print(f"Sink nodes: {count}")  # Vertex 3 is the only sink
    print(f"Sink vertices: {find_sink_nodes(4, edges1)}")

    # Example 2: Multiple sinks
    print("\n=== Example 2: Multiple Sinks ===")
    edges2 = [[0, 1], [0, 2]]
    sinks2 = find_sink_nodes(5, edges2)
    print(f"Sink nodes: {sinks2}")  # 2, 3, 4 are sinks
    print(f"Count: {len(sinks2)}")

    # Example 3: Adjacency list
    print("\n=== Example 3: Adjacency List ===")
    adj3 = [[1, 2], [2], [], [], []]
    count3 = count_sink_nodes_adjlist(adj3)
    print(f"Sink nodes: {count3}")  # Vertices 2, 3, 4

    # Example 4: Full analysis
    print("\n=== Example 4: Full Analysis ===")
    edges4 = [[0, 1], [1, 2], [0, 3], [4, 5]]
    analysis = get_sink_analysis(6, edges4)
    print(f"Number of sinks: {analysis['num_sinks']}")
    print(f"Sink nodes: {analysis['sink_nodes']}")
    print(f"Out-degrees: {analysis['out_degrees']}")
    print(f"In-degrees: {analysis['in_degrees']}")

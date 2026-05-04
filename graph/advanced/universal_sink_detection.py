"""
Universal Sink Detection in a Directed Graph

A universal sink in a directed graph is a vertex that has:
- In-degree = V - 1 (all other vertices have edges to it)
- Out-degree = 0 (no edges going out from it)

Efficient O(V) approach using adjacency matrix:
- Start from (0, 0) in the matrix
- If M[i][j] = 1, then i cannot be a sink (has outgoing edge), move to i+1
- If M[i][j] = 0, then j cannot be a sink (no incoming from i), move to j+1
- After reaching boundary, verify the candidate

Time Complexity: O(V) with adjacency matrix, O(V + E) with adjacency list
Space Complexity: O(1)
"""

from typing import List, Optional


def find_universal_sink_matrix(adj_matrix: List[List[int]]) -> int:
    """
    Find universal sink using adjacency matrix in O(V) time.

    Args:
        adj_matrix: V x V adjacency matrix where M[i][j] = 1 means edge i->j

    Returns:
        Index of universal sink, or -1 if none exists
    """
    n = len(adj_matrix)
    if n == 0:
        return -1

    # Phase 1: Find candidate in O(V)
    i, j = 0, 0
    while i < n and j < n:
        if adj_matrix[i][j] == 1:
            # i has an outgoing edge, so i cannot be sink
            i += 1
        else:
            # j has no incoming edge from i, so j cannot be sink
            j += 1

    # Candidate is i (if i < n)
    if i >= n:
        return -1

    candidate = i

    # Phase 2: Verify candidate is a universal sink
    # Check: out-degree = 0 (row should be all 0s)
    for k in range(n):
        if adj_matrix[candidate][k] == 1:
            return -1

    # Check: in-degree = V-1 (column should be all 1s except diagonal)
    for k in range(n):
        if k != candidate and adj_matrix[k][candidate] == 0:
            return -1

    return candidate


def find_universal_sink_adjlist(num_vertices: int, adj: List[List[int]]) -> int:
    """
    Find universal sink using adjacency list in O(V + E) time.

    Args:
        num_vertices: Number of vertices
        adj: Adjacency list

    Returns:
        Index of universal sink, or -1 if none exists
    """
    # Calculate in-degree and out-degree
    in_degree = [0] * num_vertices
    out_degree = [0] * num_vertices

    for u in range(num_vertices):
        out_degree[u] = len(adj[u])
        for v in adj[u]:
            in_degree[v] += 1

    # Find vertex with in-degree = V-1 and out-degree = 0
    for v in range(num_vertices):
        if in_degree[v] == num_vertices - 1 and out_degree[v] == 0:
            return v

    return -1


def has_universal_sink(num_vertices: int, edges: List[List[int]]) -> bool:
    """
    Check if a universal sink exists given edge list.

    Args:
        num_vertices: Number of vertices
        edges: List of [u, v] directed edges

    Returns:
        True if universal sink exists
    """
    in_degree = [0] * num_vertices
    out_degree = [0] * num_vertices

    for u, v in edges:
        out_degree[u] += 1
        in_degree[v] += 1

    return any(
        in_degree[v] == num_vertices - 1 and out_degree[v] == 0
        for v in range(num_vertices)
    )


def get_universal_sink_info(num_vertices: int, edges: List[List[int]]) -> dict:
    """
    Get detailed info about universal sink.

    Args:
        num_vertices: Number of vertices
        edges: List of directed edges

    Returns:
        Dictionary with sink info
    """
    in_degree = [0] * num_vertices
    out_degree = [0] * num_vertices

    for u, v in edges:
        out_degree[u] += 1
        in_degree[v] += 1

    sink = -1
    for v in range(num_vertices):
        if in_degree[v] == num_vertices - 1 and out_degree[v] == 0:
            sink = v
            break

    return {
        "has_sink": sink != -1,
        "sink_vertex": sink if sink != -1 else None,
        "in_degrees": in_degree,
        "out_degrees": out_degree,
    }


if __name__ == "__main__":
    # Example 1: Graph with universal sink
    print("=== Example 1: Universal Sink at vertex 3 ===")
    # 0->3, 1->3, 2->3 (3 has in-degree 3, out-degree 0)
    adj1 = [[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
    sink1 = find_universal_sink_matrix(adj1)
    print(f"Universal sink: {sink1}")

    # Example 2: No universal sink
    print("\n=== Example 2: No Universal Sink ===")
    adj2 = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    sink2 = find_universal_sink_matrix(adj2)
    print(f"Universal sink: {sink2}")  # -1

    # Example 3: Adjacency list approach
    print("\n=== Example 3: Adjacency List ===")
    adj3 = [[3], [3], [3], []]
    sink3 = find_universal_sink_adjlist(4, adj3)
    print(f"Universal sink: {sink3}")

    # Example 4: Edge list approach
    print("\n=== Example 4: Edge List ===")
    edges = [[0, 4], [1, 4], [2, 4], [3, 4]]
    info = get_universal_sink_info(5, edges)
    print(f"Has sink: {info['has_sink']}")
    print(f"Sink vertex: {info['sink_vertex']}")
    print(f"In-degrees: {info['in_degrees']}")
    print(f"Out-degrees: {info['out_degrees']}")

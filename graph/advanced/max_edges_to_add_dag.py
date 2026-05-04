"""
Maximum Edges That Can Be Added to DAG While Keeping It a DAG

Given a directed acyclic graph (DAG), find the maximum number of additional
edges that can be added without creating any cycles.

Approach:
- In a DAG with V nodes, the maximum possible edges is V*(V-1)/2 (all forward
  edges in a topological ordering).
- The answer is simply: max_possible_edges - existing_edges

Time Complexity: O(V + E) for counting edges
Space Complexity: O(1)
"""

from typing import List


def max_edges_to_add(num_vertices: int, edges: List[List[int]]) -> int:
    """
    Calculate maximum edges that can be added to a DAG while keeping it a DAG.

    Args:
        num_vertices: Number of vertices in the DAG (0 to V-1)
        edges: List of directed edges [u, v]

    Returns:
        Maximum number of additional edges that can be added
    """
    max_possible = num_vertices * (num_vertices - 1) // 2
    existing = len(edges)
    return max_possible - existing


def max_edges_to_add_with_topo_sort(adj: List[List[int]]) -> List[List[int]]:
    """
    Find which specific edges can be added to the DAG using topological sort.

    Args:
        adj: Adjacency list representation of the DAG

    Returns:
        List of edges [u, v] that can be added
    """
    n = len(adj)

    # Kahn's algorithm for topological sort
    indegree = [0] * n
    for u in range(n):
        for v in adj[u]:
            indegree[v] += 1

    queue = [i for i in range(n) if indegree[i] == 0]
    topo_order = []

    while queue:
        u = queue.pop(0)
        topo_order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # Build edge existence set for O(1) lookup
    exists = set()
    for u in range(n):
        for v in adj[u]:
            exists.add((u, v))

    # Find all forward edges not already present
    addable = []
    for i in range(n):
        for j in range(i + 1, n):
            u, v = topo_order[i], topo_order[j]
            if (u, v) not in exists:
                addable.append([u, v])

    return addable


if __name__ == "__main__":
    # Example 1: Simple DAG
    print("=== Example 1: Count only ===")
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
    v = 4
    result = max_edges_to_add(v, edges)
    print(f"Vertices: {v}, Existing edges: {len(edges)}")
    print(f"Max edges that can be added: {result}")
    # Max possible = 4*3/2 = 6, existing = 4, so answer = 2

    # Example 2: Using topological sort to find specific edges
    print("\n=== Example 2: Find specific edges ===")
    adj = [[1, 2], [2], [3], []]
    addable = max_edges_to_add_with_topo_sort(adj)
    print(f"Graph adj: {adj}")
    print(f"Edges that can be added: {addable}")

    # Example 3: Larger DAG
    print("\n=== Example 3: Larger DAG ===")
    edges3 = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
    v3 = 5
    result3 = max_edges_to_add(v3, edges3)
    print(f"Vertices: {v3}, Existing edges: {len(edges3)}")
    print(f"Max edges that can be added: {result3}")
    # Max possible = 5*4/2 = 10, existing = 5, so answer = 5

"""
Hierholzer's Algorithm for Directed Graph

Hierholzer's algorithm efficiently finds an Eulerian circuit in a directed graph.

Algorithm:
1. Start from any vertex, follow edges until returning to start (forms a cycle)
2. If not all edges are used, find a vertex on the current cycle with unused edges
3. Start a new trail from that vertex and splice it into the main cycle
4. Repeat until all edges are used

Implementation uses a stack-based approach:
- Maintain a current path stack and a circuit list
- If current vertex has unused edges, push to stack and move forward
- If no unused edges, add vertex to circuit and backtrack

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List
from collections import defaultdict


def find_eulerian_circuit(adj: List[List[int]]) -> List[int]:
    """
    Find Eulerian circuit in a directed graph using Hierholzer's algorithm.

    Assumes the graph has an Eulerian circuit (all vertices have equal
    in-degree and out-degree, and graph is strongly connected).

    Args:
        adj: Adjacency list of directed graph (will be modified)

    Returns:
        List of vertices in the Eulerian circuit
    """
    n = len(adj)
    if n == 0:
        return []

    # Make a copy to avoid modifying input
    adj_copy = [list(neighbors) for neighbors in adj]

    curr_path = [0]  # Start from vertex 0
    circuit = []

    while curr_path:
        curr = curr_path[-1]

        if adj_copy[curr]:
            # Follow an unused edge
            next_v = adj_copy[curr].pop()
            curr_path.append(next_v)
        else:
            # No more edges from this vertex, add to circuit
            circuit.append(curr_path.pop())

    circuit.reverse()
    return circuit


def find_eulerian_circuit_from(adj: List[List[int]], start: int) -> List[int]:
    """
    Find Eulerian circuit starting from a specific vertex.

    Args:
        adj: Adjacency list (will be modified)
        start: Starting vertex

    Returns:
        Eulerian circuit starting from 'start'
    """
    adj_copy = [list(neighbors) for neighbors in adj]

    curr_path = [start]
    circuit = []

    while curr_path:
        curr = curr_path[-1]
        if adj_copy[curr]:
            next_v = adj_copy[curr].pop()
            curr_path.append(next_v)
        else:
            circuit.append(curr_path.pop())

    circuit.reverse()
    return circuit


def has_eulerian_circuit_directed(adj: List[List[int]]) -> bool:
    """
    Check if a directed graph has an Eulerian circuit.

    Args:
        adj: Adjacency list

    Returns:
        True if Eulerian circuit exists
    """
    n = len(adj)
    in_degree = [0] * n

    for u in range(n):
        for v in adj[u]:
            in_degree[v] += 1

    # Check in-degree == out-degree for all vertices
    for i in range(n):
        if len(adj[i]) != in_degree[i]:
            return False

    # Check strong connectivity (only for non-zero degree vertices)
    # Find a vertex with non-zero degree
    start = -1
    for i in range(n):
        if len(adj[i]) > 0:
            start = i
            break

    if start == -1:
        return True  # No edges, trivially Eulerian

    # DFS on original graph
    visited = [False] * n
    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    for i in range(n):
        if len(adj[i]) > 0 and not visited[i]:
            return False

    # DFS on transpose
    transpose: List[List[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            transpose[v].append(u)

    visited = [False] * n
    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()
        for v in transpose[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    for i in range(n):
        if len(adj[i]) > 0 and not visited[i]:
            return False

    return True


def find_eulerian_path_directed(adj: List[List[int]]) -> List[int]:
    """
    Find Eulerian path (not necessarily a circuit) in directed graph.

    Args:
        adj: Adjacency list (will be modified)

    Returns:
        List of vertices in Eulerian path, or empty if none exists
    """
    n = len(adj)
    if n == 0:
        return []

    in_degree = [0] * n
    for u in range(n):
        for v in adj[u]:
            in_degree[v] += 1

    # Find start vertex
    # Start = vertex with out_degree - in_degree = 1
    # If no such vertex, start from any vertex with non-zero degree
    start = 0
    found_start = False
    for i in range(n):
        diff = len(adj[i]) - in_degree[i]
        if diff == 1:
            start = i
            found_start = True
            break

    if not found_start:
        for i in range(n):
            if len(adj[i]) > 0:
                start = i
                break

    return find_eulerian_circuit_from(adj, start)


def format_circuit(circuit: List[int]) -> str:
    """Format circuit as a readable string."""
    if not circuit:
        return "No circuit found"
    return " -> ".join(map(str, circuit))


if __name__ == "__main__":
    # Example 1: Simple Eulerian circuit
    print("=== Example 1: Simple Circuit ===")
    adj1 = [
        [1],  # 0 -> 1
        [2],  # 1 -> 2
        [0],  # 2 -> 0
    ]
    circuit1 = find_eulerian_circuit(adj1)
    print(f"Circuit: {format_circuit(circuit1)}")

    # Example 2: More complex graph
    print("\n=== Example 2: Complex Graph ===")
    adj2 = [
        [1, 2],  # 0 -> 1, 0 -> 2
        [2],  # 1 -> 2
        [3, 4],  # 2 -> 3, 2 -> 4
        [0],  # 3 -> 0
        [1],  # 4 -> 1
    ]
    if has_eulerian_circuit_directed(adj2):
        adj2_copy = [list(n) for n in adj2]
        circuit2 = find_eulerian_circuit(adj2_copy)
        print(f"Circuit: {format_circuit(circuit2)}")
        print(f"Circuit length: {len(circuit2) - 1} edges")
    else:
        print("No Eulerian circuit")

    # Example 3: Eulerian path (not circuit)
    print("\n=== Example 3: Eulerian Path ===")
    adj3 = [
        [1],  # 0 -> 1 (out=1, in=0, diff=1 => start)
        [2],  # 1 -> 2
        [0],  # 2 -> 0 (out=1, in=1, diff=0)
    ]
    path3 = find_eulerian_path_directed(adj3)
    print(f"Path: {format_circuit(path3)}")

    # Example 4: Check Eulerian property
    print("\n=== Example 4: Check Property ===")
    adj4 = [
        [1, 2],  # out=2
        [0, 2],  # out=2
        [0, 1],  # out=2
    ]
    print(f"Has Eulerian circuit: {has_eulerian_circuit_directed(adj4)}")

    # Example 5: Not Eulerian
    print("\n=== Example 5: Not Eulerian ===")
    adj5 = [
        [1],  # out=1, in=0
        [2],  # out=1, in=1
        [],  # out=0, in=1
    ]
    print(f"Has Eulerian circuit: {has_eulerian_circuit_directed(adj5)}")

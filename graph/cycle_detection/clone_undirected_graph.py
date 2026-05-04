"""
Clone an Undirected Graph

Problem: Given a connected undirected graph where each node has a value and a list
of neighbors, create a deep copy (clone) of the entire graph.

Algorithm: Both BFS and DFS approaches are implemented.
- Use a hash map (dictionary) to track already cloned nodes (original -> clone)
- This prevents infinite loops when the graph contains cycles
- For each node, create a clone and recursively/iteratively clone all neighbors

BFS Approach: Level-by-level traversal using a queue
DFS Approach: Recursive depth-first traversal

Time Complexity: O(V + E) for both approaches
Space Complexity: O(V) for the clone map and queue/recursion stack
"""

from __future__ import annotations
from collections import deque


class UndirectedGraphNode:
    """Node class for an undirected graph."""

    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.neighbors: list[UndirectedGraphNode] = []

    def __repr__(self) -> str:
        neighbor_vals = [n.val for n in self.neighbors]
        return f"Node(val={self.val}, neighbors={neighbor_vals})"


def clone_graph_bfs(node: UndirectedGraphNode | None) -> UndirectedGraphNode | None:
    """
    Clone an undirected graph using BFS (iterative approach).

    Args:
        node: The starting node of the graph to clone

    Returns:
        The clone of the starting node
    """
    if node is None:
        return None

    clone_map: dict[UndirectedGraphNode, UndirectedGraphNode] = {}
    queue: deque[UndirectedGraphNode] = deque()

    clone_map[node] = UndirectedGraphNode(node.val)
    queue.append(node)

    while queue:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in clone_map:
                clone_map[neighbor] = UndirectedGraphNode(neighbor.val)
                queue.append(neighbor)

            clone_map[current].neighbors.append(clone_map[neighbor])

    return clone_map[node]


def clone_graph_dfs(node: UndirectedGraphNode | None) -> UndirectedGraphNode | None:
    """
    Clone an undirected graph using DFS (recursive approach).

    Args:
        node: The starting node of the graph to clone

    Returns:
        The clone of the starting node
    """
    if node is None:
        return None

    clone_map: dict[UndirectedGraphNode, UndirectedGraphNode] = {}

    def dfs(original: UndirectedGraphNode) -> UndirectedGraphNode:
        if original in clone_map:
            return clone_map[original]

        clone = UndirectedGraphNode(original.val)
        clone_map[original] = clone

        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


def build_graph_from_adj_list(adj_list: list[list[int]]) -> UndirectedGraphNode | None:
    """
    Build an undirected graph from an adjacency list representation.

    Args:
        adj_list: List where adj_list[i] contains neighbor values for node i

    Returns:
        The node with value 0 (or None if empty)
    """
    if not adj_list:
        return None

    nodes: dict[int, UndirectedGraphNode] = {}

    for val in range(len(adj_list)):
        nodes[val] = UndirectedGraphNode(val)

    for val, neighbor_vals in enumerate(adj_list):
        for neighbor_val in neighbor_vals:
            nodes[val].neighbors.append(nodes[neighbor_val])

    return nodes[0]


def bfs_traversal_values(
    node: UndirectedGraphNode | None,
) -> list[tuple[int, list[int]]]:
    """
    Perform BFS traversal and return node values and their neighbors for verification.

    Args:
        node: The starting node

    Returns:
        List of (node_value, sorted_neighbor_values) tuples in BFS order
    """
    if node is None:
        return []

    result: list[tuple[int, list[int]]] = []
    visited: set[int] = set()
    queue: deque[UndirectedGraphNode] = deque([node])
    visited.add(node.val)

    while queue:
        current = queue.popleft()
        neighbor_vals = sorted([n.val for n in current.neighbors])
        result.append((current.val, neighbor_vals))

        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                visited.add(neighbor.val)
                queue.append(neighbor)

    return result


def graphs_are_equal(
    original: UndirectedGraphNode | None, cloned: UndirectedGraphNode | None
) -> bool:
    """
    Check if two graphs are structurally and value-wise equal.

    Args:
        original: Root of the original graph
        cloned: Root of the cloned graph

    Returns:
        True if graphs are identical in structure and values
    """
    return bfs_traversal_values(original) == bfs_traversal_values(cloned)


if __name__ == "__main__":
    print("=" * 60)
    print("Clone an Undirected Graph")
    print("=" * 60)

    # Example 1: Graph with cycle (square with diagonal)
    #   0 -- 1
    #   | \  |
    #   |  \ |
    #   3 -- 2
    print("\nExample 1: Clone graph with cycle")
    adj1 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    original1 = build_graph_from_adj_list(adj1)
    print(f"  Input adj list: {adj1}")
    print(f"  Original BFS:   {bfs_traversal_values(original1)}")

    cloned1_bfs = clone_graph_bfs(original1)
    print(f"  Cloned (BFS):   {bfs_traversal_values(cloned1_bfs)}")
    print(f"  BFS clone correct: {graphs_are_equal(original1, cloned1_bfs)}")

    cloned1_dfs = clone_graph_dfs(original1)
    print(f"  Cloned (DFS):   {bfs_traversal_values(cloned1_dfs)}")
    print(f"  DFS clone correct: {graphs_are_equal(original1, cloned1_dfs)}")

    # Example 2: Simple triangle
    #   0 -- 1
    #    \  /
    #     2
    print("\nExample 2: Clone triangle graph")
    adj2 = [[1, 2], [0, 2], [0, 1]]
    original2 = build_graph_from_adj_list(adj2)
    print(f"  Input adj list: {adj2}")

    cloned2_bfs = clone_graph_bfs(original2)
    print(f"  Original BFS:   {bfs_traversal_values(original2)}")
    print(f"  Cloned (BFS):   {bfs_traversal_values(cloned2_bfs)}")
    print(f"  BFS clone correct: {graphs_are_equal(original2, cloned2_bfs)}")

    # Example 3: Linear graph (no cycle)
    #   0 -- 1 -- 2
    print("\nExample 3: Clone linear graph")
    adj3 = [[1], [0, 2], [1]]
    original3 = build_graph_from_adj_list(adj3)
    print(f"  Input adj list: {adj3}")

    cloned3_dfs = clone_graph_dfs(original3)
    print(f"  Original BFS:   {bfs_traversal_values(original3)}")
    print(f"  Cloned (DFS):   {bfs_traversal_values(cloned3_dfs)}")
    print(f"  DFS clone correct: {graphs_are_equal(original3, cloned3_dfs)}")

    # Example 4: Single node
    print("\nExample 4: Clone single node")
    adj4 = [[]]
    original4 = build_graph_from_adj_list(adj4)
    print(f"  Input adj list: {adj4}")

    cloned4_bfs = clone_graph_bfs(original4)
    print(f"  Original BFS:   {bfs_traversal_values(original4)}")
    print(f"  Cloned (BFS):   {bfs_traversal_values(cloned4_bfs)}")
    print(f"  BFS clone correct: {graphs_are_equal(original4, cloned4_bfs)}")

    # Example 5: None input
    print("\nExample 5: Clone None")
    cloned_none = clone_graph_bfs(None)
    print(f"  Result: {cloned_none}")

    # Example 6: GeeksforGeeks example
    #   0 -- 1
    #   |    |
    #   2 -- 3
    print("\nExample 6: GFG example - square graph")
    adj6 = [[1, 2], [0, 2], [0, 1, 3], [2]]
    original6 = build_graph_from_adj_list(adj6)
    print(f"  Input adj list: {adj6}")

    cloned6_dfs = clone_graph_dfs(original6)
    print(f"  Original BFS:   {bfs_traversal_values(original6)}")
    print(f"  Cloned (DFS):   {bfs_traversal_values(cloned6_dfs)}")
    print(f"  DFS clone correct: {graphs_are_equal(original6, cloned6_dfs)}")

    print("\n" + "=" * 60)

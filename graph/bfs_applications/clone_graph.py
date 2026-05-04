"""
Clone an Undirected Graph

Problem:
Given a reference to a node in a connected undirected graph, return a deep copy (clone)
of the graph.

Each node contains:
- val: integer value
- neighbors: list of Node objects

The graph may contain cycles, so we need to track cloned nodes to avoid infinite loops.

Algorithm: BFS
- Clone the starting node and store in a map (original -> clone)
- Use a queue to process nodes level by level
- For each node, clone its neighbors if not already cloned
- Build the neighbor relationships in the cloned graph

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque
from typing import Optional


class Node:
    """Node in an undirected graph."""

    def __init__(self, val: int = 0, neighbors: Optional[list["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f"Node({self.val})"


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    Clone an undirected graph using BFS.

    Args:
        node: Reference to a node in the graph

    Returns:
        Reference to the cloned graph
    """
    if node is None:
        return None

    # Map from original node to cloned node
    cloned = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for neighbor in curr.neighbors:
            if neighbor not in cloned:
                cloned[neighbor] = Node(neighbor.val)
                queue.append(neighbor)

            cloned[curr].neighbors.append(cloned[neighbor])

    return cloned[node]


def clone_graph_dfs(node: Optional[Node]) -> Optional[Node]:
    """
    Clone an undirected graph using DFS (recursive).

    Args:
        node: Reference to a node in the graph

    Returns:
        Reference to the cloned graph
    """
    cloned = {}

    def dfs(curr: Optional[Node]) -> Optional[Node]:
        if curr is None:
            return None

        if curr in cloned:
            return cloned[curr]

        cloned[curr] = Node(curr.val)

        for neighbor in curr.neighbors:
            cloned[curr].neighbors.append(dfs(neighbor))

        return cloned[curr]

    return dfs(node)


def build_graph_from_adj_list(adj_list: list[list[int]]) -> Optional[Node]:
    """Build a graph from an adjacency list representation."""
    if not adj_list:
        return None

    nodes = [Node(i + 1) for i in range(len(adj_list))]

    for i, neighbors in enumerate(adj_list):
        for neighbor_idx in neighbors:
            nodes[i].neighbors.append(nodes[neighbor_idx - 1])

    return nodes[0]


def graph_to_adj_list(node: Optional[Node]) -> list[list[int]]:
    """Convert a graph to adjacency list representation."""
    if node is None:
        return []

    adj_list = {}
    queue = deque([node])
    visited = {node}

    while queue:
        curr = queue.popleft()
        if curr.val not in adj_list:
            adj_list[curr.val] = []

        for neighbor in curr.neighbors:
            adj_list[curr.val].append(neighbor.val)
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Convert to list of lists
    max_val = max(adj_list.keys())
    result = [[] for _ in range(max_val)]
    for val, neighbors in adj_list.items():
        result[val - 1] = sorted(neighbors)

    return result


def are_graphs_equal(node1: Optional[Node], node2: Optional[Node]) -> bool:
    """Check if two graphs are structurally equal (but different objects)."""
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False

    queue1 = deque([node1])
    queue2 = deque([node2])
    visited1 = {node1}
    visited2 = {node2}

    while queue1 and queue2:
        curr1 = queue1.popleft()
        curr2 = queue2.popleft()

        if curr1.val != curr2.val:
            return False
        if len(curr1.neighbors) != len(curr2.neighbors):
            return False

        # Sort neighbors by value for comparison
        n1_sorted = sorted(curr1.neighbors, key=lambda n: n.val)
        n2_sorted = sorted(curr2.neighbors, key=lambda n: n.val)

        for neighbor1, neighbor2 in zip(n1_sorted, n2_sorted):
            if neighbor1.val != neighbor2.val:
                return False
            if neighbor1 not in visited1:
                visited1.add(neighbor1)
                queue1.append(neighbor1)
            if neighbor2 not in visited2:
                visited2.add(neighbor2)
                queue2.append(neighbor2)

    return len(queue1) == 0 and len(queue2) == 0


if __name__ == "__main__":
    # Example 1: Simple square graph
    #   1 -- 2
    #   |    |
    #   4 -- 3
    print("Example 1: Square graph")
    adj1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = build_graph_from_adj_list(adj1)
    cloned_bfs = clone_graph(original)
    cloned_dfs = clone_graph_dfs(original)

    print(f"  Original: {graph_to_adj_list(original)}")
    print(f"  BFS Clone: {graph_to_adj_list(cloned_bfs)}")
    print(f"  DFS Clone: {graph_to_adj_list(cloned_dfs)}")
    print(f"  BFS equal: {are_graphs_equal(original, cloned_bfs)}")
    print(f"  DFS equal: {are_graphs_equal(original, cloned_dfs)}")
    print(f"  BFS is different object: {original is not cloned_bfs}")

    # Example 2: Single node with no neighbors
    print("\nExample 2: Single isolated node")
    adj2 = [[]]
    original2 = build_graph_from_adj_list(adj2)
    cloned2 = clone_graph(original2)
    print(f"  Original: {graph_to_adj_list(original2)}")
    print(f"  Clone: {graph_to_adj_list(cloned2)}")

    # Example 3: Empty graph
    print("\nExample 3: Empty graph")
    cloned3 = clone_graph(None)
    print(f"  Result: {cloned3}")

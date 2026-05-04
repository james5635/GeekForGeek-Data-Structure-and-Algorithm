"""
Clone a Directed Acyclic Graph (DAG)

Problem: Given a directed acyclic graph (DAG), create a deep copy of the graph.
A DAG is a directed graph with no cycles.

Algorithm: DFS-based cloning with visited tracking
1. Initialize a hash map to keep track of visited nodes and their clones
2. Perform DFS traversal of the original graph
3. For each unvisited node, create a clone and add it to the map
4. Recursively clone all neighbors
5. Build the adjacency structure in the cloned graph

Time Complexity: O(V + E) where V = vertices, E = edges
Space Complexity: O(V) for the visited map and recursion stack
"""

from __future__ import annotations


class DAGNode:
    """Node class for a Directed Acyclic Graph."""

    def __init__(self, key: int = 0) -> None:
        self.key = key
        self.adj: list[DAGNode] = []

    def __repr__(self) -> str:
        return f"DAGNode(key={self.key})"


def clone_dag(root: DAGNode | None) -> DAGNode | None:
    """
    Create a deep copy of a directed acyclic graph.

    Args:
        root: The starting node of the DAG to clone

    Returns:
        The root node of the cloned DAG
    """
    if root is None:
        return None

    clone_map: dict[DAGNode, DAGNode] = {}

    def dfs(node: DAGNode) -> DAGNode:
        if node in clone_map:
            return clone_map[node]

        clone = DAGNode(node.key)
        clone_map[node] = clone

        for neighbor in node.adj:
            clone.adj.append(dfs(neighbor))

        return clone

    return dfs(root)


def print_dag_edges(root: DAGNode | None) -> list[tuple[int, int]]:
    """
    Print all edges in a DAG for verification.

    Args:
        root: The starting node of the DAG

    Returns:
        List of edges as (source_key, destination_key) tuples
    """
    if root is None:
        return []

    edges: list[tuple[int, int]] = []
    visited: set[int] = set()

    def dfs(node: DAGNode) -> None:
        visited.add(node.key)
        for neighbor in node.adj:
            edges.append((node.key, neighbor.key))
            if neighbor.key not in visited:
                dfs(neighbor)

    dfs(root)
    return edges


def build_sample_dag() -> tuple[DAGNode, dict[int, DAGNode]]:
    """
    Build a sample DAG for testing.

    Graph structure:
        0 --> 1 --> 4
        |    / \\    ^
        |   /   \\   |
        |  /     \\  |
        v v       v |
        2 -------> 3

    Edges: 0->1, 0->2, 1->2, 1->3, 1->4, 2->3, 3->4

    Returns:
        Tuple of (root_node, all_nodes_map)
    """
    nodes = {i: DAGNode(i) for i in range(5)}

    nodes[0].adj.extend([nodes[1], nodes[2]])
    nodes[1].adj.extend([nodes[2], nodes[3], nodes[4]])
    nodes[2].adj.append(nodes[3])
    nodes[3].adj.append(nodes[4])

    return nodes[0], nodes


def build_simple_dag() -> tuple[DAGNode, dict[int, DAGNode]]:
    """
    Build a simple DAG for testing.

    Graph structure:
        0 --> 1 --> 2
              |
              v
              3

    Edges: 0->1, 1->2, 1->3

    Returns:
        Tuple of (root_node, all_nodes_map)
    """
    nodes = {i: DAGNode(i) for i in range(4)}

    nodes[0].adj.append(nodes[1])
    nodes[1].adj.extend([nodes[2], nodes[3]])

    return nodes[0], nodes


if __name__ == "__main__":
    print("=" * 60)
    print("Clone a Directed Acyclic Graph (DAG)")
    print("=" * 60)

    # Example 1: Complex DAG
    print("\nExample 1: Clone a complex DAG")
    root1, nodes1 = build_sample_dag()
    original_edges1 = print_dag_edges(root1)
    print(f"  Original graph edges: {original_edges1}")

    cloned_root1 = clone_dag(root1)
    cloned_edges1 = print_dag_edges(cloned_root1)
    print(f"  Cloned graph edges:   {cloned_edges1}")
    print(f"  Edges match: {sorted(original_edges1) == sorted(cloned_edges1)}")
    print(f"  Nodes are different objects: {root1 is not cloned_root1}")

    # Verify deep copy
    cloned_edges1_check = print_dag_edges(cloned_root1)
    print(f"  Clone is independent: {cloned_edges1_check == cloned_edges1}")

    # Example 2: Simple DAG
    print("\nExample 2: Clone a simple DAG")
    root2, nodes2 = build_simple_dag()
    original_edges2 = print_dag_edges(root2)
    print(f"  Original graph edges: {original_edges2}")

    cloned_root2 = clone_dag(root2)
    cloned_edges2 = print_dag_edges(cloned_root2)
    print(f"  Cloned graph edges:   {cloned_edges2}")
    print(f"  Edges match: {sorted(original_edges2) == sorted(cloned_edges2)}")

    # Example 3: Single node DAG
    print("\nExample 3: Clone a single-node DAG")
    single_node = DAGNode(0)
    original_edges3 = print_dag_edges(single_node)
    print(f"  Original graph edges: {original_edges3}")

    cloned_single = clone_dag(single_node)
    cloned_edges3 = print_dag_edges(cloned_single)
    print(f"  Cloned graph edges:   {cloned_edges3}")
    print(f"  Edges match: {sorted(original_edges3) == sorted(cloned_edges3)}")

    # Example 4: None input
    print("\nExample 4: Clone None (empty graph)")
    cloned_none = clone_dag(None)
    print(f"  Result: {cloned_none}")

    print("\n" + "=" * 60)

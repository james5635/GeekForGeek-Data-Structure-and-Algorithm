"""
Sum of Dependencies in a Graph

Given a directed graph with N nodes, if there is an edge from u to v,
then u depends on v. The task is to find the sum of dependencies for
every node.

For each node, the number of dependencies equals the number of outgoing
edges from that node. The total sum of dependencies equals the total
number of edges in the graph.

Example:
    A -> C, A -> D    (A depends on 2 nodes)
    B -> C            (B depends on 1 node)
    D -> C            (D depends on 1 node)
    C -> (none)       (C depends on 0 nodes)
    Sum = 2 + 1 + 1 + 0 = 4

Time Complexity: O(V) to sum adjacency list sizes
Space Complexity: O(V + E) for adjacency list storage
"""


def sum_of_dependencies(adj: list[list[int]], num_vertices: int) -> int:
    """
    Calculate the sum of dependencies for all nodes in a directed graph.

    The dependency count for a node equals the number of outgoing edges
    from that node. The total sum equals the total number of edges.

    Args:
        adj: Adjacency list where adj[u] contains all vertices v
             such that there is a directed edge u -> v.
        num_vertices: Number of vertices in the graph.

    Returns:
        The total sum of dependencies across all nodes.
    """
    total = 0
    for u in range(num_vertices):
        total += len(adj[u])
    return total


def get_dependencies_per_node(
    adj: list[list[int]], num_vertices: int
) -> dict[int, int]:
    """
    Get the dependency count for each individual node.

    Args:
        adj: Adjacency list representation of the graph.
        num_vertices: Number of vertices in the graph.

    Returns:
        A dictionary mapping each vertex to its dependency count.
    """
    return {u: len(adj[u]) for u in range(num_vertices)}


def build_graph_from_edges(
    edges: list[tuple[int, int]], num_vertices: int
) -> list[list[int]]:
    """
    Build an adjacency list from a list of directed edges.

    Args:
        edges: List of (source, destination) tuples.
        num_vertices: Number of vertices in the graph.

    Returns:
        Adjacency list representation of the graph.
    """
    adj: list[list[int]] = [[] for _ in range(num_vertices)]
    for src, dest in edges:
        adj[src].append(dest)
    return adj


if __name__ == "__main__":
    # Example 1: GFG example
    #   A(0) -> C(2), A(0) -> D(3)
    #   B(1) -> C(2)
    #   D(3) -> C(2)
    #   C(2) -> (none)
    print("Example 1:")
    print("Edges: 0->2, 0->3, 1->2, 3->2")

    edges1 = [(0, 2), (0, 3), (1, 2), (3, 2)]
    adj1 = build_graph_from_edges(edges1, 4)

    deps1 = get_dependencies_per_node(adj1, 4)
    print("Dependencies per node:")
    for node, count in deps1.items():
        print(f"  Node {node}: {count} dependencies")

    total1 = sum_of_dependencies(adj1, 4)
    print(f"Total sum of dependencies: {total1}")
    print()

    # Example 2: Linear chain
    #   0 -> 1 -> 2 -> 3
    print("Example 2:")
    print("Edges: 0->1, 1->2, 2->3")

    edges2 = [(0, 1), (1, 2), (2, 3)]
    adj2 = build_graph_from_edges(edges2, 4)

    deps2 = get_dependencies_per_node(adj2, 4)
    print("Dependencies per node:")
    for node, count in deps2.items():
        print(f"  Node {node}: {count} dependencies")

    total2 = sum_of_dependencies(adj2, 4)
    print(f"Total sum of dependencies: {total2}")
    print()

    # Example 3: Empty graph
    print("Example 3: Empty graph (no edges)")
    adj3: list[list[int]] = [[], [], []]
    total3 = sum_of_dependencies(adj3, 3)
    print(f"Total sum of dependencies: {total3}")

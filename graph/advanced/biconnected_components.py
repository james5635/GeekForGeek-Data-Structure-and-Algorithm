"""
Biconnected Components

A biconnected component is a maximal biconnected subgraph.
A graph is biconnected if it has no articulation points (cut vertices).

Algorithm (Hopcroft-Tarjan):
- Use DFS with disc and low values (similar to articulation points)
- Maintain a stack of visited edges
- When an articulation point is found, pop all edges from stack until
  the edge to the articulation point - these form one biconnected component
- After DFS completes, remaining edges in stack form the last component

A biconnected component is either:
- A maximal set of edges where any two edges lie on a common cycle, or
- A single bridge (edge whose removal disconnects the graph)

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List, Tuple
from collections import defaultdict


def find_biconnected_components(
    num_vertices: int, edges: List[List[int]]
) -> List[List[Tuple[int, int]]]:
    """
    Find all biconnected components in an undirected graph.

    Args:
        num_vertices: Number of vertices
        edges: List of undirected edges

    Returns:
        List of biconnected components, each as a list of edges
    """
    # Build adjacency list
    adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * num_vertices
    low = [-1] * num_vertices
    parent = [-1] * num_vertices
    edge_stack: List[Tuple[int, int]] = []
    components: List[List[Tuple[int, int]]] = []
    timer = [0]

    def dfs(u: int) -> None:
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        children = 0

        for v in adj[u]:
            if disc[v] == -1:  # v not visited
                children += 1
                parent[v] = u
                edge_stack.append((u, v))
                dfs(v)

                low[u] = min(low[u], low[v])

                # If u is an articulation point, pop component
                if (parent[u] == -1 and children > 1) or (
                    parent[u] != -1 and low[v] >= disc[u]
                ):
                    component = []
                    while edge_stack and edge_stack[-1] != (u, v):
                        component.append(edge_stack.pop())
                    if edge_stack:
                        component.append(edge_stack.pop())
                    components.append(component)

            elif v != parent[u] and disc[v] < disc[u]:  # Back edge
                low[u] = min(low[u], disc[v])
                edge_stack.append((u, v))

    for i in range(num_vertices):
        if disc[i] == -1:
            dfs(i)
            # Remaining edges form a component
            if edge_stack:
                components.append(edge_stack[:])
                edge_stack.clear()

    return components


class BiconnectedComponents:
    """Object-oriented biconnected components finder."""

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: List[List[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add undirected edge."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def find_components(self) -> List[List[Tuple[int, int]]]:
        """
        Find all biconnected components.

        Returns:
            List of components, each a list of edges (u, v)
        """
        disc = [-1] * self.num_vertices
        low = [-1] * self.num_vertices
        parent = [-1] * self.num_vertices
        edge_stack: List[Tuple[int, int]] = []
        components: List[List[Tuple[int, int]]] = []
        timer = [0]

        def dfs(u: int) -> None:
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            children = 0

            for v in self.adj[u]:
                if disc[v] == -1:
                    children += 1
                    parent[v] = u
                    edge_stack.append((u, v))
                    dfs(v)

                    low[u] = min(low[u], low[v])

                    if (parent[u] == -1 and children > 1) or (
                        parent[u] != -1 and low[v] >= disc[u]
                    ):
                        component = []
                        while edge_stack[-1] != (u, v):
                            component.append(edge_stack.pop())
                        component.append(edge_stack.pop())
                        components.append(component)

                elif v != parent[u] and disc[v] < disc[u]:
                    low[u] = min(low[u], disc[v])
                    edge_stack.append((u, v))

        for i in range(self.num_vertices):
            if disc[i] == -1:
                dfs(i)
                if edge_stack:
                    components.append(list(edge_stack))
                    edge_stack.clear()

        return components

    def count_components(self) -> int:
        """Return number of biconnected components."""
        return len(self.find_components())

    def is_biconnected(self) -> bool:
        """Check if the entire graph is biconnected."""
        components = self.find_components()
        return len(components) == 1


def get_bcc_analysis(num_vertices: int, edges: List[List[int]]) -> dict:
    """
    Analyze biconnected components of a graph.

    Returns:
        Dictionary with analysis results
    """
    components = find_biconnected_components(num_vertices, edges)

    return {
        "num_components": len(components),
        "components": components,
        "is_biconnected": len(components) == 1,
    }


if __name__ == "__main__":
    # Example 1: Classic biconnected components example
    print("=== Example 1: Multiple BCCs ===")
    edges1 = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],  # Cycle 0-1-2-3
        [2, 4],
        [1, 4],  # Triangle 1-2-4
        [4, 5],
        [5, 6],  # Bridge 4-5 and edge 5-6
        [6, 7],
        [7, 6],  # Self-loop on 6-7
    ]
    # Remove duplicate
    edges1 = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],
        [2, 4],
        [1, 4],
        [4, 5],
        [5, 6],
        [6, 7],
    ]

    bcc = BiconnectedComponents(8)
    for u, v in edges1:
        bcc.add_edge(u, v)

    components = bcc.find_components()
    print(f"Number of biconnected components: {len(components)}")
    for i, comp in enumerate(components):
        print(f"  BCC {i}: {comp}")

    # Example 2: Simple cycle (one BCC)
    print("\n=== Example 2: Single BCC (Cycle) ===")
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 0]]
    result2 = get_bcc_analysis(4, edges2)
    print(f"Is biconnected: {result2['is_biconnected']}")
    print(f"Components: {result2['components']}")

    # Example 3: Tree (each edge is a BCC)
    print("\n=== Example 3: Tree ===")
    edges3 = [[0, 1], [1, 2], [1, 3]]
    result3 = get_bcc_analysis(4, edges3)
    print(f"Number of BCCs: {result3['num_components']}")
    for i, comp in enumerate(result3["components"]):
        print(f"  BCC {i}: {comp}")

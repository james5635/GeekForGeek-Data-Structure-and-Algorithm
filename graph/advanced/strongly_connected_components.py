"""
Strongly Connected Components (Kosaraju's Algorithm)

A Strongly Connected Component (SCC) in a directed graph is a maximal
subset of vertices where every vertex is reachable from every other
vertex in the subset.

Kosaraju's Algorithm (3 passes):
1. DFS on original graph, push vertices to stack by finish time
2. Transpose (reverse) the graph
3. DFS on transposed graph in order of decreasing finish time
   Each DFS tree in step 3 is one SCC

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List
from collections import defaultdict


def kosaraju_scc(num_vertices: int, adj: List[List[int]]) -> List[List[int]]:
    """
    Find all strongly connected components using Kosaraju's algorithm.

    Args:
        num_vertices: Number of vertices (0 to V-1)
        adj: Adjacency list of the directed graph

    Returns:
        List of SCCs, each SCC is a list of vertices
    """
    # Step 1: DFS and fill stack with finish times
    visited = [False] * num_vertices
    stack = []

    def dfs1(v: int) -> None:
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(v)

    for i in range(num_vertices):
        if not visited[i]:
            dfs1(i)

    # Step 2: Transpose the graph
    rev_adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u in range(num_vertices):
        for v in adj[u]:
            rev_adj[v].append(u)

    # Step 3: DFS on transposed graph in stack order
    visited = [False] * num_vertices
    sccs = []

    def dfs2(v: int, component: List[int]) -> None:
        visited[v] = True
        component.append(v)
        for neighbor in rev_adj[v]:
            if not visited[neighbor]:
                dfs2(neighbor, component)

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            component = []
            dfs2(vertex, component)
            sccs.append(component)

    return sccs


class KosarajuSCC:
    """Object-oriented Kosaraju's SCC implementation."""

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: List[List[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add directed edge u -> v."""
        self.adj[u].append(v)

    def find_sccs(self) -> List[List[int]]:
        """
        Find all strongly connected components.

        Returns:
            List of SCCs
        """
        visited = [False] * self.num_vertices
        stack = []

        def dfs_fill(v: int) -> None:
            visited[v] = True
            for neighbor in self.adj[v]:
                if not visited[neighbor]:
                    dfs_fill(neighbor)
            stack.append(v)

        for i in range(self.num_vertices):
            if not visited[i]:
                dfs_fill(i)

        # Transpose
        rev_adj: List[List[int]] = [[] for _ in range(self.num_vertices)]
        for u in range(self.num_vertices):
            for v in self.adj[u]:
                rev_adj[v].append(u)

        # Second DFS
        visited = [False] * self.num_vertices
        sccs = []

        def dfs_collect(v: int, component: List[int]) -> None:
            visited[v] = True
            component.append(v)
            for neighbor in rev_adj[v]:
                if not visited[neighbor]:
                    dfs_collect(neighbor, component)

        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                dfs_collect(v, component)
                sccs.append(component)

        return sccs

    def count_sccs(self) -> int:
        """Return number of strongly connected components."""
        return len(self.find_sccs())


def find_sccs_iterative(num_vertices: int, edges: List[List[int]]) -> List[List[int]]:
    """
    Iterative version of Kosaraju's algorithm to avoid recursion limits.

    Args:
        num_vertices: Number of vertices
        edges: List of [u, v] directed edges

    Returns:
        List of SCCs
    """
    adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj[u].append(v)

    # Step 1: Iterative DFS to fill stack
    visited = [False] * num_vertices
    stack = []

    for start in range(num_vertices):
        if visited[start]:
            continue
        dfs_stack = [(start, False)]
        while dfs_stack:
            node, processed = dfs_stack.pop()
            if processed:
                stack.append(node)
                continue
            if visited[node]:
                continue
            visited[node] = True
            dfs_stack.append((node, True))
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_stack.append((neighbor, False))

    # Step 2: Transpose
    rev_adj: List[List[int]] = [[] for _ in range(num_vertices)]
    for u in range(num_vertices):
        for v in adj[u]:
            rev_adj[v].append(u)

    # Step 3: DFS on transposed graph
    visited = [False] * num_vertices
    sccs = []

    while stack:
        start = stack.pop()
        if visited[start]:
            continue
        component = []
        dfs_stack = [start]
        while dfs_stack:
            node = dfs_stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            component.append(node)
            for neighbor in rev_adj[node]:
                if not visited[neighbor]:
                    dfs_stack.append(neighbor)
        sccs.append(component)

    return sccs


if __name__ == "__main__":
    # Example 1: Basic SCC
    print("=== Example 1: Basic SCC ===")
    # Graph: 0->1, 1->2, 2->0, 1->3, 3->4
    adj1: List[List[int]] = [[1], [2, 3], [0], [4], []]
    sccs1 = kosaraju_scc(5, adj1)
    print(f"Number of SCCs: {len(sccs1)}")
    for i, scc in enumerate(sccs1):
        print(f"  SCC {i}: {scc}")

    # Example 2: Using class
    print("\n=== Example 2: Class-based ===")
    g = KosarajuSCC(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    sccs2 = g.find_sccs()
    print(f"Number of SCCs: {len(sccs2)}")
    for i, scc in enumerate(sccs2):
        print(f"  SCC {i}: {sorted(scc)}")

    # Example 3: Fully connected component
    print("\n=== Example 3: Fully connected ===")
    edges3 = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]
    sccs3 = find_sccs_iterative(6, edges3)
    print(f"Number of SCCs: {len(sccs3)}")
    for i, scc in enumerate(sccs3):
        print(f"  SCC {i}: {sorted(scc)}")

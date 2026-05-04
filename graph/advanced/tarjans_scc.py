"""
Tarjan's Algorithm for Strongly Connected Components

Tarjan's algorithm finds all SCCs in a single DFS pass using:
- Discovery time (disc): When a vertex was first visited
- Low-link value (low): Earliest discovery time reachable from vertex
- A stack to track vertices in the current SCC exploration

When disc[u] == low[u], vertex u is the root of an SCC.
Pop all vertices from stack until u to get one SCC.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List


def tarjan_scc(num_vertices: int, adj: List[List[int]]) -> List[List[int]]:
    """
    Find all strongly connected components using Tarjan's algorithm.

    Args:
        num_vertices: Number of vertices (0 to V-1)
        adj: Adjacency list of directed graph

    Returns:
        List of SCCs, each SCC is a list of vertices
    """
    disc = [-1] * num_vertices
    low = [-1] * num_vertices
    on_stack = [False] * num_vertices
    stack: List[int] = []
    sccs: List[List[int]] = []
    timer = [0]

    def dfs(u: int) -> None:
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if disc[v] == -1:  # v not visited
                dfs(v)
                low[u] = min(low[u], low[v])

            elif on_stack[v]:  # v is in current SCC
                low[u] = min(low[u], disc[v])

        # If u is root of an SCC
        if low[u] == disc[u]:
            scc = []
            while True:
                v = stack.pop()
                on_stack[v] = False
                scc.append(v)
                if v == u:
                    break
            sccs.append(scc)

    for i in range(num_vertices):
        if disc[i] == -1:
            dfs(i)

    return sccs


def tarjan_scc_iterative(num_vertices: int, adj: List[List[int]]) -> List[List[int]]:
    """
    Iterative version of Tarjan's SCC algorithm.

    Args:
        num_vertices: Number of vertices
        adj: Adjacency list

    Returns:
        List of SCCs
    """
    disc = [-1] * num_vertices
    low = [-1] * num_vertices
    on_stack = [False] * num_vertices
    stack: List[int] = []
    sccs: List[List[int]] = []
    timer = 0

    for start in range(num_vertices):
        if disc[start] != -1:
            continue

        # Iterative DFS with post-order processing
        dfs_stack = [(start, iter(adj[start]), False)]
        disc[start] = low[start] = timer
        timer += 1
        stack.append(start)
        on_stack[start] = True

        while dfs_stack:
            u, children, post_order = dfs_stack[-1]

            if not post_order:
                dfs_stack[-1] = (u, children, True)

                try:
                    while True:
                        v = next(children)
                        if disc[v] == -1:
                            disc[v] = low[v] = timer
                            timer += 1
                            stack.append(v)
                            on_stack[v] = True
                            dfs_stack.append((v, iter(adj[v]), False))
                            break
                        elif on_stack[v]:
                            low[u] = min(low[u], disc[v])
                except StopIteration:
                    pass
            else:
                # Post-order: process after all children
                dfs_stack.pop()

                if disc[u] == low[u]:
                    scc = []
                    while True:
                        v = stack.pop()
                        on_stack[v] = False
                        scc.append(v)
                        if v == u:
                            break
                    sccs.append(scc)

                # Update parent's low value
                if dfs_stack:
                    parent = dfs_stack[-1][0]
                    low[parent] = min(low[parent], low[u])

    return sccs


def count_sccs(num_vertices: int, adj: List[List[int]]) -> int:
    """
    Count the number of strongly connected components.

    Args:
        num_vertices: Number of vertices
        adj: Adjacency list

    Returns:
        Number of SCCs
    """
    return len(tarjan_scc(num_vertices, adj))


def get_scc_map(num_vertices: int, adj: List[List[int]]) -> List[int]:
    """
    Get mapping from vertex to SCC index.

    Args:
        num_vertices: Number of vertices
        adj: Adjacency list

    Returns:
        List where index i contains the SCC index of vertex i
    """
    sccs = tarjan_scc(num_vertices, adj)
    vertex_to_scc = [-1] * num_vertices

    for scc_idx, scc in enumerate(sccs):
        for v in scc:
            vertex_to_scc[v] = scc_idx

    return vertex_to_scc


class TarjanSCC:
    """Object-oriented Tarjan's SCC implementation."""

    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: List[List[int]] = [[] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        """Add directed edge."""
        self.adj[u].append(v)

    def find_sccs(self) -> List[List[int]]:
        """Find all SCCs."""
        disc = [-1] * self.num_vertices
        low = [-1] * self.num_vertices
        on_stack = [False] * self.num_vertices
        stack: List[int] = []
        sccs: List[List[int]] = []
        timer = [0]

        def dfs(u: int) -> None:
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            stack.append(u)
            on_stack[u] = True

            for v in self.adj[u]:
                if disc[v] == -1:
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif on_stack[v]:
                    low[u] = min(low[u], disc[v])

            if low[u] == disc[u]:
                scc = []
                while True:
                    v = stack.pop()
                    on_stack[v] = False
                    scc.append(v)
                    if v == u:
                        break
                sccs.append(scc)

        for i in range(self.num_vertices):
            if disc[i] == -1:
                dfs(i)

        return sccs


if __name__ == "__main__":
    # Example 1: Basic SCC
    print("=== Example 1: Basic SCC ===")
    # Graph: 0->1, 1->2, 2->0, 1->3, 3->4, 4->5, 5->3
    adj1: List[List[int]] = [
        [1],  # 0 -> 1
        [2, 3],  # 1 -> 2, 3
        [0],  # 2 -> 0
        [4],  # 3 -> 4
        [5],  # 4 -> 5
        [3],  # 5 -> 3
    ]

    sccs = tarjan_scc(6, adj1)
    print(f"Number of SCCs: {len(sccs)}")
    for i, scc in enumerate(sccs):
        print(f"  SCC {i}: {sorted(scc)}")

    # Example 2: Iterative version
    print("\n=== Example 2: Iterative ===")
    sccs2 = tarjan_scc_iterative(6, adj1)
    print(f"Number of SCCs: {len(sccs2)}")
    for i, scc in enumerate(sccs2):
        print(f"  SCC {i}: {sorted(scc)}")

    # Example 3: SCC map
    print("\n=== Example 3: SCC Mapping ===")
    scc_map = get_scc_map(6, adj1)
    for v, scc_idx in enumerate(scc_map):
        print(f"  Vertex {v} -> SCC {scc_idx}")

    # Example 4: All vertices in one SCC
    print("\n=== Example 4: Fully Connected ===")
    adj4: List[List[int]] = [[1, 2], [0, 2], [0, 1]]
    sccs4 = tarjan_scc(3, adj4)
    print(f"SCCs: {sccs4}")  # One SCC: [0, 1, 2]

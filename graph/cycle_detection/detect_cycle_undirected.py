"""
Detect Cycle in an Undirected Graph

Problem: Given an undirected graph represented as an adjacency list, determine
whether the graph contains a cycle.

Algorithm: DFS with parent tracking. During DFS traversal, if we encounter a visited
node that is NOT the parent of the current node, then a cycle exists. The parent
tracking prevents false positives since in an undirected graph, the edge (u,v) means
both u->v and v->u exist, so reaching the parent doesn't count as a cycle.

Both DFS and BFS approaches are implemented.

Time Complexity: O(V + E) for both approaches
Space Complexity: O(V) for visited array and recursion stack/queue
"""

from collections import deque


def has_cycle_undirected_dfs(n: int, adj: list[list[int]]) -> bool:
    """
    Detect cycle in an undirected graph using DFS.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        adj: Adjacency list where adj[i] contains all neighbors of vertex i

    Returns:
        True if the graph contains a cycle, False otherwise
    """
    visited: list[bool] = [False] * n

    def dfs(node: int, parent: int) -> bool:
        visited[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False


def has_cycle_undirected_bfs(n: int, adj: list[list[int]]) -> bool:
    """
    Detect cycle in an undirected graph using BFS.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        adj: Adjacency list where adj[i] contains all neighbors of vertex i

    Returns:
        True if the graph contains a cycle, False otherwise
    """
    visited: list[bool] = [False] * n

    def bfs(start: int) -> bool:
        queue: deque[tuple[int, int]] = deque()
        queue.append((start, -1))
        visited[start] = True

        while queue:
            node, parent = queue.popleft()

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True

        return False

    for i in range(n):
        if not visited[i]:
            if bfs(i):
                return True

    return False


def has_cycle_from_edges(n: int, edges: list[tuple[int, int]]) -> bool:
    """
    Detect cycle in an undirected graph given as edge list.

    Args:
        n: Number of vertices (labeled 0 to n-1)
        edges: List of undirected edges as (u, v) tuples

    Returns:
        True if the graph contains a cycle, False otherwise
    """
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    return has_cycle_undirected_dfs(n, adj)


if __name__ == "__main__":
    print("=" * 60)
    print("Detect Cycle in an Undirected Graph")
    print("=" * 60)

    # Example 1: Graph WITH a cycle
    #   0 -- 1
    #   |    |
    #   3 -- 2
    print("\nExample 1: Graph with a cycle (square)")
    n1 = 4
    adj1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(f"  Vertices: {n1}")
    print(f"  Adjacency list: {adj1}")
    print(f"  Has cycle (DFS): {has_cycle_undirected_dfs(n1, adj1)}")
    print(f"  Has cycle (BFS): {has_cycle_undirected_bfs(n1, adj1)}")

    # Example 2: Graph WITHOUT a cycle (tree)
    #       0
    #      / \
    #     1   2
    #         |
    #         3
    print("\nExample 2: Graph without a cycle (tree)")
    n2 = 4
    adj2 = [[1, 2], [0], [0, 3], [2]]
    print(f"  Vertices: {n2}")
    print(f"  Adjacency list: {adj2}")
    print(f"  Has cycle (DFS): {has_cycle_undirected_dfs(n2, adj2)}")
    print(f"  Has cycle (BFS): {has_cycle_undirected_bfs(n2, adj2)}")

    # Example 3: Single edge, no cycle
    print("\nExample 3: Single edge, no cycle")
    n3 = 2
    adj3 = [[1], [0]]
    print(f"  Vertices: {n3}")
    print(f"  Adjacency list: {adj3}")
    print(f"  Has cycle (DFS): {has_cycle_undirected_dfs(n3, adj3)}")
    print(f"  Has cycle (BFS): {has_cycle_undirected_bfs(n3, adj3)}")

    # Example 4: Triangle cycle
    #   0 -- 1
    #    \  /
    #     2
    print("\nExample 4: Triangle cycle")
    n4 = 3
    adj4 = [[1, 2], [0, 2], [0, 1]]
    print(f"  Vertices: {n4}")
    print(f"  Adjacency list: {adj4}")
    print(f"  Has cycle (DFS): {has_cycle_undirected_dfs(n4, adj4)}")
    print(f"  Has cycle (BFS): {has_cycle_undirected_bfs(n4, adj4)}")

    # Example 5: Disconnected graph, one component has cycle
    #   0 -- 1 (no cycle)    2 -- 3
    #                        |    |
    #                        4 -- 5 (cycle!)
    print("\nExample 5: Disconnected graph with cycle in one component")
    n5 = 6
    edges5 = [(0, 1), (2, 3), (3, 5), (5, 4), (4, 2)]
    print(f"  Vertices: {n5}")
    print(f"  Edges: {edges5}")
    print(f"  Has cycle: {has_cycle_from_edges(n5, edges5)}")

    print("\n" + "=" * 60)

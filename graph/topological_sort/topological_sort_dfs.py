"""
Topological Sort using DFS (Depth First Search)

Topological sorting for a Directed Acyclic Graph (DAG) is a linear ordering
of vertices such that for every directed edge u -> v, vertex u comes before v
in the ordering.

Algorithm:
1. Perform DFS on each unvisited vertex
2. After visiting all neighbors of a vertex, push it onto a stack
3. Pop elements from the stack to get the topological ordering

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import TypeAlias

AdjList: TypeAlias = list[list[int]]


def topological_sort_dfs(adj: AdjList) -> list[int]:
    """
    Perform topological sort on a DAG using DFS.

    Args:
        adj: Adjacency list representation of the graph.
             adj[u] contains all vertices v such that there is an edge u -> v.

    Returns:
        A list representing one valid topological ordering of vertices.

    Raises:
        ValueError: If the graph contains a cycle.
    """
    n = len(adj)
    visited = [False] * n
    rec_stack = [False] * n  # for cycle detection
    stack: list[int] = []

    def dfs(node: int) -> None:
        """Recursively visit all neighbors, then push node to stack."""
        visited[node] = True
        rec_stack[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
            elif rec_stack[neighbor]:
                raise ValueError(
                    "Graph contains a cycle; topological sort not possible."
                )

        rec_stack[node] = False
        stack.append(node)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return stack[::-1]


if __name__ == "__main__":
    # Example 1: Graph from GFG
    #   0 -> 1 -> 2
    #   3 -> 2
    #   3 -> 4
    # Expected output: [0, 3, 1, 4, 2] (or similar valid ordering)
    n = 5
    adj1: AdjList = [[] for _ in range(n)]
    adj1[0].append(1)
    adj1[1].append(2)
    adj1[3].append(2)
    adj1[3].append(4)

    print("Example 1:")
    print(f"Graph edges: 0->1, 1->2, 3->2, 3->4")
    result = topological_sort_dfs(adj1)
    print(f"Topological sort: {result}")
    print()

    # Example 2: Another DAG
    #   0 -> 1
    #   1 -> 2
    #   2 -> 3
    #   4 -> 5
    #   5 -> 1, 5 -> 2
    # Expected output: [0, 4, 5, 1, 2, 3] (or similar valid ordering)
    n2 = 6
    adj2: AdjList = [[] for _ in range(n2)]
    adj2[0].append(1)
    adj2[1].append(2)
    adj2[2].append(3)
    adj2[4].append(5)
    adj2[5].append(1)
    adj2[5].append(2)

    print("Example 2:")
    print(f"Graph edges: 0->1, 1->2, 2->3, 4->5, 5->1, 5->2")
    result2 = topological_sort_dfs(adj2)
    print(f"Topological sort: {result2}")
    print()

    # Example 3: Cycle detection
    print("Example 3 (cycle detection):")
    n3 = 3
    adj3: AdjList = [[] for _ in range(n3)]
    adj3[0].append(1)
    adj3[1].append(2)
    adj3[2].append(0)  # Creates a cycle: 0->1->2->0

    print(f"Graph edges: 0->1, 1->2, 2->0 (cycle)")
    try:
        topological_sort_dfs(adj3)
    except ValueError as e:
        print(f"Caught expected error: {e}")

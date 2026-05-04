"""
Check if a Graph is Bipartite

Problem:
A graph is bipartite if its vertices can be divided into two disjoint sets such that
every edge connects a vertex from one set to a vertex from the other set.
Equivalently, a graph is bipartite if it can be colored using only 2 colors
such that no two adjacent vertices have the same color.

Algorithm: BFS with 2-coloring
- For each unvisited node, start BFS and assign color 0
- For each neighbor, assign the opposite color
- If a neighbor already has the same color as current node, graph is not bipartite
- Handle disconnected graphs by checking all nodes

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque


def is_bipartite(adj: list[list[int]], n: int) -> bool:
    """
    Check if an undirected graph is bipartite.

    Args:
        adj: Adjacency list representation of the graph
        n: Number of vertices (labeled 0 to n-1)

    Returns:
        True if the graph is bipartite, False otherwise
    """
    # Color array: -1 = uncolored, 0 and 1 are the two colors
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        # Start BFS from this uncolored node
        queue = deque()
        queue.append(start)
        color[start] = 0

        while queue:
            node = queue.popleft()

            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    # Assign opposite color
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # Adjacent nodes have same color - not bipartite
                    return False

    return True


def is_bipartite_dfs(adj: list[list[int]], n: int) -> bool:
    """
    Check if an undirected graph is bipartite using DFS.

    Args:
        adj: Adjacency list representation of the graph
        n: Number of vertices (labeled 0 to n-1)

    Returns:
        True if the graph is bipartite, False otherwise
    """
    color = [-1] * n

    def dfs(node: int, c: int) -> bool:
        color[node] = c
        for neighbor in adj[node]:
            if color[neighbor] == -1:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True

    for start in range(n):
        if color[start] == -1:
            if not dfs(start, 0):
                return False

    return True


if __name__ == "__main__":
    # Example 1: Bipartite graph (square)
    #   0 -- 1
    #   |    |
    #   3 -- 2
    adj1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(f"Graph 1 (square): {is_bipartite(adj1, 4)}")  # Output: True

    # Example 2: Non-bipartite graph (triangle)
    #   0 -- 1
    #    \  /
    #      2
    adj2 = [[1, 2], [0, 2], [0, 1]]
    print(f"Graph 2 (triangle): {is_bipartite(adj2, 3)}")  # Output: False

    # Example 3: Bipartite graph (path)
    #   0 -- 1 -- 2 -- 3
    adj3 = [[1], [0, 2], [1, 3], [2]]
    print(f"Graph 3 (path): {is_bipartite(adj3, 4)}")  # Output: True

    # Example 4: Disconnected bipartite graph
    adj4 = [[1], [0], [3], [2]]
    print(f"Graph 4 (disconnected): {is_bipartite(adj4, 4)}")  # Output: True

    # Example 5: Using DFS approach
    print(f"\nDFS approach:")
    print(f"Graph 1: {is_bipartite_dfs(adj1, 4)}")  # Output: True
    print(f"Graph 2: {is_bipartite_dfs(adj2, 3)}")  # Output: False

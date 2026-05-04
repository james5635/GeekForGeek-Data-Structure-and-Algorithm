"""
Max Flow Problem Introduction.

The max flow problem involves finding the maximum amount of flow that can be sent from a source node s to a sink node t in a flow network, where each edge has a capacity constraint. This module explains the problem, the naive greedy approach (which fails), residual graphs, and presents the Ford-Fulkerson algorithm as a solution.

Based on: https://www.geeksforgeeks.org/max-flow-problem-introduction/
"""

from collections import deque
from typing import List


def bfs(
    residual_graph: List[List[int]], source: int, sink: int, parent: List[int]
) -> bool:
    """Check if there's a path from source to sink in the residual graph, and fill parent to store the path."""
    num_vertices = len(residual_graph)
    visited = [False] * num_vertices
    queue = deque([source])
    visited[source] = True
    parent[source] = -1

    while queue:
        u = queue.popleft()
        for v in range(num_vertices):
            if not visited[v] and residual_graph[u][v] > 0:
                queue.append(v)
                parent[v] = u
                visited[v] = True
    return visited[sink]


def ford_fulkerson(graph: List[List[int]], source: int, sink: int) -> int:
    """
    Compute the maximum flow from source to sink using the Ford-Fulkerson algorithm.

    Args:
        graph: Adjacency matrix representation of the flow network, where graph[u][v] is capacity of edge u->v.
        source: Source vertex index.
        sink: Sink vertex index.

    Returns:
        Maximum flow from source to sink.
    """
    num_vertices = len(graph)
    residual_graph = [[0] * num_vertices for _ in range(num_vertices)]
    for u in range(num_vertices):
        for v in range(num_vertices):
            residual_graph[u][v] = graph[u][v]

    parent = [-1] * num_vertices
    max_flow = 0

    while bfs(residual_graph, source, sink, parent):
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = parent[v]

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow


if __name__ == "__main__":
    # Example graph from GeeksforGeeks
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0],
    ]
    source = 0
    sink = 5
    print(
        f"Maximum possible flow (intro example): {ford_fulkerson(graph, source, sink)}"
    )

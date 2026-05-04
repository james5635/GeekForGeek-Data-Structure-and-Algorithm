"""
Maximum Number of Edge-Disjoint Paths Between Two Vertices.

Edge-disjoint paths share no common edges. The maximum number equals the max flow from s to t when all edge capacities are set to 1.

Based on: https://www.geeksforgeeks.org/problems/find-maximum-number-of-edge-disjoint-paths-between-two-vertices/1
"""

from collections import deque
from typing import List


def _bfs(
    residual_graph: List[List[int]], source: int, sink: int, parent: List[int]
) -> bool:
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


def _ford_fulkerson(graph: List[List[int]], source: int, sink: int) -> int:
    num_vertices = len(graph)
    residual_graph = [[0] * num_vertices for _ in range(num_vertices)]
    for u in range(num_vertices):
        for v in range(num_vertices):
            residual_graph[u][v] = graph[u][v]
    parent = [-1] * num_vertices
    max_flow = 0
    while _bfs(residual_graph, source, sink, parent):
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


def max_edge_disjoint_paths(graph: List[List[int]], source: int, sink: int) -> int:
    """
    Compute maximum edge-disjoint paths from source to sink.

    Args:
        graph: Adjacency matrix where graph[u][v] = 1 if edge u->v exists.
        source: Source vertex.
        sink: Sink vertex.

    Returns:
        Maximum number of edge-disjoint paths.
    """
    capacity_graph = [
        [1 if graph[u][v] > 0 else 0 for v in range(len(graph))]
        for u in range(len(graph))
    ]
    return _ford_fulkerson(capacity_graph, source, sink)


if __name__ == "__main__":
    # Graph: 0->1, 0->2, 1->2, 1->3, 2->3
    graph = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
    print(
        f"Max edge-disjoint paths: {max_edge_disjoint_paths(graph, 0, 3)}"
    )  # Output: 2

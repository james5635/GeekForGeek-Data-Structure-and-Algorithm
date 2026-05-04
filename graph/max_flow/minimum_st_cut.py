"""
Minimum s-t Cut in a Flow Network.

Finds the minimum capacity cut separating source s and sink t. Uses max flow and residual graph analysis.

Based on: https://www.geeksforgeeks.org/find-minimum-s-t-cut-in-a-flow-network/
"""

from collections import deque
from typing import List, Tuple


def _bfs(residual_graph: List[List[int]], source: int, visited: List[bool]) -> None:
    queue = deque([source])
    visited[source] = True
    while queue:
        u = queue.popleft()
        for v in range(len(residual_graph)):
            if residual_graph[u][v] > 0 and not visited[v]:
                visited[v] = True
                queue.append(v)


def ford_fulkerson(
    graph: List[List[int]], source: int, sink: int
) -> Tuple[int, List[List[int]]]:
    num_vertices = len(graph)
    residual_graph = [[0] * num_vertices for _ in range(num_vertices)]
    for u in range(num_vertices):
        for v in range(num_vertices):
            residual_graph[u][v] = graph[u][v]
    parent = [-1] * num_vertices

    def bfs() -> bool:
        visited = [False] * num_vertices
        queue = deque([source])
        visited[source] = True
        parent[source] = -1
        while queue:
            u = queue.popleft()
            for v in range(num_vertices):
                if not visited[v] and residual_graph[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        return visited[sink]

    max_flow = 0
    while bfs():
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
    return max_flow, residual_graph


def find_min_st_cut(
    graph: List[List[int]], source: int, sink: int
) -> Tuple[int, List[Tuple[int, int]]]:
    """Find minimum s-t cut capacity and edges."""
    max_flow, residual_graph = ford_fulkerson(graph, source, sink)
    reachable = [False] * len(graph)
    _bfs(residual_graph, source, reachable)

    cut_edges = []
    for u in range(len(graph)):
        for v in range(len(graph)):
            if graph[u][v] > 0 and reachable[u] and not reachable[v]:
                cut_edges.append((u, v))
    return max_flow, cut_edges


if __name__ == "__main__":
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0],
    ]
    capacity, edges = find_min_st_cut(graph, 0, 5)
    print(f"Minimum s-t cut capacity: {capacity}")  # Output: 23
    print("Cut edges:", edges)  # Output: [(1,3), (4,3), (4,5)]

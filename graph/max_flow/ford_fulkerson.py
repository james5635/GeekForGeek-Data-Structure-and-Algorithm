"""
Ford-Fulkerson Algorithm for Maximum Flow Problem.

The Ford-Fulkerson algorithm computes maximum flow by finding augmenting paths and sending flow until no more paths exist. Uses residual graphs with reverse edges to enable flow redistribution.

Based on: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow/
"""

from collections import deque
from typing import List


class FlowNetwork:
    """Flow network with residual graph tracking."""

    def __init__(self, graph: List[List[int]], source: int, sink: int):
        self.original_graph = graph
        self.num_vertices = len(graph)
        self.source = source
        self.sink = sink
        self.residual_graph = [
            [0] * self.num_vertices for _ in range(self.num_vertices)
        ]
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                self.residual_graph[u][v] = graph[u][v]
        self.parent = [-1] * self.num_vertices

    def _bfs(self) -> bool:
        """Find augmenting path from source to sink."""
        visited = [False] * self.num_vertices
        queue = deque([self.source])
        visited[self.source] = True
        self.parent[self.source] = -1

        while queue:
            u = queue.popleft()
            for v in range(self.num_vertices):
                if not visited[v] and self.residual_graph[u][v] > 0:
                    queue.append(v)
                    self.parent[v] = u
                    visited[v] = True
        return visited[self.sink]

    def compute_max_flow(self) -> int:
        """Compute maximum flow from source to sink."""
        max_flow = 0
        while self._bfs():
            path_flow = float("inf")
            v = self.sink
            while v != self.source:
                u = self.parent[v]
                path_flow = min(path_flow, self.residual_graph[u][v])
                v = self.parent[v]

            v = self.sink
            while v != self.source:
                u = self.parent[v]
                self.residual_graph[u][v] -= path_flow
                self.residual_graph[v][u] += path_flow
                v = self.parent[v]

            max_flow += path_flow
        return max_flow


def ford_fulkerson(graph: List[List[int]], source: int, sink: int) -> int:
    """Wrapper function for Ford-Fulkerson algorithm."""
    network = FlowNetwork(graph, source, sink)
    return network.compute_max_flow()


if __name__ == "__main__":
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0],
    ]
    print(f"Maximum flow (Ford-Fulkerson): {ford_fulkerson(graph, 0, 5)}")

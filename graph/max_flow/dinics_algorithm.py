"""
Dinic's Algorithm for Maximum Flow.

Faster max flow algorithm using BFS for level graphs and DFS for blocking flows. Time complexity: O(EV²).

Based on: https://www.geeksforgeeks.org/dinics-algorithm-for-maximum-flow/
"""

from collections import deque
from typing import List


class Edge:
    def __init__(self, to: int, rev: int, capacity: int):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.flow = 0


class Dinic:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj = [[] for _ in range(num_vertices)]
        self.level = [0] * num_vertices

    def add_edge(self, u: int, v: int, capacity: int) -> None:
        forward = Edge(v, len(self.adj[v]), capacity)
        backward = Edge(u, len(self.adj[u]), 0)
        self.adj[u].append(forward)
        self.adj[v].append(backward)

    def _bfs(self, source: int, sink: int) -> bool:
        self.level = [-1] * self.num_vertices
        self.level[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for edge in self.adj[u]:
                if self.level[edge.to] == -1 and edge.capacity - edge.flow > 0:
                    self.level[edge.to] = self.level[u] + 1
                    queue.append(edge.to)
        return self.level[sink] != -1

    def _dfs(self, u: int, sink: int, flow: int, start: List[int]) -> int:
        if u == sink:
            return flow
        while start[u] < len(self.adj[u]):
            edge = self.adj[u][start[u]]
            if (
                self.level[edge.to] == self.level[u] + 1
                and edge.capacity - edge.flow > 0
            ):
                curr_flow = min(flow, edge.capacity - edge.flow)
                temp_flow = self._dfs(edge.to, sink, curr_flow, start)
                if temp_flow > 0:
                    edge.flow += temp_flow
                    self.adj[edge.to][edge.rev].flow -= temp_flow
                    return temp_flow
            start[u] += 1
        return 0

    def max_flow(self, source: int, sink: int) -> int:
        if source == sink:
            return 0
        total_flow = 0
        while self._bfs(source, sink):
            start = [0] * self.num_vertices
            while True:
                flow = self._dfs(source, sink, float("inf"), start)
                if flow == 0:
                    break
                total_flow += flow
        return total_flow


if __name__ == "__main__":
    dinic = Dinic(6)
    dinic.add_edge(0, 1, 16)
    dinic.add_edge(0, 2, 13)
    dinic.add_edge(1, 2, 10)
    dinic.add_edge(1, 3, 12)
    dinic.add_edge(2, 1, 4)
    dinic.add_edge(2, 4, 14)
    dinic.add_edge(3, 2, 9)
    dinic.add_edge(3, 5, 20)
    dinic.add_edge(4, 3, 7)
    dinic.add_edge(4, 5, 4)
    print(f"Maximum flow (Dinic's): {dinic.max_flow(0, 5)}")  # Output: 23

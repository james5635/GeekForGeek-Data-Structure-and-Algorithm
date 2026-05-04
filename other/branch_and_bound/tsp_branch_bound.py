"""Traveling Salesman Problem using Branch and Bound."""

from __future__ import annotations

import heapq


class TSPNode:
    """Node for TSP branch and bound search."""

    def __init__(
        self, level: int, path: list[int], visited: set[int], cost: float, bound: float
    ) -> None:
        self.level = level
        self.path = path
        self.visited = visited
        self.cost = cost
        self.bound = bound

    def __lt__(self, other: "TSPNode") -> bool:
        return self.bound > other.bound


def _calculate_bound(node: TSPNode, graph: list[list[float]], n: int) -> float:
    bound = node.cost

    if node.level == n - 1:
        return bound + graph[node.path[-1]][0]

    last = node.path[-1]
    visited = node.visited

    min_edge = float("inf")
    for j in range(n):
        if j not in visited and graph[last][j] < min_edge:
            min_edge = graph[last][j]
    if min_edge < float("inf"):
        bound += min_edge

    min_remaining = 0.0
    for i in range(n):
        if i not in visited:
            min_out = float("inf")
            for j in range(n):
                if j != i and (j not in visited or j == 0) and graph[i][j] < min_out:
                    min_out = graph[i][j]
            if min_out < float("inf"):
                min_remaining += min_out

    return bound + min_remaining


def tsp_branch_bound(graph: list[list[float]]) -> tuple[list[int], float]:
    """Solve TSP using Branch and Bound.

    Args:
        graph: Adjacency matrix where graph[i][j] is the cost from city i to city j.

    Returns:
        Tuple of (optimal path, optimal cost).
    """
    n = len(graph)
    root = TSPNode(0, [0], {0}, 0.0, 0.0)
    root.bound = _calculate_bound(root, graph, n)
    pq: list[TSPNode] = [root]
    heapq.heapify(pq)

    best_cost = float("inf")
    best_path: list[int] = []

    while pq:
        current = heapq.heappop(pq)

        if current.bound >= best_cost:
            continue

        if current.level == n - 1:
            total = current.cost + graph[current.path[-1]][0]
            if total < best_cost:
                best_cost = total
                best_path = current.path[:]
            continue

        last = current.path[-1]
        for j in range(n):
            if j not in current.visited and graph[last][j] < float("inf"):
                new_path = current.path + [j]
                new_visited = current.visited | {j}
                new_cost = current.cost + graph[last][j]
                child = TSPNode(current.level + 1, new_path, new_visited, new_cost, 0.0)
                child.bound = _calculate_bound(child, graph, n)
                if child.bound < best_cost:
                    heapq.heappush(pq, child)

    if best_path:
        best_path.append(0)
    return best_path, best_cost


if __name__ == "__main__":
    INF = float("inf")
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    path, cost = tsp_branch_bound(graph)
    print(f"Optimal path: {path}")
    print(f"Optimal cost: {cost}")

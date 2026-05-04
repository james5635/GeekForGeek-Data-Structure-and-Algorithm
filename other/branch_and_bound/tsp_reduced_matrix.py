"""Traveling Salesman Problem using Reduced Matrix Method."""

from __future__ import annotations

import copy
import heapq
from dataclasses import dataclass, field

INF = float("inf")


@dataclass
class TSPReducedNode:
    """Node for TSP with reduced matrix."""

    reduced_matrix: list[list[float]]
    path: list[int]
    cost: float
    level: int
    visited: set[int] = field(default_factory=set)

    def __lt__(self, other: "TSPReducedNode") -> bool:
        return self.cost < other.cost


def _reduce_matrix(
    matrix: list[list[float]], n: int
) -> tuple[list[list[float]], float]:
    reduction_cost = 0.0
    new_matrix = [row[:] for row in matrix]

    for i in range(n):
        row_min = min(new_matrix[i])
        if row_min < INF:
            reduction_cost += row_min
            for j in range(n):
                if new_matrix[i][j] < INF:
                    new_matrix[i][j] -= row_min

    for j in range(n):
        col_min = INF
        for i in range(n):
            if new_matrix[i][j] < col_min:
                col_min = new_matrix[i][j]
        if col_min < INF:
            reduction_cost += col_min
            for i in range(n):
                if new_matrix[i][j] < INF:
                    new_matrix[i][j] -= col_min

    return new_matrix, reduction_cost


def _set_path_infinity(
    matrix: list[list[float]], u: int, v: int, n: int
) -> list[list[float]]:
    new_matrix = [row[:] for row in matrix]
    for i in range(n):
        new_matrix[u][i] = INF
        new_matrix[i][v] = INF
    new_matrix[v][0] = INF
    new_matrix[u][u] = INF
    return new_matrix


def tsp_reduced_matrix(graph: list[list[float]]) -> tuple[list[int], float]:
    """Solve TSP using Reduced Matrix method with Branch and Bound.

    Args:
        graph: Adjacency matrix where graph[i][j] is the cost from city i to city j.

    Returns:
        Tuple of (optimal path, optimal cost).
    """
    n = len(graph)
    reduced, root_cost = _reduce_matrix(graph, n)

    root = TSPReducedNode(
        reduced_matrix=reduced,
        path=[0],
        cost=root_cost,
        level=0,
        visited={0},
    )

    pq: list[TSPReducedNode] = [root]
    best_cost = INF
    best_path: list[int] = []

    while pq:
        heapq.heapify(pq)
        current = heapq.heappop(pq)

        if current.cost >= best_cost:
            continue

        if current.level == n - 1:
            return current.path + [0], current.cost

        last = current.path[-1]
        for j in range(n):
            if j not in current.visited and current.reduced_matrix[last][j] < INF:
                new_matrix = _set_path_infinity(current.reduced_matrix, last, j, n)
                reduced, reduction = _reduce_matrix(new_matrix, n)
                child = TSPReducedNode(
                    reduced_matrix=reduced,
                    path=current.path + [j],
                    cost=current.cost + current.reduced_matrix[last][j] + reduction,
                    level=current.level + 1,
                    visited=current.visited | {j},
                )
                if child.cost < best_cost:
                    heapq.heappush(pq, child)

    return best_path, best_cost


if __name__ == "__main__":
    graph = [
        [INF, 10, 15, 20],
        [10, INF, 35, 25],
        [15, 35, INF, 30],
        [20, 25, 30, INF],
    ]
    path, cost = tsp_reduced_matrix(graph)
    print(f"Optimal path: {path}")
    print(f"Optimal cost: {cost}")

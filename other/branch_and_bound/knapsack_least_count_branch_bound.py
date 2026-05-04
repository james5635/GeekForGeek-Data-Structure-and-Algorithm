"""0/1 Knapsack Problem using Least Count (Least Cost) Branch and Bound."""

from __future__ import annotations

import heapq


class LCNode:
    """Node for Least Count Branch and Bound."""

    def __init__(
        self,
        level: int,
        profit: int,
        weight: int,
        cost: int,
        parent: "LCNode | None" = None,
        include: bool = False,
    ) -> None:
        self.level = level
        self.profit = profit
        self.weight = weight
        self.cost = cost
        self.parent = parent
        self.include = include

    def __lt__(self, other: "LCNode") -> bool:
        return self.cost < other.cost


def _calculate_upper_bound(
    level: int,
    current_profit: int,
    current_weight: int,
    n: int,
    capacity: int,
    weights: list[int],
    profits: list[int],
    ratios: list[float],
) -> int:
    bound = current_profit
    remaining_weight = current_weight

    for i in range(level + 1, n):
        if remaining_weight + weights[i] <= capacity:
            remaining_weight += weights[i]
            bound += profits[i]
        else:
            bound += int((capacity - remaining_weight) * ratios[i])
            break

    return bound


def knapsack_least_count(weights: list[int], profits: list[int], capacity: int) -> int:
    """Solve 0/1 Knapsack using Least Count Branch and Bound.

    Uses a min-priority queue ordered by the cost (total potential profit - upper bound).

    Args:
        weights: List of item weights.
        profits: List of item profits.
        capacity: Maximum weight capacity of the knapsack.

    Returns:
        Maximum profit achievable.
    """
    n = len(weights)
    indices = sorted(range(n), key=lambda i: profits[i] / weights[i], reverse=True)
    weights_sorted = [weights[i] for i in indices]
    profits_sorted = [profits[i] for i in indices]
    ratios = [profits_sorted[i] / weights_sorted[i] for i in range(n)]

    total_potential = sum(profits_sorted)

    root_bound = _calculate_upper_bound(
        -1, 0, 0, n, capacity, weights_sorted, profits_sorted, ratios
    )
    root = LCNode(-1, 0, 0, total_potential - root_bound)
    pq: list[LCNode] = [root]
    max_profit = 0

    while pq:
        heapq.heapify(pq)
        current = heapq.heappop(pq)

        level = current.level + 1
        if level == n:
            continue

        left_profit = current.profit + profits_sorted[level]
        left_weight = current.weight + weights_sorted[level]

        if left_weight <= capacity:
            left_bound = _calculate_upper_bound(
                level,
                left_profit,
                left_weight,
                n,
                capacity,
                weights_sorted,
                profits_sorted,
                ratios,
            )
            if left_profit > max_profit:
                max_profit = left_profit
            left_cost = total_potential - left_bound
            left_node = LCNode(
                level, left_profit, left_weight, left_cost, current, True
            )
            heapq.heappush(pq, left_node)

        right_bound = _calculate_upper_bound(
            level,
            current.profit,
            current.weight,
            n,
            capacity,
            weights_sorted,
            profits_sorted,
            ratios,
        )
        right_cost = total_potential - right_bound
        right_node = LCNode(
            level, current.profit, current.weight, right_cost, current, False
        )
        if right_bound > max_profit:
            heapq.heappush(pq, right_node)

    return max_profit


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    profits = [3, 4, 5, 6]
    capacity = 5
    result = knapsack_least_count(weights, profits, capacity)
    print(f"Maximum profit: {result}")

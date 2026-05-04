"""Implementation of 0/1 Knapsack Problem using Branch and Bound."""

from __future__ import annotations

import heapq


class KnapsackNode:
    """Node for the branch and bound tree."""

    def __init__(self, level: int, profit: int, weight: int, bound: float) -> None:
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    def __lt__(self, other: "KnapsackNode") -> bool:
        return self.bound > other.bound


def _calculate_bound(
    level: int,
    current_profit: int,
    current_weight: int,
    n: int,
    capacity: int,
    weights: list[int],
    profits: list[int],
    ratios: list[float],
) -> float:
    if current_weight >= capacity:
        return float(current_profit)

    bound = float(current_profit)
    remaining_weight = float(current_weight)

    for i in range(level + 1, n):
        if remaining_weight + weights[i] <= capacity:
            remaining_weight += weights[i]
            bound += profits[i]
        else:
            bound += (capacity - remaining_weight) * ratios[i]
            break

    return bound


def knapsack_branch_bound(weights: list[int], profits: list[int], capacity: int) -> int:
    """Solve 0/1 Knapsack using Branch and Bound with max-heap.

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

    root = KnapsackNode(
        -1,
        0,
        0,
        _calculate_bound(-1, 0, 0, n, capacity, weights_sorted, profits_sorted, ratios),
    )
    pq: list[KnapsackNode] = [root]
    heapq.heapify(pq)
    max_profit = 0

    while pq:
        current = heapq.heappop(pq)

        if current.bound <= max_profit:
            continue

        level = current.level + 1
        if level == n:
            continue

        left = KnapsackNode(
            level,
            current.profit + profits_sorted[level],
            current.weight + weights_sorted[level],
            0,
        )
        if left.weight <= capacity:
            left.bound = _calculate_bound(
                level,
                left.profit,
                left.weight,
                n,
                capacity,
                weights_sorted,
                profits_sorted,
                ratios,
            )
            if left.profit > max_profit:
                max_profit = left.profit
            if left.bound > max_profit:
                heapq.heappush(pq, left)

        right = KnapsackNode(level, current.profit, current.weight, 0)
        right.bound = _calculate_bound(
            level,
            right.profit,
            right.weight,
            n,
            capacity,
            weights_sorted,
            profits_sorted,
            ratios,
        )
        if right.bound > max_profit:
            heapq.heappush(pq, right)

    return max_profit


if __name__ == "__main__":
    weights = [10, 20, 30]
    profits = [60, 100, 120]
    capacity = 50
    result = knapsack_branch_bound(weights, profits, capacity)
    print(f"Maximum profit: {result}")

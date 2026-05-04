"""0/1 Knapsack Problem using Branch and Bound."""

from __future__ import annotations


class Node:
    """Represents a node in the branch and bound tree."""

    def __init__(
        self,
        level: int,
        profit: float,
        weight: float,
        bound: float,
        include: list[bool],
    ) -> None:
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound
        self.include = include[:]


def _bound(
    node: Node,
    n: int,
    capacity: float,
    weights: list[float],
    profits: list[float],
    ratio: list[float],
) -> float:
    if node.weight >= capacity:
        return node.profit

    result = node.profit
    total_weight = node.weight

    for i in range(node.level + 1, n):
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            result += profits[i]
        else:
            result += (capacity - total_weight) * ratio[i]
            break

    return result


def knapsack_branch_bound(
    weights: list[float], profits: list[float], capacity: float
) -> float:
    """Solve 0/1 Knapsack using Branch and Bound.

    Args:
        weights: List of item weights.
        profits: List of item profits.
        capacity: Maximum weight capacity of the knapsack.

    Returns:
        Maximum profit achievable.
    """
    n = len(weights)
    pairs = sorted(zip(profits, weights), key=lambda x: x[0] / x[1], reverse=True)
    profits_sorted = [p for p, _ in pairs]
    weights_sorted = [w for _, w in pairs]
    ratio = [p / w for p, w in pairs]

    root = Node(
        -1,
        0.0,
        0.0,
        _bound(
            Node(-1, 0.0, 0.0, 0.0, []),
            n,
            capacity,
            weights_sorted,
            profits_sorted,
            ratio,
        ),
        [],
    )
    queue: list[Node] = [root]
    max_profit = 0.0

    while queue:
        queue.sort(key=lambda node: node.bound, reverse=True)
        current = queue.pop(0)

        if current.bound <= max_profit:
            continue

        level = current.level + 1
        if level == n:
            continue

        u = Node(
            level,
            current.profit + profits_sorted[level],
            current.weight + weights_sorted[level],
            0.0,
            current.include + [True],
        )

        if u.weight <= capacity:
            u.bound = _bound(u, n, capacity, weights_sorted, profits_sorted, ratio)
            if u.bound > max_profit:
                max_profit = max(max_profit, u.profit)
                queue.append(u)

        v = Node(level, current.profit, current.weight, 0.0, current.include + [False])
        v.bound = _bound(v, n, capacity, weights_sorted, profits_sorted, ratio)
        if v.bound > max_profit:
            queue.append(v)

    return max_profit


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    profits = [3, 4, 5, 6]
    capacity = 5
    result = knapsack_branch_bound(weights, profits, capacity)
    print(f"Maximum profit: {result}")

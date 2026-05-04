"""Check if given four points form a square."""

import math


def dist(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def four_points_square(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
) -> bool:
    """Check if four points form a square.

    Args:
        p1, p2, p3, p4: Four points as (x, y) tuples.

    Returns:
        True if points form a square, False otherwise.
    """
    points = [p1, p2, p3, p4]
    distances = []

    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(dist(points[i], points[j]))

    distances.sort()

    if distances[0] == 0:
        return False

    side = distances[0]
    diagonal = distances[-1]

    return (
        distances[0] == distances[1] == distances[2] == distances[3]
        and distances[4] == distances[5]
        and distances[4] == 2 * side
    )


if __name__ == "__main__":
    print(f"Square: {four_points_square((0, 0), (1, 0), (1, 1), (0, 1))}")
    print(f"Square: {four_points_square((0, 0), (2, 0), (2, 1), (0, 1))}")

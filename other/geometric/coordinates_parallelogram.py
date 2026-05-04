"""Find possible coordinates of parallelogram."""

from typing import List


def coordinates_parallelogram(
    p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]
) -> list[tuple[float, float]]:
    """Find all possible fourth vertices of a parallelogram given three vertices.

    Args:
        p1, p2, p3: Three known vertices as (x, y) tuples.

    Returns:
        List of possible fourth vertex coordinates.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return [
        (x1 + x3 - x2, y1 + y3 - y2),
        (x1 + x2 - x3, y1 + y2 - y3),
        (x2 + x3 - x1, y2 + y3 - y1),
    ]


if __name__ == "__main__":
    possible = coordinates_parallelogram((0, 0), (4, 0), (2, 3))
    print(f"Possible fourth points: {possible}")

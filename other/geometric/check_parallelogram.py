"""Check whether four points make a parallelogram."""

import math


def dist(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def check_parallelogram(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
) -> bool:
    """Check if four points form a parallelogram.

    Args:
        p1, p2, p3, p4: Four points as (x, y) tuples.

    Returns:
        True if points form a parallelogram, False otherwise.
    """
    mid1 = ((p1[0] + p3[0]) / 2, (p1[1] + p3[1]) / 2)
    mid2 = ((p2[0] + p4[0]) / 2, (p2[1] + p4[1]) / 2)

    if abs(mid1[0] - mid2[0]) < 1e-10 and abs(mid1[1] - mid2[1]) < 1e-10:
        return True

    mid1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    mid2 = ((p3[0] + p4[0]) / 2, (p3[1] + p4[1]) / 2)

    if abs(mid1[0] - mid2[0]) < 1e-10 and abs(mid1[1] - mid2[1]) < 1e-10:
        return True

    mid1 = ((p1[0] + p4[0]) / 2, (p1[1] + p4[1]) / 2)
    mid2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)

    return abs(mid1[0] - mid2[0]) < 1e-10 and abs(mid1[1] - mid2[1]) < 1e-10


if __name__ == "__main__":
    print(f"Parallelogram: {check_parallelogram((0, 0), (4, 0), (5, 3), (1, 3))}")
    print(f"Parallelogram: {check_parallelogram((0, 0), (2, 0), (3, 2), (1, 3))}")

"""Find missing point of a parallelogram."""


def missing_point_parallelogram(
    p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]
) -> tuple[float, float]:
    """Find the fourth point of a parallelogram given three consecutive vertices.

    Args:
        p1, p2, p3: Three consecutive vertices as (x, y) tuples.

    Returns:
        Fourth vertex coordinates.
    """
    x4 = p1[0] + p3[0] - p2[0]
    y4 = p1[1] + p3[1] - p2[1]
    return (x4, y4)


if __name__ == "__main__":
    print(f"Missing point: {missing_point_parallelogram((0, 0), (4, 0), (2, 3))}")

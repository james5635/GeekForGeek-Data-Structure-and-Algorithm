"""Check whether a given point lies inside a rectangle or not."""


def point_inside_rectangle(
    px: float,
    py: float,
    ax: float,
    ay: float,
    bx: float,
    by: float,
    cx: float,
    cy: float,
    dx: float,
    dy: float,
) -> bool:
    """Check if a point lies inside a rectangle.

    Args:
        px, py: Point coordinates.
        ax, ay, bx, by, cx, cy, dx, dy: Rectangle vertices in order.

    Returns:
        True if point is inside or on rectangle boundary, False otherwise.
    """

    def cross_product(
        o: tuple[float, float], a: tuple[float, float], b: tuple[float, float]
    ) -> float:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    p = (px, py)
    signs = []
    for v1, v2 in (
        [(ax, ay), (bx, by)],
        [(bx, by), (cx, cy)],
        [(cx, cy), (dx, dy)],
        [(dx, dy), (ax, ay)],
    ):
        cp = cross_product(v1, v2, (px, py))
        if cp > 0:
            signs.append(1)
        elif cp < 0:
            signs.append(-1)

    return not (1 in signs and -1 in signs)


if __name__ == "__main__":
    print(f"(2, 2) in rect: {point_inside_rectangle(2, 2, 0, 0, 4, 0, 4, 4, 0, 4)}")
    print(f"(5, 5) in rect: {point_inside_rectangle(5, 5, 0, 0, 4, 0, 4, 4, 0, 4)}")

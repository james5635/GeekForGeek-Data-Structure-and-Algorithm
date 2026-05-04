"""Finding vertex, focus, and directrix of parabola."""


def parabola_vertex_focus_directrix(
    a: float, b: float, c: float
) -> tuple[tuple[float, float], tuple[float, float], float]:
    """Find vertex, focus, and directrix of a parabola y = ax^2 + bx + c.

    Args:
        a, b, c: Coefficients of the parabola equation.

    Returns:
        Tuple of (vertex, focus, directrix_y).
    """
    vx = -b / (2 * a)
    vy = a * vx * vx + b * vx + c

    p = 1 / (4 * a)

    focus = (vx, vy + p)
    directrix = vy - p

    return (
        (round(vx, 4), round(vy, 4)),
        (round(focus[0], 4), round(focus[1], 4)),
        round(directrix, 4),
    )


if __name__ == "__main__":
    vertex, focus, directrix = parabola_vertex_focus_directrix(1, -2, 1)
    print(f"Vertex: {vertex}")
    print(f"Focus: {focus}")
    print(f"Directrix: y = {directrix}")

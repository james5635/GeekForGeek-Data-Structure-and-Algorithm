"""Number of triangles that can be formed from given set of lines."""

from itertools import combinations


def triangles_from_lines(lines: list[tuple[float, float, float]]) -> int:
    """Count number of triangles formed by intersection of lines.

    Args:
        lines: List of tuples (a, b, c) representing lines ax + by = c.

    Returns:
        Number of triangles that can be formed.
    """
    count = 0
    for l1, l2, l3 in combinations(lines, 3):
        a1, b1, c1 = l1
        a2, b2, c2 = l2
        a3, b3, c3 = l3

        d1 = a1 * b2 - a2 * b1
        d2 = a2 * b3 - a3 * b2
        d3 = a3 * b1 - a1 * b3

        if d1 != 0 and d2 != 0 and d3 != 0:
            count += 1

    return count


if __name__ == "__main__":
    lines = [(1, 1, 2), (2, -1, 1), (1, 2, 3), (3, 1, 4)]
    print(f"Triangles: {triangles_from_lines(lines)}")

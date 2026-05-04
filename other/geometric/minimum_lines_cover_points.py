"""Minimum lines to cover points."""

import math
from typing import Set


def get_slope_key(p1: tuple[int, int], p2: tuple[int, int]) -> str:
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    if dx == 0:
        return f"inf_{p1[0]}"
    if dy == 0:
        return f"0_{p1[1]}"

    g = math.gcd(dx, dy)
    dx //= g
    dy //= g
    if dx < 0:
        dx, dy = -dx, -dy

    intercept = p1[1] * dx - p1[0] * dy
    return f"{dy}/{dx}_{intercept}"


def minimum_lines_cover_points(points: list[tuple[int, int]]) -> int:
    """Find minimum number of lines to cover all points.

    Args:
        points: List of (x, y) coordinate tuples.

    Returns:
        Minimum number of lines needed.
    """
    n = len(points)
    if n <= 1:
        return n

    covered: Set[int] = set()
    lines = 0

    while len(covered) < n:
        best_line: Set[int] = set()
        first_uncovered = -1
        for i in range(n):
            if i not in covered:
                first_uncovered = i
                break

        for j in range(first_uncovered + 1, n):
            if j in covered:
                continue
            line_points: Set[int] = {first_uncovered, j}
            for k in range(j + 1, n):
                if k in covered:
                    continue
                s1 = (points[j][1] - points[first_uncovered][1]) * (
                    points[k][0] - points[j][0]
                )
                s2 = (points[k][1] - points[j][1]) * (
                    points[j][0] - points[first_uncovered][0]
                )
                if s1 == s2:
                    line_points.add(k)

            if len(line_points) > len(best_line):
                best_line = line_points

        if not best_line:
            best_line = {first_uncovered}

        covered.update(best_line)
        lines += 1

    return lines


if __name__ == "__main__":
    points = [(1, 1), (2, 2), (3, 3), (1, 2), (2, 4)]
    print(f"Minimum lines: {minimum_lines_cover_points(points)}")

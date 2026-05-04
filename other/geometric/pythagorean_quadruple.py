"""Pythagorean quadruple."""

from typing import List


def pythagorean_quadruple(n: int) -> list[tuple[int, int, int, int]]:
    """Find Pythagorean quadruples where a^2 + b^2 + c^2 = d^2 with d <= n.

    Args:
        n: Maximum value for d.

    Returns:
        List of tuples (a, b, c, d) forming Pythagorean quadruples.
    """
    results = []
    for a in range(1, n):
        for b in range(a, n):
            for c in range(b, n):
                s = a * a + b * b + c * c
                d = int(s**0.5)
                if d * d == s and d <= n:
                    results.append((a, b, c, d))
    return results


if __name__ == "__main__":
    quads = pythagorean_quadruple(20)
    print(f"Pythagorean quadruples: {quads}")

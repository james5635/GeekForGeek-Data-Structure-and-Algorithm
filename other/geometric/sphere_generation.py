"""L3NS3 sphere generation algorithm.

Generates sphere-like point distributions on a unit sphere.
"""

import math


def sphere_generation(num_points: int) -> list[tuple[float, float, float]]:
    """Generate points distributed on a unit sphere using Fibonacci lattice.

    Args:
        num_points: Number of points to generate.

    Returns:
        List of (x, y, z) coordinates on the unit sphere.
    """
    points = []
    golden_ratio = (1 + math.sqrt(5)) / 2

    for i in range(num_points):
        theta = 2 * math.pi * i / golden_ratio
        phi = math.acos(1 - 2 * (i + 0.5) / num_points)

        x = math.sin(phi) * math.cos(theta)
        y = math.sin(phi) * math.sin(theta)
        z = math.cos(phi)

        points.append((round(x, 4), round(y, 4), round(z, 4)))

    return points


if __name__ == "__main__":
    points = sphere_generation(10)
    print(f"Sphere points: {points}")

"""Number of parallelograms when n horizontal parallel lines intersect m vertical parallel lines."""


def parallelograms_parallel_lines(n: int, m: int) -> int:
    """Count parallelograms formed by n horizontal and m vertical parallel lines.

    Args:
        n: Number of horizontal parallel lines.
        m: Number of vertical parallel lines.

    Returns:
        Number of parallelograms formed.
    """
    return (n * (n - 1) * m * (m - 1)) // 4


if __name__ == "__main__":
    print(
        f"Parallelograms (4 horizontal, 4 vertical): {parallelograms_parallel_lines(4, 4)}"
    )
    print(
        f"Parallelograms (3 horizontal, 2 vertical): {parallelograms_parallel_lines(3, 2)}"
    )

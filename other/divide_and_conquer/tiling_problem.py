def tiling_problem(n: int) -> int:
    """
    Solve the tiling problem: count ways to tile a 2xn board with 2x1 tiles.

    Args:
        n: Length of the board (width is 2)

    Returns:
        Number of ways to tile the board
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    return tiling_problem(n - 1) + tiling_problem(n - 2)


def tiling_problem_efficient(n: int) -> int:
    """
    Solve the tiling problem iteratively in O(n) time.

    Args:
        n: Length of the board (width is 2)

    Returns:
        Number of ways to tile the board
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print(tiling_problem_efficient(3))
    print(tiling_problem_efficient(4))
    print(tiling_problem_efficient(5))

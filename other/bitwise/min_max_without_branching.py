def min_without_branching(a: int, b: int) -> int:
    """Compute the minimum of two integers without branching."""
    return b ^ ((a ^ b) & (a - b) >> 31)


def max_without_branching(a: int, b: int) -> int:
    """Compute the maximum of two integers without branching."""
    return a ^ ((a ^ b) & (a - b) >> 31)


if __name__ == "__main__":
    print(min_without_branching(5, 3))
    print(max_without_branching(5, 3))

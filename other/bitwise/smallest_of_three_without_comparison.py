def smallest_of_three_without_comparison(a: int, b: int, c: int) -> int:
    """Find smallest of three integers without comparison operators."""
    x, y, z = a, b, c
    x = (~((x - y) >> 31)) & x
    x = ((y - x) >> 31) | x
    y = (~((y - z) >> 31)) & y
    y = ((z - y) >> 31) | y
    x = (~((x - y) >> 31)) & x
    x = ((y - x) >> 31) | x
    return x


if __name__ == "__main__":
    print(smallest_of_three_without_comparison(3, 1, 2))
    print(smallest_of_three_without_comparison(5, 5, 5))
    print(smallest_of_three_without_comparison(10, 3, 7))

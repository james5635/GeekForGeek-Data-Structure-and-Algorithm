def swap_without_temp(a: int, b: int) -> tuple[int, int]:
    """Swap two numbers without using temporary variable."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == "__main__":
    print(swap_without_temp(5, 3))
    print(swap_without_temp(10, 20))

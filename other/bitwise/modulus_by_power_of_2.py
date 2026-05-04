def modulus_by_power_of_2(n: int, p: int) -> int:
    """Compute modulus division by a power-of-2 number (2^p)."""
    return n & ((1 << p) - 1)


if __name__ == "__main__":
    print(modulus_by_power_of_2(10, 3))
    print(modulus_by_power_of_2(27, 4))
    print(modulus_by_power_of_2(15, 2))

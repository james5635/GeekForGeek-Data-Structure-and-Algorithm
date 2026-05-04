def modular_exponentiation(base: int, exp: int, mod: int) -> int:
    """
    Calculate (base^exp) % mod using divide and conquer.

    Args:
        base: Base value
        exp: Exponent
        mod: Modulus

    Returns:
        (base^exp) % mod
    """
    if exp == 0:
        return 1 % mod

    if exp < 0:
        raise ValueError("Negative exponents not supported for modular arithmetic")

    base = base % mod

    half = modular_exponentiation(base, exp // 2, mod)
    result = (half * half) % mod

    if exp % 2 == 1:
        result = (result * base) % mod

    return result


if __name__ == "__main__":
    print(modular_exponentiation(2, 10, 1000000007))
    print(modular_exponentiation(3, 5, 7))
    print(modular_exponentiation(5, 0, 13))

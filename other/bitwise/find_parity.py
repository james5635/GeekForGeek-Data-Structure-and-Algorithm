def find_parity(n: int) -> int:
    """Find parity of a number (1 if odd number of set bits, 0 otherwise)."""
    parity = 0
    while n:
        parity ^= 1
        n &= n - 1
    return parity


if __name__ == "__main__":
    print(find_parity(5))
    print(find_parity(7))
    print(find_parity(0))

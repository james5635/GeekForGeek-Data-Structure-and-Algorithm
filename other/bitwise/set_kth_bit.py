def set_kth_bit(n: int, k: int) -> int:
    """Set k-th bit (0-indexed) in a given integer."""
    return n | (1 << k)


if __name__ == "__main__":
    print(set_kth_bit(5, 1))
    print(set_kth_bit(5, 2))
    print(set_kth_bit(0, 3))

def check_kth_bit(n: int, k: int) -> bool:
    """Check whether k-th bit (0-indexed) is set or not."""
    return (n & (1 << k)) != 0


if __name__ == "__main__":
    print(check_kth_bit(5, 0))
    print(check_kth_bit(5, 1))
    print(check_kth_bit(5, 2))

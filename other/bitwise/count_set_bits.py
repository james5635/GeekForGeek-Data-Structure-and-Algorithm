def count_set_bits(n: int) -> int:
    """Count set bits in an integer using Brian Kernighan's algorithm."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


if __name__ == "__main__":
    print(count_set_bits(5))
    print(count_set_bits(7))
    print(count_set_bits(0))

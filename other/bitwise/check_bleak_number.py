def check_bleak_number(n: int) -> bool:
    """Check if a number is bleak (no number exists such that sum of number and its set bits equals n)."""
    for i in range(1, n):
        if i + count_set_bits(i) == n:
            return False
    return True


def count_set_bits(n: int) -> int:
    """Count set bits in an integer."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


if __name__ == "__main__":
    print(check_bleak_number(3))
    print(check_bleak_number(4))
    print(check_bleak_number(5))

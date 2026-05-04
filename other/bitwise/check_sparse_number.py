def check_sparse_number(n: int) -> bool:
    """Check if a given number is sparse (no two adjacent bits set)."""
    return (n & (n << 1)) == 0


if __name__ == "__main__":
    print(check_sparse_number(5))
    print(check_sparse_number(6))
    print(check_sparse_number(10))

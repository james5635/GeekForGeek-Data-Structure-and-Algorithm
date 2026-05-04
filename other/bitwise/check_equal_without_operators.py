def check_equal_without_operators(a: int, b: int) -> bool:
    """Check if two numbers are equal without using arithmetic and comparison operators."""
    return (a ^ b) == 0


if __name__ == "__main__":
    print(check_equal_without_operators(5, 5))
    print(check_equal_without_operators(5, 3))

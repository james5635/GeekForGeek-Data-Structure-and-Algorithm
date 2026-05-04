def linearity_expectation_basic() -> float:
    """Demonstrate linearity of expectation with dice example.

    Expected value of sum of two dice = E[die1] + E[die2] = 3.5 + 3.5 = 7
    """
    return 3.5 + 3.5


def expected_fixed_points(n: int) -> float:
    """Calculate expected number of fixed points in a random permutation of size n.

    By linearity of expectation, each position has 1/n probability of being a fixed point.
    E[X] = n * (1/n) = 1
    """
    return 1.0


def expected_heads(n: int) -> float:
    """Calculate expected number of heads in n fair coin tosses."""
    return n * 0.5


if __name__ == "__main__":
    print(f"Expected sum of two dice: {linearity_expectation_basic()}")
    print(f"Expected fixed points (permutation of 5): {expected_fixed_points(5)}")
    print(f"Expected fixed points (permutation of 100): {expected_fixed_points(100)}")
    print(f"Expected heads in 10 tosses: {expected_heads(10)}")

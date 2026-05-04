def expected_value(arr: list[float]) -> float:
    """Calculate the expected value (mean) of an array assuming uniform probability."""
    if not arr:
        raise ValueError("Array cannot be empty")
    return sum(arr) / len(arr)


def expected_value_with_probabilities(
    values: list[float], probabilities: list[float]
) -> float:
    """Calculate expected value given values and their corresponding probabilities."""
    if len(values) != len(probabilities):
        raise ValueError("Values and probabilities must have same length")
    if abs(sum(probabilities) - 1.0) > 1e-9:
        raise ValueError("Probabilities must sum to 1")
    return sum(v * p for v, p in zip(values, probabilities))


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(f"Expected value (uniform): {expected_value(arr)}")

    values = [1, 2, 3]
    probs = [0.1, 0.3, 0.6]
    print(
        f"Expected value (weighted): {expected_value_with_probabilities(values, probs)}"
    )

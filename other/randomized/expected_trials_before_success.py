def expected_trials_before_success(p: float) -> float:
    """Calculate expected number of trials before first success with probability p (geometric distribution)."""
    if p <= 0 or p > 1:
        raise ValueError("Probability must be in (0, 1]")
    return 1 / p


def expected_trials_at_least_n(p: float, n: int) -> float:
    """Calculate expected number of trials until success with probability of success p."""
    return expected_trials_before_success(p)


if __name__ == "__main__":
    probs = [0.5, 1 / 6, 1 / 52, 0.1, 0.9]
    for p in probs:
        exp = expected_trials_before_success(p)
        print(f"P={p:.4f}: Expected trials = {exp:.4f}")

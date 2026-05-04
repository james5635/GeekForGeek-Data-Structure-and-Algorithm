import random


def estimate_pi_monte_carlo(num_samples: int = 1000000) -> float:
    """Estimate Pi using Monte Carlo method by sampling random points in a unit square."""
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_samples


if __name__ == "__main__":
    import math

    for n in [1000, 10000, 100000, 1000000]:
        pi_est = estimate_pi_monte_carlo(n)
        print(f"Samples={n:>7}: Pi ≈ {pi_est:.6f} (error: {abs(pi_est - math.pi):.6f})")

import random


class RandomNumberDistribution:
    """Generate random numbers in an arbitrary probability distribution."""

    def __init__(self, values: list[int], probabilities: list[float]):
        if len(values) != len(probabilities):
            raise ValueError("Values and probabilities must have same length")
        if abs(sum(probabilities) - 1.0) > 1e-9:
            raise ValueError("Probabilities must sum to 1")

        self.values = values
        self.cumulative = []
        total = 0.0
        for p in probabilities:
            total += p
            self.cumulative.append(total)

    def generate(self) -> int:
        """Generate a random number according to the defined distribution."""
        r = random.random()
        for i, c in enumerate(self.cumulative):
            if r <= c:
                return self.values[i]
        return self.values[-1]


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    probs = [0.1, 0.2, 0.3, 0.25, 0.15]
    dist = RandomNumberDistribution(values, probs)

    results = [dist.generate() for _ in range(10000)]
    counts = {v: results.count(v) for v in values}
    print("Distribution results:")
    for v in values:
        print(
            f"  {v}: {counts[v]:4d} ({counts[v] / len(results) * 100:.2f}%) (target: {probs[v - 1] * 100:.1f}%)"
        )

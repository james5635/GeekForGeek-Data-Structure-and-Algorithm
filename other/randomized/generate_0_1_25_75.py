import random


def generate_0_1_25_75() -> int:
    """Generate 0 with 25% probability and 1 with 75% probability using two random bits."""
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    return a | b


if __name__ == "__main__":
    results = [generate_0_1_25_75() for _ in range(20)]
    print(results)
    print(f"0s: {results.count(0)}, 1s: {results.count(1)}")

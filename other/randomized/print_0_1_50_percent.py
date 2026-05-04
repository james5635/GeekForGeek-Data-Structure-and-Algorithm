import random


def print_0_1_50_percent() -> int:
    """Print 0 or 1 with 50% probability each."""
    return random.randint(0, 1)


if __name__ == "__main__":
    results = [print_0_1_50_percent() for _ in range(20)]
    print(results)
    print(f"0s: {results.count(0)}, 1s: {results.count(1)}")

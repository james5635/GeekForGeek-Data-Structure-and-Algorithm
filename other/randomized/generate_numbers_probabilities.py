import random


def generate_numbers_probabilities(
    probabilities: list[float], count: int = 3
) -> list[int]:
    """Generate numbers according to given probabilities using cumulative distribution."""
    cumulative = []
    total = 0
    for p in probabilities:
        total += p
        cumulative.append(total)

    result = []
    for _ in range(count):
        r = random.random()
        for i, c in enumerate(cumulative):
            if r <= c:
                result.append(i)
                break
    return result


if __name__ == "__main__":
    probs = [0.5, 0.3, 0.2]
    print(generate_numbers_probabilities(probs, 10))

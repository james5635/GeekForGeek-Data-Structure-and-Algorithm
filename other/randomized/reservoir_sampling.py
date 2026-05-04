import random


def reservoir_sampling(stream: list, k: int) -> list:
    """Select k random items from a stream using reservoir sampling algorithm."""
    if k > len(stream):
        raise ValueError("k cannot be larger than stream length")

    reservoir = stream[:k]
    for i in range(k, len(stream)):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    return reservoir


if __name__ == "__main__":
    stream = list(range(100))
    k = 5
    print(f"Stream size: {len(stream)}, Sample size: {k}")
    for _ in range(5):
        sample = reservoir_sampling(stream, k)
        print(f"  Sample: {sample}")

import math


def birthday_paradox_probability(n: int) -> float:
    """Calculate the probability that at least two people share a birthday in a group of n."""
    if n > 365:
        return 1.0
    prob_unique = 1.0
    for i in range(n):
        prob_unique *= (365 - i) / 365
    return 1 - prob_unique


def min_people_for_probability(p: float) -> int:
    """Find minimum number of people needed for collision probability >= p."""
    n = 1
    prob_unique = 1.0
    while True:
        prob_unique *= (365 - (n - 1)) / 365
        if 1 - prob_unique >= p:
            return n
        n += 1


if __name__ == "__main__":
    for n in [5, 10, 23, 30, 50, 70]:
        prob = birthday_paradox_probability(n)
        print(f"n={n}: P(collision)={prob:.4f}")
    print(f"\nPeople needed for 50%: {min_people_for_probability(0.5)}")
    print(f"People needed for 99%: {min_people_for_probability(0.99)}")

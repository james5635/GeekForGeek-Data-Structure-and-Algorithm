import random


def shuffle_deck_cards(deck: list) -> list:
    """Shuffle a deck of cards using Fisher-Yates algorithm."""
    shuffled = deck[:]
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled


if __name__ == "__main__":
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = [f"{r} of {s}" for s in suits for r in ranks]
    print(f"Original deck size: {len(deck)}")
    shuffled = shuffle_deck_cards(deck)
    print(f"First 5 cards: {shuffled[:5]}")

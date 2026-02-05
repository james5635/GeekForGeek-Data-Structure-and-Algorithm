"""
Pangram Checking

Problem: Check if a given sentence is a pangram.
A pangram is a sentence containing every letter of the alphabet at least once.

Examples:
- Input: "The quick brown fox jumps over the lazy dog"
  Output: True (contains all 26 letters)
- Input: "Hello World"
  Output: False

Time Complexity: O(n) where n is length of string
Space Complexity: O(1) - fixed size set of 26 letters
"""


def is_pangram(sentence: str) -> bool:
    """
    Check if the sentence is a pangram.

    Args:
        sentence: Input sentence to check

    Returns:
        True if sentence contains all 26 letters, False otherwise
    """
    # Create a set to store unique letters
    letters = set()

    for char in sentence.lower():
        if char.isalpha():
            letters.add(char)

    return len(letters) == 26


def is_pangram_set(sentence: str) -> bool:
    """
    Alternative implementation using set comprehension.

    Args:
        sentence: Input sentence

    Returns:
        True if pangram, False otherwise
    """
    return len({char.lower() for char in sentence if char.isalpha()}) == 26


def is_pangram_alphabet(sentence: str) -> bool:
    """
    Check by verifying each alphabet letter is present.

    Args:
        sentence: Input sentence

    Returns:
        True if pangram, False otherwise
    """
    sentence = sentence.lower()
    return all(chr(ord("a") + i) in sentence for i in range(26))


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("The quick brown fox jumps over the lazy dog", True),
        ("Hello World", False),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("", False),
        ("Pack my box with five dozen liquor jugs", True),
        ("The five boxing wizards jump quickly", True),
        ("abc", False),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
    ]

    print("=" * 70)
    print("Pangram Checking - Test Results")
    print("=" * 70)

    for sentence, expected in test_cases:
        result = is_pangram(sentence)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{sentence[:40]}{'...' if len(sentence) > 40 else ''}'")
        print(f"Expected: {expected} | Got: {result} | {status}")
        print("-" * 70)

    print("=" * 70)

    # Compare all implementations
    print("\nComparing all implementations:")
    for sentence, expected in test_cases[:5]:
        r1 = is_pangram(sentence)
        r2 = is_pangram_set(sentence)
        r3 = is_pangram_alphabet(sentence)
        all_match = r1 == r2 == r3 == expected
        status = "PASS" if all_match else "FAIL"
        print(f"Input: '{sentence[:30]}...' | All Match: {status}")

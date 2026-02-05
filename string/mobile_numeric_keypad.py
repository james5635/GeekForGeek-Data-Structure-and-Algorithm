"""
Convert Sentence to Mobile Numeric Keypad Sequence

Given a sentence, convert it into its equivalent mobile numeric keypad sequence.

Approach: Dictionary Mapping - O(n) Time and O(1) Space
Map each character to its keypad sequence.
"""


def convert_to_keypad(s):
    """
    Convert sentence to mobile numeric keypad sequence.

    Args:
        s: Input sentence

    Returns:
        Keypad sequence string
    """
    # Keypad mapping
    keypad = {
        "A": "2",
        "B": "22",
        "C": "222",
        "D": "3",
        "E": "33",
        "F": "333",
        "G": "4",
        "H": "44",
        "I": "444",
        "J": "5",
        "K": "55",
        "L": "555",
        "M": "6",
        "N": "66",
        "O": "666",
        "P": "7",
        "Q": "77",
        "R": "777",
        "S": "7777",
        "T": "8",
        "U": "88",
        "V": "888",
        "W": "9",
        "X": "99",
        "Y": "999",
        "Z": "9999",
        " ": "0",
    }

    result = []
    for char in s.upper():
        if char in keypad:
            result.append(keypad[char])

    return "".join(result)


def main():
    """Test cases for mobile numeric keypad conversion."""
    test_cases = [
        ("GEEKSFORGEEKS", "4333355777733366677743333557777"),
        ("HELLO", "4433555555666"),
        ("ABC", "222222"),  # A=2, B=22, C=222 -> 2+22+222 = 6 characters
        ("HELLO WORLD", "4433555555666096667775553"),  # space = 0
    ]

    print("=" * 50)
    print("Mobile Numeric Keypad Sequence")
    print("=" * 50)

    for s, expected in test_cases:
        result = convert_to_keypad(s)
        status = "✓" if result == expected else "✗"
        print(f"\nInput: '{s}'")
        print(f"Output: {result}")
        print(f"Expected: {expected} {status}")


if __name__ == "__main__":
    main()

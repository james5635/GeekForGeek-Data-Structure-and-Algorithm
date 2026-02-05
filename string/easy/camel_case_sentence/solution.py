"""
Camel Case Sentence

Problem: Given a sentence, convert it to camel case.
Camel case combines words by capitalizing all words (except the first one)
and removing spaces.

Examples:
- Input: "i love programming", Output: "iLoveProgramming"
- Input: "hello world", Output: "helloWorld"

Time Complexity: O(n) where n is length of string
Space Complexity: O(n) for the result string
"""


def to_camel_case(sentence: str) -> str:
    """
    Convert a sentence to camel case.

    Args:
        sentence: Input sentence with words separated by spaces

    Returns:
        Camel case version of the sentence
    """
    words = sentence.split()
    if not words:
        return ""

    # First word in lowercase
    result = words[0].lower()

    # Capitalize first letter of remaining words
    for word in words[1:]:
        if word:
            result += word[0].upper() + word[1:].lower()

    return result


def to_camel_case_alternative(sentence: str) -> str:
    """
    Alternative implementation using title() and concatenation.

    Args:
        sentence: Input sentence

    Returns:
        Camel case version of the sentence
    """
    words = sentence.split()
    if not words:
        return ""

    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("i love programming", "iLoveProgramming"),
        ("hello world", "helloWorld"),
        ("this is a test", "thisIsATest"),
        ("python", "python"),
        ("", ""),
        ("HELLO WORLD", "helloWorld"),
        ("camel case example", "camelCaseExample"),
        ("one", "one"),
    ]

    print("=" * 60)
    print("Camel Case Sentence - Test Results")
    print("=" * 60)

    for sentence, expected in test_cases:
        result = to_camel_case(sentence)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{sentence}'")
        print(f"Expected: '{expected}' | Got: '{result}' | {status}")
        print("-" * 60)

    print("=" * 60)

    # Test alternative implementation
    print("\nTesting alternative implementation:")
    for sentence, expected in test_cases[:4]:
        result = to_camel_case_alternative(sentence)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Input: '{sentence}' | Expected: '{expected}' | Got: '{result}' | {status}"
        )

"""
Camel Case of a Given Sentence
Convert a sentence to camelCase where the first word is lowercase and
each subsequent word starts with uppercase.

Time Complexity: O(n), where n is the length of the sentence
Auxiliary Space: O(n), to store the result
"""


def convert_to_camel_case(s: str) -> str:
    """
    Convert a sentence to camelCase.

    Args:
        s: Input sentence with lowercase words separated by spaces

    Returns:
        Camel case version of the sentence
    """
    result = []
    capitalize_next = False

    for char in s:
        if char == " ":
            capitalize_next = True
        elif capitalize_next:
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)

    return "".join(result)


def main():
    """Test the camel case converter with various inputs."""
    test_cases = [
        ("i got intern at geeksforgeeks", "iGotInternAtGeeksforgeeks"),
        ("here comes the garden", "hereComesTheGarden"),
        ("hello world", "helloWorld"),
        ("a b c d", "aBCD"),
        ("single", "single"),
        ("", ""),
    ]

    print("Camel Case Converter")
    print("=" * 60)

    for input_str, expected in test_cases:
        result = convert_to_camel_case(input_str)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} | Input: '{input_str}'")
        print(f"       | Expected: '{expected}'")
        print(f"       | Got:      '{result}'")
        print()


if __name__ == "__main__":
    main()

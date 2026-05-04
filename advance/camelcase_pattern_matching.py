"""
CamelCase Pattern Matching

Given a list of words where each word follows CamelCase notation, print all
words in the list that match the given pattern, where the pattern consists
of uppercase characters only.

A word matches the pattern if all characters of the pattern appear sequentially
in the word's uppercase letters.

Time Complexity: O(n * len) where n is size of array and len is max word length
Space Complexity: O(1)
"""


def camel_case(arr, pat):
    """
    Find all words that match the CamelCase pattern.

    Args:
        arr: List of CamelCase words
        pat: Pattern consisting of uppercase characters

    Returns:
        List of words matching the pattern
    """
    res = []
    for word in arr:
        i, j = 0, 0
        while i < len(word) and j < len(pat):
            if word[i].islower():
                i += 1
            elif word[i] != pat[j]:
                break
            else:
                i += 1
                j += 1

        if j == len(pat):
            res.append(word)

    return res


if __name__ == "__main__":
    arr1 = ["WelcomeGeek", "WelcomeToGeeksForGeeks", "GeeksForGeeks", "WayToGo"]
    pat1 = "WTG"
    result1 = camel_case(arr1, pat1)
    print(f"Words: {arr1}")
    print(f"Pattern: '{pat1}'")
    print(f"Matched: {result1}")
    print()

    arr2 = [
        "Hi",
        "Hello",
        "HelloWorld",
        "HiTech",
        "HiGeek",
        "HiTechWorld",
        "HiTechCity",
        "HiTechLab",
    ]
    pat2 = "HA"
    result2 = camel_case(arr2, pat2)
    print(f"Words: {arr2}")
    print(f"Pattern: '{pat2}'")
    print(f"Matched: {result2}")
    print()

    arr3 = ["HelloWorld", "HiWorld", "HelloYou", "HeyWorld"]
    pat3 = "HW"
    result3 = camel_case(arr3, pat3)
    print(f"Words: {arr3}")
    print(f"Pattern: '{pat3}'")
    print(f"Matched: {result3}")

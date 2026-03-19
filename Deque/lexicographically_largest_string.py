"""
Lexicographically Largest String after K removals
Use greedy stack-based approach to maximize the resulting string
"""

from collections import deque


def lexicographically_largest_string(s, k):
    """
    Find lexicographically largest string by removing exactly k characters

    Approach:
    - Use a greedy stack approach
    - For each character, try to remove smaller characters before it
    - If we still have removals left and current char > stack top, pop and continue
    - Finally, if removals remain, remove from end

    Time: O(n), Space: O(n)
    """
    if not s or k <= 0:
        return s

    n = len(s)
    if k >= n:
        return ""

    stack = []
    removals = k

    for char in s:
        while removals > 0 and stack and stack[-1] < char:
            stack.pop()
            removals -= 1
        stack.append(char)

    while removals > 0 and stack:
        stack.pop()
        removals -= 1

    return "".join(stack)


def main():
    print("=" * 60)
    print("Lexicographically Largest String after K Removals")
    print("=" * 60)

    print("\n--- Test Case 1 ---")
    s = "zebra"
    k = 3
    result = lexicographically_largest_string(s, k)
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')
    print(f'Expected: "zr"')
    print(f"Pass: {result == 'zr'}")

    print("\n--- Test Case 2 ---")
    s = "ritz"
    k = 2
    result = lexicographically_largest_string(s, k)
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')
    print(f'Expected: "tz"')
    print(f"Pass: {result == 'tz'}")

    print("\n--- Test Case 3 ---")
    s = "abcabc"
    k = 3
    result = lexicographically_largest_string(s, k)
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')
    print(f'Expected: "cc"')
    print(f"Pass: {result == 'cc'}")

    print("\n--- Test Case 4 ---")
    s = "cbacdcbc"
    k = 2
    result = lexicographically_largest_string(s, k)
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')

    print("\n--- Test Case 5 ---")
    s = "aaaaa"
    k = 2
    result = lexicographically_largest_string(s, k)
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')
    print(f'Expected: "aaa"')
    print(f"Pass: {result == 'aaa'}")

    print("\n--- Test Case 6 ---")
    s = "geeksforgeeks"
    k = 5
    result = lexicographically_largest_string(s, k)
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')

    print("\n--- Test Case 7 ---")
    s = "abcd"
    k = 0
    result = lexicographically_largest_string(s, k)
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')
    print(f'Expected: "abcd"')
    print(f"Pass: {result == 'abcd'}")

    print("\n--- Test Case 8 ---")
    s = "a"
    k = 1
    result = lexicographically_largest_string(s, k)
    print(f'Input: s = "{s}", k = {k}')
    print(f'Output: "{result}"')
    print(f'Expected: ""')
    print(f"Pass: {result == ''}")


if __name__ == "__main__":
    main()

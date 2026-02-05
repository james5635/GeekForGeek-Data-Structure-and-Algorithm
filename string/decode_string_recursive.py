"""
Decode a String Encoded with Recursive Substring Counts

Given an encoded string where the encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated
exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; no extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any
digits and that digits are only for those repeat numbers, k.

Examples:
- s = "3[a]2[bc]" -> Output: "aaabcbc"
- s = "3[a2[c]]" -> Output: "accaccacc"
- s = "2[abc]3[cd]ef" -> Output: "abcabccdcdcdef"

Time Complexity: O(n * max(k)) where n is length of decoded string
Space Complexity: O(n) for recursion stack
"""


def decodeString(s):
    """
    Decode string using recursion
    """

    def decode(index):
        result = []
        num = 0

        while index[0] < len(s):
            char = s[index[0]]

            if char.isdigit():
                num = num * 10 + int(char)
                index[0] += 1
            elif char == "[":
                index[0] += 1
                # Recursively decode the substring
                substring = decode(index)
                result.append(substring * num)
                num = 0
            elif char == "]":
                index[0] += 1
                return "".join(result)
            else:
                result.append(char)
                index[0] += 1

        return "".join(result)

    return decode([0])


def decodeStringStack(s):
    """
    Decode string using stack (iterative approach)
    """
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            # Push current state to stack
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == "]":
            # Pop from stack and decode
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char

    return current_string


def decodeStringMultipleDigits(s):
    """
    Handle multiple digit numbers properly
    """
    stack = []
    current = ""
    num = 0

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stack.append((current, num))
            current = ""
            num = 0
        elif c == "]":
            prev, k = stack.pop()
            current = prev + current * k
        else:
            current += c

    return current


def decodeNested(s):
    """
    Handle deeply nested structures
    """

    def helper(i):
        res = ""
        num = 0

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "[":
                i, substring = helper(i + 1)
                res += substring * num
                num = 0
            elif s[i] == "]":
                return i, res
            else:
                res += s[i]
            i += 1

        return res

    return helper(0)


# Test the functions
if __name__ == "__main__":
    test_cases = [
        "3[a]2[bc]",
        "3[a2[c]]",
        "2[abc]3[cd]ef",
        "100[leetcode]",
        "3[z]2[2[y]pq4[2[jk]e1[f]]]",
        "2[3[a]b]",
    ]

    print("Decode String with Recursive Substring Counts")
    print("=" * 50)

    for s in test_cases:
        print(f"Encoded:  '{s}'")

        # Recursive solution
        decoded_rec = decodeString(s)
        print(
            f"Decoded (recursive): '{decoded_rec[:50]}...'"
            if len(decoded_rec) > 50
            else f"Decoded (recursive): '{decoded_rec}'"
        )

        # Stack solution
        decoded_stack = decodeStringStack(s)
        print(
            f"Decoded (stack):     '{decoded_stack[:50]}...'"
            if len(decoded_stack) > 50
            else f"Decoded (stack):     '{decoded_stack}'"
        )

        print()

    print("Pattern explanation:")
    print("- k[string]: repeat 'string' k times")
    print("- Nested brackets are evaluated from inside out")
    print("- Example: 3[a2[c]] = 3[acc] = accaccacc")

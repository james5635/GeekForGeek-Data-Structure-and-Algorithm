def find_closing_bracket(expr, open_index):
    brackets = {"(": ")", "[": "]", "{": "}"}
    if expr[open_index] not in brackets:
        return -1
    stack = []
    for i in range(open_index, len(expr)):
        ch = expr[i]
        if ch in brackets:
            stack.append(ch)
        elif ch in brackets.values():
            if stack and brackets[stack[-1]] == ch:
                stack.pop()
                if not stack:
                    return i
            else:
                return -1
    return -1


if __name__ == "__main__":
    expr = "[a+b*(c+d)+{e+f}]"
    idx = expr.index("[")
    print(f"Expression: {expr}")
    print(
        f"Opening '[' at index {idx}, closing ']' at index {find_closing_bracket(expr, idx)}"
    )

    idx = expr.index("(")
    print(
        f"Opening '(' at index {idx}, closing ')' at index {find_closing_bracket(expr, idx)}"
    )

    idx = expr.index("{")
    print(
        f"Opening '{{' at index {idx}, closing '}}' at index {find_closing_bracket(expr, idx)}"
    )

    expr2 = "((a+b))"
    idx = expr2.index("(")
    print(f"\nExpression: {expr2}")
    print(
        f"Opening '(' at index {idx}, closing ')' at index {find_closing_bracket(expr2, idx)}"
    )

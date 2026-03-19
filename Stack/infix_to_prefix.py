def precedence(op):
    if op == "+" or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2
    if op == "^":
        return 3
    return 0


def is_operand(ch):
    return ch.isalnum()


def infix_to_prefix(expression):
    reversed_expr = expression[::-1]
    swapped = []
    for ch in reversed_expr:
        if ch == "(":
            swapped.append(")")
        elif ch == ")":
            swapped.append("(")
        else:
            swapped.append(ch)
    swapped = "".join(swapped)

    stack = []
    result = []

    for ch in swapped:
        if is_operand(ch):
            result.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
        else:
            if ch == "^":
                while stack and precedence(stack[-1]) > precedence(ch):
                    result.append(stack.pop())
            else:
                while stack and precedence(stack[-1]) >= precedence(ch):
                    result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return "".join(result[::-1])


if __name__ == "__main__":
    tests = [
        "(A-B/C)*(A/K-L)",
        "a+b*(c^d-e)^(f+g*h)-i",
        "a+b*c",
    ]
    for expr in tests:
        print(f"Infix: {expr}")
        print(f"Prefix: {infix_to_prefix(expr)}")
        print()

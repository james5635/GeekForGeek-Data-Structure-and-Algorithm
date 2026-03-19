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


def infix_to_postfix(expression):
    stack = []
    result = []

    for ch in expression:
        if is_operand(ch):
            result.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return "".join(result)


if __name__ == "__main__":
    tests = [
        "a+b*(c^d-e)^(f+g*h)-i",
        "A*(B+C)/D",
        "a+b*c",
    ]
    for expr in tests:
        print(f"Infix: {expr}")
        print(f"Postfix: {infix_to_postfix(expr)}")
        print()

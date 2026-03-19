def is_operator(ch):
    return ch in {"+", "-", "*", "/", "^"}


def postfix_to_prefix(expression):
    stack = []
    for ch in expression:
        if ch.isalnum():
            stack.append(ch)
        elif is_operator(ch):
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(ch + op1 + op2)
    return stack.pop()


if __name__ == "__main__":
    tests = [
        "AB+CD-*",
        "ABC/-AK/L-*",
        "abc^de-fgh*+^*+i-",
    ]
    for expr in tests:
        print(f"Postfix: {expr}")
        print(f"Prefix: {postfix_to_prefix(expr)}")
        print()

def is_operator(ch):
    return ch in {"+", "-", "*", "/", "^"}


def prefix_to_infix(expression):
    stack = []
    for ch in reversed(expression):
        if ch.isalnum():
            stack.append(ch)
        elif is_operator(ch):
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"({op1}{ch}{op2})")
    return stack.pop()


if __name__ == "__main__":
    tests = [
        "*+AB-CD",
        "*-A/BC-/AKL",
        "+a*b^-^cde+f*ghi",
    ]
    for expr in tests:
        print(f"Prefix: {expr}")
        print(f"Infix: {prefix_to_infix(expr)}")
        print()

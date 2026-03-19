def evaluate_postfix(expression):
    stack = []
    for ch in expression.split():
        if ch.lstrip("-").isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == "+":
                stack.append(a + b)
            elif ch == "-":
                stack.append(a - b)
            elif ch == "*":
                stack.append(a * b)
            elif ch == "/":
                stack.append(a // b)
            elif ch == "^":
                stack.append(a**b)
    return stack.pop()


if __name__ == "__main__":
    tests = [
        "2 3 1 * + 9 -",
        "10 2 8 * + 3 -",
        "5 3 + 8 2 - *",
        "4 2 + 3 5 1 - * +",
    ]
    for expr in tests:
        print(f"Postfix: {expr}")
        print(f"Result: {evaluate_postfix(expr)}")
        print()

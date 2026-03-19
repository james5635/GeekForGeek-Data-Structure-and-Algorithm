def has_redundant_brackets(expression):
    stack = []
    for ch in expression:
        if ch == ")":
            top = stack.pop()
            has_operator = False
            while top != "(":
                if top in {"+", "-", "*", "/"}:
                    has_operator = True
                top = stack.pop()
            if not has_operator:
                return True
        else:
            stack.append(ch)
    return False


if __name__ == "__main__":
    tests = [
        "((a+b))",
        "(a+(b)/c)",
        "(a+b*(c-d))",
        "((a+b)*(c+d))",
        "(a)",
    ]
    for expr in tests:
        result = "Yes" if has_redundant_brackets(expr) else "No"
        print(f'"{expr}" -> Redundant: {result}')

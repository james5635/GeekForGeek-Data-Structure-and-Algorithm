def remove_brackets(expression):
    result = []
    for ch in expression:
        if ch not in "()[]{}":
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    tests = [
        "a+(b*c)",
        "(a-b)*(c+d)",
        "((a+b)*(c-d))",
        "gfg+(a-b)",
        "((a-b+c))",
    ]
    for expr in tests:
        print(f'"{expr}" -> "{remove_brackets(expr)}"')

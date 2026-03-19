def is_balanced(expression):
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}

    for ch in expression:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    tests = [
        "{()}[]",
        "([)]",
        "((()))",
        "{[()]}",
        "((())",
        "",
    ]
    for expr in tests:
        result = "Balanced" if is_balanced(expr) else "Not Balanced"
        print(f'"{expr}" -> {result}')

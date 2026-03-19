def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)


def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5]
    print("Original:", s)
    reverse_stack(s)
    print("Reversed:", s)

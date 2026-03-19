def delete_middle(stack, current, mid):
    if not stack or current == mid:
        stack.pop()
        return
    top = stack.pop()
    delete_middle(stack, current + 1, mid)
    stack.append(top)


def delete_mid(stack):
    if not stack:
        return
    mid = len(stack) // 2
    delete_middle(stack, 0, mid)


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5]
    print("Original:", s)
    delete_mid(s)
    print("After deleting middle:", s)

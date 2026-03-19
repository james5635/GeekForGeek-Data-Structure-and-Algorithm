def reverse_stack(stack):
    temp = []
    while stack:
        temp.append(stack.pop())
    while temp:
        stack.append(temp.pop())


if __name__ == "__main__":
    s = [1, 2, 3, 4, 5]
    print("Original:", s)
    reverse_stack(s)
    print("Reversed:", s)

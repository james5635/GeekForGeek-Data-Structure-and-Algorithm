def sort_stack(stack):
    temp = []
    while stack:
        val = stack.pop()
        while temp and temp[-1] > val:
            stack.append(temp.pop())
        temp.append(val)
    while temp:
        stack.append(temp.pop())


if __name__ == "__main__":
    s = [34, 3, 31, 98, 92, 23]
    print("Original:", s)
    sort_stack(s)
    print("Sorted:", s)

def check_stack_sortable(arr):
    stack = []
    expected = 1

    for num in arr:
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1

        if num == expected:
            expected += 1
        else:
            stack.append(num)

    while stack and stack[-1] == expected:
        stack.pop()
        expected += 1

    return not stack


if __name__ == "__main__":
    a1 = [4, 1, 2, 3]
    print(f"Array {a1}: {check_stack_sortable(a1)}")

    a2 = [4, 3, 1, 2]
    print(f"Array {a2}: {check_stack_sortable(a2)}")

    a3 = [3, 2, 1, 4]
    print(f"Array {a3}: {check_stack_sortable(a3)}")

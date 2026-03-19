def largest_after_k_removals(s, k):
    stack = []
    for ch in s:
        while k > 0 and stack and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    while k > 0:
        stack.pop()
        k -= 1
    return "".join(stack)


if __name__ == "__main__":
    assert largest_after_k_removals("zebra", 3) == "zr"
    assert largest_after_k_removals("abcdef", 3) == "def"
    assert largest_after_k_removals("aaa", 2) == "a"
    assert largest_after_k_removals("abc", 0) == "abc"
    assert largest_after_k_removals("cbaz", 1) == "cbz"
    print("All tests passed!")

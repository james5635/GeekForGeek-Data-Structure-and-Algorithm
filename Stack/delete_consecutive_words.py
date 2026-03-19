def delete_consecutive_words(s):
    words = s.split()
    stack = []
    for word in words:
        if stack and stack[-1] == word:
            continue
        stack.append(word)
    return " ".join(stack)


if __name__ == "__main__":
    print(delete_consecutive_words("aaa bbb bbb aaa aaa ccc"))
    print(delete_consecutive_words("hello hello world"))
    print(delete_consecutive_words("one two two three three three"))
    print(delete_consecutive_words("abc"))
    print(delete_consecutive_words("a a a b b c c"))

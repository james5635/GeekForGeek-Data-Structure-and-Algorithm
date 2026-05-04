def word_break_backtracking(s: str, word_dict: list[str]) -> list[str]:
    """Word Break problem using backtracking - find all possible sentences."""
    word_set = set(word_dict)
    result: list[str] = []

    def backtrack(idx: int, words: list[str]) -> None:
        if idx == len(s):
            result.append(" ".join(words))
            return
        for i in range(idx + 1, len(s) + 1):
            word = s[idx:i]
            if word in word_set:
                words.append(word)
                backtrack(i, words)
                words.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    sentences = word_break_backtracking(s, word_dict)
    for sentence in sentences:
        print(sentence)

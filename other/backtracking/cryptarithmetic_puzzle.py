def solve_cryptarithmetic(puzzle: str) -> dict[str, int] | None:
    """Solve cryptarithmetic puzzle like 'SEND+MORE=MONEY'."""
    parts = puzzle.replace(" ", "").split("=")
    operands = parts[0].split("+")
    result = parts[1]
    words = operands + [result]
    letters = set()
    for w in words:
        letters.update(w)
    letters = sorted(letters)
    if len(letters) > 10:
        return None

    first_letters = {w[0] for w in words if len(w) > 1}

    def solve(
        assigned: dict[str, int], used: set[int], idx: int
    ) -> dict[str, int] | None:
        if idx == len(letters):

            def word_value(word: str) -> int:
                val = 0
                for c in word:
                    val = val * 10 + assigned[c]
                return val

            lhs = sum(word_value(w) for w in operands)
            rhs = word_value(result)
            return assigned.copy() if lhs == rhs else None
        letter = letters[idx]
        for d in range(10):
            if d in used:
                continue
            if d == 0 and letter in first_letters:
                continue
            assigned[letter] = d
            used.add(d)
            res = solve(assigned, used, idx + 1)
            if res:
                return res
            del assigned[letter]
            used.remove(d)
        return None

    return solve({}, set(), 0)


if __name__ == "__main__":
    puzzle = "SEND+MORE=MONEY"
    solution = solve_cryptarithmetic(puzzle)
    if solution:
        for letter, digit in solution.items():
            print(f"{letter}: {digit}")
    else:
        print("No solution found")

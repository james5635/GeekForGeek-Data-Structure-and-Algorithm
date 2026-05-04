def combinatorial_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Find all combinations of numbers that sum to target. Each number can be used multiple times."""
    candidates.sort()
    result: list[list[int]] = []

    def backtrack(start: int, current: list[int], remaining: int) -> None:
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    combinations = combinatorial_sum(candidates, target)
    for c in combinations:
        print(c)

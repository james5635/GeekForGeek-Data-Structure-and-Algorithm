def tug_of_war(arr: list[int]) -> tuple[list[int], list[int]]:
    """Solve Tug of War problem - divide into two sets with minimum difference."""
    n = len(arr)
    total_sum = sum(arr)
    best_diff = float("inf")
    best_set: list[int] = []
    current_set: list[int] = []

    def backtrack(idx: int, current_sum: int) -> None:
        nonlocal best_diff, best_set
        diff = abs((total_sum - current_sum) - current_sum)
        if diff < best_diff:
            best_diff = diff
            best_set = current_set[:]
        for i in range(idx, n):
            current_set.append(i)
            backtrack(i + 1, current_sum + arr[i])
            current_set.pop()

    backtrack(0, 0)
    set1 = [arr[i] for i in best_set]
    set2 = [arr[i] for i in range(n) if i not in best_set]
    return set1, set2


if __name__ == "__main__":
    arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
    set1, set2 = tug_of_war(arr)
    print(f"Set 1: {set1}, Sum: {sum(set1)}")
    print(f"Set 2: {set2}, Sum: {sum(set2)}")

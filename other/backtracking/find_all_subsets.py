def find_all_subsets(nums: list[int]) -> list[list[int]]:
    """Find all subsets of a given set using backtracking."""
    result: list[list[int]] = []

    def backtrack(start: int, current: list[int]) -> None:
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    subsets = find_all_subsets(nums)
    for s in subsets:
        print(s)

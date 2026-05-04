def find_distinct_subsets(nums: list[int]) -> list[list[int]]:
    """Find all distinct subsets of a given set (handles duplicates)."""
    nums.sort()
    result: list[list[int]] = []

    def backtrack(start: int, current: list[int]) -> None:
        result.append(current[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = [1, 2, 2]
    subsets = find_distinct_subsets(nums)
    for s in subsets:
        print(s)

def has_subset_sum(nums: list[int], target: int) -> bool:
    """Check if there exists a subset with the given sum."""

    def backtrack(idx: int, current: int) -> bool:
        if current == target:
            return True
        if current > target or idx >= len(nums):
            return False
        if backtrack(idx + 1, current + nums[idx]):
            return True
        return backtrack(idx + 1, current)

    return backtrack(0, 0)


if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    print(f"Subset with sum {target} exists: {has_subset_sum(nums, target)}")
    target = 30
    print(f"Subset with sum {target} exists: {has_subset_sum(nums, target)}")

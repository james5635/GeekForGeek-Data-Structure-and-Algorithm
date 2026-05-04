def partition_k_subsets(arr: list[int], k: int) -> list[list[int]] | None:
    """Partition a set into k subsets of equal sum."""
    total = sum(arr)
    if total % k != 0:
        return None
    target = total // k
    n = len(arr)
    subsets: list[list[int]] = [[] for _ in range(k)]
    arr.sort(reverse=True)

    def solve(idx: int) -> bool:
        if idx == n:
            return all(sum(s) == target for s in subsets)
        for i in range(k):
            if sum(subsets[i]) + arr[idx] <= target:
                subsets[i].append(arr[idx])
                if solve(idx + 1):
                    return True
                subsets[i].pop()
                if not subsets[i]:
                    break
        return False

    if solve(0):
        return subsets
    return None


if __name__ == "__main__":
    arr = [2, 12, 4, 8, 6]
    k = 3
    result = partition_k_subsets(arr, k)
    if result:
        for i, s in enumerate(result):
            print(f"Subset {i + 1}: {s}, Sum: {sum(s)}")
    else:
        print("No valid partition found")

from collections import deque


def find_permutation_with_k_differences(n, k):
    result = []
    available = list(range(1, n + 1))

    def backtrack(current):
        if len(current) == n:
            return list(current)

        last = current[-1] if current else None

        for val in available:
            if last is None or abs(val - last) <= k:
                current.append(val)
                available.remove(val)

                result_found = backtrack(current)
                if result_found:
                    return result_found

                current.pop()
                available.append(val)
                available.sort()

        return None

    return backtrack([])


def main():
    # Test Case 1: N=7, K=1 -> 1 2 3 4 5 6 7
    print("Test Case 1: N=7, K=1")
    result1 = find_permutation_with_k_differences(7, 1)
    print(f"Result: {' '.join(map(str, result1))}")
    print(f"Expected: 1 2 3 4 5 6 7")
    print()

    # Test Case 2: N=3, K=2 -> 1 3 2
    print("Test Case 2: N=3, K=2")
    result2 = find_permutation_with_k_differences(3, 2)
    print(f"Result: {' '.join(map(str, result2))}")
    print(f"Expected: 1 3 2")
    print("Note: 1 2 3 is also valid as all differences are <= 2")
    print()

    # Test Case 3: N=5, K=1 -> 1 2 3 4 5
    print("Test Case 3: N=5, K=1")
    result3 = find_permutation_with_k_differences(5, 1)
    print(f"Result: {' '.join(map(str, result3))}")
    print(f"Expected: 1 2 3 4 5")
    print()

    # Test Case 4: N=4, K=3
    print("Test Case 4: N=4, K=3")
    result4 = find_permutation_with_k_differences(4, 3)
    print(f"Result: {' '.join(map(str, result4))}")
    print()

    # Test Case 5: N=1, K=0
    print("Test Case 5: N=1, K=0")
    result5 = find_permutation_with_k_differences(1, 0)
    print(f"Result: {' '.join(map(str, result5))}")
    print(f"Expected: 1")
    print()

    # Test Case 6: N=6, K=2
    print("Test Case 6: N=6, K=2")
    result6 = find_permutation_with_k_differences(6, 2)
    print(f"Result: {' '.join(map(str, result6))}")


if __name__ == "__main__":
    main()

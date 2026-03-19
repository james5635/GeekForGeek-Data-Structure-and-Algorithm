from itertools import permutations


def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result = result + numbers[i + 1]
        elif op == "*":
            result = result * numbers[i + 1]
    return result


def min_number_by_operations_brute(A, S):
    n = len(A)

    all_results = []

    op_combinations = permutations(S, n - 1) if n > 1 else [[]]
    for op_tuple in op_combinations:
        ops = list(op_tuple)

        for perm in permutations(A):
            numbers = list(perm)
            result = evaluate_expression(numbers, ops)
            all_results.append((result, list(perm), ops))

    min_result = min(all_results, key=lambda x: x[0])
    return min_result[0]


def min_number_dfs(A, S):
    n = len(A)
    used = [False] * n
    result = [float("inf")]

    def dfs(current_val, idx, used_local):
        if idx == n:
            result[0] = min(result[0], current_val)
            return

        for i in range(n):
            if not used_local[i]:
                used_local[i] = True

                if idx == 0:
                    dfs(A[i], idx + 1, used_local)
                else:
                    for j, op in enumerate(S):
                        if op == "+":
                            dfs(current_val + A[i], idx + 1, used_local)
                        elif op == "*":
                            dfs(current_val * A[i], idx + 1, used_local)

                used_local[i] = False

    dfs(0, 0, used)
    return result[0]


def min_number_dp(A, S):
    n = len(A)
    min_val = [float("inf")]

    def helper(idx, current_val, used_mask):
        if idx == n:
            min_val[0] = min(min_val[0], current_val)
            return

        for i in range(n):
            if not (used_mask & (1 << i)):
                new_mask = used_mask | (1 << i)

                if idx == 0:
                    helper(idx + 1, A[i], new_mask)
                else:
                    for op in S:
                        if op == "+":
                            helper(idx + 1, current_val + A[i], new_mask)
                        elif op == "*":
                            helper(idx + 1, current_val * A[i], new_mask)

    helper(0, 0, 0)
    return min_val[0]


def main():
    # Test Case 1: A=[2,2,2,2], S="**+" -> 8
    print("Test Case 1: A=[2,2,2,2], S='**+'")
    arr1 = [2, 2, 2, 2]
    ops1 = "+*"
    result1 = min_number_dp(arr1, ops1)
    print(f"Minimum number: {result1}")
    print(f"Expected: 8")
    print()

    # Test Case 2: A=[1,2], S="+"
    print("Test Case 2: A=[1,2], S='+'")
    arr2 = [1, 2]
    ops2 = "+"
    result2 = min_number_dp(arr2, ops2)
    print(f"Minimum number: {result2}")
    print(f"Expected: 3")
    print()

    # Test Case 3: A=[1,2], S="*"
    print("Test Case 3: A=[1,2], S='*'")
    arr3 = [1, 2]
    ops3 = "*"
    result3 = min_number_dp(arr3, ops3)
    print(f"Minimum number: {result3}")
    print(f"Expected: 2")
    print()

    # Test Case 4: A=[3,4,5], S="+*"
    print("Test Case 4: A=[3,4,5], S='+*'")
    arr4 = [3, 4, 5]
    ops4 = "+*"
    result4 = min_number_dp(arr4, ops4)
    print(f"Minimum number: {result4}")
    print()

    # Test Case 5: A=[5,1,2], S="+*"
    print("Test Case 5: A=[5,1,2], S='+*'")
    arr5 = [5, 1, 2]
    ops5 = "+*"
    result5 = min_number_dp(arr5, ops5)
    print(f"Minimum number: {result5}")
    print()

    # Test Case 6: A=[1,2,3,4], S="++*"
    print("Test Case 6: A=[1,2,3,4], S='++*'")
    arr6 = [1, 2, 3, 4]
    ops6 = "+*"
    result6 = min_number_dp(arr6, ops6)
    print(f"Minimum number: {result6}")
    print()

    # Test Case 7: Single element
    print("Test Case 7: A=[7], S=''")
    arr7 = [7]
    ops7 = ""
    result7 = min_number_dp(arr7, ops7)
    print(f"Minimum number: {result7}")
    print(f"Expected: 7")


if __name__ == "__main__":
    main()

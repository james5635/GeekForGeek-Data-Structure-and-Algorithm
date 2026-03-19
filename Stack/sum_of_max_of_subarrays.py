def sum_of_max_of_subarrays(arr):
    n = len(arr)

    next_greater = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            next_greater[i] = stack[-1]
        stack.append(i)

    prev_greater = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        if stack:
            prev_greater[i] = stack[-1]
        stack.append(i)

    total = 0
    for i in range(n):
        left_count = i - prev_greater[i]
        right_count = next_greater[i] - i
        total += arr[i] * left_count * right_count
    return total


if __name__ == "__main__":
    arr1 = [1, 3, 2]
    print("Array:", arr1)
    print("Sum of max of subarrays:", sum_of_max_of_subarrays(arr1))

    arr2 = [3, 1, 2, 4]
    print("\nArray:", arr2)
    print("Sum of max of subarrays:", sum_of_max_of_subarrays(arr2))

    arr3 = [1, 2, 3, 4]
    print("\nArray:", arr3)
    print("Sum of max of subarrays:", sum_of_max_of_subarrays(arr3))

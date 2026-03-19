def max_diff_nearest_left_right_smaller(arr):
    n = len(arr)

    left_smaller = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left_smaller[i] = arr[stack[-1]]
        stack.append(i)

    right_smaller = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right_smaller[i] = arr[stack[-1]]
        stack.append(i)

    max_diff = 0
    for i in range(n):
        diff = abs(left_smaller[i] - right_smaller[i])
        max_diff = max(max_diff, diff)
    return max_diff


if __name__ == "__main__":
    arr1 = [2, 4, 8, 7, 7, 9, 3]
    print("Array:", arr1)
    print("Max difference:", max_diff_nearest_left_right_smaller(arr1))

    arr2 = [5, 1, 9, 2, 5, 1, 7]
    print("\nArray:", arr2)
    print("Max difference:", max_diff_nearest_left_right_smaller(arr2))

    arr3 = [2, 1, 8, 1]
    print("\nArray:", arr3)
    print("Max difference:", max_diff_nearest_left_right_smaller(arr3))

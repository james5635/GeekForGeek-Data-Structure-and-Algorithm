def nearest_smaller_on_left(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result


if __name__ == "__main__":
    arr1 = [1, 6, 4, 10, 2, 5]
    print("Array:", arr1)
    print("Nearest smaller on left:", nearest_smaller_on_left(arr1))

    arr2 = [4, 5, 2, 10, 8]
    print("\nArray:", arr2)
    print("Nearest smaller on left:", nearest_smaller_on_left(arr2))

    arr3 = [1, 3, 0, 2, 5]
    print("\nArray:", arr3)
    print("Nearest smaller on left:", nearest_smaller_on_left(arr3))

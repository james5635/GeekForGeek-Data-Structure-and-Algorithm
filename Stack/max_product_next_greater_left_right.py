def max_product_next_greater_left_right(arr):
    n = len(arr)

    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    right = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    max_prod = 0
    for i in range(n):
        l = left[i] if left[i] != -1 else 0
        r = right[i] if right[i] != -1 else 0
        max_prod = max(max_prod, l * r)
    return max_prod


if __name__ == "__main__":
    arr1 = [5, 4, 3, 4, 5]
    print("Array:", arr1)
    print("Max product:", max_product_next_greater_left_right(arr1))

    arr2 = [1, 1, 1, 1, 0, 1, 2, 3, 2, 1]
    print("\nArray:", arr2)
    print("Max product:", max_product_next_greater_left_right(arr2))

    arr3 = [6, 2, 1, 7, 5, 8, 10, 6]
    print("\nArray:", arr3)
    print("Max product:", max_product_next_greater_left_right(arr3))

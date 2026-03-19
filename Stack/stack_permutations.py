def check_stack_permutation(input_queue, output_queue):
    stack = []
    i = 0

    for item in input_queue:
        stack.append(item)
        while stack and stack[-1] == output_queue[i]:
            stack.pop()
            i += 1

    return not stack


if __name__ == "__main__":
    input1 = [1, 2, 3]
    output1 = [2, 1, 3]
    print(
        f"Input {input1}, Output {output1}: {check_stack_permutation(input1, output1)}"
    )

    input2 = [1, 2, 3]
    output2 = [3, 1, 2]
    print(
        f"Input {input2}, Output {output2}: {check_stack_permutation(input2, output2)}"
    )

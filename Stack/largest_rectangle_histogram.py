def largest_rectangle_histogram(heights):
    n = len(heights)
    stack = []
    max_area = 0
    for i in range(n + 1):
        h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)
        stack.append(i)
    return max_area


if __name__ == "__main__":
    h1 = [2, 1, 5, 6, 2, 3]
    print("Heights:", h1)
    print("Largest rectangle:", largest_rectangle_histogram(h1))

    h2 = [6, 2, 5, 4, 5, 1, 6]
    print("\nHeights:", h2)
    print("Largest rectangle:", largest_rectangle_histogram(h2))

    h3 = [2, 4]
    print("\nHeights:", h3)
    print("Largest rectangle:", largest_rectangle_histogram(h3))

def stock_span(prices):
    n = len(prices)
    span = [0] * n
    stack = []
    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return span


if __name__ == "__main__":
    prices1 = [100, 80, 60, 70, 60, 75, 85]
    print("Prices:", prices1)
    print("Span:   ", stock_span(prices1))

    prices2 = [10, 4, 5, 90, 120, 80]
    print("\nPrices:", prices2)
    print("Span:   ", stock_span(prices2))

    prices3 = [31, 27, 14, 21, 30, 22]
    print("\nPrices:", prices3)
    print("Span:   ", stock_span(prices3))

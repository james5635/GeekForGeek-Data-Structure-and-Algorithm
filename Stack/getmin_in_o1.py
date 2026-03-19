class MinStack:
    def __init__(self):
        self.stack = []
        self.min_element = None

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.min_element = val
        elif val < self.min_element:
            self.stack.append(2 * val - self.min_element)
            self.min_element = val
        else:
            self.stack.append(val)

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        top = self.stack.pop()
        if top < self.min_element:
            old_min = self.min_element
            self.min_element = 2 * self.min_element - top
            return old_min
        if not self.stack:
            self.min_element = None
        return top

    def top(self):
        if not self.stack:
            raise IndexError("top from empty stack")
        top = self.stack[-1]
        if top < self.min_element:
            return self.min_element
        return top

    def get_min(self):
        if not self.stack:
            raise IndexError("get_min from empty stack")
        return self.min_element

    def __str__(self):
        return f"MinStack({self.stack}, min={self.min_element})"


if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    s.push(1)
    print(f"Stack: {s}")
    print(f"Current min: {s.get_min()}")
    print(f"Top: {s.top()}")
    print(f"Popped: {s.pop()}")
    print(f"After pop, min: {s.get_min()}")
    print(f"Popped: {s.pop()}")
    print(f"After pop, min: {s.get_min()}")
    print(f"Top: {s.top()}")

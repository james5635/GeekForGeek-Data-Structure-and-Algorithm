class MinMaxStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        self.max_stack = []

    def push(self, item):
        self.main_stack.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self.main_stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        if item == self.max_stack[-1]:
            self.max_stack.pop()
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.main_stack[-1]

    def get_min(self):
        if not self.min_stack:
            raise IndexError("empty stack")
        return self.min_stack[-1]

    def get_max(self):
        if not self.max_stack:
            raise IndexError("empty stack")
        return self.max_stack[-1]

    def is_empty(self):
        return len(self.main_stack) == 0

    def size(self):
        return len(self.main_stack)


if __name__ == "__main__":
    s = MinMaxStack()
    items = [5, 3, 8, 1, 4, 7, 2]
    print(f"Pushing: {items}")
    for item in items:
        s.push(item)
        print(f"Push {item}: min={s.get_min()}, max={s.get_max()}")

    print(f"\nCurrent min: {s.get_min()}")
    print(f"Current max: {s.get_max()}")
    print(f"Size: {s.size()}")

    print(f"\nPopping 3 items:")
    for _ in range(3):
        popped = s.pop()
        print(f"Popped {popped}: min={s.get_min()}, max={s.get_max()}")

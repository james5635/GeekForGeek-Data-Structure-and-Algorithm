class TwoStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top1 = -1
        self.top2 = capacity

    def push1(self, item):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = item
        else:
            raise OverflowError("Stack 1 is full")

    def push2(self, item):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = item
        else:
            raise OverflowError("Stack 2 is full")

    def pop1(self):
        if self.top1 >= 0:
            item = self.arr[self.top1]
            self.top1 -= 1
            return item
        raise IndexError("Stack 1 is empty")

    def pop2(self):
        if self.top2 < self.capacity:
            item = self.arr[self.top2]
            self.top2 += 1
            return item
        raise IndexError("Stack 2 is empty")

    def is_empty1(self):
        return self.top1 == -1

    def is_empty2(self):
        return self.top2 == self.capacity

    def size1(self):
        return self.top1 + 1

    def size2(self):
        return self.capacity - self.top2


if __name__ == "__main__":
    ts = TwoStacks(10)
    print("Pushing to stack1: 1, 2, 3")
    ts.push1(1)
    ts.push1(2)
    ts.push1(3)
    print("Pushing to stack2: 10, 20, 30")
    ts.push2(10)
    ts.push2(20)
    ts.push2(30)
    print(f"Stack1 size: {ts.size1()}")
    print(f"Stack2 size: {ts.size2()}")
    print(f"Pop from stack1: {ts.pop1()}")
    print(f"Pop from stack2: {ts.pop2()}")
    print(f"Stack1 size after pop: {ts.size1()}")
    print(f"Stack2 size after pop: {ts.size2()}")

class KStacks:
    def __init__(self, k, capacity):
        self.k = k
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top = [-1] * k
        self.next = list(range(1, capacity)) + [-1]
        self.free = 0

    def is_full(self):
        return self.free == -1

    def is_empty(self, sn):
        return self.top[sn] == -1

    def push(self, item, sn):
        if self.is_full():
            raise OverflowError("Stack is full")
        i = self.free
        self.free = self.next[i]
        self.next[i] = self.top[sn]
        self.top[sn] = i
        self.arr[i] = item

    def pop(self, sn):
        if self.is_empty(sn):
            raise IndexError(f"Stack {sn} is empty")
        i = self.top[sn]
        self.top[sn] = self.next[i]
        self.next[i] = self.free
        self.free = i
        return self.arr[i]

    def peek(self, sn):
        if self.is_empty(sn):
            raise IndexError(f"Stack {sn} is empty")
        return self.arr[self.top[sn]]


if __name__ == "__main__":
    k = 3
    n = 10
    ks = KStacks(k, n)

    ks.push(15, 2)
    ks.push(45, 2)

    ks.push(17, 1)
    ks.push(49, 1)
    ks.push(39, 1)

    ks.push(11, 0)
    ks.push(9, 0)
    ks.push(7, 0)

    print(f"Popped element from stack 2: {ks.pop(2)}")
    print(f"Popped element from stack 1: {ks.pop(1)}")
    print(f"Popped element from stack 0: {ks.pop(0)}")
    print(f"Peek stack 2: {ks.peek(2)}")
    print(f"Peek stack 1: {ks.peek(1)}")
    print(f"Peek stack 0: {ks.peek(0)}")

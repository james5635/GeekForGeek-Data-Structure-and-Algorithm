class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val):
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

    def pop(self):
        if self.max_freq == 0:
            raise IndexError("pop from empty stack")
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            del self.group[self.max_freq]
            self.max_freq -= 1
        return val

    def peek_freq(self):
        if self.max_freq == 0:
            return 0
        return self.max_freq


if __name__ == "__main__":
    fs = FreqStack()
    fs.push(5)
    fs.push(7)
    fs.push(5)
    fs.push(7)
    fs.push(4)
    fs.push(5)

    print(f"Max frequency: {fs.peek_freq()}")
    print(f"Popped: {fs.pop()}")
    print(f"Popped: {fs.pop()}")
    print(f"Popped: {fs.pop()}")
    print(f"Popped: {fs.pop()}")
    print(f"Popped: {fs.pop()}")
    print(f"Popped: {fs.pop()}")

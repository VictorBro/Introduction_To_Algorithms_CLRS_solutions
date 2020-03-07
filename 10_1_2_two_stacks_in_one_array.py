class Stack:
    def __init__(self, n):
        self._S = [0] * n
        self._n = n
        self._top_a = -1
        self._top_b = n

    def push_a(self, x):
        if self._top_a + 1 == self._top_b:
            raise Exception("Overflow")
        self._top_a += 1
        self._S[self._top_a] = x

    def push_b(self, x):
        if self._top_b - 1 == self._top_a:
            raise Exception("Overflow")
        self._top_b -= 1
        self._S[self._top_b] = x

    def pop_a(self):
        if self._top_a == -1:
            raise Exception("Underflow")
        self._top_a -= 1
        return self._S[self._top_a + 1]

    def pop_b(self):
        if self._top_b == self._n:
            raise Exception("Underflow")
        self._top_b += 1
        return self._S[self._top_b - 1]

    def __str__(self):
        return str(self._S[:self._top_a + 1]) + str(self._S[self._top_b:])


def main():
    s = Stack(5)
    s.push_a(4)
    s.push_a(5)
    s.push_a(6)
    s.push_b(3)
    s.push_b(4)
    print(s)
    s.pop_a()
    print(s)


if __name__ == "__main__":
    main()

class Deque:
    def __init__(self, n):
        self._Q = [0] * n
        self._n = n
        self._head = self._tail = 0

    def push_to_tail(self, x):
        next = (self._tail + 1) % self._n
        if next == self._head:
            raise Exception("Overflow")
        self._Q[self._tail] = x
        self._tail = next

    def pop_from_head(self):
        if self._tail == self._head:
            raise Exception("Underflow")
        x = self._Q[self._head]
        self._head = (self._head + 1) % self._n
        return x

    def push_to_head(self, x):
        prev = (self._n + self._head - 1) % self._n
        if prev == self._tail:
            raise Exception("Overflow")
        self._head = prev
        self._Q[self._head] = x

    def pop_from_tail(self):
        if self._tail == self._head:
            raise Exception("Underflow")
        self._tail = (self._n + self._tail - 1) % self._n
        return self._Q[self._tail]

    def __str__(self):
        ret = []
        i = self._head
        while i != self._tail:
            ret.append(self._Q[i])
            i = (i + 1) % self._n
        return str(ret) + str(self._head) + "," + str(self._tail)


def main():
    q = Deque(3)
    q.push_to_head(23)
    q.push_to_tail(34)
    q.pop_from_head()
    q.pop_from_tail()
    print(q)


if __name__ == "__main__":
    main()

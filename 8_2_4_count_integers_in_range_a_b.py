class CountInRange:
    def __init__(self, A, k):
        self.n = len(A)
        self.k = k
        self.C = [0] * (k+1)
        for i in range(self.n):
            self.C[A[i]] += 1
        for i in range(1, k+1):
            self.C[i] += self.C[i - 1]

    def count_integers_in_range(self, a, b):
        if b > self.k:
            b = self.k
        if a <= 0:
            return self.C[b]
        else:
            return self.C[b] - self.C[a - 1]


def main():
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    count_in_range = CountInRange(A, max(A))
    print(count_in_range.count_integers_in_range(4, 6))
    print(count_in_range.count_integers_in_range(0, 7))


if __name__ == "__main__":
    main()

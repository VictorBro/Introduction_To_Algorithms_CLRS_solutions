LINEAR      = 1
QUADRATIC   = 2
DOUBLE      = 3

def h(x):
    return x


class Hash:
    def __init__(self):
        self.m = 11
        self.hash = [None] * self.m

    def linear_probe(self, x, i):
        return (h(x) + i) % self.m

    def quadratic_probe(self, x, i):
        return (h(x) + 1 * i + 3 * i * i) % self.m

    def h1(self, x):
        return 1 + (x % (self.m - 1))

    def double_hashing(self, x, i):
        return (h(x) + i * self.h1(x)) % self.m

    def hash_insert(self, x, method=LINEAR):
        hash_func = self.linear_probe
        if method == LINEAR:
            hash_func = self.linear_probe
        elif method == QUADRATIC:
            hash_func = self.quadratic_probe
        else:
            hash_func = self.double_hashing

        i = 0
        while i < self.m:
            j = hash_func(x, i)
            if self.hash[j] is None:
                self.hash[j] = x
                return j
            i += 1
        return None


def main():
    arr = [10, 22, 31, 4, 15, 28, 17, 88, 59]
    my_hash = Hash()
    for x in arr:
        print(my_hash.hash_insert(x, LINEAR))

    print()
    my_hash = Hash()
    for x in arr:
        print(my_hash.hash_insert(x, QUADRATIC))

    print()
    my_hash = Hash()
    for x in arr:
        print(my_hash.hash_insert(x, DOUBLE))


if __name__ == "__main__":
    main()
